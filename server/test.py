#!/usr/bin/env python
# license removed for brevity
import math

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def move(x,y,z):

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = defef(z)

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()
def defef(f):
    return math.sqrt(1-math.pow(f,2))
if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = move(0.57,0.65,0.7)
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
