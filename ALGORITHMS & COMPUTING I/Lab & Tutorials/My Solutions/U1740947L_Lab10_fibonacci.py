#Question (10)
import time                                                                     #importing time functions into python

def r_fibonacci(numbers):                                                       #Defining Fibonacci numbers with recursive functions
    if numbers == 0:                                                            #Sequence starts with 0
        return 0                                                                #Return value 0
    elif numbers == 1:                                                          #Sequence starts with 1
        return 1                                                                #Return value 1
    else:                                                                       
        return r_fibonacci(numbers-1) + r_fibonacci(numbers-2)                  #Otherwise, return the sum of previous 2 Fibonacci numbers


start_recursive = time.clock()                                                  #Timer for timing how long the program took to calculate Fibonacci numbers using recursive functions
print(r_fibonacci(35))                                                          #Printing and calling function to calculate numbers = 35
RecursiveF_time = (time.clock()-start_recursive)
print('The time taken to caculate Fibonacci numbers using recursive functions is %f seconds' %(RecursiveF_time))




def i_fibonacci(numbers):                                                       #Defining Fibonacci numbers with iterative functions
    Starting_Sequence = [0,1]                                                   #Create a list of [0,1]
    for i in range(numbers):                                                    #Using for loops to range through (numbers)
        [Starting_Sequence[0],Starting_Sequence[1]] = [Starting_Sequence[1],Starting_Sequence[1] + Starting_Sequence[0]] #Using indexes to get the values
    return Starting_Sequence[0]                                                 #Returning the output 


start_iterative = time.clock()                                                  #Timer for timing how long the program took to calculate Fibonacci numbers using iterative functions
print(i_fibonacci(35))                                                          #Printing and calling function to calculate numbers = 35
IterativeF_time = (time.clock()-start_iterative)
print('The time taken to caculate Fibonacci numbers using iterative functions is %f seconds' %(IterativeF_time))

#Question: Which functions is easier to write?
#Answer: The recursive function is easier to write as the code is shorter and less complicated in terms of the steps
        #In this case there are only 1 general case and 2 base case to be considered

#Question: Which one is faster when calling the function for number=35?
#Answer: The iterative function works faster than recursive functions for calculating fibonacci numbers

#Question: Draw the tree of the successive recurisve calls to the function r_fibonacci (starting from F4)?
#Answer: 
    #At example F5,
    #r_fibonacci(5) .....layer 1
    #[r_fibonacci(4) + r_fibonacci(3)] .....layer 2
    #[[r_fibonacci(3) + r_fibonacci(2)]] + [[r_fibonacci(2) + r_fibonnaci(1)]].....Layer 3
    #[[[r_fibonacci(2) + r_fibonacci(1)]]] + [[[r_fibonacci(1) + r_fibonacci(0)]]] + [[[r_fibonnaci(1) + r_fibonacci(0)]]] .....Layer 4
    #[[[[r_fibonacci(1) + r_fibonacci(0)]]]] .....Layer 5
    #Return value = 5*1 + 3*0 = 5 (because there is 5 of r_fibonacci(1) which return 1 each + 3 of r_fibonacci(0) which return 0 each)
    
#Question: Explanation of the difference in timing?
#Answer: For recursive functions, there are multiple layers and in each layer there are mutiple values inside to be handled
#        If the number is too big, there will be many layers and many many more values in each layer to be handled
#        Hence the program will take longer to handle more datas, therefore recursive fuctions process takes longer time