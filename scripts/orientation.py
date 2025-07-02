# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 09:07:03 2025

@author: Forest
"""
def orientation_vertical(fx, fy, bx, by, y_max):
    import math
    
    try:
        # get the slope of the line
        # going from front to back
        slope = (fy - by) / (fx - bx)
        # get the x-intercept
        xint = ((y_max-fy) / slope) + fx
    except ZeroDivisionError:
        # if the slop is zero, then 
        # the mouse is either facing 0
        # or 180 degrees 
        
        if (fx > bx):
            # if fx more right than bx
            theta = 0
        elif (fx < bx):
            # if fx more left than bx
            theta = math.pi
        else:
            # if an unknown error occurs
            # return a nan value 
            theta = math.nan
        
    
    # calculate the angle
    if ((fx > bx) and (fy < by)):
        # if the front is further right
        # and higher than the back
        
        length = fx - xint
        height = y_max - fy
        theta = math.atan(height/length)
    
    elif ((fx < bx) and (fy < by)):
        # if the front point is further left
        # and higher than the back point
        
        length = xint - fx
        height = y_max - fy
        theta = math.pi - (math.atan(height/length))
        
    elif ((fx < bx) and (fy > by)):
        # if the front point is further to the left
        # than the back point and if
        # the front is lower than the back
        
        length = bx - xint
        height = y_max - by
        theta = math.pi + (math.atan(height/length))
    
    elif ((fx > bx) and (fy > by)):
        # if the front point is further right
        # and lower than the back point
        
        length = xint - bx
        height = y_max - by
        theta = (2*math.pi) - (math.atan(height/length))
        
    else:
        # in the case of invalid coords
        theta = math.nan
    
    return theta
        
def orientation_horizontal(rx, ry, lx, ly, y_max):
    import math
    
    # get the slope of the line
    # between the right and left
    slope = (ry - ly) / (rx - lx)
    # get x-intercept
    xint = ((y_max - ry) / slope) + rx
    
    if ((rx > lx) and (ry < ly)):
        # if right point further right
        # and higher than left point
        
        length = rx - xint
        height = y_max - ry
        theta = math.atan(height/length)
        
    elif ((rx < lx) and (ry < ly)):
        # if right point further left
        # and higher than left
        length = xint - rx
        height = y_max - ry
        theta = math.pi - (math.atan(height/length))
        
    elif ((rx < lx) and (ry > ly)):
        # if right point further left
        # and lower than left point
        
        length = lx - xint
        height = y_max - ly
        theta = math.pi + (math.atan(height/length))
    
    elif ((rx > lx) and (ry > ly)):
        # if right point is further right
        # and lower than left point
        
        length = xint - lx 
        height = y_max - ly
        theta = (2*math.pi) - (math.atan(height/length))
    
    else:
        theta = math.nan
        
    return theta, slope, xint
        
    
        
