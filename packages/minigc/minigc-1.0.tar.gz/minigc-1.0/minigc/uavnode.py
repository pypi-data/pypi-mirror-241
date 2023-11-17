#!/usr/bin/env python
# coding:utf-8
# created by Peixuan Shu
# 2023.11
"""
Functions:
1. listen to uav states and check if it is connected
2. listen to /command, /land_num and /takeoff_num to takeoff or land
3. read from mocap/uwb source and forward the pose data to /uavi/mavros/vision_pose/pose
"""

# import numpy as np
# from math import *
# from enum import Enum
import time

# import os
import sys
from threading import Thread
# import subprocess
import yaml

import rospy
import math
from std_msgs.msg import Int32
from std_msgs.msg import Empty

from geometry_msgs.msg import PoseStamped, Quaternion
from sensor_msgs.msg import Imu, BatteryState, NavSatFix
from mavros_msgs.msg import State, GPSRAW
from mavros_msgs.srv import CommandLong

# from tf.transformations import euler_from_quaternion

class UAVnode():
    """
    UAV communication node
    """
    def __init__(self, id, config_path, main_gui):
        self.id = id
        self.main_gui = main_gui
        self.print_console = self.main_gui.print_console
        self.warning_msg = self.main_gui.warning_msg
        self.minidrone_yaml = config_path
        ############ states initialize ############
        self.offline_sec = 0.8
        self.lose_pose_sec = 0.3
        self.check_loop_rate = 10 # Hz
        self.offline_flag = True
        self.pose_source_ok = False # if source pose is streaming pose data
        self.pose_aligned = False # if local_position is aligned with the source position
        self.battery_perct = -999.0  
        self.imu_quat = Quaternion() # read from /mavros/imu/data
        self.source_position = PoseStamped() # read from vrpn or uwb topic depending on the pose_source
        self.local_position = PoseStamped() # read from /mavros/local_position/pose
        self.mode = None # /mavros/state
        self.last_battery_time = 0.0
        self.last_imu_time = 0.0
        self.last_pose_time = 0.0
        ############ parse minidrone_config ###########
        self.ip = "not found"
        self.pose_source = "not found"
        self.drone_port = "not found"
        self.gcs_port = "not found"
        with open(self.minidrone_yaml, 'r') as ymlfile:
            cfg = yaml.safe_load(ymlfile)
        for uav in cfg["uavs"]:
            uav_id = int(uav["id"])
            if uav_id == self.id: ## parse uav info
                self.ip = uav["ip"]
                self.drone_port = uav["drone_port"]
                self.gcs_port = uav["gcs_port"]
                self.pose_source = uav["pose_source"]
                if self.pose_source == "mocap":
                    self.mocap_markerset = uav["mocap_markerset"]
                elif self.pose_source == "nluwb":
                    self.nluwb_tag_id = uav["nluwb_tag_id"]
                elif self.pose_source == "none":
                    pass
                else:
                    self.print_console("[Error] invalid pose_source: {} for minidrone {}".format(self.pose_source, self.id))
                break  
        if self.ip == "not found":
            # self.main_gui.topframe.uav_button[self.id].configure(bg="red") 
            self.warning_msg("[Error] id {} not found in config file: {}".format(self.id, self.minidrone_yaml))
        ############ ROS initialize ############
        try:
            rospy.init_node('minidronegc_node', anonymous=True)
        except:
            pass # avoid overinit
        # self.print_console("load uavnode{}".format(self.id))
        self.prefix = "uav"+str(self.id)
        ############## ROS topics ##############
        self.subs = []; self.pubs = []
        self.subs.append(rospy.Subscriber('/command', Int32, self.command_callback, queue_size=1))
        self.subs.append(rospy.Subscriber('/land_num', Int32, self.land_num_callback, queue_size=1))
        self.subs.append(rospy.Subscriber('/takeoff_num', Int32, self.takeoff_num_callback, queue_size=1))
        self.subs.append(rospy.Subscriber(self.prefix+'/mavros/battery', BatteryState, self.battery_callback, queue_size=1))
        self.subs.append(rospy.Subscriber(self.prefix+'/mavros/state', State, self.state_callback, queue_size=1))
        self.subs.append(rospy.Subscriber(self.prefix+'/mavros/local_position/pose', PoseStamped, self.local_position_callback, queue_size=1))
        self.subs.append(rospy.Subscriber(self.prefix+'/mavros/imu/data', Imu, self.imu_callback, queue_size=1))
        if self.pose_source == "mocap":
            self.subs.append(rospy.Subscriber("/vrpn_client_node/" + self.mocap_markerset + "/pose", PoseStamped, self.mocap_callback, queue_size=1))
        elif self.pose_source == "nluwb":
            # sys.path.append(self.main_gui.workspace + '/devel/lib/python3/dist-packages') # add nlink_parser path
            try: 
                import nlink_parser.msg ## rely on nooploop UWB ros driver package (nlink_parser)
                self.subs.append(rospy.Subscriber("/nlink_linktrack_anchorframe0", nlink_parser.msg.LinktrackAnchorframe0, self.nluwb_callback, queue_size=1))
            except AttributeError:
                self.print_console("[Error] uav{} fails to subscribe to /nlink_linktrack_anchorframe0. Check UWB ROS package nlink_parser is installed and sourced!".format(self.id), color="red")
                raise Exception('nlink_parser not found. Check nlink_parser ROS package is installed and sourced!')
        self.pose_pub = rospy.Publisher(self.prefix+'/mavros/vision_pose/pose', PoseStamped, queue_size=10)
        self.takeoff_pub = rospy.Publisher(self.prefix+'/takeoff', Empty, queue_size=10)
        self.land_pub = rospy.Publisher(self.prefix+'/land', Empty, queue_size=10)
        self.pubs.append(self.pose_pub)
        self.pubs.append(self.takeoff_pub)
        self.pubs.append(self.land_pub)
        ############# ROS service ################
        # rospy.wait_for_service(self.prefix+'/mavros/cmd/command')
        self.mavcmd = rospy.ServiceProxy(self.prefix+'/mavros/cmd/command', CommandLong)
        ############ status check thread #########
        self.kill_thread = False
        self.check_thread = Thread(target=self.check_status_loop)
        self.check_thread.start()
        self.pose_forward_thread = Thread(target=self.pose_forward_loop)
        self.pose_forward_thread.start()
        self.display_tip_thread = Thread(target=self.display_tip_loop)
        self.display_tip_thread.start()

    def __del__(self):
        for subcriber in self.subs:
            subcriber.unregister()
        for publisher in self.pubs:
            publisher.unregister()
        self.kill_thread = True
        del self

    def check_status_loop(self):
        count = 0
        while not self.kill_thread:
            """ check if uav is connected by imu data streaming """
            if time.time() - self.last_imu_time > self.offline_sec:
                if self.offline_flag == False:
                    self.main_gui.topframe.uav_button[self.id].configure(bg="yellow") 
                    self.print_console("uav{} is offline!".format(self.id))   
                self.offline_flag = True     
            else:
                if self.offline_flag == True:
                    self.main_gui.topframe.uav_button[self.id].configure(bg="green") 
                    self.print_console("uav{} is online now!".format(self.id))     
                self.offline_flag = False  
            
            """ check if pose_source is streaming pose data (mocap or uwb) """
            if time.time() - self.last_pose_time > self.lose_pose_sec:
                self.pose_source_ok = False
            else:
                self.pose_source_ok = True
            
            """ check if source pose is forwarded to px4 flight controller correctly """
            if math.sqrt(math.pow(self.source_position.pose.position.x - self.local_position.pose.position.x,2) + 
                math.pow(self.source_position.pose.position.y - self.local_position.pose.position.y,2)) < 0.1:
                self.pose_aligned = True
            else:
                self.pose_aligned = False
            
            """ check if mavros node is timeout and exit """   
            ### The command "subprocess.getoutput("rosnode list")" is heavily cpu-costing. 
            ### So this check is abandoned.
            # if self.prefix + '/mavros' not in subprocess.getoutput("rosnode list"):
            #     count = count + 1
            # if count >= 0.5 * self.check_loop_rate: # mavros node is timeout for 0.5 s
            #     defaultbg = self.main_gui.root.cget('bg') # default button color
            #     self.main_gui.topframe.uav_button[self.id].configure(bg=defaultbg)
            #     self.print_console(self.prefix + '/mavros node is timeout!')
            #     # kill the mavros node
            #     if self.id in self.main_gui.minidronedriver_nodes:
            #         self.main_gui.minidronedriver_nodes[self.id].terminate()
            #         self.main_gui.minidronedriver_nodes.pop(self.id) # delete the minidronedriver_nodes dict item
            #     self.main_gui.uav_nodes.pop(self.id) # delete the uavnodes dict item 
            #     self.__del__() # delete this object
            
            """ check safety and kill motor in case of emergency"""
            # TODO

            time.sleep(1.0/self.check_loop_rate)

    def pose_forward_loop(self):
        """ forward mocap or uwb source position to /mavros/vision_pose/pose """
        while not self.kill_thread:
            if self.pose_source_ok == True:
                self.pose_pub.publish(self.source_position)
            rate = 50.0
            time.sleep(1.0/rate)

    def display_tip_loop(self):
        """ update states in tip window """
        while not self.kill_thread:
            if self.offline_flag == False: # uav is connected
                ### if tip window is on, then refresh it
                if self.main_gui.topframe.uav_button[self.id].tip_on == True:
                    button = self.main_gui.topframe.uav_button[self.id]
                    button.status_label["text"] = 'Status: {}'.format(self.mode)
                    x = self.local_position.pose.position.x
                    y = self.local_position.pose.position.y
                    z = self.local_position.pose.position.z
                    button.xyz_label["text"] = "Local: {:.2f}, {:.2f}, {:.2f} m".format(x,y,z)
            rate = 5.0
            time.sleep(1.0/rate)

    def battery_callback(self,msg):
        self.battery_perct = msg.percentage
        self.main_gui.topframe.show_status(self.id, self.battery_perct, self.pose_source_ok, self.pose_aligned, self.pose_source)    
        self.last_battery_time =time.time()

    def imu_callback(self,msg):
        """ imu orientation, angular velocity and linear_acceleration from minidrone onboard imu sensor"""
        self.imu_quat = msg.orientation # yaw is relative to the turn-on moment heading
        self.last_imu_time =time.time()

    def local_position_callback(self,msg):
        """ local pose from /mavros/local_position/pose """
        self.local_position = msg

    def state_callback(self, msg):
        # mode_dict = {     'MANUAL' : 1, 
        #                   'ACRO' : 2, 
        #                   'ALTCTL' : 3, 
        #                   'POSCTL' : 4, 
        #                   'OFFBOARD' : 5, 
        #                   'STABILIZED' : 6, 
        #                   'RATTITUDE' : 7, 
        #                   'AUTO.MISSION' : 8, 
        #                   'AUTO.LOITER' : 9, 
        #                   'AUTO.RTL' : 10, 
        #                   'AUTO.LAND' : 11, 
        #                   'AUTO.RTGS' : 12, 
        #                   'AUTO.READY' : 13, 
        #                   'AUTO.TAKEOFF' : 14   }
        self.mode = msg.mode

    def mocap_callback(self,msg):
        self.source_position = msg
        self.source_position.header.stamp = rospy.Time.now()
        self.last_pose_time =time.time()
        # data = msg
        # # self.state_pos[0] = data.pose.position.x
        # # self.state_pos[1] = data.pose.position.y
        # # self.state_pos[2] = data.pose.position.z
        # # qw = data.pose.orientation.w
        # # qx = data.pose.orientation.x
        # # qy = data.pose.orientation.y 
        # # qz = data.pose.orientation.z 
        # # euler = euler_from_quaternion([qx, qy, qz, qw])
        # # self.yaw = euler[2]        

    def nluwb_callback(self,msg):
        nodes = msg.nodes
        for node in nodes:
            tag_id = node.id
            if tag_id == self.nluwb_tag_id:
                self.source_position.header.stamp = rospy.Time.now()
                self.source_position.pose.position.x = node.pos_3d[0] # uwb x
                self.source_position.pose.position.y = node.pos_3d[1] # uwb y
                self.source_position.pose.position.z = node.pos_3d[2] # uwb z (not precise, so usually not adpoted by px4)
                # self.source_position.pose.orientation = self.imu_quat # orientation quaternion from minidrone onboard sensor
                self.last_pose_time = time.time()
                break

    def reboot_fcu(self):
        # http://mavlink.io/en/messages/common.html#MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN
        self.mavcmd(command=246,param1=1)

    def command_callback(self,msg):
        command = msg.data
        if command == 1:
            for i in range(10): # loop for 10 times
                pub_msg = Empty()
                self.takeoff_pub.publish(pub_msg)
                # time.sleep(0.1)
        elif command == 9:
            for i in range(20): # loop for 20 times
                pub_msg = Empty()
                self.land_pub.publish(pub_msg)
                # time.sleep(0.1)        

    def land_num_callback(self,msg):
        num = msg.data
        if num == self.id:
            for i in range(20): # loop for 20 times
                pub_msg = Empty()
                self.land_pub.publish(pub_msg)
                # time.sleep(0.1)  

    def takeoff_num_callback(self,msg):
        num = msg.data
        if num == self.id:
            for i in range(10): # loop for 10 times
                pub_msg = Empty()
                self.takeoff_pub.publish(pub_msg)
                # time.sleep(0.1)     