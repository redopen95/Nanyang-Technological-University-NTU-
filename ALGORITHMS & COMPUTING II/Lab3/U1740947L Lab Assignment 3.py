# Matric Number: U1740947L

class TreeNode:                                                                 #Creating a class of TreeNode
    def __init__(self, initKey, initParent = None, initLeftChild = None, initRightChild = None): #Initialize the attributes of the class
        self.key = initKey                                                      #Create a node with the input key
        self.parent = initParent                                                #The created node will have no parent, no leftChild and no rightChild initially
        self.leftChild = initLeftChild
        self.rightChild = initRightChild


class BinarySearchTree:                                                         #Creating a class of BST
    def __init__(self, initRoot = None):                                        #Initialize the attributes of the class
        if initRoot != None:
            self.root = TreeNode(initRoot)                                      #Create a root from the input


    # IMPLEMENT HERE #
    def search(self, k):                                                        #Defining the search function for BST
        ReferenceNode = self.root                                               #Start the search from the root of BST
        NewNode = TreeNode(k)                                                   #Creating a new node with the key that is required to be searched
        
        while True:                                                             #Forcing the while loop to run
            if NewNode.key == ReferenceNode.key:                                #If the key are equal means found
                return ReferenceNode                                            #Returning the found key
            
            elif NewNode.key > ReferenceNode.key:                               #If the required key is bigger than the root means need search right side of the root
                if ReferenceNode.rightChild == None:                            #If there is no right child means nothing to search which means not found
                    return None                                                 #Return None if nothing is found
                elif ReferenceNode.rightChild.key == NewNode.key:               #If the keys are equal means found
                    return ReferenceNode.rightChild                             #Return the found key
                else:                                                               
                    ReferenceNode = ReferenceNode.rightChild                    #Else keep going right in the while loop
                    
            elif NewNode.key < ReferenceNode.key:                               #If the required key is smaller than the root means need search left side of the root
                if ReferenceNode.leftChild == None:                             #If there is no left child means nothing to search which means not found
                    return None                                                 #Return None if nothing is found
                elif ReferenceNode.leftChild.key == NewNode.key:                #If the keys are equal means found
                    return ReferenceNode.leftChild                              #Return the found key
                else:
                    ReferenceNode = ReferenceNode.leftChild                     #Else keep going left in the while loop
            
                                                            
    # IMPLEMENT HERE #
    def insert(self, k):                                                        #Defining insert function for BST
        NewNode = TreeNode(k)                                                   #Creating a new node with the key that is required to be inserted
        ReferenceNode = self.root                                               #Start the search from the root of BST
        
        if ReferenceNode.key == NewNode.key:                                    #Cannot insert same key
            print("Error! Key already existed in BST")
                
        while True:                                                             #Forcing the while loop to run
            if ReferenceNode.key > NewNode.key:                                 #If the root is bigger than the key to be inserted, means need insert on the left side
                if ReferenceNode.leftChild == None:                             #If there is no left child means just insert as the left child 
                    ReferenceNode.leftChild = NewNode                           #Link from top to bottom direction between the child and parent
                    NewNode.parent = ReferenceNode                              #Link from bottom to top direction between the child and parent
                    break                                                       #After successfully inserted the required key, need to break away from the while loop to prevent repeated insertion
                else:
                    ReferenceNode = ReferenceNode.leftChild                     #Else keep going left in the while loop
                    
                    
            if ReferenceNode.key < NewNode.key:                                 #If the root is smaller than the key to be inserted, means need insert on the right side
                if ReferenceNode.rightChild == None:                            #If there is no left child means just insert as the right child 
                    ReferenceNode.rightChild = NewNode                          #Link from top to bottom direction between the child and parent
                    NewNode.parent = ReferenceNode                              #Link from bottom to top direction between the child and parent
                    break                                                       #After successfully inserted the required key, need to break away from the while loop to prevent repeated insertion
                else:
                    ReferenceNode = ReferenceNode.rightChild                    #Else keep going right in the while loop
                    
                    
    
    # IMPLEMENT HERE #
    def delete(self, k):                                                        #Defining delete function for BST
        ReferenceNode = self.search(k)                                          #Using the search function to find the required key to be deleted

        if ReferenceNode == None:                                               #If the search function cannot find that key required to be deleted
            print("Invalid deletion choice")                                    #Means nothing to delete
            return None
        #Workable
        
        if ReferenceNode.leftChild == None and ReferenceNode.rightChild == None: #For leafs or external node
            if ReferenceNode.parent.leftChild == ReferenceNode:                 #Left external node
                ReferenceNode.parent.leftChild = None                           #Remove the child from the parent
            elif ReferenceNode.parent.rightChild == ReferenceNode:              #Right external node
                ReferenceNode.parent.rightChild = None                          #Remove the child from the parent

            ReferenceNode.parent = None                                         #Removing the link from the removed node from its parent
            
            if ReferenceNode == self.root:                                      #If the node that is to be deleted is the root with no child
                self.root = None                                                #Update the tree is empty with no root
        #Workable
                     
        elif ReferenceNode.leftChild != None and ReferenceNode.rightChild == None: #For internal node with only left child
            if ReferenceNode!= self.root:                                       #If the node to be deleted is not the root
                if ReferenceNode.parent.rightChild == ReferenceNode:            #If the node to be deleted itself is a right child
                    ReferenceNode.parent.rightChild = ReferenceNode.leftChild   #Link the original parent to its new child
                    ReferenceNode.leftChild.parent = ReferenceNode.parent       #Link the original child to its new parent
                    
            if ReferenceNode!= self.root:                                       #If the node to be deleted is not the root
                if ReferenceNode.parent.leftChild == ReferenceNode:             #If the node to be deleted itself is a left child
                    ReferenceNode.parent.leftChild = ReferenceNode.leftChild    #Link from top to bottom direction (original parent to its new child)
                    ReferenceNode.leftChild.parent = ReferenceNode.parent       #Link from bottom to top direction (Link the original child to its new parent)
            #else:
               # ReferenceNode.leftChild.parent = ReferenceNode.parent          
            ReferenceNode.parent = None                                         #Removing the link from the removed node from its parent
            ReferenceNode.leftChild = None                                      #Removing the link from the removed node from its left child
            
            if ReferenceNode == self.root:                                      #If the node that is to be deleted is the root with left child
                self.root = ReferenceNode.leftChild                             #Update the new root be the leftchild of reference node
        #Workable    
                
        elif ReferenceNode.leftChild == None and ReferenceNode.rightChild != None: #For internal node with only right child
            if ReferenceNode!= self.root:                                       #If the node to be deleted is not the root
                if ReferenceNode.parent.rightChild == ReferenceNode:            #If the node to be deleted itself is a right child
                    ReferenceNode.parent.rightChild = ReferenceNode.rightChild  #Link from top to bottom direction (original parent to its new child)
                    ReferenceNode.rightChild.parent = ReferenceNode.parent      #Link from bottom to top direction (Link the original child to its new parent)
                       
            if ReferenceNode!= self.root:                                       #If the node to be deleted is not the root
                if ReferenceNode.parent.leftChild == ReferenceNode:             #If the node to be deleted itself is a left child
                    ReferenceNode.parent.leftChild = ReferenceNode.rightChild   #Link from top to bottom direction (original parent to its new child)
                    ReferenceNode.rightChild.parent = ReferenceNode.parent      #Link from bottom to top direction (Link the original child to its new parent)
            
            ReferenceNode.parent = None                                         #Removing the link from the removed node from its parent
            ReferenceNode.rightChild = None                                     #Removing the link from the removed node from its right child
            
            if ReferenceNode == self.root:                                      #If the node that is to be deleted is the root with right child 
                self.root = ReferenceNode.rightChild                            #Update the new root be the rightchild of reference node
        #Workable
        
        elif ReferenceNode.leftChild != None and ReferenceNode.rightChild != None: #For internal node with both child
               
            TempNode = ReferenceNode.rightChild                                 #Jump down to the right of the tree by once
                
            while TempNode.leftChild != None:                                   #Start searching for the most left node after the jump 
                TempNode = TempNode.leftChild
            
            if ReferenceNode.rightChild != TempNode:                            #If traverse to left already
                if TempNode.rightChild == None:                                 #If got traverse to left already and no more right child
                    ReferenceNode.key = TempNode.key                            #Swap the ReferenceNode key to become TempNode key
                    TempNode.parent.leftChild = None                            #Remove the link from the parent from its left child
                elif TempNode.rightChild != None:                               #If got traverse to left already and also got right child
                    ReferenceNode.key = TempNode.key                            #Swap the ReferenceNode key to become TempNode key
                    TempNode.parent.leftChild = TempNode.rightChild             #Link from top to bottom direction (original parent to its new child)
                    TempNode.rightChild.parent = TempNode.parent                #Link from bottom to top direction (Link the original child to its new parent)
                    
            else:   #If ReferenceNode.rightChild == TempNode                    #If tempNode did not traverse to the left. Aka tempNode is reference node's right child.
                ReferenceNode.key = TempNode.key                                #Swap the value of the ReferenceNode key to TempNode key
                ReferenceNode.rightChild = TempNode.rightChild                  #Link from top to bottom direction (original parent to its new child)
                if TempNode.rightChild != None:                                 #If TempNode has right child
                    TempNode.rightChild.parent = TempNode.parent                #Link from bottom to top direction (Link the original child to its new parent)
                    
            
            TempNode.parent = None                                              #Removing the link from the removed node from its parent
            TempNode.leftChild = None                                           #Removing the link from the removed node from its left child
            TempNode.rightChild = None                                          #Removing the link from the removed node from its right child
        #Workable
        
        
    def inOrderNextTraversal(self, k):                                          #Defining the inOrder traversal function to work on for SearchByRange function
        if k.leftChild == None and k.rightChild == None:                        #If k is an external node means we must go back to the first node that which you are not a right child. This is the next node that we want
            while (k.parent).rightChild == k:                                   #Itself is still a right child
                k = k.parent                                                    #Let it become its parent
                if k.parent == None:                                            #If we reach the root, means this is the biggest number and has no next node
                    return None                                                 #Means cannot find its next inorder traversal node
            return k.parent                                                     #Return the next node (inOrder traversal) that we want

        elif k.rightChild != None:                                              #It is an internal with right child. If k is an internal node, we must go to its right subtree and find the leftmost node
            k = k.rightChild                                                    #Jump once to the right
            while k.leftChild != None:                                          #Tthe right child got left child
                k = k.leftChild                                                 #Keep go left child to find the furthest left child
            return k                                                            #Return the next node (inOrder traversal) that we want

        elif k.rightChild == None:                                              #It is an internal with no right chilf
            while (k.parent).rightChild == k:                                   #Itself is still a right child
                k = k.parent                                                    #Let it become its parent
                if k.parent == None:                                            #If we reach the root, means this is the biggest number and has no next node
                    return None                                                 #Means cannot find its next inorder traversal node
            return k.parent                                                     #Return the next node (inOrder) that we want
        
        
    
    def searchByRange(self, minimum, maximum):                                  #Defining the SearchByRange function
        ReferenceNode = self.root                                               #Start the search from the root
        while ReferenceNode.key != minimum:                                     #If the key value is not equal to the minimum boundary set
            if ReferenceNode.key > minimum:                                     #Search the left subtree until you reached an external node
                if ReferenceNode.leftChild == None:                             #If cannot find any further left child
                    ReferenceNode = ReferenceNode                               #Thats the value we want
                    break                                                       #Break the while loop
                else:
                    ReferenceNode = ReferenceNode.leftChild                     #Keep making the node become its next left child
            
            elif ReferenceNode.key < maximum:                                   #Search the right subtree until you reached a external node
                if ReferenceNode.rightChild == None:                            #If cannot find any further left child
                    ReferenceNode = ReferenceNode                               #Thats the value we want
                    break                                                       #Break the while loop
                else:
                    ReferenceNode = ReferenceNode.rightChild                    #Keep making the node become its next left child
                
        OutputList = []                                                         #Create empty list
        if ReferenceNode.key >= minimum and ReferenceNode.key <= maximum:       #The key values is in between the stated range
            OutputList.append(ReferenceNode)                                    #Start appending the node into the output list
            
        while ReferenceNode.key < maximum:                                      #As long as the updated key does not exceeds the maximum boundary
            
            NextNode = self.inOrderNextTraversal(ReferenceNode)                 #Calling the next traversal node 
            OutputList.append(NextNode)                                         #Appending the result into the outputlist
            ReferenceNode = NextNode                                            #Replacing the current node with its traversal next node
        
        return OutputList                                                       #Return the final output result
        
    
    
    def printTree(self):
        x = [self.root]              
        print("--------- Tree begins here ----------")
        NonEmptyLevel = True
        while NonEmptyLevel == True:
            y = []
            NonEmptyLevel = False
            for i in range(len(x)):
                if x[i] != None:
                    print(x[i].key, end=' ')
                    NonEmptyLevel = True
                    y += [x[i].leftChild, x[i].rightChild]
                else:
                    print(' ', end=' ')
            x = y
            print()
        print("--------- Tree ends here -------------")


