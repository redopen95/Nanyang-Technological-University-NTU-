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
        
        for i in range(5):                                                      #Loop over 5 rows
            for j in range(5):                                                  #Loop over 5 columns so total loop = 5 x 5 =25 times
                RowSumAverage[i]+=(MATRIX[i][j])/5                              #Compute sum of the values in each row of MATRIX independently and divide by 5
    
        for i in RowSumAverage: 
            if i<THRESHOLD:                                                     #If i<THRESHOLD, it fails the requirement
                RowSumAverage=[0,0,0,0,0]                                       #Average sum of the rows will be resetted back to 0 once there is failure
                CorrectRows=0                                                   #Number of correct rows will be resetted back to 0 once there is failure
                CountRetry+=1                                                   #Number of tries will increased by 1 each time it fails
                break                                                           #Command to break the loop
            
            else:
                CorrectRows+=1                                                  #If i>THRESHOLD, CorrectRows will increased by 1

    
    print('Congratulations! Solution matrix found!')                            #Printing output message
    print('Solution Matrix is: \n {}'.format(MATRIX))                           #Print solution matrix
    print('Average value for each row is: \n {}'.format(RowSumAverage))         #Print average value for each individual row
    print('Number of tries taken is: {}'.format(CountRetry))                    #Print number of tries taken to generate the solution matrix
    print('Number of correct rows is: {}'.format(CorrectRows))                  #Check to ensure that number of correct rows is 5 to satisfy the condition
