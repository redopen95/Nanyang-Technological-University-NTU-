#Question (10)

import numpy as np                                                              #Importing numpy fucntion into script

SalariesData=np.loadtxt('salaries_data.txt')                                    #Loading the salaries_data.txt file into the script
#Store each column of the array to a variable (column counting starts from 0)
EmployeeID = (SalariesData[:,0])                                                #1st column
Prevyr_Salaryperhour = (SalariesData[:,1])                                      #2nd column
Prevyr_Hoursworked = (SalariesData[:,2])                                        #3rd column
Curryear_Salaryperhour = (SalariesData[:,3])                                    #4th column
Curryear_Hoursworked = (SalariesData[:,4])                                      #5th column

CurrentYearTotalSalary = (Curryear_Salaryperhour*Curryear_Hoursworked)          #Calculates current year total salaries for employees
PreviousYearTotalSalary = (Prevyr_Salaryperhour*Prevyr_Hoursworked)             #Calculates previous year total salaries for employees

TotalSalaryIncrease = ((CurrentYearTotalSalary - PreviousYearTotalSalary)/PreviousYearTotalSalary)*100 #Express in terms of percentage
AvgTotalSalaryIncrease = (np.sum(TotalSalaryIncrease)/len(SalariesData[:,0]))   #Calculates the average salary increase for employees
HappyEmployee = TotalSalaryIncrease > 5                                         #Employees whose increase in total salary is more than 5%

#Printing output
print('The average total salary increase is %.4f' %AvgTotalSalaryIncrease,'%')  #Perecentage expressed in 4 decimal place
print('The following employee IDs got a total salary increase greater than 5 %s:\n %s'%('%',(EmployeeID[HappyEmployee]))) #Employee ID number