bst = BinarySearchTree('H')
print("Initializing the tree with 'H'")
bst.printTree()
bst.insert('B')
print("Inserting 'B'")
bst.printTree()
bst.insert('M')
print("Inserting 'M'")
bst.printTree()
bst.insert('A')
print("Inserting 'A'")
bst.printTree()
bst.insert('E')
print("Inserting 'E'")
bst.printTree()
bst.insert('C')
print("Inserting 'C'")
bst.printTree()
bst.insert('D')
print("Inserting 'D'")
bst.printTree()
bst.insert('L')
print("Inserting 'L'")
bst.printTree()
bst.insert('N')
print("Inserting 'N'")
bst.printTree()
found = bst.searchByRange('B', 'M')
print("Searching by the range (minimum = 'B', maximum='M')")
for i in range(len(found)):
    print(found[i].key, end=' ')
print()
bst.delete('B')
print("Deleting 'B'")
bst.printTree()
bst.delete('A')
print("Deleting 'A'")
bst.printTree()
bst.delete('H')
print("Deleting 'H'")
bst.printTree()
bst.delete('B')
print("Deleting 'B'")
bst.printTree()
bst.delete('L')
print("Deleting 'L'")
bst.printTree()
bst.delete('M')
print("Deleting 'M'")
bst.printTree()
bst.delete('C')
print("Deleting 'C'")
bst.printTree()
bst.delete('E')
print("Deleting 'E'")
bst.printTree()


