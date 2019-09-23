#!/usr/bin/env python
# --- talker.py ------
# Version vom 17.09.2018 by OJ

import rospy
from std_msgs.msg import String
from turtlesim.msg import Pose
import geometry_msgs.msg

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    pub2 = rospy.Publisher('turtle1/cmd_vel', geometry_msgs.msg.Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "WHS - Hello python world %s" % rospy.get_time()
	
	angular = 0.0
	linear = 1.0
	cmd = geometry_msgs.msg.Twist()
	cmd.linear.x = linear
	cmd.angular.z = angular

        rospy.loginfo(hello_str)
        pub.publish(hello_str)
	pub2.publish(cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
