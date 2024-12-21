# Matric Number:

class TreeNode:
    def __init__(self, initKey, initParent = None, initLeftChild = None, initRightChild = None):
        self.key = initKey
        self.parent = initParent
        self.leftChild = initLeftChild
        self.rightChild = initRightChild


class BinarySearchTree:
    def __init__(self, initRoot = None):
        if initRoot != None:
            self.root = TreeNode(initRoot)

    # IMPLEMENT HERE #
    def search(self, k):
 

    # IMPLEMENT HERE #
    def insert(self, k):
 
    
    # IMPLEMENT HERE #
    def delete(self, k):
 
    # IMPLEMENT HERE #
    def searchByRange(self, minimum, maximum):

# ------------- test code from here ------------------
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
