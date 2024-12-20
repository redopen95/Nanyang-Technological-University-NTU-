#Question (7)

#Cost of travel by walking is free
travel=0
#Cost of travel by motorcycle is 0.22 SGD/km
motorcycle=0.22
#Cost of travel by car is 0.26 SGD/km
car=0.26
#Cost of travel by plane is 0.78 SGD/km
plane=0.78

Distance=float(input('Enter the travel distance in kilometer: ')) #prompts user to input for a travel distance

if Distance < 0: #Error check for distance input by user
    print('Distance cannot be negative!')#Distance 0km and below is not possible
    
else:
    if Distance <=20: #Walking cant be done for more than 20km
        print('Cost by walking is free!')#print cost of travel by walking
    else:
        print('Distance is too far to walk!')#print distance is too far to be travelled by walking
    
    if Distance <=200: #Travel by motorcycle cant be done for more than 200km
        print('Cost by motorcycle is {motorcyclecost:.2f} in SGD'.format(motorcyclecost=motorcycle*Distance))#print cost of travel by motorcycle
    else:
        print('Distance is too far to travel by motorcycle')#print distance is too far to be travelled by motorcycle
        
    if Distance <=800: #Travel by car cant be done for more than 800km
        print('Cost by car is {carcost:.2f} in SGD'.format(carcost=car*Distance))#print cost of travel by car
    else:
        print('Distance is too far to travel by car')#print distance is too far to be travelled by car
    
    if Distance >=100: #Travel by plane cant be done for less than 100km
        print('Cost by plane is {planecost:.2f} in SGD'.format(planecost=plane*Distance)) #print cost of travel by plane
    else:
        print('Your travel distance is too short to be done by plane')#print distance is too short to be travelled by plane