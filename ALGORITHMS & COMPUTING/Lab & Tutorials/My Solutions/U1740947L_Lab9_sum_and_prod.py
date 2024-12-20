#Question (9)

import numpy as np                                                              #importing the numpy function

def sum_and_prod(my_mat):                                                       #defining the functions of calculating sum and products 
    (rows,columns)=my_mat.shape                                                 #Returns the number of elements in each of the dimensions of the array
    
    my_product=1                                                                #Initializing the product = 1 instead of 0 should be done before the for loops
    my_sum=0                                                                    #Initializing the sum = 0 should be done before the for loops
    
    for r in range(rows):                                                       #The student forget to put the "range" word & ":" for the for loops rows and columns
        for c in range(columns):
            my_sum += my_mat[r,c]                                               #Calculating the sum of all the elements in the matrix
            my_product *= my_mat[r,c]                                           #Calculating the products of all the elements in the matrix
            
    return print(my_sum,my_product,my_mat)                                      #The student forget to put "print" after the word "return"            
                                                                                #Added my_mat in the return print to print out the matrix to check whether correct