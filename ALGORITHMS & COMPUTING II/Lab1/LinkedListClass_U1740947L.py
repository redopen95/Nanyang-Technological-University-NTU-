class Node:                                                                     #Creating a class of Node
    def __init__(self,initializedata):                                          #Initialize the attributes of the class
        self.data = initializedata
        self.next = None
        self.prev = None

A = Node('A')                                                                   #Creating Nodes with Alphabet element inside
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
X = Node('X')
Y = Node('Y')
Z = Node('Z')

class LinkedList:                                                               #Creating a class of LinkedList
    def __init__(self):                                                         #Creating the head and tail nodes as base case
        self.head = Node('Head')                                                #Head is empty
        self.tail = Node('Tail')                                                #Tail is empty
        self.size = 0                                                           #Size of the head and tail is 0
        self.head.next = self.tail                                              #Linking the head to tail
        self.tail.prev = self.head                                              #Linking the tail to head

    def firstNodes(self):                                                       #Defining functions to return the position of the first element in the LinkedList
        if self.size == 0:                                                      #If size of the LinkedList is empty
            print('NULL')                                                       #Returning empty
        else:                                                                   #Otherwise conditions
            return self.head.next.data                                          #Return the desired output
    
    def lastNodes(self):                                                        #Defining functions to return the position of the last element in the LinkedList
        if self.size == 0:                                                      #If size of the LinkedList is empty
            print('NULL')                                                       #Returning empty
        else:                                                                   #Otherwise conditions
            return self.tail.prev.data                                          #Return the desired output
    
    def beforeNodes(self,ReferenceElement):                                     #Defining functions to return the node immediately before a given reference node
        n = self.head                                                           #Let n be the head
        if ReferenceElement == self.head.next:                                  #Means its the first element straight after head
            return 'Null'                                                       #Means this is head
        else:                                                                   #Otherwise conditions
            return ReferenceElement.prev.data                                   #Return the previous node WRT to the given node
            
    def afterNodes(self,ReferenceElement):                                      #Defining functions to return the node immediately after a given reference node
        n = self.head                                                           #Let n be the head
        counter = 0                                                             #Initialize a counter to be 0 for counting purpose during the for loop
        for i in range(self.size):                                              #Ranging through the length of the LinkedList
            n = n.next                                                          #Making n take on the next value
            counter += 1                                                        #Increase count by 1 each loop
            if counter == self.size:                                            #If the counter is the same size as the LinkedList
                return 'Null'                                                   #Means the ReferenceElement is already in the last position, after that is tail already
            elif n == ReferenceElement:                                         #If n loop until it matches ReferenceElement
                return ReferenceElement.next.data                               #Return the value of the node immediately after the ReferenceElement
    
    def isEmpty(self):                                                          #Defining functions to check whether the LinkedList is empty
        if self.size == 0:                                                      #If its empty    
            return True                                                         #Return True Value
        else:                                                                   #If not
            return print('Not Empty')                                           #Means not empty
            
        
    def sizes(self):                                                            #Defining functions to return the number of elements in the LinkedList
        return self.size                                                        #Excluding the head and tail nodes
    
    
    def insertBeforeNodes(self,ReferenceElement,NewElement):                    #Defining functions to insert node before a given node    
        TempStorage = self.tail.prev                                            #Creating a temporary storage variable and assign it to be the last element before the tail
        while TempStorage != ReferenceElement and TempStorage.data != None:     #As long as the TempStorage and ReferenceElement is not the same value it will keep looping
            TempStorage = TempStorage.prev                                      #Make TempStorage take on the previous value
        TempStorage.prev.next = NewElement                                      #After they macthes: Eg existing (Head,A,C,D,Tail). Eg want add B before C. TempStorage.prev.next means the next after A link to new element B
        NewElement.next = ReferenceElement                                      #NewElement is B. Link to ReferenceElement which is C
        NewElement.prev = TempStorage.prev                                      #The previous of B is link to the previous old list C which is refering to A
        ReferenceElement.prev = NewElement                                      #The prev of C is linked to B 
        self.size +=1                                                           #size count increase by 1 each time
    
    def insertAfterNodes(self,ReferenceElement,NewElement):                     #Defining functions to insert node after a given node    
        TempStorage = self.head.next                                            #Creating a temporary storage variable and assign it to be the first element after head 
        while TempStorage != ReferenceElement and TempStorage.data != None:     #As long as the TempStorage and ReferenceElement is not the same value it will keep looping
            TempStorage = TempStorage.next                                      #Make TempStorage take on the next value
        TempStorage.next.prev = NewElement                                      #After they matches: Eg existing (Head,A,C,D,Tail). Eg want add E after C. TempStorage.prev.next means the the prev of D link to new element B
        NewElement.prev = ReferenceElement                                      #New element is E. The previous of E is link to reference element C
        NewElement.next = TempStorage.next                                      #next of E is link to the previous old list D
        ReferenceElement.next = NewElement                                      #The next of C is linked to new element E
        self.size += 1                                                          #size count increase by 1 each time
    
    def removeNodes(self,ReferenceElement):                                     #Defining functions to removed the given Node
        TempStorage = self.head.next                                            #Create a temporary storage variable and assign it to be the first element after head
        while TempStorage != ReferenceElement and TempStorage.data != None:     #As long as the TempStorage and ReferenceElement is not the same value it will keep looping
            TempStorage = TempStorage.next                                      #Make TempStorage take on the next value
        TempStorage.prev.next = ReferenceElement.next                           #After they matches: Eg existing (Head,A,B,C,Tail). Want to remove B. In this case will loop until TempStorage is B. The prev of B is A and want to link A to the next of B which is C
        TempStorage.next.prev = ReferenceElement.prev                           #Linking back the other way round
        self.size -= 1                                                          #Decrease size count by 1 each time
               
 
    def addNodes(self,Indexes,Element):                                         #Defining a function to add nodes with respect to the index into the LinkedList
        NewNode = Element                                                       #Let NewNode variable = input element
        n = self.head                                                           #Let n be the head  
        for i in range(Indexes):                                                #For loop to loop through the position
            n = n.next                                                          #Make n take on the next value
        n.next.prev = NewNode                                                   #Eg (0,A): Want to add A between Head and Tail, in this case n.next.prev = NewNode means before tail link to the NewNode
        NewNode.prev = n                                                        #Previous of NewNode link to the n in this case is the head
        NewNode.next = n.next                                                   #Next after NewNode link to n.next in this case is the tail
        n.next = NewNode                                                        #The next of n link to the NewNode
        self.size += 1                                                          #Increase size count by 1 each time    
    
    
    def printAllNodes(self):                                                    #Defining functions to print out all the nodes
        ListOfNodes = []                                                        #Create an empty list to be appended with nodes
        n=self.head                                                             #Let n be the head
        while n != None:                                                        #Keep continue looping when n is not = None
            ListOfNodes.append(n.data)                                          #Appending the nodes
            n=n.next                                                            #Making n take the next value
        print(ListOfNodes)                                                      #Printing output
    
    
