# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:26:44 2017

@author: Hong Kai
"""

#Question (9)

import math #firstly need to input math functions into python

SelectFunction = str(input('Choose function \'A\' or \'B\' or \'C\': '))        #User select one function

if SelectFunction != 'A' and SelectFunction != 'B' and SelectFunction != 'C':   #Error checking
    print('Error! please choose functions A or B or C only! (Case Sensitive!)') #Can only choose 'A' or 'B' or 'C' only! Case sensitive!
    
else: 
    SelectX=float(input('Input an \'x\' value: '))                              #User input a 'x' value
    if SelectFunction == 'A':                                                   #If user select 'A'
        if SelectX <= 0:                                                        #If 'x' <= 0
            FunctionAns = SelectX+2                                             #A(x)=x+2
        elif SelectX > 0:                                                       #If 'x' > 0
            FunctionAns = SelectX/(math.sqrt(SelectX))                          #A(x) = x/(square root of x)
        print('A(x) = {}'.format(FunctionAns))                                  #print output for A(x)
    
    elif SelectFunction == 'B':                                                 #If user select 'B'
        FunctionAns = 2*(SelectX**6) + 3*SelectX - 2                            #B(x) = 2x**6 + 3*x -2
        print('B(x) = {}'.format(FunctionAns))                                  #print output for B(x)
    
    elif SelectFunction == 'C':                                                 #If user select 'C'
        if SelectX < -6:                                                        #If 'x' < -6
            FunctionAns = 6                                                     #C(x) = 6
        elif SelectX >= -6 and SelectX < 3:                                     #If 'x' >= -6 and x < 3
            FunctionAns = -SelectX                                              #C(x) = -x
        elif SelectX >= 3:                                                      #If 'x' >= 3
            FunctionAns = 0                                                     #C(x) = 0
        print('C(x) = {}'.format(FunctionAns))                                  #print output for C(x)
    
    
        
        
            
        

       
            
    