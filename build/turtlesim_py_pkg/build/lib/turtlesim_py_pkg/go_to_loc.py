#!/usr/bin/env python3
import sys 
import math
import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class GoToLocationNode(Node): # 1
    def __init__(self):
        super().__init__("go_to_loc_node") # 2
        self.pose_threshold_linear = 0.3
        self.pose_threshold_angular = 0.03

        self.target_x = float(sys.argv[1]) # 0.0 - 11.0 [info: default loc_x ~ 5.5]
        self.target_y = float(sys.argv[2]) # 0.0 - 11.0 [info: default loc_y ~ 5.5]
        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose,10)
        self.timer = self.create_timer(1,self.turtle_controller)


        self.get_logger().info("Go To Location node has been started !")

    def callback_turtle_pose(self,msg):
        self.pose_ = msg
    def turtle_controller(self):
        msg = Twist()
        dist_x = self.target_x - self.pose_.x
        dist_y = self.target_y - self.pose_.y

        distance = math.sqrt(dist_x**2 + dist_y**2)
        target_theta = math.atan2(dist_y,dist_x)
        
        if abs(target_theta - self.pose_.theta) > self.pose_threshold_angular:  
            msg.angular.z = (target_theta - self.pose_.theta)
        else:  
            if distance >= self.pose_threshold_linear:
                msg.linear.x = distance
            else : 
                msg.linear.x = 0.0
                self.get_logger().info("Success ! ")

        self.publisher_.publish(msg)

def main(args = None):   
    rclpy.init(args=args)
    node = GoToLocationNode()# 3
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

 