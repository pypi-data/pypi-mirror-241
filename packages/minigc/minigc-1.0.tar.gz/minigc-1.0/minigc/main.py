#!/usr/bin/env python
# coding:utf-8
# created by Peixuan Shu
# 2023.11
"""
minidrone ground control:
1. connect and reconnect (launch minidrone mavros ROS node)
2. display connection, battery and pose_source state
3. forward pose data to topic /uavi/mavros/vision_pose/pose
"""
"""
TODO:
1. data log record
2. python wrapper around ROS topics
3. trajectory display
"""

import tkinter as tk
import tkinter.messagebox 
# from ttkbootstrap import Style
# from tkinter import ttk

import subprocess
import time
import os
# from datetime import datetime

from .topframe import TopFrame
from .consoleframe import ConsoleFrame
from .uavnode import UAVnode

import rospy
from std_msgs.msg import Int32


def main():
    print("Minidrone ground control GUI started!")

    # style = Style(theme='lumen') # classic
    # #['vista', 'classic', 'cyborg', 'journal', 'darkly', 'flatly', 'clam', 'alt', 'solar', 'minty', 'litera', 
    # # 'united', 'xpnative', 'pulse', 'cosmo', 'lumen', 'yeti', 'superhero', 'winnative', 'sandstone', 'default']

    # root = style.master

    root = tk.Tk()

    root.resizable(1,1) # window size changable

    normal_width = 850 # normal width
    normal_height = 550 # normal height
    height_times = 0.4 # real_height / screen_height 

    root.scale_factor = int(root.winfo_screenheight() * height_times) / float(normal_height)
    # root.scale_factor = 1.0
    win_width = int(normal_width * root.scale_factor)
    win_height = int(normal_height * root.scale_factor)
    off_y = int( (root.winfo_screenheight() - 600) / 4.0 )
    off_x = int( (root.winfo_screenwidth() - 800) / 2.0 )
    root.geometry("{}x{}+{}+{}".format(win_width, win_height, off_x, off_y))
    # print("root.scale_factor: ", root.scale_factor)
    # print(win_width,win_height)

    root.title('Minidrone Swarm Ground Control')

    init_time = time.time()

    ################### create the log file folder #################
    # record data file path "../../data_log/log%month%date%hour%min%sec"
#     folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     log_path = folder + '/data_log/log' + datetime.now().strftime("%Y%m%d") + \
# '-' + datetime.now().strftime("%H%M%S")
#     os.mkdir(log_path) # do not use os.makedirs() for error reporting


    # Load the image file from disk.
    workspace = os.path.dirname(os.path.abspath(__file__)) # absolute path of this folder 
    # workspace = os.path.dirname(os.path.dirname(workspace)) # up up folder
    icon = tk.PhotoImage(file=workspace+"/image/minidrone-logo.png")
    # Set it as the window icon.
    root.iconphoto(True, icon)

    gui = Gui(root, init_time, workspace)

    root.protocol('WM_DELETE_WINDOW', gui.__del__)

    root.mainloop()

