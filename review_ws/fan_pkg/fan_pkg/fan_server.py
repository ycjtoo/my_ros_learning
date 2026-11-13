import rclpy
from rclpy.node import Node

class FanServer(Node):
    def __init__(self):
        super().__init__('fan_server')

        self.declare_parameter('speed',1)
        self.declare_parameter('is_on',True)

        self.add_on_set_parameters_callback(self.param_callback) #注册参数修改的回调事件，交给 self.param_callback 这个函数处理
        self.get_logger().info("监听参数变化中...")


    def param_callback(self,parameters):
        from rcl_interfaces.msg import SetParametersResult

        for param in parameters:
            if param.name =='speed':
                self.get_logger().info(f"已从旧档切换为{param.value}") #name为参数名，value为参数值
            elif param.name == 'is_on':
                self.get_logger().info(f"风扇状态变更为{param.value}")
        return SetParametersResult(successful=True)#这个修改合法，可改变参数

def main():
    rclpy.init()
    node = FanServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()