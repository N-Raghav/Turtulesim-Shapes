#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import pi

def shapes():
    rospy.init_node("shapes")
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    s = input("Enter the shape you want\n1.Rectangle\n2.Triangle\n3.Square\n4.Star\n")

    if s == 'Rectangle':
        move = Twist()
        stop = Twist()
        while not rospy.is_shutdown():
            for i in range(2):
                # move lengthwise
                move.linear.x = 2.0
                move.angular.z = 0
                pub.publish(move)
                rospy.sleep(2.5)  # Adjust the sleep time to control the distance covered
                pub.publish(stop)
                # rotate
                move.linear.x = 0
                move.angular.z = -pi / 2
                pub.publish(move)
                rospy.sleep(1.5)  # Adjust the sleep time to control the rotation
                pub.publish(stop)
                # move breadthwise
                move.linear.x = 2.0
                move.angular.z = 0
                pub.publish(move)
                rospy.sleep(2.5)  # Adjust the sleep time to control the distance covered
                pub.publish(stop)
                # rotate
                move.linear.x = 0
                move.angular.z = -pi / 2
                pub.publish(move)
                rospy.sleep(1.5)  # Adjust the sleep time to control the rotation
                pub.publish(stop)

    elif s == "Triangle":
        move = Twist()
        stop = Twist()
        while not rospy.is_shutdown():
            for i in range(3):
                # move forward
                move.linear.x = 2.0
                move.angular.z = 0
                pub.publish(move)
                rospy.sleep(2.5)  # Adjust the sleep time to control the distance covered
                pub.publish(stop)
                # rotate
                move.linear.x = 0
                move.angular.z = 2 * pi / 3
                pub.publish(move)
                rospy.sleep(1.5)  # Adjust the sleep time to control the rotation
                pub.publish(stop)

    elif s == "Square":
        move = Twist()
        stop = Twist()
        while not rospy.is_shutdown():
            for i in range(4):
                # move forward
                move.linear.x = 2.0
                move.angular.z = 0
                pub.publish(move)
                rospy.sleep(2.5)  # Adjust the sleep time to control the distance covered
                pub.publish(stop)
                # rotate
                move.linear.x = 0
                move.angular.z = -pi / 2
                pub.publish(move)
                rospy.sleep(1.5)  # Adjust the sleep time to control the rotation
                pub.publish(stop)

    elif s == "Star":
        move = Twist()
        stop = Twist()
        while not rospy.is_shutdown():
            for i in range(5):
                # move forward
                move.linear.x = 2.0
                move.angular.z = 0
                pub.publish(move)
                rospy.sleep(2.5)  # Adjust the sleep time to control the distance covered
                pub.publish(stop)
                # rotate
                move.linear.x = 0
                move.angular.z = 4 * pi / 5
                pub.publish(move)
                rospy.sleep(1.5)  # Adjust the sleep time to control the rotation
                pub.publish(stop)

    else:
        rospy.loginfo("Enter a valid shape!!!!")


if __name__ == '__main__':
    shapes()

