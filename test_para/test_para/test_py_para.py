import rclpy
from rclpy.node import Node

class Tparam(Node):
    def __init__(self):
        super().__init__("Tparam")
        self.declare_parameter('my_para', '내가만든파라미터')
        self.timer = self.create_timer(1, self.para)
        self.a = 'ssss'

    def para(self):
        my_para = self.get_parameter('my_para').get_parameter_value()._string_value # 외부에서 쓰지 말라고 개발자가 _를 앞에 씀
        my_para = self.get_parameter('my_para').get_parameter_value().string_value
        self.get_logger().info(f'파라미터를 출력합니다 {my_para}')
        self.get_logger().warn(f'파라미터를 출력합니다 {my_para}')

def main(args =None):
    rclpy.init()
    node = Tparam()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()