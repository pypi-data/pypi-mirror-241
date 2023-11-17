#!/usr/bin/env python
# coding:utf-8
# created by Peixuan Shu
# 2023.11
"""
buttons and console frame
"""

import tkinter as tk
from tkinter import ttk
import tkinter.tix as tix
# import tkinter.messagebox 
from tkinter import filedialog
# import matplotlib.pyplot as plt
# from PIL import Image, ImageTk

# import rospy
from std_msgs.msg import Int32

import os
import time
import subprocess
import re

green = '#95C943'
font = 'TkDefaultFont'+' ' # Times

class UAVbutton(tk.Button):
    """ Styled and configured UAV Button  """

    def __init__(self, master, id, width, **kwargs):
        self.master = master
        self.id = id
        self.scale = master.scale
        super().__init__(master, font=font+'12', width=int(width*1.0), fg=green, text=str(id))
        self.config(**kwargs)

        ### right click menu
        self.right_click_menu = tk.Menu(self)
        # self.menu1.add_cascade(label = 'folder', menu=self.menu)
        self.right_click_menu.bind('<Leave>', self.destroy_menu)

        ### right click
        self.bind('<Button-3>', self.pop_menu)
        ### enter
        self.bind('<Enter>', self.cursor_enter)
        ### leave
        self.bind('<Leave>', self.cursor_leave)

        ### tip window
        self.topwindow = None
        self.tip_on = False
        self.cursor_on_button = False

    def cursor_enter(self, event):
            self.config(fg='black')
            self.cursor_on_button = True
            ### hover top window
            self.after(250, self.cursor_pop_tip) # wait for 250 ms
    
    def cursor_leave(self, event):
            self.cursor_on_button = False
            self.config(fg=green)
            ### destroy tip window
            if self.tip_on:
                self.destroy_tip(event)

    def cursor_pop_tip(self):
        """ pop out top window when cursor stays for a moment """
        if self.id in self.master.main_gui.uav_nodes:
            if self.cursor_on_button and not self.tip_on:
                cursor_x = self.master.main_gui.root.winfo_pointerx()
                cursor_y = self.master.main_gui.root.winfo_pointery()
                self.pop_tip(window_x = cursor_x, window_y = cursor_y)

    def pop_tip(self, window_x = None, window_y=None):
        """ pop out top window displaying state tips """
        if self.id in self.master.main_gui.uav_nodes:
            self.tip_on = True
            ### create toplevel window
            self.topwindow = tk.Toplevel(self)
            self.topwindow.overrideredirect(True) # hide title and state bar
            self.topwindow.wm_attributes('-alpha', 0.7)
            # self.topwindow.attributes("-topmost", 1)  # 也可以使用 `-topmost`
            # self.topwindow.resizable(width=True,height=True)
            width = int(self.master.main_gui.root.winfo_width() / 4.0)
            height = int(self.master.main_gui.root.winfo_height() / 8.0)
            self.topwindow.geometry("{}x{}".format(width, height))
            if window_x and window_y:
                self.topwindow.geometry("+{}+{}".format(window_x+5, window_y))
            self.topwindow.bind('<Leave>', self.destroy_tip)
            ### create state label
            # self.canvas = tk.Canvas(self.topwindow)
            # self.canvas.pack(side=tix.TOP, fill=tix.BOTH, expand=1) #放置canvas的位置
            # self.canvas.create_text(10, 10, anchor='w', font='Courier 10', fill='black', text='aaaaaaaaaaaaaaa', tags='warning')
            self.id_label =  tk.Label(self.topwindow, font=font+'10', fg="black", anchor='w', text='ID: {}'.format(self.id))
            self.id_label.pack(side='top',fill='x', padx = 2, pady=1)
            self.status_label =  tk.Label(self.topwindow, font=font+'10', fg="black", anchor='w', text='Status: '.format())
            self.status_label.pack(side='top',fill='x', padx = 2, pady=1)
            self.xyz_label = tk.Label(self.topwindow, font=font+'10', fg="black", anchor='w', text='Local Pos: '.format())
            self.xyz_label.pack(side='top',fill='x', padx = 2, pady=1)

    def destroy_tip(self, event=None):
        ### destroy top window
        if self.tip_on:
            self.topwindow.destroy()
            self.tip_on = False
    
    def pop_menu(self, event):
        """ pop out menu"""
        self.right_click_menu.post(event.x_root, event.y_root) 

    def destroy_menu(self, event):
        self.right_click_menu.unpost()


