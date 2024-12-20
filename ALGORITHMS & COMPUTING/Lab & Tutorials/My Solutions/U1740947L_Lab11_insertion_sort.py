#Question(5)

def insertion_sort(inlist):
    """ This function implements a sorting algorithm where it extract
    the elements of the inlist one at a time and placed into a outlist such
    such that outlist always remain a sorted list
    Format of call: insertion_sort(inlist)
    Returns: outlist
    """
    
    outlist=[]                                                                  #Initialized the outlist as an empty list
    outlist.append(inlist[0])                                                   #Appending the outlist with the element of 0 index of inlist
    inlist.pop(0)                                                               #Popping out the element of 0 index of the inlist                                                                 
    
    for inlist_numbers in inlist:                                               #For loops for inlist
        for outlist_numbers in range(len(outlist)):                             #For loops for ranging through outlist
            if inlist_numbers < outlist[outlist_numbers]:                       #Comparing the inlist_numbers with the outlist_numbers
                outlist.insert(outlist_numbers,inlist_numbers)                  #Inserting the inlist_numbers(smaller value) infront of outlist_numbers(bigger value)
                break                                                           #Breaking the for loops
        
        if inlist_numbers > outlist[len(outlist)-1]:                            #If inlist_numbers value is greater than last element value of outlist. Length counting starts from 1, index counting starts from 0 so need -1
            outlist.append(inlist_numbers)                                      #Appending the outlist with inlist_number(bigger value) 
            
    return outlist                                                              #Returns outlist value
        


