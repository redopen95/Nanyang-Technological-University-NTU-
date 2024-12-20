# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:10:32 2017

@author: Hong Kai
"""

#Question 8
#farmer has 123kg of tomatoes
#farmer has 247kg of carrots
tomato_price=3.29#price in SGD per kilo
carrot_price=1.80#price in SGD per kilo

#Question 8(a)
Total_amount_8a = (123*tomato_price)+(247*carrot_price)#in SGD if farmer sells all its tomatoes and carrots
#Answer=$849.27

#Question 8(b)
Total_amount_8b = round((0.87*123*tomato_price)+(0.67*247*carrot_price),2)#in SGD if farmer sells 87% of tomatoes and 67% of carrots
#Answer=$649.94

#Question 8(c)
Total_amount_8c = round((0.85*Total_amount_8b),2)#in SGD after paying 15% tax for his sales in Question 8(b)
#Answer=$552.45

#Question 8(d)
Total_amount_8d=round(Total_amount_8c)#in SGD to the nearest dollar
#Answer=$552



#Question 10
#Assume that the angles are in radian
import math
#help(math)

#Question 10(a)
Expression_a=((math.exp(1.4)+math.log(465**2))/(math.sqrt(2)+14))+(12/math.sqrt(math.exp(1)+4))
#Answers=5.689

#Question 10(b)
Expression_b=(-2.6)**0.2+((math.exp(-math.sqrt(43.3)))/math.tan(276))+(17**(-1/7))
#Answers=1.6437301622977478+0.7115629957801659j

#Question 10(c)
Expression_c=((math.pi**3)-5.6**2+1)/((1.2**(math.pi/2))-math.sin(43))+(14.8/5)**((math.pi)-1.8)
#Answers=4.586997643



#Question 11
import random
#help(random)

#Question 11(a)
print(random.random())

#Question 11(b)
print(random.uniform(0,0.2))

#Question 11(c)
print(random.uniform(0.5,50))

#Question 11(d)
print(random.randint(32,60))
