#Question (6)

n = int(input('Please input a value for n: '))                                  #Prompt the user to input a value for n
m = int(input('Please input a value for m: '))                                  #Prompt the user to input a value for m

def C(n,m):                                                                     #Defining recursive functions for C(n,m)

    if m==0 or m==n:                                                            #Conditions for the function
        return 1                                                                #If conditions are met, return value of 1
    elif m < 0 or n < 0 or n < m:                                               #If condition of 0 <= m <= n is not respected, return the value of -1
        return -1
    else:                                                                       #Otherwise, return value of C(n-1,m-1) + C(n-1,m)
        return C(n-1,m-1) + C(n-1,m)

print(C(n,m))                                                                   #Printing output

