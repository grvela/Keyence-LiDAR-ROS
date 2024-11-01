import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from .KeyenceSZ16D import KeyenceSZ16D
from .FakerLaserData import FakeLaser

class CloudPointsPublisher(Node):
    def __init__(self):
        super().__init__('cloud_points_publisher')
        self.publisher = self.create_publisher(LaserScan, 'cloud_points_topic', 10)   
        self.timer = self.create_timer(0.120, self.laser_callback)
    
    def laser_callback(self):
        scan_response_in_s = 0.120
        num_points = 751

        laser = LaserScan()
        
        laser.header.frame_id = "frame_keyence_scan"
        laser.header.stamp = self.get_clock().now().to_msg()
        
        angle_min_in_rad = -0.785398 
        angle_max_in_rad = 3.92699
        angle_increment_in_rad = 0.006283185

        laser.angle_min = angle_min_in_rad
        laser.angle_max = angle_max_in_rad
        laser.angle_increment = angle_increment_in_rad
        
        laser.scan_time = scan_response_in_s
        laser.time_increment = scan_response_in_s / num_points
        
        range_min_in_m = 0.01
        range_max_in_m = 10.0

        laser.range_min = range_min_in_m
        laser.range_max = range_max_in_m

        laser_inputs = KeyenceSZ16D()

        laser.ranges = laser_inputs.get_laser_scan() 

        self.publisher.publish(laser)

        self.get_logger().info("Publishing: %s" % laser.ranges)

def main():

    rclpy.init()

    publisher = CloudPointsPublisher()

    rclpy.spin(publisher)

    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()