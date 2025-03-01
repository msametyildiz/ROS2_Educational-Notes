#!/usr/bin/env python3

# 1. Library 

import rclpy
from rclpy.node import Node

# 2. Method

def main(args=None):
    rclpy.init(args=args)
    node = Node("py_node")

    # print("hello world")
    node.get_logger().info("hello world")

    rclpy.spin(node)
    rclpy.shutdown()

# 3. "if __name__" block

if __name__== "__main__": # ben bu scripti çağırdığımda main methodunu çalıştır
    main()
