#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def talker():

  pub = rospy.Publisher('pettersson', Int32, queue_size=10)
  # Tells rospy the name of the node, which is needed for comunication with rosmaster
  rospy.init_node('loop_publisher', anonymous=True)
  rate = rospy.Rate(0.5) # 10hz
  n = 4
  k = 0

  while not rospy.is_shutdown():
    # Create the message which is to be published
    message = k
    # Print the message to infofile/ terminal
    rospy.loginfo(message)
    # Publish the message
    pub.publish(message)
    # increase k by the value of n for each iteration
    k += n
    rate.sleep()

if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass