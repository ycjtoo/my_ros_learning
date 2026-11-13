import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PubNode(Node):
      def __init__(self,node_name):
        super().__init__(node_name)
        self.publisher_ = self.create_publisher(String,"traffic_status",10)
        self.is_red = True
        self.timer = self.create_timer(3.0,self.pub_callback)
        
      def pub_callback(self):
          msg=String()
          if self.is_red:
              msg.data ="当前是红灯"
          else:
              msg.data ="当前是绿灯"
          self.publisher_.publish(msg)
          self.get_logger().info(f"{msg.data}")
          self.is_red = not self.is_red


def main():
    rclpy.init()
    node=PubNode("light_publisher")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()
          

