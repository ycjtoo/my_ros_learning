import rclpy
from rclpy.node import Node 
from exercise_interfaces.srv import Area

class AreaServer(Node):
     def __init__(self):
          super().__init__('area_server')
          self.srv = self.create_service(Area,'calc_area',self.calculate_callback)
          self.get_logger().info("面积计算服务已启动，等待请求")

     def calculate_callback(self,request,response):
          width = request.width
          height = request.height

          response.area =width*height

          self.get_logger().info(f'收到请求，宽={width},高={height},面积={response.area}')

          return response

def main(args=None):
     rclpy.init(args=args)
     node=AreaServer()
     rclpy.spin(node)
     rclpy.shutdown()

if __name__ =='__init__':
     main()