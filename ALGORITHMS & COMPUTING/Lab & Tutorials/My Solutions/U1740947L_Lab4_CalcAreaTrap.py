# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 16:39:10 2017

@author: SPMS2017
"""

#Question (6)

#Ask the user for the value of parallel trapezoid length, a & b
Trapezoid_length_a=float(input('Enter length \'a\' of trapezoid in 2 decimal place:'))#parallel length
Trapezoid_length_b=float(input('Enter length \'b\' of trapezoid in 2 decimal place:'))#parallel length

#Ask the user for the value of trapezoid height, h
Trapezoid_height_h=float(input('Enter height \'h\' of trapezoid in 2 decimal place:'))#perpendicular height

#Calculate area of trapezoid
Area_of_trapezoid=Trapezoid_height_h*((Trapezoid_length_a+Trapezoid_length_b)/2)#Area of trapezoid = h*((length_a+length_b)/2)

#Output the result
print('Trapezoid area with length \'a\' %.2f and length \'b\' %.2f and height \'h\' %.2f is %.2f'%(Trapezoid_length_a,Trapezoid_length_b,Trapezoid_height_h,Area_of_trapezoid))


