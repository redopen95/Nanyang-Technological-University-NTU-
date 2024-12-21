import random
from U1740947L_Lab11_counting import counting
My_Slist = [random.randint(0,20) for i in range(20)]
My_Slist.sort()

An_Integer = random.randint(0,20)

print(An_Integer)
print(My_Slist)
print(counting(My_Slist,An_Integer))
