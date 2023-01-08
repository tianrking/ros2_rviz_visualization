import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
import random

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Range, 'topic', 10)
        
        self.ranges = [float('NaN'), 1.0, -float('Inf'), 3.0, float('Inf')]
        self.min_range = 0.1
        self.max_range = 1.0
        
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Range()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "/base_link"
        msg.radiation_type = 0
        msg.field_of_view = 0.1
        msg.min_range = self.min_range
        msg.max_range = self.max_range
        msg.range = random.uniform(0.1, 1)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publishemsg.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()