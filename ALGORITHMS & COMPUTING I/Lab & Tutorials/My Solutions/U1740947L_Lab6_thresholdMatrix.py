#Question (11)

import numpy as np                                                              #Import numpy function to be able to create matrix

THRESHOLD=float(input('Please enter a threshold value between 0 to 1: '))       #Prompt user to input a value between 0 to 1

if THRESHOLD <=0 or THRESHOLD >=1:                                              #Error check to ensure user only input values within the stated condition
    print('Threshold value can only be between 0 to 1 exclusively')

else:                                                                           #If no error, proceed on
    CorrectRows=0                                                               #Number of correct rows will start from 0
    CountRetry=0                                                                #Number of tries will start from 0
    RowSumAverage=[0,0,0,0,0]                                                   #Average Sum of the rows will start from 0
    
    while CorrectRows !=5:                                                      #The number of correct rows must be 5 in order to pass the requirement
                                                            
        MATRIX=np.random.rand(5,5)                                              #Generate 5x5 size matrix filled with random values in (0,1)
        
        for row in range(5):                                                      #Loop over 5 rows
            for col in range(5):                                                  #Loop over 5 columns so total loop = 5 x 5 =25 times
                RowSumAverage[row]+=(MATRIX[row][col])/5                              #Compute sum of the values in each row of MATRIX independently and divide by 5
        
        for i in RowSumAverage:                                                 #loop over RowSumAverage
            if i>THRESHOLD:                                                     #If i > input THRESHOLD value, condition satisfied
                CorrectRows+=1                                                  #Increase number of correct rows count by 1
                
            else:                                                               #If i < input THRESHOLD value, condition not satisfied
                RowSumAverage=[0,0,0,0,0]                                       #Resetting Average sum of rows back to 0
                CorrectRows=0                                                   #Resetting number of correct rows back to 0
                CountRetry+=1                                                   #Increase number of tries by 1
                break                                                           #Break the loop and restart the process


    
    print('Congratulations! Solution matrix found!')                            #Printing output message
    print('Solution Matrix is: \n {}'.format(MATRIX))                           #Print the solution matrix
    print('Average value for each row is: \n {}'.format(RowSumAverage))         #Print average value for each inidividual row
    print('Number of tries taken is: {}'.format(CountRetry))                    #Print number of tries taken to generate the solution matrix
    print('Number of correct rows is: {}'.format(CorrectRows))                  #Check to ensure that number of correct rows is 5 to satisfy the condition


