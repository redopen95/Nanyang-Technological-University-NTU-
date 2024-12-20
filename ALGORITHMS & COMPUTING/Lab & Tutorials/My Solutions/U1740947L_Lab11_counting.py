#Question (7)
Count_Present = 0                                                               #Initializing the counter to = 0

def counting(My_Slist,An_Integer):
    """This function counts the number of times an integer is present in a sorted list of integers
    Format of call: counting(My_Slist,An_Integer)
    Return: Number of times present
    """
    global Count_Present                                                        #Transforming the Count_Present = 0 into a global variable 

    if len(My_Slist) == 0:                                                      #If the length of the sorted list is 0
        Count_Present += 0                                                      #This will not increase the counts
    
    elif len(My_Slist) == 1:                                                    #If the length of the sorted list is 1
        if My_Slist[0] == An_Integer:                                           #If lucky the first element (0 index position) is equals to the An_Integer
            Count_Present += 1                                                  #This will increase the counts by 1
        else:                                                                   #Otherwise nothing happens to the counter
            Count_Present += 0
    
    while len(My_Slist) > 1:                                                    #For the cases where length of the sorted this is bigger than 1
        mid = int(len(My_Slist)/2)                                              #Making the middle point of the sorted list as an integer value to use as an index later
    
        if An_Integer == My_Slist[mid]:                                         #If the value of An_Integer equals to the value of My_Slist[mid] element
            Count_Present += 1                                                  #This increase the counts by 1
            del My_Slist[mid]                                                   #If the value is the same, delete the My_Slist[mid] to prevent repeating the comparison
            return counting(My_Slist,An_Integer)                                #Returning the output
   
        elif An_Integer < My_Slist[mid]:                                        #If the value of An_Integer is smaller than value of My_Slist[mid]
            return counting(My_Slist[:mid],An_Integer)                          #Return upper part(Smaller value numbers) of the My_Slist elements only
        
        else:                                                                   #If the value of An_Integer is bigger than value of My_Slist[mid]
            return counting(My_Slist[mid:],An_Integer)                          #Return lower part(Bigger value numbers) of the My_Slist elements only
    
    return Count_Present                                                        #Returning the counter value
