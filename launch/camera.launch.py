import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():



    return LaunchDescription([

        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            output='screen',
            namespace='camera',
            parameters=[{
                'image_size': [640,480],
		'output_encoding': "yuv422_yuy2",
                'camera_frame_id': 'camera_link_optical'
	    }]
	)
   ])
