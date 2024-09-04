import math
import rospy
import tf
from geometry_msgs.msg import Vector3Stamped, Twist
from nav_msgs.msg import Odometry

yaw_off = 0
v_off = 1
rx_off = 2
ry_off = 3
L_off = 4
maxAngle_off = 5

car = [0,0,0,0,0.68,50]#25.7]

rPath = []

def read_path():
    global rPath
    file = open('/home/imrl/Desktop/path.txt')
    #for line in file.readlines()[11:]:
    for line in file.readlines():
       # x = [-float(p.strip()) for p in line.split(' ')]
       # rPath.append([x[2], x[0]])
       x = [float(p.strip()) for  p in line.split(' ')]
       rPath.append(x)
    # rPath = [[-float(p.strip()) for p in line.split(' ')] for line in file.readlines()[11:]]
    file.close()

old_ind = 0

def calc_target_index():
    thres = 4
    global old_ind
    min = 9999999
    minn = old_ind
    global rPath
    global car
    for i in range(len(rPath)):
        if i < old_ind: continue
        if i - minn > thres: break
        dx = car[rx_off] - rPath[i][0]
        dy = car[ry_off] - rPath[i][1]
        d = math.sqrt(dx**2+dy**2)
        if min > d:
            min = d
            minn = i
    ind = minn
    temp_ind = ind
    print("ind")
    print(ind)
    l = 0.0
    Lf = 1.0#2.0
    while Lf > l and (ind + 1) < len(rPath):
        dx = rPath[ind+1][0] - rPath[ind][0]
        dy = rPath[ind+1][1] - rPath[ind][1]
        l += math.sqrt(dx**2+dy**2)
        ind += 1
    old_ind = temp_ind
    return ind

def pure_pursuit_control():
    target_ind = calc_target_index()
    print("target_ind")
    print(target_ind)
    global car
    global rPath
    #target_ind = target_ind-1
    print("Present robot pose:")
    print(car[rx_off],car[ry_off])
    print("target_ind:")
    print(target_ind)
    print("waypoint:")
    print(rPath[target_ind])

    alpha = car[yaw_off] - math.atan2(rPath[target_ind][0] - car[rx_off], rPath[target_ind][1] - car[ry_off])
    #alpha = car[yaw_off] - math.atan2(rPath[target_ind][1] - car[ry_off], rPath[target_ind][0] - car[rx_off])
    print("car[yaw_off]:")
    print(car[yaw_off]/3.14*180)
    Lf= 2.0
    phi = math.atan2(2.0 * car[L_off] * math.sin(-alpha) / Lf , 1.0)
    
    print("phi:")
    print(phi)   
    
    max_rotate = car[maxAngle_off] / 180.0 * math.pi
    if phi > max_rotate:
        phi = max_rotate
    if phi < -max_rotate:
        phi = -max_rotate
    return phi

def relocalCallback(msg):
    global car
   
    car[rx_off] = msg.pose.pose.position.y
    car[ry_off] = -msg.pose.pose.position.x
    
    #print("msg.pose.pose.orientation.x:")  
    #print(msg.pose.pose.orientation.x)  
    #print("msg.pose.pose.orientation.y:")  
    #print(msg.pose.pose.orientation.y) 
    #print("msg.pose.pose.orientation.z:")  
    #print(msg.pose.pose.orientation.z) 
    #print("msg.pose.pose.orientation.w:")  
    #print(msg.pose.pose.orientation.w) 
    
    yaw = quart_to_rpy(msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
    
    #??
    if yaw < math.pi:
        car[yaw_off] = yaw
    else:
        car[yaw_off] = -(yaw - 2 * math.pi)
    car[yaw_off] = -car[yaw_off]
    #print "car.x=%f, car.y=%f, car.yaw=%f" % (car[rx_off], car[ry_off], car[yaw_off])

def quart_to_rpy(x, y, z, w):
    roll = math.atan2(2 * (w * x + y * z), 1 - 2 * (x * x + y * y))
    pitch = math.asin(2 * (w * y - x * z))
    yaw = math.atan2(2 * (w * z + x * y), 1 - 2 * (z * z + y * y))
    #return roll, pitch, yaw
    return yaw

def main():
    read_path()
    rospy.init_node('pathFollow', anonymous=True)
    rate = rospy.Rate(10)
    rospy.Subscriber('/localization', Odometry, relocalCallback)
    pub = rospy.Publisher('/cmd_vel', Twist)
    while not rospy.is_shutdown():
        #-ip to pi
        angular = pure_pursuit_control()
        twist = Twist()
        twist.linear.x = 1
        twist.angular.z = angular
        
        print("twist.angular.z")
        print(twist.angular.z)
        pub.publish(twist)
        rate.sleep()
        global car
        if math.sqrt((car[rx_off] - rPath[-1][0]) ** 2 + (car[ry_off] - rPath[-1][1]) ** 2) < 0.5:
            # twist.linear.x = 0.0
            # twist.angular.z = 0.0
            # pub.publish(twist)
            # break
            global old_ind
            old_ind = 0

main()

