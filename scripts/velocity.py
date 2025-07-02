# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 09:52:42 2025

@author: Forest
"""
def calculate_velocity(time, x_position, y_position):
    # create lists for storing values
    times = []
    velocities = []
    
    for i in range(0, len(time)-1):
        time_1 = time[i]
        time_2 = time[i+1]
        x_1 = x_position[i]
        x_2 = x_position[i+1]
        y_1 = y_position[i]
        y_2 = y_position[i+1]
        
        # calculate changes in position and time
        delta_x = x_2 - x_1
        delta_y = y_2 - y_1
        delta_t = time_2 - time_1

        # calculate velocity
        distance = ((delta_x**2)+(delta_y**2))**(1/2)
        velocities.append(distance/delta_t)
        times.append(time_2)

        return velocities, times 

def bin_velocities(time_window, velocities, times):
    
    # see how many velocity data points we have 
    num_data_points = len(velocities)        
        
    # number of velocity points should equal number time points
    if (num_data_points != len(times)):
        print("Error: Velocity and Time point number do not match")
        
    elif (num_data_points == len(times)):
        # max time / window size = number of windows
        num_windows = int((int(times[-1]))/time_window)
        
        # lists to hold values for each window
        binned_velocities = []
        binned_times = []
        
        # get velocity in each window
        for i in range(0, (num_windows-1)):
            # set time boundaries for window
            min_time_bound = i*time_window
            max_time_bound = (i+1)*time_window
            
            # store values in each loop
            loop_time = []
            loop_velocity = []
            
            for ii in range(0, len(velocities)):
                if((times[ii] > min_time_bound) and (times[ii] < max_time_bound)):
                    loop_time.append(times[ii])
                    loop_velocity.append(velocities[ii])
                    
            binned_velocities.append(loop_velocity)
            binned_times.append(binned_times)
        
        return binned_velocities, binned_times
    else:
        print("bin_velocities - An unknown error has occured.")
        return -1, -1