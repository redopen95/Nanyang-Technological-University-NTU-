# doubly linked list
# Author: Huang Tao

from NodeClass import Node

class LinkedList:

	def __init__(self, node = None):
		if node == None:
			self.firstNode = None
			self.lastNode  = None
			self.size = 0
		else:
			self.firstNode = node
			self.lastNode  = node
			self.size = 1

	def first(self):
		'''
		Return first node
		'''
		return self.firstNode

	def last(self):
		'''
		Return last node
		'''
		return self.lastNode

	def before(self, p):
		'''
		Return node before p
		'''
		return p.getPrev()              # or you can return p.prev
#                return p.prev
        
	def after(self, p):
		'''
		Return node after p
		'''
		return p.getNext()
#               return p.next

	def isEmpty(self):
		'''
		When the linked list is empty return true, otherwise return false
		'''
		return (self.size == 0)

	def size(self):
		'''
		Return size of the linked list
		'''
		return self.size

	def insertBefore(self, p, e):
		'''
		Insert node e into linked list before p
		'''
		e.prev = p.prev
		e.next = p
		p.prev = e
		if (e.prev == None):
			self.firstNode = e
		else:
			e.prev.next = e
		self.size += 1

	def insertAfter(self, p, e):
		'''
		Insert node e into linked list after p
		'''
		e.next = p.next
		e.prev = p
		p.next = e
		if (e.next == None):
			self.lastNode = e
		else:
			e.next.prev = e
		self.size += 1

	def remove(self, p):
		'''
		Remove node p
		'''
		p.prev.next = p.next
		p.next.prev = p.prev
		self.size -= 1

	def printAll(self):
		'''
		Output data in the linked list
		'''
		p = self.first()
		while (p.next != None):
			print(p.data, end = ' ')
			p = p.next
		print(p.data)

# test cases: 
if __name__ == '__main__':
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	llist = LinkedList(a)
	llist.printAll()
	llist.insertAfter(a, b)
	llist.printAll()
	llist.insertAfter(b, c)
	llist.printAll()

	print((llist.first()).data)
	print(llist.last().data)
	print(llist.before(b).data)
	print(llist.after(b).data)
	print(llist.isEmpty())

	llist.insertBefore(b, d)
	llist.insertAfter(b, e)
	llist.printAll()

	llist.remove(b)
	llist.printAll()

	print(llist.size)


	
	
