import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
      def __init__(self):
         super().__init__('talker_node')
         self.publisher_ =self.create_publisher(String,'my_channel',10)
         self.timer = self.create_timer(2.0,self.timer_callback)
         self.count=0

      def timer_callback(self):
           msgs=String()
           self.count+=1
           msgs.data= f"我是广播站，这里是第{self.count}次播报"
           self.publisher_.publish(msgs)
           self.get_logger().info(f"发送消息{msgs.data}")

def main():
     rclpy.init()
     node=TalkerNode()
     rclpy.spin(node)
     rclpy.shutdown()

if __name__ =="__main__":
     main()    

           
        
