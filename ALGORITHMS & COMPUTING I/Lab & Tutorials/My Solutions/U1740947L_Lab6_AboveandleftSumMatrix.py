#Question (7)
import numpy as np                                                              #Import numpy function to be able to create matrix

ROW=int(input('Please enter the number of ROWS:'))                              #Prompt the user to enter the number of Rows
COLUMN=int(input('Please enter the number of COLUMNS:'))                        #Prompt the user to enter the number of Columns
                
MatrixSolution=np.zeros([ROW,COLUMN])                                           #Creates structure of matrix filled with zeros with the input values of rows and columns by the user

for i in range(ROW):                                                            #The value of each element in the first row is the number of the column
    MatrixSolution[i,0]=i+1                                                     #Row counting starts from 0
    
for j in range(COLUMN):                                                         #The value of each element in the first column is the number of the row
    MatrixSolution[0,j]=j+1                                                     #Column counting starts from 0

for i in range(1,ROW):                                                          #Looping the rows from the second row onwards
    for j in range(1,COLUMN):                                                   #Looping the columns from the second column onwards
        MatrixSolution[i,j]=MatrixSolution[i,j-1]+MatrixSolution[i-1,j]         #MatrixSolution[i,j] = Sum of the element above it & left to it

print(MatrixSolution)                                                           #Print output of the MatrixSolution