class Gui:
    """ 
    Main GUI object 
    It consists of a Top frame, which is the menu and a main frame,
    which contains all the visual logs to the Minidrone.
    """
    def __init__(self, root, init_time, workspace="."):
        self.root = root
        self.init_time = init_time
        self.workspace = workspace

        ############ Read minidrone config ###########
        self.minidrone_config = self.workspace + "/config/minidrone_config.yaml"

        self.minidronedriver_nodes = {}
        self.uav_nodes = {}

        self.consoleframe = ConsoleFrame(root, self)
        self.topframe = TopFrame(root, self)
        
        self.topframe.pack(side='top', fill="both", expand="yes")
        self.consoleframe.pack(side='bottom', fill="both", expand="yes")

        self.scale = root.scale_factor

        self.print_console("Minidrone ground control GUI started!",color = "green")

        # launch roscore
        self.roscore_bygui = False
        self.rosmaster_pid = subprocess.getoutput("pgrep rosmaster")
        if not self.rosmaster_pid:
            self.roscore = subprocess.Popen(['/bin/bash', '-i', '-c', 'roscore'],start_new_session=True)
            self.roscore_bygui = True
            self.print_console("rosmaster started!",color = "green")
        else:
            self.roscore_bygui = False
            self.print_console("rosmaster already exists! pid: {}".format(self.rosmaster_pid),color = "green")

        # # launch switch node for uwb pos read and simultaneous takeoff and land
        # self.switch_node_bygui = False # if switch node is launched by this gui
        # self.switch_node_pid = subprocess.getoutput("pgrep switch_node")
        # if not self.switch_node_pid:
        #     cmd = 'roslaunch switch switch.launch'
        #     self.switch_node = subprocess.Popen(['/bin/bash', '-i', '-c', cmd],start_new_session=True)
        #     self.switch_node_bygui = True
        #     self.print_console("switch_node started!")
        # else:
        #     self.switch_node_bygui = False
        #     self.print_console("switch_node already exists! pid: {}".format(self.switch_node_pid))      

        ############ ROS initialize ############
        time.sleep(0.1)
        try:
            rospy.init_node('minigc_node', anonymous=True)
        except:
            pass # avoid overinit
        self.cmd_pub = rospy.Publisher('/command', Int32, queue_size=10)  
        self.land_num_pub = rospy.Publisher('/land_num', Int32, queue_size=10)
        self.takeoff_num_pub = rospy.Publisher('/takeoff_num', Int32, queue_size=10)  

    def __del__(self):
        """ close window """
        try:
            self.root.destroy() # if window not closed, close it
        except:
            pass
        """ delete uav_nodes and finish threads """ 
        for id in self.uav_nodes:
            self.uav_nodes[id].__del__()
        """if switch_node/roscore is launched by this GUI, kill it when exiting"""
        # if self.switch_node_bygui:
        #     self.switch_node.terminate()
        #     self.switch_node.wait()
        if self.roscore_bygui:
            self.roscore.terminate()
            self.roscore.wait()
        """ kill minidrone driver ROS nodes"""
        for id in self.minidronedriver_nodes:
            self.minidronedriver_nodes[id].terminate()
        for id in self.minidronedriver_nodes:
            self.minidronedriver_nodes[id].wait()         

    def update_minidrone_config(self, minidrone_config_path):
        """update self.minidrone_config """
        if minidrone_config_path.endswith(".yaml"):
            self.minidrone_config = minidrone_config_path
            self.print_console('Load minidrone_config: {}'.format(self.minidrone_config))
            self.print_console('Please reconnect all nodes to refresh them')
            self.showinfo_msg('Successfully load: {}.\n \nPlease reconnect all nodes to refresh them'.format(self.minidrone_config))  
            self.topframe.config_entry.delete(0,"end")
            self.topframe.config_entry.insert(0, self.minidrone_config)
        else:
            self.print_console('[Error] The config file is invalid: {}'.format(minidrone_config_path))  
            self.warning_msg('[Error] The config file is invalid: {}'.format(minidrone_config_path))  

    def connect(self, id):
        """ add uavnode and connect to minidrone """

        ### add uav_node ###
        if id in self.uav_nodes:
            self.uav_nodes[id].__del__() # close the former uav node
        self.uav_nodes[id] = UAVnode(id, self.minidrone_config, self)

        ### check if id is in minidrone_config yaml
        if self.uav_nodes[id].ip == "not found":
            self.uav_nodes[id].__del__()
            self.print_console("[Error] id {} not found in config file: {}".format(id, self.minidrone_config))
            defaultbg = self.root.cget('bg') # default button color
            self.topframe.uav_button[id].configure(bg=defaultbg) 
        else:
            ### launch mavros driver for minidrone ###
            if id in self.minidronedriver_nodes:
                self.minidronedriver_nodes[id].terminate() # close the former minidrone driver (mavros)
                # self.minidronedriver_nodes[id].wait()
                # self.warning_msg('UAV exists!')
                self.print_console('Reconnecting to uav'+str(id)+" ip:" + self.uav_nodes[id].ip + " drone_port:" + str(self.uav_nodes[id].drone_port) 
                                   + " gcs_port:" + str(self.uav_nodes[id].gcs_port) + " pos_src:" + self.uav_nodes[id].pose_source)
            else:
                self.print_console('Connecting to uav'+str(id)+" ip:" + self.uav_nodes[id].ip + " drone_port:" + str(self.uav_nodes[id].drone_port) 
                                   + " gcs_port:" + str(self.uav_nodes[id].gcs_port) + " pos_src:" + self.uav_nodes[id].pose_source)
            source_cmd = "cd {}/launch && ".format(self.workspace) # cd the folder path
            cmd = ("roslaunch mavros.launch id:=" + str(id) + " drone_ip:=" + self.uav_nodes[id].ip 
                                    + " drone_port:=" + str(self.uav_nodes[id].drone_port) + " mavros_port:=" + str(self.uav_nodes[id].gcs_port))
            self.minidronedriver_nodes[id] = subprocess.Popen(['/bin/bash', '-i', '-c',source_cmd+cmd],shell=False,start_new_session=True)

    def disconnect(self, id):
        """ kill mavros node and uavnode """
        if id in self.minidronedriver_nodes:
            self.minidronedriver_nodes[id].terminate() # kill mavros
            del self.minidronedriver_nodes[id] # delete the minidronedriver_nodes dict item
        if id in self.uav_nodes:
            self.uav_nodes[id].__del__() # delete the uavnode
            del self.uav_nodes[id] # delete the uavnodes dict item
            # reset the button bolor
            defaultbg = self.root.cget('bg') # default button color
            self.topframe.uav_button[id].configure(bg=defaultbg)
            self.print_console("Disconnecting uav{}".format(id))

    def reboot_fcu(self, id):
        """ reboot flight controller """
        if id in self.uav_nodes:
            self.uav_nodes[id].reboot_fcu()
            self.print_console("Rebooting uav{} fcu".format(id))

    def start_mocap_vrpn(self, vrpn_server_ip):
        """ start vrpn_client_ros """
        cmd = "roslaunch vrpn_client_ros sample.launch server:=" + vrpn_server_ip
        subprocess.Popen(['/bin/bash', '-i', '-c', cmd],shell=False,start_new_session=True)

    def stop_mocap_vrpn(self):
        """ stop vrpn_client_ros """
        cmd = "rosnode kill /vrpn_client_node"
        subprocess.Popen(['/bin/bash', '-i', '-c', cmd],shell=False,start_new_session=True)

    def start_uwb(self, port, baud):
        """ start UWB node """
        if "package 'nlink_parser' not found" in subprocess.getoutput("rospack find nlink_parser"):
            self.print_console("[Error] Can not find nlink_parser! Check nlink_parser ROS package is installed and sourced!", color = "red")   
            self.topframe.uwb_button_off()
        else:
            source_cmd = "cd {}/launch && ".format(self.workspace) # cd the folder path
            cmd = "roslaunch linktrack.launch port_name:={} baud_rate:={}".format(port,baud)
            subprocess.Popen(['/bin/bash', '-i', '-c', source_cmd+cmd],shell=False,start_new_session=True)
            ### check if linktrack node is launched correctly:
            self.root.after(1000, self.check_uwb_node, port, baud) # do check after 1000ms

    def check_uwb_node(self, port, baud):
        if "linktrack0" not in subprocess.getoutput("rostopic info /nlink_linktrack_anchorframe0"):
            # check if /linktrack0 exits and is the publisher of /nlink_linktrack_anchorframe0
            self.stop_uwb()
            self.topframe.uwb_button_off()
            self.print_console("[Error] Failed to launch linktrack on port /{} with baud_rate {}. Check your connection and UWB protocol. Or have you installed and sourced nlink_parser properly?".format(port, baud), color = "red")            
        else:
            self.print_console("[UWB] Connectted to UWB port:{} with baud rate {}".format(port, baud))

    def stop_uwb(self):
        """ stop UWB node """
        cmd = "rosnode kill /linktrack0"
        subprocess.Popen(['/bin/bash', '-i', '-c', cmd],shell=False,start_new_session=True)


    def warning_msg(self, msg):
        tkinter.messagebox.showwarning('warning', msg)
    
    def showinfo_msg(self, msg):
        tkinter.messagebox.showinfo('', msg)

    def print_console(self, msg, color = "white"):
        self.consoleframe.print_console(msg, color)

if __name__ == '__main__':
    main()
