#!/usr/bin/env python
# ROS python API
import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import *
from mavros_msgs.srv import *
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import BatteryState
from geometry_msgs.msg import *
from std_msgs.msg import Float64


def velocity_callback(message):
    linear_x=message.twist.linear.x
    linear_y=message.twist.linear.y
    linear_z=message.twist.linear.z
    ##print("Velocity x = ",linear_x," Velocity y = ",linear_y," Velocity z = ",linear_z)

def status_callback(status):
    ##print("Drone's mode = "+status.mode)
    ##rospy.sleep(1)
    i=1
    

def battery_callback(message):
    ##print("Plane's battery = ",message.percentage*100)
    ##rospy.sleep(1)
    i=1

def localpose_callback(pose_info):
    roll=pose_info.pose.orientation.x
    pitch=pose_info.pose.orientation.y
    yaw=pose_info.pose.orientation.z
    ##print(" Roll = ",roll," Pitch = ",pitch," Yaw = ",yaw)
    ##rospy.sleep(1)

def compass_callback(message):
    compass_angle=message.data
    print("Compass angle = ",compass_angle)
    

def mission():
    rospy.init_node('the_node',anonymous=True)
    rospy.Subscriber('mavros/global_position/raw/gps_vel',TwistStamped,velocity_callback)
    rospy.Subscriber('mavros/state',State,status_callback)
    rospy.Subscriber('mavros/battery',BatteryState,battery_callback)
    rospy.Subscriber('mavros/local_position/pose',PoseStamped,localpose_callback)
    rospy.Subscriber('mavros/global_position/compass_hdg',Float64,compass_callback)
    
    rospy.sleep(20)



if __name__=="__main__":
    try: mission()
    except rospy.ROSInterruptException:
        pass
