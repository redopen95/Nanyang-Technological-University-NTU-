# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:39:17 2017

@author: SPMS2017
"""

#Question (10)
import random #First need to import random function
import numpy as np #First need to import numpy function

#Create a 3 rows x 4 columns size matrix of random integers in the range[10,99]
RanMatrix=np.random.randint(10,100,size=(3,4))

#Output Matrix (Free format)
print('The generated matrix is: \n %s'%(RanMatrix))

#Prompt user to enter a row value
Row=int(input('Please enter the row (Counting starts at 0):'))

#Prompt user to enter a column value
Column=int(input('Please enter the column (Counting starts at 0):'))

#Output: Sum of all elements of the entered row (in field of width 3)
Sum_Row=RanMatrix[Row][0]+RanMatrix[Row][1]+RanMatrix[Row][2]+RanMatrix[Row][3]
print('The sum of all elements of row %d is %3d'%(Row,Sum_Row))

#Output: Sum of all elements of the entered column (in field of width 3)
Sum_Column=RanMatrix[:,Column][0]+RanMatrix[:,Column][1]+RanMatrix[:,Column][2]
print('The sum of all elements of column %d is %3d'%(Column,Sum_Column))

 
