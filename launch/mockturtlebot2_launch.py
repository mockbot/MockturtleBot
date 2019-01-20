"""Launch Mockturtlebot"""

from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='Mockturtledriver', node_executable='pymatadriver.py', output='screen'),
        launch_ros.actions.Node(
            package='Mockturtlebot2', node_executable='pytreesdriver.py', output='screen'),
])