TestingList = LinkedList()                                                      #Creating a Testing list with the data of LinkedList
TestingList.addNodes(0,A)                                                       #Adding Node('A') into the TestingList 1st position
TestingList.addNodes(1,B)                                                       #Adding Node('B') into the TestingList 2nd position
TestingList.addNodes(2,C)                                                       #Adding Node('C') into the TestingList 3rd position
TestingList.addNodes(3,X)                                                       #Adding Node('X') into the TestingList 4th position
TestingList.addNodes(4,Y)                                                       #Adding Node('Y') into the TestingList 5th position




print(TestingList.firstNodes())                                                 #Testing the result for first node
print(TestingList.lastNodes())                                                  #Testing the result for last node
print(TestingList.beforeNodes(B))                                               #Testing the result for before a given node
print(TestingList.afterNodes(B))                                                #Testing the result for after a given node
TestingList.isEmpty()                                                           #Testing whether the LinkedList is empty
TestingList.insertBeforeNodes(B,D)                                              #Inserting Node('D') immediately before Node('C')
TestingList.insertAfterNodes(B,E)                                               #Inserting Node('Z') immediately after Node('A')
TestingList.removeNodes(B)                                                      #Removing Node('B')
TestingList.printAllNodes()                                                     #Printing out the LinkedList
print(TestingList.sizes())                                                      #Checking the size of LinkedList