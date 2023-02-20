# Test the robot
import math
import robot_model
# A: The two-link planar manipulator
def two_link_manipulator():
	# test values:
 	# joint 1: theta = pi/2, a = 1, d = 0, alpha = 0
 	# joint 2: theta = pi/2, a = 1, d = 0, alpha = 0
 	
 	# 2D array for parameters of each joint
 	parameters = [(math.pi/2), 1, 0, 0], [(math.pi/2), 1, 0, 0]
 	# passes parameters to kinematic_chain
 	hTrans = robot_model.kinematic_chain(parameters)
 	# get x, y, z
 	x, y, z = robot_model.get_pos(hTrans)
 	# get roll, pitch, yaw
 	roll, pitch, yaw = robot_model.get_rot(hTrans)
 	# print test results:
 	print('X: ' ,x, 'meters\n Y: ' ,y, 'meters\n Z: ' ,z, 'meters\n Roll: ' ,roll, 'radians\n Pitch: ' ,pitch, 'radians\n Yaw: ' ,yaw, 'radians')

# B: 6 DoF UR5e robot
# case 1	
def UR5e1():
	# insert parameters for joints 1-6 from the slides
	DHParameters = [[0, 0, 0.1625, math.pi/2],
					[0, -0.425, 0, 0],
					[0, -0.3922, 0, 0],
					[0, 0, 0.1333, math.pi/2],
					[0, 0, 0.0997, -math.pi/2], 
					[0, 0, 0.0996, 0]]
					
	# pass parameters and get homogeneous trans from kinematic_chain				
	hTrans = robot_model.kinematic_chain(DHParameters)
	# get x, y, z
	x, y, z = robot_model.get_pos(hTrans)
	# get roll, pitch, yaw
	roll, pitch, yaw = robot_model.get_rot(hTrans)
	# print test results:
	print('X: ' ,x, 'meters\n Y: ' ,y, 'meters\n Z: ' ,z, 'meters\n Roll: ' ,roll, 'radians\n Pitch: ' ,pitch, 'radians\n Yaw: ' ,yaw, 'radians')

# case 2: joint 2 theta = -pi/2
def UR5e2():
	# insert parameters for joints 1-6 from the slides
	DHParameters = [[0, 0, 0.1625, math.pi/2],
					[-math.pi/2, -0.425, 0, 0],
					[0, -0.3922, 0, 0],
					[0, 0, 0.1333, math.pi/2],
					[0, 0, 0.0997, -math.pi/2], 
					[0, 0, 0.0996, 0]]
					
	# pass parameters and get homogeneous trans from kinematic_chain			
	hTrans = robot_model.kinematic_chain(DHParameters)
	# get x, y, z
	x, y, z = robot_model.get_pos(hTrans)
	# get roll, pitch, yaw
	roll, pitch, yaw = robot_model.get_rot(hTrans)
	# print test results:
	print('X: ' ,x, 'meters\n Y: ' ,y, 'meters\n Z: ' ,z, 'meters\n Roll: ' ,roll, 'radians\n Pitch: ' ,pitch, 'radians\n Yaw: ' ,yaw, 'radians')
	
# show tests results 		
if __name__ == '__main__':
	print("Two-Link Planar Manipulator: ")
	two_link_manipulator()
	print("\nUR5e Case 1: ")
	UR5e1()
	print("\nUR5e Case 2: ")
	UR5e2()
