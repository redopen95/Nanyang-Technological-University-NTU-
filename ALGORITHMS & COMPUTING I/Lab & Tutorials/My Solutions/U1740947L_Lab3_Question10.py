# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:51:50 2017

@author: Hong Kai
"""

#Question10
import numpy as np#first have to load the NumPy package
myMat=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])#4x4 square matrix
myRandMat=np.random.rand(4,4)#4x4 square matrix filled with random values in [0,1)
myNewMat=(2*myMat)+(myRandMat)**2
print(myNewMat)
