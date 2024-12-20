# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 18:11:49 2017

@author: Hong Kai
"""

#Quesiton 6
myList1 = ["a","b","c","d","e"]
myList2 = [1,2,3,4,5]

#Question 6(a)
myList1.remove("e")
myList2.remove(1)
myList1.append("Hello")#adding "Hello" element to at the end of myList1
myList1.extend(myList2)#concatenante the 2 myList
print(myList1)


#Question 6(b)
myList1b=["a","b","c","d","e"]
myList2b=[1,2,3,4,5]
del myList1b[4]
del myList2b[0]
x=myList1b#new myList1b
y=myList2b#new myList2b
z=x + ["Hello"] + y#combining new myList1b & myList2b & "Hello" element together
print(z)
