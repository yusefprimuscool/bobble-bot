import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):

    def __init__(self):
        super().__init__('my_talker')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.count = 0
        self.timer = self.create_timer(1.0, self.send_message)

    def send_message(self):
        msg = String()
        msg.data = f'Hello from Yusef: {self.count}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.count += 1


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()