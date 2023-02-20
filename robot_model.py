# Alexa Rodriguez
import math
import numpy as np

def dh_transformation(theta, a, d, alpha):
	#receives the Denavit-Hartenberg parameters 
	trans = np.array([[math.cos(theta),  -math.sin(theta)*math.cos(alpha), math.sin(theta)*math.sin(alpha), a*math.cos(theta)],
				    [math.sin(theta), math.cos(theta)*math.cos(alpha), -math.cos(theta)*math.sin(alpha), a*math.sin(theta)],
				    [0.0, math.sin(alpha), math.cos(alpha), d],
					[0.0, 0.0, 0.0, 1.0]])
	# returns a combined homogenous transformation according to this convention. 		
	return trans

def kinematic_chain(twoDArray):
	# receives a 2D list/array containing the DH parameters of a robotic manipulator
	hTrans = np.array([[1.0,  0.0, 0.0, 0.0],
				    [0.0, 1.0, 0.0, 0.0],
				    [0.0, 0.0, 1.0, 0.0],
					[0.0, 0.0, 0.0, 1.0]]) 
	#set up a loop that scans the rows (joint parameters) and multiplies the transformation to get a total transformation.				
	for joint in twoDArray:
		# passes the DH parameters to the dh_transformation function
		DHresult = dh_transformation(joint[0], joint[1], joint[2], joint[3])
		# multiply matrix by total
		hTrans = np.matmul(hTrans, DHresult)
	# returns a homogenous transformation for the kinematic chain
	return hTrans
	

def get_pos(trans): 
# receives a homogeneous transformation as input and returns the x, y, z components of the position.
	x = trans[0][3]
	y = trans[1][3]
	z = trans[2][3]
	return x, y, z


def get_rot(trans): 
	# receives a homogeneous transformation as input and returns roll-pith-yaw angles
	# find roll by using the given formula
	roll = (math.atan2((trans[2][1]),(trans[2][2])))
	# find pitch by using the given formula
	pitch = (math.atan2(-(trans[2][0]), math.sqrt((trans[2][1])**2 + (trans[2][2] **2))))
	# find yaw by using the given formula
	yaw = (math.atan2((trans[1][0]), (trans[0][0])))
	# return the values
	return roll, pitch, yaw
