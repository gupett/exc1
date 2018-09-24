#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

'''
Do not forget to source worskpace every time opening a new terminal 
source ./delev/setup.bash
Do not forget to make python file executable everytime creating a new pyhon node
chmod +x file_name.py
'''

class Listener(object):
    """docstring for listener"""
    def __init__(self):
        # In ROS, nodes are uniquely named. If two nodes with the same
        # node are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('listener', anonymous=True)
        # set the csllback function for the topic 'pettersson'
        rospy.Subscriber("pettersson", Int32, self.callback)
        # define an instance of a publisher
        self.publisher = rospy.Publisher('kthfs/result', Int32, queue_size=10)


    def run(self):
        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()
        
    def callback(self, data):
        # the message should be devided by q (q=0.15)
        val = data.data / 0.15
        # printing the received value to file/ terminal
        rospy.loginfo("I heard %d, and published %d", data.data, val)
        # publishing the new value to topic 'kthfs/reult'
        # ensures that a new message is published with the same frequency as the received one
        self.publisher.publish(val)


if __name__ == '__main__':
    listener = Listener()
    listener.run()