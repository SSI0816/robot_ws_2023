import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile


class move_turtle(Node):
    def __init__(self):
        super().__init__('move_turtle')
        self.qos_profile = QoSProfile(depth = 10)
        self.move_turtle1 = self.create_publisher(Twist, 'turtle1/cmd_vel', self.qos_profile)
        self.timer = self.create_timer(0.1, self.turtle_move)
        self.velocity = 0.0

    def turtle_move(self):
        msg1 = Twist()
        msg1.linear.x = self.velocity
        msg1.linear.y = 0.0
        msg1.linear.z = 0.0

        msg1.angular.x = 1.0
        msg1.angular.y = 0.0
        msg1.angular.z = 1.0

        self.move_turtle1.publish(msg1)
        self.get_logger().info(f"Publisher message: {msg1.linear}, {msg1.angular}")

        self.velocity += 0.01


def main(args = None) :
    rclpy.init(args=args)
    node = move_turtle()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt!!!!')
    finally :
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__' :
    main()
