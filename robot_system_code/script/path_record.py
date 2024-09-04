import math
import rospy
from geometry_msgs.msg import Vector3Stamped
from nav_msgs.msg import Odometry


last = None

poses = []

def cb(data):
    global last
    cur = [data.pose.pose.position.y, -data.pose.pose.position.x]
    if not (last is None):
        if math.sqrt((last[0] - cur[0])**2 + (last[1] - cur[1]) ** 2) < 0.2:
            return
    print("saved")
    last = cur
    poses.append(cur)

def main():
    rospy.init_node('recorder', anonymous=True)
    cmdPub = rospy.Subscriber('/localization', Odometry, cb)
    rospy.spin()
    file = open('path.txt', 'w')
    for p in poses:
        file.write('%f %f\n' % (p[0], p[1]))
    file.close()

if __name__ == "__main__":
    main()

