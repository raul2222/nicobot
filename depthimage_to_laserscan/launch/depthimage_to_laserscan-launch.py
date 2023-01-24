# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# /* Author: Gary Liu */

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, launch_description_sources
from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import launch_ros.actions
import launch_ros.descriptions

def generate_launch_description():
  param_config = os.path.join(get_package_share_directory('depthimage_to_laserscan'), 'cfg', 'param.yaml')
  ld = LaunchDescription()

  node1= Node(
            package='depthimage_to_laserscan',
            executable='depthimage_to_laserscan_node',
            name='depthimage_to_laserscan_node',
            remappings=[('depth','/stereo/converted_depth'),
                        ('depth_camera_info', '/stereo/camera_info')],
            parameters=[param_config]
)
  ld.add_action(node1)


#### tf2 static transforms

## tf2 - base_footprint to laser
  node_tf2_fp2laser = Node(
    name='tf2_ros_fp_laser',
    package='tf2_ros',
    executable='static_transform_publisher',
    output='screen',
    arguments=['0', '0', '0', '0.0', '0.0', '0.0', 'base_footprint', 'face_link'],   
)
  ld.add_action(node_tf2_fp2laser)

## tf2 - base_footprint to map
  node_tf2_fp2map = Node(
    name='tf2_ros_fp_map',
    package='tf2_ros',
    executable='static_transform_publisher',
    output='screen',
    arguments=['0', '0', '0', '0.0', '0.0', '0.0', 'base_footprint', 'map'], 
)
  ld.add_action(node_tf2_fp2map)

## tf2 - base_footprint to odom
  node_tf2_fp2odom = Node(
    name='tf2_ros_fp_odom',
    package='tf2_ros',
    executable='static_transform_publisher',
    output='screen',
    arguments=['0', '0', '0', '0.0', '0.0', '0.0', 'base_footprint', 'odom'],
)
  ld.add_action(node_tf2_fp2odom)


## Later, at the end...
  return ld