class SwitchButton(tk.Button):
    """ on-off switching button """
    def __init__(self, master, **kwargs):
        self.master = master
        self.scale = master.scale
        super().__init__(master)
        self.config(**kwargs)

        folder = os.path.dirname(os.path.abspath(__file__)) # absolute path of this folder 
        # image = Image.open(folder + "/image/on.png")
        # img = image.resize((100,200))
        # self.on_image = ImageTk.PhotoImage(img)
        self.on_image = tk.PhotoImage(file = folder + "/image/on.png")
        self.off_image = tk.PhotoImage(file = folder + "/image/off.png")
        self.is_on = False
        self.config(image = self.off_image)



class TopFrame(tk.Frame):
    """
    Top fram contains the menu to add URI's and choose which test to run
    """

    def __init__(self, root, main_gui):
        self.scale = root.scale_factor
        frame_width = int(850 * self.scale)
        frame_height = int(380 * self.scale)
        super().__init__(root, width=frame_width, height=frame_height, bd=2, relief='ridge')
        # print("self.scale:", self.scale)
        # print(frame_width,frame_height)
        self.main_gui = main_gui
        self.pack()
        self.grid_propagate(0) # 0

        self.add_id = 0
        self.allselect = tk.StringVar()
        self.allselect.set("no")

        self.show_buttons()

    def show_buttons(self):
        """ Buttons for controlling the URI listbox """
        padx = int(5*self.scale)
        pady = int(5*self.scale)
        row_num = 5
        col_num = 6
        self.uav_button = {}
        self.battery_label = {}
        self.pose_src_label = {}
        for i in range(row_num):
            for j in range(col_num):
                id = i*col_num+j+1
                ### uav button
                button = UAVbutton(self, id, width=5)
                button.grid(row=2*i, column=2*j, columnspan=2, padx=padx, pady=pady)
                self.uav_button[id] = button
                # callbacks = self._button_callbacks(id)
                ### left click uav button callback
                self.uav_button[id].configure(command=self._connect_single(id)) # left click to connect to uav
                ### right click uav button callback
                self.uav_button[id].right_click_menu.add_command(label='disconnect', command=self._disconnect_single(id))
                self.uav_button[id].right_click_menu.add_command(label='reboot', command=self._reboot_single(id))
                self.uav_button[id].right_click_menu.add_command(label='takeoff', command=self._takeoff_single(id))
                self.uav_button[id].right_click_menu.add_command(label='land', command=self._land_single(id))
                # self.uav_button[id].right_click_menu.add_command(label='cancle')
                ### uav battery percentage label
                label = tk.Label(self, font=font+'10', fg=green, text='')
                label.grid(row=2*i+1, column=j*2)
                self.battery_label[id] = label
                ### pose source label
                label = tk.Label(self, font=font+'10', fg=green, text='')
                label.grid(row=2*i+1, column=j*2+1)
                self.pose_src_label[id] = label
        
        # init number entry
        self.init_num_entry = tk.Entry(self, font='Coself.urier 12', width=5, bd=2, relief='ridge',
                            highlightthickness=0, justify="center")
        self.init_num_entry.grid(row=0, column=col_num*2+1, padx=padx, pady=pady)
        self.init_num_entry.insert(0, '1')
        self.init_num_entry.focus_set()      
        # init_label = tk.Label(self, font=font+'10', fg=green, text='from')
        # init_label.grid(row=1, column=col_num+1)

        ### init number label
        from_label = tk.Label(self, font=font+'10', fg="grey", text='from')
        from_label.grid(row=1, column=col_num*2+1)

        # end number entry
        self.end_num_entry = tk.Entry(self, font='Coself.urier 12', width=5, bd=2, relief='ridge',
                            highlightthickness=0, justify="center")
        self.end_num_entry.grid(row=0, column=col_num*2+2, padx=padx, pady=pady)
        self.end_num_entry.insert(0, '10')
        self.end_num_entry.focus_set()   
        # end_label = tk.Label(self, font=font+'10', fg=green, text='to')
        # end_label.grid(row=3, column=col_num+1)

        ### end number label
        to_label = tk.Label(self, font=font+'10', fg="grey", text='to')
        to_label.grid(row=1, column=col_num*2+2)

        # connect button
        self.connect_button = tk.Button(self, font=font+'12', text="Connect", fg="grey", width=11, command=self._cb_connect_button)
        self.connect_button.grid(row=2, column=col_num*2+1, columnspan=2, padx=padx, pady=pady)

        # disconnect button
        self.connect_button = tk.Button(self, font=font+'12', text="Disconnect", fg="grey", width=11, command=self._cb_disconnect_button)
        self.connect_button.grid(row=4, column=col_num*2+1, columnspan=2, padx=padx, pady=pady)

        #  reboot button
        self.connect_button = tk.Button(self, font=font+'12', text="Reboot", fg="grey", width=11, command=self._cb_reboot_button)
        self.connect_button.grid(row=6, column=col_num*2+1, columnspan=2, padx=padx, pady=pady)

        #  pop tip state button
        self.state_button = tk.Button(self, font=font+'12', text="Show State", fg="grey", width=11, command=self._cb_state_button)
        self.state_button.grid(row=8, column=col_num*2+1, columnspan=2, padx=padx, pady=pady)
        self.state_button.tips_on = False

        # config file path entry
        self.config_entry = tk.Entry(self, font='Coself.urier 12', bd=2, relief='ridge',
                            highlightthickness=0)
        self.config_entry.grid(row=row_num*2, column=0, columnspan=5*2, padx=padx, pady=pady, sticky="WE")
        self.config_entry.insert(0, self.main_gui.minidrone_config)
        self.config_entry.focus_set()   

        # browse button
        self.browse_button = tk.Button(self, font=font+'12', width=5, fg="grey", text="browse", command=self._cb_update_config)
        self.browse_button.grid(row=row_num*2, column=5*2, columnspan=2, padx=padx, pady=pady)

        # take off button
        self.takeoff_button = tk.Button(self, font=font+'12', width=5, bg="grey", fg="white", text="takeoff", command=self._cb_takeoff_button)
        self.takeoff_button.grid(row=row_num*2, column=col_num*2+1, padx=padx, pady=pady)

        # land button
        self.land_button = tk.Button(self, font=font+'12', width=4, bg="grey", fg="white", text="land", command=self._cb_land_button)
        self.land_button.grid(row=row_num*2, column=col_num*2+2, padx=padx, pady=pady)

        # vrpn server IP entry
        self.vrpn_ip_entry = tk.Entry(self, font='Coself.urier 10', width=13, fg="grey", bd=2, relief='ridge',
                            highlightthickness=0, justify="center")
        self.vrpn_ip_entry.grid(row=0, column=col_num*2+3, columnspan=2, padx=padx, pady=pady)
        self.vrpn_ip_entry.insert(0, '192.168.31.105')
        self.vrpn_ip_entry.focus_set()      

        ### vrpn server IP label
        vrpn_ip_label = tk.Label(self, font=font+'10', fg="grey", text='vrpn server')
        vrpn_ip_label.grid(row=1, column=col_num*2+3, columnspan=2)

        # vrpn button
        self.vrpn_button = SwitchButton(self, command=self._cb_vrpn_button)
        self.vrpn_button.grid(row=2, column=col_num*2+3, columnspan=2, padx=padx, pady=pady)

        ## uwb port list
        """ find all usb ports """
        tty_string = subprocess.getoutput("dmesg | grep tty")
        port_list = [item for item in tty_string.split(" ") if re.search(re.compile("tty"), item)]
        port_list.remove("[tty0]")
        self.port_box = ttk.Combobox(self, values=port_list, font=font+'10', width=6, postcommand=self._cb_portbox_update)
        self.port_box.grid(row=4, column=col_num*2+3, columnspan=1)
        self.port_box.set(port_list[-1])

        ## uwb port baudrate list
        """ find all usb ports """
        baud_list = ["921600","115200"]
        self.baud_box = ttk.Combobox(self, values=baud_list, state='readonly', font=font+'10', width=6)
        self.baud_box.grid(row=4, column=col_num*2+4, columnspan=1)
        self.baud_box.set(baud_list[0])

        ### UWB usb port label
        usb_label = tk.Label(self, font=font+'10', fg="grey", text='UWB port')
        usb_label.grid(row=5, column=col_num*2+3, columnspan=2)

        # UWB button
        self.uwb_button = SwitchButton(self, command=self._cb_uwb_button)
        self.uwb_button.grid(row=6, column=col_num*2+3, columnspan=2, padx=padx, pady=pady)        

        # command number entry
        self.cmd_num_entry = tk.Entry(self, font='Coself.urier 12', width=13, bd=2, relief='ridge',
                            highlightthickness=0, justify="center")
        self.cmd_num_entry.grid(row=8, column=col_num*2+3, columnspan=2, padx=padx, pady=pady)
        self.cmd_num_entry.insert(0, '2')
        self.cmd_num_entry.focus_set()   

        ### command number label
        command_label = tk.Label(self, font=font+'10', fg="grey", text='/command')
        command_label.grid(row=9, column=col_num*2+3, columnspan=2)

        # send command button
        self.send_button = tk.Button(self, font=font+'12', text="send", bg="grey", fg="white", width=11, command=self._cb_send_button)
        self.send_button.grid(row=10, column=col_num*2+3, columnspan=2, padx=padx, pady=pady)

    def show_status(self, id, battery_perct, pose_source_ok, pose_aligned, pose_source):
        # display battery perctentage
        self.battery_label[id].configure(text="{:.0f}%".format(battery_perct*100)) 
        if battery_perct > 0.2:
            self.battery_label[id].configure(fg=green) 
        else:
            self.battery_label[id].configure(fg="red") 
        # display pose source status
        if pose_source_ok == True:
            if pose_aligned == True:
                self.pose_src_label[id].configure(text=pose_source, fg=green)
            else:
                self.pose_src_label[id].configure(text=pose_source, fg="yellow")
        else:
            self.pose_src_label[id].configure(text=pose_source, fg="red")

    ###### Callback from buttons #########
    def _cb_connect_button(self):
        """ select connecting uavs """
        init_num = int(self.init_num_entry.get())
        end_num = int(self.end_num_entry.get())
        if (init_num <1):
            self.main_gui.print_console("[Invalid] init number should be larger than 1!", color = "red")
        elif (end_num >30):
            self.main_gui.print_console("[Invalid] end number should be smaller than 30!", color = "red")
        elif (end_num < init_num):
            self.main_gui.print_console("[Invalid] end number should be larger than start number!", color = "red")
        else:
            for id in range(init_num, end_num+1):
                self._connect_single(id)() # note that self._connect_single(id) returns a function
                time.sleep(0.05)

    def _cb_disconnect_button(self):
        """  disconnecting uavs """
        init_num = int(self.init_num_entry.get())
        end_num = int(self.end_num_entry.get())
        if (init_num <1):
            self.main_gui.print_console("[Invalid] init number should be larger than 1!", color = "red")
        elif (end_num >30):
            self.main_gui.print_console("[Invalid] end number should be smaller than 30!", color = "red")
        elif (end_num < init_num):
            self.main_gui.print_console("[Invalid] end number should be larger than start number!", color = "red")
        else:
            for id in range(init_num, end_num+1):
                self._disconnect_single(id)()  # note that self._disconnect_single(id) returns a function
                time.sleep(0.05)

    def _cb_reboot_button(self):
        """ reboot uavs """
        """ select rebooting uavs """
        init_num = int(self.init_num_entry.get())
        end_num = int(self.end_num_entry.get())
        if (init_num <1):
            self.main_gui.print_console("[Invalid] init number should be larger than 1!", color = "red")
        elif (end_num >30):
            self.main_gui.print_console("[Invalid] end number should be smaller than 30!", color = "red")
        elif (end_num < init_num):
            self.main_gui.print_console("[Invalid] end number should be larger than start number!", color = "red")
        else:
            for id in range(init_num, end_num+1):
                self._reboot_single(id)() # note that self._reboot_single(id) returns a function
                time.sleep(0.05)

    def _cb_state_button(self):
        if self.state_button.tips_on == False:
            """ pop out all state tips """
            self.state_button.tips_on = True
            win_x = self.main_gui.root.winfo_rootx()
            win_y = self.main_gui.root.winfo_rooty()
            win_width = self.main_gui.root.winfo_width()
            win_height = self.main_gui.root.winfo_height()
            padx = int(win_width / 4.0)
            pady = int(win_height / 8.0)
            row = 0
            col = 0
            dict = self.main_gui.uav_nodes
            # sort the uav_nodes according to id and pop out tips
            for i, item in enumerate(sorted(dict.items(), key=lambda dict:dict[0], reverse=False)):
                id = item[0]
                window_x = win_x + win_width + padx * col
                window_y = win_y + pady * row
                self.uav_button[id].pop_tip(window_x, window_y)
                row = row + 1
                if window_y + pady >= win_y + win_height:
                    row = 0
                    col = col + 1                
            self.main_gui.print_console("Displaying all online UAV states")
        else:
            """ close all state tips """
            self.state_button.tips_on = False
            for i, id in enumerate(self.main_gui.uav_nodes):
                self.uav_button[id].destroy_tip()
            self.main_gui.print_console("Closing all online UAV states tips")

    def _cb_vrpn_button(self):
        """ start vrpn """
        if self.vrpn_button.is_on == False:
            # switch button image
            self.vrpn_button.is_on = True
            self.vrpn_button.config(image=self.vrpn_button.on_image)
            # launch vrpn_client_ros
            server_ip = self.vrpn_ip_entry.get()
            self.main_gui.start_mocap_vrpn(server_ip)
            self.main_gui.print_console("[vrpn] connecting to vrpn server:{}".format(server_ip))
        else:
            # switch button image
            self.vrpn_button.is_on = False
            self.vrpn_button.config(image=self.vrpn_button.off_image)   
            # close vrpn_client_ros
            self.main_gui.stop_mocap_vrpn()
            self.main_gui.print_console("[vrpn] killed vrpn_client_node")

    def _cb_uwb_button(self):
        """ start UWB """
        if self.uwb_button.is_on == False:
            # switch button image
            self.uwb_button.is_on = True
            self.uwb_button.config(image=self.uwb_button.on_image)
            # launch nlink_parser UWB node
            port = self.port_box.get()
            baud = self.baud_box.get()
            self.main_gui.start_uwb(port, baud)
        else:
            # switch button image
            self.uwb_button.is_on = False
            self.uwb_button.config(image=self.uwb_button.off_image)   
            # kill nlink_parser UWB node
            self.main_gui.stop_uwb()
            self.main_gui.print_console("[UWB] killed UWB node")   

    def uwb_button_off(self):
            # switch button image
            self.uwb_button.is_on = False
            self.uwb_button.config(image=self.uwb_button.off_image)  

    def _cb_portbox_update(self):
        """ search and update USB ports list """
        tty_string = subprocess.getoutput("dmesg | grep tty")
        port_list = [item for item in tty_string.split(" ") if re.search(re.compile("tty"), item)]
        port_list.remove("[tty0]")
        self.port_box["value"] = port_list

    def _cb_send_button(self):
        """ send number to /command topic """
        msg = Int32()
        msg.data = int(self.cmd_num_entry.get())
        self.main_gui.cmd_pub.publish(msg)
        self.main_gui.print_console("[Send] send {} to /command".format(msg.data))        

    def _cb_takeoff_button(self):
        """send takeoff command 1"""
        msg = Int32()
        msg.data = 1
        self.main_gui.cmd_pub.publish(msg)
        self.main_gui.print_console("[Takeoff] send {} to /command".format(msg.data))

    def _cb_land_button(self):
        """send land command 9"""
        msg = Int32()
        msg.data = 9
        self.main_gui.cmd_pub.publish(msg)
        self.main_gui.print_console("[Land] send {} to /command".format(msg.data))

    def _cb_update_config(self):
        """ browse and update config file path """
        default_dir = self.main_gui.workspace + "/config"
        config_path = filedialog.askopenfilename(title='choose minidrone config yaml',initialdir=default_dir)
        self.main_gui.update_minidrone_config(config_path)

    def _connect_single(self, id):
        """ connect uav and check if connected """
        def func():
            self.main_gui.connect(id) # init and connect to uav
            self.uav_button[id].configure(bg="yellow") # change button to yellow color
        return func

    def _disconnect_single(self, id):
        """ kill mavros node """
        def func():
            self.main_gui.disconnect(id)
        return func

    def _reboot_single(self, id):
        """ reboot flight controller """
        def func():
            self.main_gui.reboot_fcu(id)
        return func

    def _takeoff_single(self, id):
        """ takeoff single uav """
        def func():
            msg = Int32()
            msg.data = id
            self.main_gui.takeoff_num_pub.publish(msg)
            self.main_gui.print_console("[Send] send {} to /takeoff_num".format(msg.data))
        return func

    def _land_single(self, id):
        """ land single uav """
        def func():
            msg = Int32()
            msg.data = id
            self.main_gui.land_num_pub.publish(msg)
            self.main_gui.print_console("[Send] send {} to /land_num".format(msg.data))
        return func
    
    # def _button_callbacks(self, id):
    #     if id==1:
    #         return lambda: self._connect(1), lambda: self._disconnect(1), lambda: self._reboot(1), lambda: self._takeoff_single(1), lambda: self._land_single(1)
    #     elif id==2:
    #         return lambda: self._connect(2), lambda: self._disconnect(2), lambda: self._reboot(2), lambda: self._takeoff_single(2), lambda: self._land_single(2)
    #     elif id==3:
    #         return lambda: self._connect(3), lambda: self._disconnect(3), lambda: self._reboot(3), lambda: self._takeoff_single(3), lambda: self._land_single(3)
    #     elif id==4:
    #         return lambda: self._connect(4), lambda: self._disconnect(4), lambda: self._reboot(4), lambda: self._takeoff_single(4), lambda: self._land_single(4)
    #     elif id==5:
    #         return lambda: self._connect(5), lambda: self._disconnect(5), lambda: self._reboot(5), lambda: self._takeoff_single(5), lambda: self._land_single(5)
    #     elif id==6:
    #         return lambda: self._connect(6), lambda: self._disconnect(6), lambda: self._reboot(6), lambda: self._takeoff_single(6), lambda: self._land_single(6)
    #     elif id==7:
    #         return lambda: self._connect(7), lambda: self._disconnect(7), lambda: self._reboot(7), lambda: self._takeoff_single(7), lambda: self._land_single(7)
    #     elif id==8:
    #         return lambda: self._connect(8), lambda: self._disconnect(8), lambda: self._reboot(8), lambda: self._takeoff_single(8), lambda: self._land_single(8)
    #     elif id==9:
    #         return lambda: self._connect(9), lambda: self._disconnect(9), lambda: self._reboot(9), lambda: self._takeoff_single(9), lambda: self._land_single(9)
    #     elif id==10:
    #         return lambda: self._connect(10), lambda: self._disconnect(10), lambda: self._reboot(10), lambda: self._takeoff_single(10), lambda: self._land_single(10)
    #     elif id==11:
    #         return lambda: self._connect(11), lambda: self._disconnect(11), lambda: self._reboot(11), lambda: self._takeoff_single(11), lambda: self._land_single(11)
    #     elif id==12:
    #         return lambda: self._connect(12), lambda: self._disconnect(12), lambda: self._reboot(12), lambda: self._takeoff_single(12), lambda: self._land_single(12)
    #     elif id==13:
    #         return lambda: self._connect(13), lambda: self._disconnect(13), lambda: self._reboot(13), lambda: self._takeoff_single(13), lambda: self._land_single(13)
    #     elif id==14:
    #         return lambda: self._connect(14), lambda: self._disconnect(14), lambda: self._reboot(14), lambda: self._takeoff_single(14), lambda: self._land_single(14)
    #     elif id==15:
    #         return lambda: self._connect(15), lambda: self._disconnect(15), lambda: self._reboot(15), lambda: self._takeoff_single(15), lambda: self._land_single(15)
    #     elif id==16:
    #         return lambda: self._connect(16), lambda: self._disconnect(16), lambda: self._reboot(16), lambda: self._takeoff_single(16), lambda: self._land_single(16)
    #     elif id==17:
    #         return lambda: self._connect(17), lambda: self._disconnect(17), lambda: self._reboot(17), lambda: self._takeoff_single(17), lambda: self._land_single(17)
    #     elif id==18:
    #         return lambda: self._connect(18), lambda: self._disconnect(18), lambda: self._reboot(18), lambda: self._takeoff_single(18), lambda: self._land_single(18)
    #     elif id==19:
    #         return lambda: self._connect(19), lambda: self._disconnect(19), lambda: self._reboot(19), lambda: self._takeoff_single(19), lambda: self._land_single(19)
    #     elif id==20:
    #         return lambda: self._connect(20), lambda: self._disconnect(20), lambda: self._reboot(20), lambda: self._takeoff_single(20), lambda: self._land_single(20)
    #     elif id==21:
    #         return lambda: self._connect(21), lambda: self._disconnect(21), lambda: self._reboot(21), lambda: self._takeoff_single(21), lambda: self._land_single(21)
    #     elif id==22:
    #         return lambda: self._connect(22), lambda: self._disconnect(22), lambda: self._reboot(22), lambda: self._takeoff_single(22), lambda: self._land_single(22)
    #     elif id==23:
    #         return lambda: self._connect(23), lambda: self._disconnect(23), lambda: self._reboot(23), lambda: self._takeoff_single(23), lambda: self._land_single(23)
    #     elif id==24:
    #         return lambda: self._connect(24), lambda: self._disconnect(24), lambda: self._reboot(24), lambda: self._takeoff_single(24), lambda: self._land_single(24)
    #     elif id==25:
    #         return lambda: self._connect(25), lambda: self._disconnect(25), lambda: self._reboot(25), lambda: self._takeoff_single(25), lambda: self._land_single(25)
    #     elif id==26:
    #         return lambda: self._connect(26), lambda: self._disconnect(26), lambda: self._reboot(26), lambda: self._takeoff_single(26), lambda: self._land_single(26)
    #     elif id==27:
    #         return lambda: self._connect(27), lambda: self._disconnect(27), lambda: self._reboot(27), lambda: self._takeoff_single(27), lambda: self._land_single(27)
    #     elif id==28:
    #         return lambda: self._connect(28), lambda: self._disconnect(28), lambda: self._reboot(28), lambda: self._takeoff_single(28), lambda: self._land_single(28)
    #     elif id==29:
    #         return lambda: self._connect(29), lambda: self._disconnect(29), lambda: self._reboot(29), lambda: self._takeoff_single(29), lambda: self._land_single(29)
    #     elif id==30:
    #         return lambda: self._connect(30), lambda: self._disconnect(30), lambda: self._reboot(30), lambda: self._takeoff_single(30), lambda: self._land_single(30)
    #     else:
    #         return lambda: self.main_gui.print_console("uav id not supported")