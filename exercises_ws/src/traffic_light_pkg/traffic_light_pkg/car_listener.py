import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubNode(Node):
      def __init__(self,node_name):
        super().__init__(node_name)
        self.subscription_ = self.create_subscription(String,"traffic_status",self.sub_callback,10)

      def sub_callback(self,msg):
           if msg.data =="当前是红灯":
              self.get_logger().info(f"{msg.data},停车等待")
           else:
              self.get_logger().info(f"{msg.data},加速通过")

def main():
    rclpy.init()
    node=SubNode("car_listener")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()
          