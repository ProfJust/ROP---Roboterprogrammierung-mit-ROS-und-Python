#!/usr/bin/env python
# --- listener.py ------
# Version vom 17.09.2018 by OJ+
# 11.10.2018 Ausgabe der TurtleSim Positions
import rospy
from std_msgs.msg import String
from turtlesim.msg import Pose

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "  I heard %s", data.data)
    #rospy.loginfo(rospy.get_caller_id() + "x %s  y %s  theta %s", data.x, data.y, data.theta)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    
    rospy.Subscriber("chatter", String, callback)

    #rospy.Subscriber("turtle1/pose", Pose, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
