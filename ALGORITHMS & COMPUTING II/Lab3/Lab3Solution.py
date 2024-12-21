# Author: Guo Jian

class TreeNode:
    def __init__(self, initKey, initParent = None, initLeftChild = None, initRightChild = None):
        self.key = initKey
        self.parent = initParent
        self.leftChild = initLeftChild
        self.rightChild = initRightChild


class BinarySearchTree:
    def __init__(self, initRoot = None):
        self.root = TreeNode(initRoot)

    def search(self, k):
        tmp = self.root
        while tmp:
            if tmp.key == k:
                return tmp
            elif k < tmp.key:
                tmp = tmp.leftChild
            else:
                tmp = tmp.rightChild
        return None

    def insert(self, k):
        node = TreeNode(k)
        if self.root == None:
            self.root = node
            return
        tmp = self.root
        while True:
            if node.key < tmp.key:
                if tmp.leftChild == None:
                    tmp.leftChild = node
                    node.parent = tmp
                    return node
                else:
                    tmp = tmp.leftChild
            elif node.key == tmp.key:
                return None
            else:
                if tmp.rightChild == None:
                    tmp.rightChild = node
                    node.parent = tmp
                    return node
                else:
                    tmp = tmp.rightChild

    
    # delete the node with key k; do nothing if not found
    def delete(self, k):
        n = self.search(k)
       
        if n == None:
#            print("key value '", k, "' is not found")
            return
#        print("node found by serach with key value ", n.key)
        # no child, just delete this node
        if n.leftChild == None and n.rightChild == None:
            if n.parent != None:
                if n.parent.leftChild == n:
                    n.parent.leftChild = None
                else:
                    n.parent.rightChild = None
            else:
                self.root = None
        # two children, replace by the leftmost node of right subtree,
        # the replacing node may have a rightChild, push it one level up
        elif n.leftChild and n.rightChild:
            tmp = n.rightChild
            while tmp.leftChild != None:
                tmp = tmp.leftChild
  
            if tmp.parent.leftChild == tmp:
                tmp.parent.leftChild = tmp.rightChild
            else:
                tmp.parent.rightChild = tmp.rightChild
            if tmp.rightChild:
                tmp.rightChild.parent = tmp.parent
#            print('replacing node is ', tmp.key)
            tmp.parent = n.parent
            tmp.leftChild = n.leftChild
            if n.rightChild != tmp:
                tmp.rightChild = n.rightChild
            if n.leftChild:
                tmp.leftChild.parent = tmp
            if n.rightChild:
                tmp.rightChild.parent = tmp
            if n.parent:
                if n == n.parent.leftChild:
                    n.parent.leftChild = tmp
                else:
                    n.parent.rightChild = tmp
            else:
                self.root = tmp
        else:
            if n.leftChild != None:
                n.leftChild.parent = n.parent
                if n.parent:
                    if n.parent.leftChild == n:
                        n.parent.leftChild = n.leftChild
                    else:
                        n.parent.rightChild = n.leftChild
                else:
                    self.root = n.leftChild
            else:
                n.rightChild.parent = n.parent
                if n.parent:
                    if n.parent.leftChild == n:
                        n.parent.leftChild = n.rightChild
                    else:
                        n.parent.rightChild = n.rightChild
                else:
                    self.root = n.rightChild
#        tmp = n
#        while tmp.parent != None:
#            tmp = tmp.parent
#        self.root = tmp
        del n
       

    # search range [minimum, maximum] both inclusive; assume minimum <= maximum already guaranteed
    def searchByRange(self, minimum, maximum):
        foundList = []
        if maximum < minimum:
            return
        n = self.root
        s = []
        while n != None:
            s += [n]
            if minimum <= n.key:
                if n.leftChild != None:
                    n = n.leftChild
                else:
                    break
            else:
                if n.rightChild != None:
                    n = n.rightChild
                else:
                    break
        # print('first node found: ', n.key)
        # check the node starting from n itself, all successive nodes, in the way of in order

        n = None           
        while True:
            if n != None:
                s += [n]
                n = n.leftChild
            else:
                n = s.pop()
                if(n.key > maximum):
                    return foundList
                if(minimum <= n.key):
                    foundList += [n]
                n = n.rightChild
                if len(s) == 0 and n == None:
                    return foundList
                            
        
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
