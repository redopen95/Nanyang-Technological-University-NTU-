#Question (5)

import random                                                                   #Import random functions from python

Temp1=[random.randint(0,40) for points in range(50)]                            #Generate temp measurements at 50 different points of time in first location between 0 to 40 degrees
Temp2=[random.randint(0,40) for points in range(50)]                            #Generate temp measurements at 50 different points of time in second location between 0 to 40 degrees
Temp3=[random.randint(0,40) for points in range(50)]                            #Generate temp measurements at 50 different points of time in third location between 0 to 40 degrees

#Using list comprehension:
Warm=[(T1,T2,T3) for (T1,T2,T3) in zip(Temp1,Temp2,Temp3) if (T1+T2+T3)>75]     #List of 3-temp tuples, containing generally warm temp such that T1+T2+T3>75
All_Cold=[(T1,T2,T3) for (T1,T2,T3) in zip(Temp1,Temp2,Temp3) if T1<10 and T2<10 and T3<10]
                                                                                #List of 3-temp tuples, containing the all-cold temp such that T1,T2,T3<10
Similar=[(T1,T2,T3) for (T1,T2,T3) in zip(Temp1,Temp2,Temp3) if abs(T1-T2)<5 and abs(T1-T3)<5 and abs(T2-T3)<5]
                                                                                #List of 3-temp tuples, containing the similar temp such that (T1-T2),(T1-T3),(T2-T3)<5
                                                                                
#printing output
print('List of warm temperatures is: \n {}'.format(Warm))
print('List of all cold temperatures is: \n {}'.format(All_Cold))
print('List of similar temperatures is: \n {}'.format(Similar))