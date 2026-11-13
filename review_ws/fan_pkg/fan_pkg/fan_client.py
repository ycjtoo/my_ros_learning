import rclpy
from rclpy.node import Node
from rcl_interfaces.srv import SetParameters
from rcl_interfaces.msg import Parameter,ParameterValue,ParameterType

class FanClient(Node):
      def __init__(self):
         super().__init__('fan_client')
         self.client = self.create_client(SetParameters,'/fan_server/set_parameters') #创建了一个客户端，目标就是去连上服务端的这个后台服务

         while not self.client.wait_for_service(timeout_sec=1.0):
               self.get_logger().info("等待服务端上线")
