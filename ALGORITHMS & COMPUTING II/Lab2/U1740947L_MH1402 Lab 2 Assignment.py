# MH1402 - Algorithms and Computing II, AY17/18 S2, LAB 2

class Stack:                                    # Creating a class of Stack
    def __init__(self):                         # Initialize the attributes of the class
        self.slist = [None] * 1000              # preset the maximum size of the list (named slist) to be 1000
        self.rear = 0                           # the index of next empty slot in the list
        self.push_count = 0                     # total number of calls to push() function
        self.pop_count = 0                      # total number of calls to pop() function

    # IMPLEMENT HERE #
    def push(self, e):                          # push element e to the stack, push nothing if the slist is already full
        if self.rear < 1000:                    # If not full yet
            self.slist[self.rear] = e           # Make the [None] become [e]
            self.rear += 1                      # Increase rear counter
            self.push_count += 1                # Increase push counter
        else:                                   # If full then do nothing
            None

    # IMPLEMENT HERE #
    def pop(self):                              # return None if the stack is empty, otherwise return the element last pushed 
        if self.rear == 0:                      # If empty nothing to pop so return nothing
            return None
        else:
            TempStorage = self.slist[self.rear-1] # Create a temporary storage to keep the last element
            self.slist[self.rear-1] = None        # Equate the last element to become [None]
            self.rear -= 1                        # Decreases the rear counter by 1
            self.pop_count += 1                   # Increase the pop counter by 1
            return TempStorage                    # Return the element that you just popped
    
    # IMPLEMENT HERE #
    def size(self):                             # return the number of elements in the stack
        return self.rear
    # IMPLEMENT HERE #
    def isEmpty(self):                          # return True if the stack is empty; False otherwise
        if self.rear == 0:                      # If size = 0 return True
            return True
        else:                                   # Else not empty
            return False

class Queue:                                    # Creating a class of Queue
    def __init__(self):                         # Initialize the attributes of the class
        self.E = Stack()                        # Creating stack E
        self.D = Stack()                        # Creating stack D
        self.en_count = 0                       # Initializing enqueue counter = 0
        self.de_count = 0                       # Initializing dequeue counter = 0

    # IMPLEMENT HERE #
    def enqueue(self,e):                        
        self.E.push(e)                          # Pushing the desired input element into the stack
        self.en_count += 1                      # Increases the enqueue counter by 1
    

    # IMPLEMENT HERE #
    def dequeue(self):
        if self.D.rear == 0:                    # If stack D is empty
            while self.E.isEmpty() == False:    # While stack E is not empty
                self.D.push(self.E.pop())       # Push the popped element from stack E into stack D
        self.de_count += 1                      # Increases the dequeue counter by 1
        return self.D.pop()                     # Return the first element in stack E which is also the last element in stack D

    def size(self):                             # return number of elements in the queue
        return self.E.size() + self.D.size()

    def total_enqueue(self):                    # return the number of calls to enqueue() function
        return self.en_count

    def total_dequeue(self):                    # return the number of calls to dequeue() function
        return self.de_count
    
    def total_stack_push(self):                 # return the total push() function calls in both stacks
        return self.E.push_count + self.D.push_count

    def total_stack_pop(self):                  # return the total pop() function calls in both stacks
        return self.E.pop_count + self.D.pop_count


# ----- test the functionalities of the queue implementation ----
test_q = Queue()
for i in reversed(range(200)):
    test_q.enqueue(i)
    
for i in range(100):
    test_q.dequeue()

print('size(): ', test_q.size(), 'dequeue(): ', test_q.dequeue())
print('Total stack push = ', test_q.total_stack_push(), ' total enqueue count = ', test_q.total_enqueue(), ', average stack push per enqueue = ', test_q.total_stack_push()/test_q.total_enqueue(), end='\n')
print('Total stack pop = ', test_q.total_stack_pop(), ' total dequeue count = ', test_q.total_dequeue(), ', average stack pop per dequeue = ', test_q.total_stack_pop()/test_q.total_dequeue(), end='\n')

for i in range(100):
    test_q.enqueue(i)

for i in range(190):
    test_q.dequeue()

print('size(): ', test_q.size(), 'dequeue(): ', test_q.dequeue())
print('Total stack push = ', test_q.total_stack_push(), ' total enqueue count = ', test_q.total_enqueue(), ', average stack push per enqueue = ', test_q.total_stack_push()/test_q.total_enqueue(), end='\n')
print('Total stack pop = ', test_q.total_stack_pop(), ' total dequeue count = ', test_q.total_dequeue(), ', average stack pop per dequeue = ', test_q.total_stack_pop()/test_q.total_dequeue(), end='\n')

for i in range(500):
    test_q.enqueue(i)
    test_q.dequeue()

print('size(): ', test_q.size(), 'dequeue(): ', test_q.dequeue())
print('Total stack push = ', test_q.total_stack_push(), ' total enqueue count = ', test_q.total_enqueue(), ', average stack push per enqueue = ', test_q.total_stack_push()/test_q.total_enqueue(), end='\n')
print('Total stack pop = ', test_q.total_stack_pop(), ' total dequeue count = ', test_q.total_dequeue(), ', average stack pop per dequeue = ', test_q.total_stack_pop()/test_q.total_dequeue(), end='\n')

# ----- end of test -----


'''
# output expected from above
size():  100 dequeue():  99
Total stack push =  400  total enqueue count =  200 , average stack push per enqueue =  2.0
Total stack pop =  301  total dequeue count =  101 , average stack pop per dequeue =  2.98019801980198
size():  9 dequeue():  91
Total stack push =  600  total enqueue count =  300 , average stack push per enqueue =  2.0
Total stack pop =  592  total dequeue count =  292 , average stack pop per dequeue =  2.0273972602739727
size():  8 dequeue():  492
Total stack push =  1595  total enqueue count =  800 , average stack push per enqueue =  1.99375
Total stack pop =  1588  total dequeue count =  793 , average stack pop per dequeue =  2.0025220680958387
'''
