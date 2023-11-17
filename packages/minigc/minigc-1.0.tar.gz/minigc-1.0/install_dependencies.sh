#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

cd ~

# If you use Ubuntu20 and have ROS noetic installed, then tkinter and ROS lib are well installed.
# If you use Ubuntu18 and ROS melodic, whose default python version is 2 rather than 3. Execute the following commands:
sudo apt install python3-pip -y # pip3
sudo apt install python3-tk -y # python3 tkinter
pip3 install rospkg # ros python3 lib


# Install python lib
pip3 install pyyaml


# Install vrpn  # change 'noetic' into 'melodic' for ubuntu18:
sudo apt install -y ros-noetic-vrpn-client-ros


# Install mavros # change 'noetic' into 'melodic' for ubuntu18:
sudo apt install ros-noetic-mavros ros-noetic-mavros-extras -y
wget https://gitee.com/shu-peixuan/px4mocap/raw/85b46df9912338f775949903841160c873af4a1d/ROS-install-command/install_geographiclib_datasets.sh
sudo chmod a+x ./install_geographiclib_datasets.sh
sudo ./install_geographiclib_datasets.sh # this step takes some time


# If you use UWB for positioning, then you should build `nlink_parser` (https://www.nooploop.com/download) ROS package for nooploop UWB module:
cd ~
mkdir -p nlink_parser_ws/src
cd nlink_parser_ws/src
git clone --recursive https://gitee.com/shu-peixuan/nlink_parser.git
cd ../
catkin_make
catkin_make
echo "source ~/nlink_parser_ws/devel/setup.bash" >> ~/.bashrc
