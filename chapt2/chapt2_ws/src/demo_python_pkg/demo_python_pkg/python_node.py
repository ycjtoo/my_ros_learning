import rclpy #导入ROS2的官方Python库，导入模块
from rclpy.node import Node #Node是类，节点继承或实例化它

def main():
    rclpy.init() #初始化工作，分配资源，后台启动通信机制（DDS)
    node=Node('python_node') #创建节点
    node.get_logger().info('你好 Pythoon节点')#打印日志
    rclpy.spin(node) #运行节点，相当于一个死循环
    rclpy.shutdown()

