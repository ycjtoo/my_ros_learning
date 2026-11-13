import rclpy
from rclpy.node import Node
from  exercise_interfaces.srv import Area

class ClientNode(Node):
    def __init__(self):
        super().__init__('area_client')

        self.client = self.create_client(Area,'calc_area')

        while not self.client.wait_for_service(timeout_sec=1.0):  #寻找并等待服务，通过循环防崩溃
            self.get_logger().info('等待服务上线')

        self.get_logger().info('服务端已上线')

    def send_request(self,w,h):
        request = Area.Request()
        request.width = float(w)
        request.height = float(h)
        self.get_logger().info(f'发送计量请求，宽={w},高={h}')
        self.future = self.client.call_async(request)  #异步发送
        self.future.add_done_callback(self.response_callback)  #绑定

    def response_callback(self,future):
        response = future.result() #拿到结果调用
        self.get_logger().info('面积为{response.area}')

    
    
def main(args=None):
        rclpy.init(args=args)
        node=ClientNode()
        node.send_request(5.0,10.0)
        rclpy.spin(node)
        rclpy.shutdown()

if __name__ =='__main__':
        main()

