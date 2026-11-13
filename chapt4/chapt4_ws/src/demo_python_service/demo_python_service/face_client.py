import rclpy
from rclpy.node import Node
from chapt4_interfaces.srv import FaceDetector

class FaceClient(Node):
    def __init__(self):
        super().__init__('face_client_node')
        self.client_ = self.create_client(FaceDetector, 'face_detect')
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('等待服务器上线...')
            
        self.get_logger().info('服务器已上线，准备发送请求！')

    def send_request(self):
        request = FaceDetector.Request()
        self.future = self.client_.call_async(request) 
        self.future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        response = future.result()
        self.get_logger().info(f'收到服务端回复: {response}')

def main():
    rclpy.init()
    node = FaceClient()
    node.send_request()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()