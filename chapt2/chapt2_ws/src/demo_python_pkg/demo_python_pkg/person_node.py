import rclpy
from rclpy.node import Node


class PersonNode(Node):
    def __init__(self,node_name:str,name:str,age:int) :
        super(). __init__(node_name)
        self.name=name
        self.age=age

    def eat(self,food_name:str):
        #print (f"{self.name},{self.age}岁,爱吃{food_name}")
        """
        方法：吃东西
        :food_name 食物东西

        """
        self.get_logger().info(f"{self.name},{self.age}岁，爱吃{food_name}")


def main():
    rclpy.init()
    node=PersonNode('Too_node',"Too",18) 
    node.eat("鱼香肉丝") 
    rclpy.spin(node)
    rclpy.shutdown()  