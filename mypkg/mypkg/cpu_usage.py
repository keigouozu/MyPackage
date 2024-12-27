# SPDX-FileCopyrightText: 2024 Keigo Uozu
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
import psutil
from rclpy.node import Node
from std_msgs.msg import Float32  


class CpuUsage(Node):
    def __init__(self):
        super().__init__("cpu_usage")
        self.pub = self.create_publisher(Float32, "cpu_usage", 10)
        psutil.cpu_percent(interval=1.0)
        self.create_timer(1.0, self.cb)

    def cb(self):
        cpu_usage = psutil.cpu_percent(interval=None)  
        msg = Float32()
        msg.data = cpu_usage
        self.pub.publish(msg)
        self.get_logger().info(f"Current cpu usage: {cpu_usage:.1f}%")        

def main():
    rclpy.init()
    node = CpuUsage()
    try:
        rclpy.spin(node)
    except rclpy.executors.ExternalShutdownException:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()
