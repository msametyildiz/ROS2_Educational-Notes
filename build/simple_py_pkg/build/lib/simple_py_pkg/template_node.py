#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class CustomNodeName(Node): # 1
    def __init__(self):
        super().__init__("custom_node_name") # 2

def main(args = None):   
    rclpy.init(args=args)
    node = CustomNodeName()# 3
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

