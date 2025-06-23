"""
Forest Ray
June 3, 2025
"""

def orientation_vertical(fx, fy, bx, by, y_max):
	"""
	Calculates the orientation of the mouse with respect to the entire arena.
	If the mouse was pointing directly right, with the front more right than the back,
	the orientation would be 0. Orientation goes from 0 to 2pi as the mouse turns counter clockwise. 
	
			      pi/2
				^
			 	|
	   			|
	      			|
		       pi <-----|-----> 0
	    			|
	    			|
	       			|
		  		v
	     		      3pi/4
	
	- mouse pointing front first to right: angle = 0
	- mouse pointing front first up:       angle = pi/2
	- mouse pointing front first left:     angle = pi
	- mouse pointing front first down:     angle = 3pi/2
	
	For example, the front point could be the nose
	and the back point could be the tail base
	  		 	 __QQ
	 			(_)_"> front point
	            back point _)     
	
	Arguments:
	- fx    (float): x-coordinate of the front point
	- fy    (float): y-coordinate of the front point
	- bx    (float): x-coordinate of the back point 
	- by    (float): y-coordinate of the back point
	"""
	# the math library is used here for its inverse tangent function
	# and to generate nan values in the case of invalid coordinates
	import math 
  
	# there is a line going from the front point to the back point
	# get the slope of the line
	slope = (fy - by) / (fx - bx)
	# get the x_intercept of the line 
	xint = ((y_max-fy) / slope) + fx

	# calulate the angle 
	if ((fx > bx) and (fy < by)):
		"""
		if the front point is further to the right than the back point
		and if the front point is higher than the back 
		 
  		       pi/2
			^   front point
			|  /
   			| /
      			|/ back point
	       pi <-----|-----> 0
    			|
    			|
       			|
	  		v
     		      3pi/4
	     	"""
		length = fx - xint
		height = y_max - fy
		theta = math.atan(height/length)
	elif ((fx < bx) and (fy < by)):
		"""
		if the front point is further to the left than the back point 
		and if the front point is higher than the back point 

  
		       pi/2
			^  front point
			|  \
   			|   \
      			|    \ back point
	       pi <-----|-----> 0
    			|
    			|
       			|
	  		v
     		      3pi/4
  		"""
		length = xint - fx
		height = y_max - fy
		theta = math.pi - (math.atan(height/length))
	elif ((fx < bx) and (fy > by)):
		"""
		if the front point is further to the left than the back point
		and if the front point is lower than the backpoint

 		      pi/2
			^   back point
			|  /
   			| /
      			|/ front point
	       pi <-----|-----> 0
    			|
    			|
       			|
	  	        v
     		      3pi/4
  
  		"""
		length = bx - xint
		height = y_max - by
		theta = math.pi + (math.atan(height/length))
	elif ((fx > bx) and (fy > by)):
		"""
		if the front point is further to the right than the back point
		and if the front point is lower than the back point
 
		      pi/2
			^  back point
			|  \
   			|   \
      			|    \ front point
	       pi <-----|-----> 0
    			|
    			|
       			|
	  		v
     		      3pi/4
  		"""
		length = xint - bx
		height = y_max - by
		theta = (2*math.pi) - (math.atan(height/length))
	else:
		# in the case of invalid coordinates
		# return a nan value 
		theta = math.nan

	return theta 

def orientation_horizontal(rx, ry, lx, ly, y_max):
	"""
 	Calculates the orientation of the mouse with respect to the entire arena.
  	For when the user selected axis is between two points that lie on the same line horizontally.

   	Arguments:
    	- rx (float): x-coordinate of the right point
	- ry (float): y-coordinate of the right point
 	- lx (float): x-coordinate of the left point
  	- ly (float): y-coordinate of the left point
   	- y_max (float): maximum y-coordinate

    	Returns:
     	- theta (float): angle of orientation in radians
      	- slope (float): slope of the line between the two selected points
        - xint  (float): x-intercept of the line between the two selected points
	"""

	import math
	
	# Get the slope of the line between the right point and the back point
	slope = (ry - ly) / (rx - lx)
	# get the x-intercept of the line
	xint = ((y_max - ry) / slope) +rx

	if ((rx > lx) and (ry < ly)):
        # if the right point is further to the right than the left point
        # and if the right point is higher than the left point
        length = rx - xint
        height = y_max - ry
        theta = math.atan(height/length)
    elif ((rx < lx) and (ry < ly)):
        # if the right point is further to the left than the left point 
        # and if the right point is higher than the left point 
        length = xint - rx
        height = y_max - ry
        theta = math.pi - (math.atan(height/length))
    elif ((rx < lx) and (ry > ly)):
        # if the right point is further to the left than the left point
        # and if the right point is lower than the left point
        length = lx - xint
        height = y_max - ly
        theta = math.pi + (math.atan(height/length))
    elif ((rx > lx) and (ry > ly)):
        # if the right point is further right than the left point
        # if the right point is lower than the left point
        length = xint - lx
        height = y_max - ly
        theta = (2*math.pi) - (math.atan(height/length))
    else:
        theta = math.nan

    return theta, slope, xint
