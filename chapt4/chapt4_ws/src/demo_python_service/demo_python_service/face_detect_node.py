import rclpy
from rclpy.node import Node
from chapt4_interfaces.srv import FaceDetector

class FaceDetectorNode(Node):
    def __init__(self):
        super().__init__('face_detect_node')
        self.declare_parameter('enable_log', True) 
        self.service_ = self.create_service(FaceDetector, 'face_detect', self.detect_callback)
        self.get_logger().info("服务端已启动，等待请求...")

    def detect_callback(self, request, response):
        is_log_enabled = self.get_parameter('enable_log').value
        
        if is_log_enabled:
            self.get_logger().info(" 收到客户端请求，开始处理！")
        else:
            self.get_logger().info(" 收到请求，但日志已被参数关闭。")
            
        response.result = "检测成功"
        return response

def main(args=None):
    rclpy.init(args=args)
    node = FaceDetectorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
