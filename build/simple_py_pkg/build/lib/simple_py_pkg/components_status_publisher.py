#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from simple_interfaces_pkg.msg import ComponentsStatus
class ComponentsStatusPublisherNode(Node): # 1
    def __init__(self):
        super().__init__("components_status_publisher") # 2
        self.components_status_publisher_ = self.create_publisher(ComponentsStatus,"components_status",10)

        self.time = self.create_timer(1.0, self.publish_components_status)
        self.get_logger().info("Components Statust has been published !")

    def publish_components_status(self):
        msg = ComponentsStatus()
        msg.camera_is_ready = True
        msg.lidar_is_ready = True
        msg.motor_is_ready = True
        msg.debug_message = "Everthing is going well !"
        self.components_status_publisher_.publish(msg)

def main(args = None):   
    rclpy.init(args=args)
    node = ComponentsStatusPublisherNode()# 3
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

