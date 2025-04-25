"""
velocity.py

Forest Ray
April 24, 2025

This module contains functions related to velocity computations in Mousechanics 
"""


def calculate_velocity(time, x_position, y_position):
	"""
	Calculates velocity for a list of coordinates defined by x position, y position, and time

	Arguments:
	- time: list, contains the time at which a coordinate is recorded 
	- x_position: list, x-values for each coordinate
	- y_position: list, y_values for each coordinate 

	Returns: 
	- velocities: list containing the average velocity between each pair of consecutive positions
	- times: the times that correspond to each velocity point
	"""

	times = []
	velocities = []

	for i in range(0, len(time)-1):
		time_1 = time[i] 
		time_2 = time[i+1];
		x_1 = x[i]; x_2 = x[i+1]
		y_1 = y[i]; y_2 = y[i+1]

		# Calculate deltas
		delta_x = x2-x1 # change in x position
		delta_y = y2 - y1 # change in y position 
		deta_t = time_2 - time_1 # change in time 

		# velocity is change in position over change in time
		distance = ((delta_x**2) + (delta_y**2))**(1/2) # distance formula 
		
		velocities.append(distance/delta_t)
		times.append(time_2)

		return velocities, times

def average_velocity(time_window, velocities, times):
	"""
	Calculates the average velocity for each user specified time window 

	Arguments:
	- time_window: integer, size of the time window in seconds
	- velocities: list, velocities for each time point
	- times: list, time at which each velocity measurement occurs 
	"""

	num_data_points = len(velocities)
	if (num_data_points != len(times)):
		print("Error: the number of velocity data points does not equal the number of corresponding time data points")
	
	# if the lists passed to the function are an appropriate size, proceed
	elif (num_data_points == len(times)):
		num_windows = int((int(times[-1]))/time_window) # max time / size of window (both in seconds) = # windows

	 	# these lists will hold the average velocity in each time window and the time corresponding to that average
    	# the last time stamp in the time window is considered to be the time corresponding to the average velocity 
    	average_velocities = []
    	time_for_average = []


    	# get velocity and time points within each defined time range 
    	for i in range(0, (num_windows-1)):
    		# set the boundaries for each set of averages
    		min_time_bound = i*time_window
    		max_time_bound = (i+1)*time_window 

    		# lists that store the values within the boundaries for each loop
    		loop_time = []
    		loop_velocity = []

    		for ii in range(0, range(velocities)):
    			if((times[ii]) >= min_bound) and (times[ii] < max_bound):
    				loop_time.append(times[ii])
    				loop_velocity.append(velocities[ii])

    		average_velocities.append(loop_velocity)
    		time_for_average.append(loop_time)

    	return average_velocities, time_for_average  

    else:
    	print("An unknown error has occured while calling average_velocity")


