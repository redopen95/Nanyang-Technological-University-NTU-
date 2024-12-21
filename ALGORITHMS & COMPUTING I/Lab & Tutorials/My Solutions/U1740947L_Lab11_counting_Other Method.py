#Question (7)

def counting(My_Slist,An_Integer):
    """This function counts the number of times an integer is present in a sorted list of integers
    Format of call: counting(My_Slist,An_Integer)
    Return: Number of times a specific element is present in the list
    """
    print(My_Slist) #(Optional to put, just to print out and show how it works)
    if len(My_Slist) == 0:                                                      #If the length of the sorted list is 0
        return 0                                                                #Return value 0
    
    elif len(My_Slist) == 1:                                                    #If the length of the sorted list is 1
        if My_Slist[0] == An_Integer:                                           #If lucky the first element (0 index position) is equals to the An_Integer
            return 1                                                            #Return 1
        else:                                                                   #Otherwise when the condition of My_Slist[0] == An_Integer is not met
            return 0                                                            #Return value 0
    else:                                                                       #For the cases where length of the sorted this is bigger than 1
        mid = int(len(My_Slist)/2)                                              #Making the middle point of the sorted list as an integer value to use as an index later
   
        if An_Integer < My_Slist[mid]:                                          #If the value of An_Integer is smaller than value of My_Slist[mid]
            return counting(My_Slist[:mid],An_Integer)                          #Return upper part(Smaller value numbers) of the My_Slist elements only
        
        elif An_Integer > My_Slist[mid]:                                        #If the value of An_Integer is bigger than value of My_Slist[mid]
            return counting(My_Slist[mid:],An_Integer)                          #Return bottom part(Bigger value numbers) of the My_Slist elements only
        
        else:                                                                   #Else if is equal
            Count_Present = 0                                                   #Initializing the counter = 0
            for element in range(len((My_Slist))):                              #For loops to range through every element in the My_Slist
                if My_Slist[element] == An_Integer:                             #If they are the same integer number
                    Count_Present += 1                                          #Would increase the counter value by 1 each time it is the same integer number
    
            return Count_Present                                                #Returning the counter value
