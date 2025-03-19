#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class ChannelNode(Node): # 1
    def __init__(self):
        super().__init__("channel_node") # 2
        self.greeting_ = "Hi awesome people :)"
        self.publisher_ = self.create_publisher(String, "channel_someting", 10)
        self.time_ = self.create_timer(0.5, self.publis_channel)
        self.get_logger().info("Channel someting has been published !")

    def publis_channel(self):
        msg = String()
        msg.data = str(self.greeting_) + "\nWelcome to the Channel Someting"
        self.publisher_.publish(msg)


def main(args = None):  
    rclpy.init(args=args)
    node = ChannelNode()# 3
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

