#!/usr/bin/env python
# --- move.py ------
# Version vom 11.10.2019 by OJ
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

#---- unsere Klasse fuer die Turtle-Sim ------
class TurtleClass:
	#---- Konstruktor ---
    def __init__(self):  
    # Creates a node with name 'turtlebot_controller' and make sure it is a
    # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)
    # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.vel_msg = Twist() # Instanziierung eines Twist() Objektes => siehe import
		
        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',  Pose, self.update_pose)
        self.pose = Pose()  # Instanziierung eines Pose() Objektes => siehe import
        self.rate = rospy.Rate(10)

	#---- Empfangen der Pose ---
    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
	
        self.pose = data  #jetzt Member der Klasse => direkter Zugriff auf pose
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
	
	#---- Los gehts =>  Move the turtle ---       
    def move(self):           
        # Get the input from the user.
        goal_x = input("Set your global x goal: [0..12] ")
        goal_y = input("Set your global y goal: [0..12]")
        # Get start Position of Turtle - meanwhile received?
        
        #### HIER CODE EINFUEGEN #####
       
       
        # calculate way to go
        
        #### HIER CODE EINFUEGEN #####
        dist_x = 
        dist_y = 
        dist = 
        sollTheta = 

        rospy.loginfo("Start Pose is %s %s", start_x, start_y)
        rospy.loginfo("Way to Go %s ", dist)
        rospy.loginfo("Still to Go %s ", abs(self.pose.theta - sollTheta))
        
        # --- zuerst Drehen ----
        while abs(self.pose.theta - sollTheta) > 0.015:
            # nur [-pi...pi] erlaubt
            if self.pose.theta > math.pi:
				self.pose.theta =self.pose.theta-2*math.pi
            elif self.pose.theta < -math.pi:
				self.pose.theta =self.pose.theta+2*math.pi
                
            # kuerzere Drehrichtung berechnen => vel_msg.angular.z
            
            #### HIER CODE EINFUEGEN #####
            
            # Publishing our vel_msg
            self.velocity_publisher.publish(self.vel_msg)
            rospy.loginfo("Pose is %s", self.pose.theta)
            rospy.loginfo("Goal pose is %s", sollTheta)
            rospy.loginfo("Still to Go %s ", abs(self.pose.theta - sollTheta))
			# Publish at the desired rate.
            self.rate.sleep()
        
        # Stopping our robot after the movement is over.
        self.vel_msg.linear.x = 0
        self.vel_msg.angular.z = 0
        self.velocity_publisher.publish(self.vel_msg)

        #--- dann vorwaerts ---
        while sqrt(pow((start_x -self.pose.x),2)+pow((start_y -self.pose.y),2)) < abs(dist):
            # Linear velocity in the x-axis.
            self.vel_msg.linear.x = 0.2
            # Publishing our vel_msg
            self.velocity_publisher.publish(self.vel_msg)
            # Publish at the desired rate.
            self.rate.sleep()
           
            rospy.loginfo("Pose is %s %s", self.pose.x, self.pose.y)
            rospy.loginfo("Still to Go %s ", dist-sqrt(pow((start_x -self.pose.x),2)+pow((start_y -self.pose.y),2))  )
        # Stopping our robot after the movement is over.
        self.vel_msg.linear.x = 0
        self.vel_msg.angular.z = 0
        self.velocity_publisher.publish(self.vel_msg)
        exit()
        # If we press control + C, the node will stop.
        rospy.spin()

if __name__ == '__main__':
    try:
        turtle1 = TurtleClass()
        turtle1.move()
    except rospy.ROSInterruptException:
        pass

