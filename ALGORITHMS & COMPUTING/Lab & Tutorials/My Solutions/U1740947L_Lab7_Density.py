#Question 6 (Script File)

from U1740947L_Lab7_Qn6_FunctionFile import countryDensity                      #Importing function file

Country=input('Please enter a country name: ')                                  #Prompts user to enter a country name                            
Area=float(input('Please enter the total land area of the country in km2: '))   #Prompts user to enter land area of country
Population=float(input('Please enter the total population of the country: '))   #Prompts user to enter population of country
                                                                                #Print output
print('The population density of {:s} is {:.0f} people per km2'.format(Country,countryDensity(Country,Area,Population)))