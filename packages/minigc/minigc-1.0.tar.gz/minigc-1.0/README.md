# minigc

Minigc is a python ground station GUI designed for Minidrone UAV swarm control and state displaying. This GUI is developed using `python3 tkinter`. 

<img src="pictures/minigc_img.png" alt="gui" align='left' style="zoom: 40%;" />

## Install

Environment: **python3**, **ROS1** **noetic**, ubuntu20

### Install dependencies

```bash
cd ~
git clone https://gitee.com/bhswift/minigc.git
cd minigc/
sudo chmod +x install_dependencies.sh
sudo ./install_dependencies.sh # make sure this step succeeds.
```

### Install minigc
- **Method 1** Install from PyPI:

```bash
pip3 install minigc --upgrade
```

- **Method 2 (recommended) **  Install from source:

```bash
cd minigc/
pip3 install -e . # do not neglect the dot '.' !!!
# pip install -e . # if you use ubuntu20 and have no pip3
# echo "export PATH=$PATH:~/.local/bin" >> ~/.bashrc   # optional
```

To uninstall:

```bash
pip3 uninstall minigc
```



## Usage

### Launch

First set minidrone ip and pose_source, markerset_name or uwb_tag_id in the `minigc/config/minidrone_config.yaml` (You can also change the config file path by clicking minigc browse button).

Launch the GUI by:

```bash
minigc # in a terminal (it will launch roscore if no rosmaster is on)
```

Press the number button and connect to the corresponding Minidrone. 

<font color=#EEB422>Yellow</font> means connecting. <font color=green>Green</font> means connected. Re-click the button will reconnect to the Minidrone.

The battery and position status will also display in different colors if connected. The <font color='green'>Green</font> means in good health.

### Positioning source

Minigc will forward the position data from either **UWB** or **motion capture system** to the uniform topic `/uav1/mavros/vision_pose/pose (geometry_msgs/PoseStamped)` depending on the `minidrone_config.yaml`. Then `mocap` or `nluwb` bar will turn <font color='green'>green</font> if the positioning source is streaming pose data, and it will turn <font color=#EEB422>yellow</font> if the positioning source data is not equal to the `mavros/local_position/pose` data, which means the the pose data is not accepted by the PX4 FCU.

#### 1. UWB

Connect the nooploop UWB console to the computer by USB. Choose the port and baud_rate in the GUI, then click the UWB switch button. It is equal to the following code:

```bash
roslaunch linktrack.launch port_name:="/dev/ttyXXX" baud_rate:="xxx"
```

In this UWB positioning mode, the height and orientation quaternion of Minidrones are get from the minidrone onboard sensor. Only x and y UWB data are adpoted by the drones.

#### 2. Motion capture system

Input the vrpn server IP in the GUI (the IP of the motion capture software computer), then click the vrpn switch button. It is equal to the following code:

```bash
# change the vrpn server ip according to your motion capture software computer IP.
roslaunch vrpn_client_ros sample.launch server:="192.168.xx.xxx"
```

Check `/uav1/mavros/local_position/pose` to see x, y, z and quaternion of Minidrone1 for example:

```bash
rostopic echo /uav1/mavros/local_position/pose
```



### Notice

1. **Do not close the gui by `Ctrl+C` in terminal!** Instead, press the `x` button on the top of the gui frame. It will close all the rosnode thoroughly.
2. Send x,y,z,yaw command to `/uav1/mavros/setpoint_raw/local` to control the Minidrone if connected.  **Place the head of the Minidrone to the world Y axis when powered on if the drone has no magnetometer.**



### Develop

Upload on PyPI:

```bash
sudo apt install twine -y
python3 setup.py sdist bdist_wheel
twine upload dist/*
```
