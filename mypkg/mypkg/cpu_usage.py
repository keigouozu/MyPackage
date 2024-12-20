import rclpy
import psutil
from rclpy.node import Node
from std_msgs.msg import Float32  


class CpuUsagePublisher(Node):
    def __init__(self):
        super().__init__("cpu_usage_publisher")
        self.publisher_ = self.create_publisher(Float32, "cpu_usage", 10)
        psutil.cpu_percent(interval=1.0)
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        cpu_usage = psutil.cpu_percent(interval=None)  
        msg = Float32()
        msg.data = cpu_usage
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing CPU usage: {cpu_usage}%")


def main():
    rclpy.init()
    node = CpuUsagePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
