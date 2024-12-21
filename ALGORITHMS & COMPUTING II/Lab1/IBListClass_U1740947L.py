class IBList:                                                                   #Creating a class named IBList
                                                                                
    def __init__(self):                                                         #Initialize the attributes of a class
        self.data = []                                                          #Initialize the list as an empty list
    
    def get(self,indexes):                                                      #Defining function for get(r)
        if indexes < 0 or indexes > (len(self.data)-1):                         #Out of index condition
            return "Error"                                                      #Tells the user error
        else:                                                                   #If no issue
            return self.data[indexes]                                           #Extract and return the element with index r
    
    def sets(self,indexes,NewElement):                                          #Defining function for set(r,e)
        if indexes < 0 or indexes > (len(self.data)-1):                         #Out of index condition
            return "Error"
        else:                                                                   #If no issue
            TempStorage = self.data                                             #Create a temporary variable to store the data
            self.data[indexes] = NewElement                                     #Replacing the element of index r with the element e
            return TempStorage                                                  #Return the value of the updated list
        
    def add(self,indexes,NewElement):                                           #Defining function for add(r,e)
        if indexes < 0 or indexes > (len(self.data)):                           #Out of index condition. This case there is no -1 here
            return "Error"
        else:                                                                   #If no issue
            self.data.insert(indexes,NewElement)                                #Insert the new element e into the index r
            return self.data                                                    #Return the value of the updated list
    
    def remove(self,indexes):                                                   #Defining function for remove(r)
        if indexes < 0 or indexes > (len(self.data)-1):                         #Out of index condition
            return "Error"                                                      #If no issue
        else:
            return self.data.pop(indexes)                                       #Return the value of updated list that removes an element at index r
            
TestingList = IBList()                                                          #Creating a testing list to check whether correct results

print(TestingList.add(0,'A'))                                                   #Adding A to the 0 index

print(TestingList.add(0,'B'))                                                   #Adding B to the 0 index in this case will be placed infront of the previous A

print(TestingList.get(1))                                                       #Get the element with index 1

print(TestingList.sets(2,'C'))                                                  #Replace the element at index 2 with the element C which will result error as currently dont have index 2

print(TestingList.add(2,'C'))                                                   #Adding C to the 2nd index which is after A

print(TestingList.add(4,'D'))                                                   #Adding D to the 4th index which will result error

print(TestingList.remove(1))                                                    #Remove element at index 1 which is A

print(TestingList.add(1,'D'))                                                   #Addding D to the 1st index which will result [B,D,C]

print(TestingList.add(1,'E'))                                                   #Adding E to the 1st index which will result [B,E,D,C]

print(TestingList.get(4))                                                       #Get the element with index 4 but in this case will result error as currently index is up to 3 only

print(TestingList.add(4,'F'))                                                   #Adding element F to index 4 = [B,E,D,C,F]

print(TestingList.sets(2,'G'))                                                  #Replacing element at index 2 in this case is D and replace it with element G

print(TestingList.get(2))                                                       #Get the element with index 2 in this case is G
print(TestingList.data)                                                         #Check the final output