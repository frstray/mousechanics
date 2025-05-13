"""
Forest Ray
May 13, 2023
"""

def get_orientation(nx, ny, tx, ty, y_max):
"""
Calculates the orientation of the mouse in the arena. 
- mouse pointing nose first to right: angle = 0
- mouse pointing nose first up:       angle = pi/2
- mouse pointing nose first left:     angle = pi
- mouse pointing nose first down:     angle = 3pi/2

Arguments:
- nx    (float): x-coordinate of the nose
- ny    (float): y-coordinate of the nose
- tx    (float): x-coordinate of the tailbase 
- ty    (float): y-coordinate of the tailbase
- y_max (float): maximum y-coordinate 

Returns: 
- theta (float): angle of orientation in radians 
"""
	# the math library is used here for its inverse tangent function
	# and to generate nan values in the case of invalid coordinates
	import math 

	# there is a line going from the tip of the tail to the tail base
	# get the slope of the line
	slope = (ny - ty) / (nx - tx)
	# get the x_intercept of the line 
	xint = ((y_max-ny) / slope) + nx

	# calulate the angle 
	if ((nx > tx) and (ny < ty)):
		# if the nose is further to the right than the tailbase
		# and if the nose is higher than the tailbase 
		length = nx - xint
		height = y_max - ny
		theta = math.atan(height/length)
	elif ((nx < tx) and (ny < ty)):
		# if the nose is further to the left than the tailbase 
		# and if the nose is higher than the tailbase 
		length = xint - nx
		height = y_max - ny
		theta = math.pi - (math.atan(height/length))
	elif ((nx < tx) and (ny > ty)):
		# if the nose is further to the left than the tailbase
		# and if the nose is lower than the tailbase 
		length = tx - xint
		height = y_max - ty
		theta = math.pi + (math.atan(height/length))
	elif ((nx > tx) and (ny > ty)):
		# if the nose is further to the right than the tailbase
		# and if the nose is lower than the tailbase
		length = xint - tx
		height = y_max - ty
		theta = (2*math.pi) - (math.atan(height/length))
	else:
		# in the case of invalid coordinates
		# return a nan value 
		theta = math.nan

	return theta 