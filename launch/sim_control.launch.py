import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart

from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'mini_ocebot'

    launch_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'launch_sim.launch.py'
        )])
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
    )

    keyboard_control = Node(
        package="teleop_twist_keyboard",
        executable="teleop_twist_keyboard",
        remappings=[('/cmd_vel', '/diff_cont/cmd_vel_unstamped')]
    )
    
    delayed_keyboard_control = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=keyboard_control,
            on_start=[rviz],
        )
    )

    return LaunchDescription([
        launch_sim,
        rviz,
        delayed_keyboard_control,
    ])