# ------------- test output from here ------------------
'''
Initializing the tree with 'H'
--------- Tree begins here ----------
H 
    
--------- Tree ends here -------------
Inserting 'B'
--------- Tree begins here ----------
H 
B   
    
--------- Tree ends here -------------
Inserting 'M'
--------- Tree begins here ----------
H 
B M 
        
--------- Tree ends here -------------
Inserting 'A'
--------- Tree begins here ----------
H 
B M 
A       
    
--------- Tree ends here -------------
Inserting 'E'
--------- Tree begins here ----------
H 
B M 
A E     
        
--------- Tree ends here -------------
Inserting 'C'
--------- Tree begins here ----------
H 
B M 
A E     
    C   
    
--------- Tree ends here -------------
Inserting 'D'
--------- Tree begins here ----------
H 
B M 
A E     
    C   
  D 
    
--------- Tree ends here -------------
Inserting 'L'
--------- Tree begins here ----------
H 
B M 
A E L   
    C       
  D 
    
--------- Tree ends here -------------
Inserting 'N'
--------- Tree begins here ----------
H 
B M 
A E L N 
    C           
  D 
    
--------- Tree ends here -------------
Searching by the range (minimum = 'B', maximum='M')
B C D E H L M 
Deleting 'B'
--------- Tree begins here ----------
H 
C M 
A E L N 
    D           
    
--------- Tree ends here -------------
Deleting 'A'
--------- Tree begins here ----------
H 
C M 
  E L N 
D           
    
--------- Tree ends here -------------
Deleting 'H'
--------- Tree begins here ----------
L 
C M 
  E   N 
D       
    
--------- Tree ends here -------------
Deleting 'B'
--------- Tree begins here ----------
L 
C M 
  E   N 
D       
    
--------- Tree ends here -------------
Deleting 'L'
--------- Tree begins here ----------
M 
C N 
  E     
D   
    
--------- Tree ends here -------------
Deleting 'M'
--------- Tree begins here ----------
N 
C   
  E 
D   
    
--------- Tree ends here -------------
Deleting 'C'
--------- Tree begins here ----------
N 
E   
D   
    
--------- Tree ends here -------------
Deleting 'E'
--------- Tree begins here ----------
N 
D   
    
--------- Tree ends here -------------
'''
