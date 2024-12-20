#Question (3)

import numpy as np                                                              #Import numpy function into the script
import matplotlib.pyplot as plt                                                 #Import plotting function into the script

SalariesData=np.loadtxt('salaries.dat',dtype=int)                               #Loading the salaries.dat file into the script & interpreting the data as integers
print('There are %d salaries in the file'%len(SalariesData[0]))                 #Print number of salaries entries in the salaries.dat file
print(SalariesData)                                                             #Print out the matrix for double checking

plt.figure(1)                                                                   #Plotting figure 1 as graph showing dependency of salary on the age
plt.axis([np.min(SalariesData[0])-3,np.max(SalariesData[0])+3,np.min(SalariesData[2])-3000,np.max(SalariesData[2])+3000]) #Set the range(min and max) for x-axis & y-axis
plt.plot(SalariesData[0],SalariesData[2],'b-')                                  #Plotting the graph using age and salaries with blue lines
plt.title('Dependency of the salary on the age')                                #Labeling the title as 'Dependency of salary on the age
plt.xlabel('Age')                                                               #Labeling x-axis as 'Age'
plt.ylabel('Salaries')                                                          #labeling y-axis as 'Salaries'

plt.show()                                                                      #Show the graph on the screen


plt.figure(2)                                                                   #Plotting figure 2 as graph showing dependency of salary on the years of experience
plt.axis([np.min(SalariesData[1])-3,np.max(SalariesData[1])+3,np.min(SalariesData[2])-3000,np.max(SalariesData[2])+3000]) #Set the range(min and max) for x-axis & y-axis
plt.plot(SalariesData[1],SalariesData[2],'g--')                                 #Plotting the graph using experience and salaries with dashed green lines
plt.title('Dependency of the salary on the years of experience')                #Labeling the title as 'Dependency of salary on the years of experience
plt.xlabel('Experience')                                                        #Labeling x-axis as 'Experience'
plt.ylabel('Salaries')                                                          #labeling y-axis as 'Salaries'

plt.show()                                                                      #Show the graph on the screen