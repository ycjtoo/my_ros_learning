import launch
import launch_ros

def generate_launch_description():
    action_declare_arg_background_g = launch.actions.DeclareLaunchArgument('launch_arg_bg',default_value="150")

    action_node_turtlesim_node =launch_ros.actions.Node(
        package='turtlesim',
        executable='turtlesim_node',
        parameters=[{'background_g': launch.substitutions.LaunchConfiguration
        ('launch_arg_bg',default="150")}],
        output='screen'
    )

    action_node_face_client =launch_ros.actions.Node(
        package='demo_python_service',
        executable='face_client',
        output='log'
    )

    action_node_face_detect =launch_ros.actions.Node(
        package='demo_python_service',
        executable='face_detect_node',
        output='both'
    )

    return launch.LaunchDescription([
        action_node_turtlesim_node,
        action_node_face_client,
        action_node_face_detect,
        action_declare_arg_background_g,
    ])