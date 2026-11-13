import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class WalkerNode(Node):
     def __init__(self):
      super().__init__('walker_')
      self.publisher_ =self.create_publisher(Twist,'/turtle1/cmd_vel' ,10)
      self.timer = self.create_timer(0.1,self.timer_callback)
      self.timer = self.create_timer(3.0,self.stop_callback)
      
     def timer_callback(self):
         msg=Twist()
         msg.linear.x = 2.0
         self.publisher_.publish(msg)

     def stop_callback(self):
           msg=Twist()
           msg.linear.x =1.0
           self.publisher_.publish(msg)    
       
def main():
    rclpy.init()
    node=WalkerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
     main()
       

           

         
            