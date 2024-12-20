#Question (11)

def Occurences(my_str,my_char):                                                 #Defining the function
    """This function computes and output the number of occurences of the character my_char in my_str
    In addition, this function will output the list of the occurences indexes
    Format of call: Occurences(my_str,my_char)"""
    
    List=[]                                                                     #Empty list
    Counter=0                                                                   #Counting of number of occurences starts from 0
    for (ind,SameAlphabet) in enumerate(my_str):                                #Enumerate function
        if SameAlphabet == my_char:                                             #If the user input character appears in the input string
            Counter +=1                                                         #When condition is met, the counter value increased by 1
            List.append(ind)                                                    #Appending the indexes into the empty list
    return(Counter,List)                                                        #Return the value of counter and list
    

my_str=input("Please enter a string: ")                                         #Prompts user to input a string
my_char=input("Please enter a character: ")                                     #Prompts user to input a character
(Characters,Index)=Occurences(my_str,my_char)                                   #Calls the function

                                                                                #Print the output
print('The number of occurence of my_char in my_str is %s and the list of occurences indexes is %s'%(Characters,Index))

