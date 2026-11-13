import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import time
import threading
from queue import Queue

class ListenerNode(Node):
      def __init__(self):
          super().__init__('listenernode')
          self.msg_queue=Queue()
          self.worker_thread = threading.Thread(target=self.process_data)
          self.worker_thread.start()
          self.subscription = self.create_subscription(String,'my_channel',self.listener_callback,10)

      def listener_callback(self,msg):
           self.msg_queue.put(msg.data)
           self.get_logger().info(f"收到消息，已存入队列，当前队列数{self.msg_queue.qsize()}")

      def process_data(self):
           while rclpy.ok():
               if not self.msg_queue.empty():
                    data=self.msg_queue.get()
                    time.sleep(3)
                    self.get_logger().info(f"处理完毕{data}")


def main():
     rclpy.init()
     node=ListenerNode()
     rclpy.spin(node)
     rclpy.shutdown()

if __name__ == "__main__":
     main()           

































