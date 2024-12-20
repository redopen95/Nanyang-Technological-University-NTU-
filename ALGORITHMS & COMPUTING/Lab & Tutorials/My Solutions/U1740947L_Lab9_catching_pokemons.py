#Question (8)

try:                                                                            #Catching Exceptions: Try statement
    PokeDex=open('pokemons.txt','r')                                            #Opening pokemon.txt as PokeDex
except FileNotFoundError:                                                       #Potential non-existence of the file must be handled with an appropriate try/catch block
    print('This source file does not exist, please try again with the correct file!')  #Output to remind user to select and open the correct file

else:                                                                           #If the file exist and is correct, continue to proceed on
    SplitPokeDex=[line.split() for line in PokeDex]                             #Separate all the words in PokeDex
    UpdatingPokeDex=[(Name,int(Index),Type) for (Name,Index,Type) in SplitPokeDex] #Creating a new list to update Final_PokeDex
    Final_PokeDex=[]                                                            #Initialise the Final_PokeDex into an empty list
                             
    for i in range(len(UpdatingPokeDex)):                                       #for loops to run through UpdatingPokeDex
        for (Name,Index,Type) in UpdatingPokeDex:                               #Nested for Loops to append Final_PokeDex
            if Index == i + 1:
                Final_PokeDex.append((Name,Index,Type))                         #Appending the empty list Final_PokeDex
                
    print(Final_PokeDex)                                                        #Printing Final_PokeDex
    

            
    UpdatedPokeDex=open('pokemons_new.txt','w+')                                #Reading & Writing a new txt file with the updated format called pokemons_new.txt
    
    for (Name,Index,Type) in Final_PokeDex:                                     #For loops for Final_PokeDex
        UpdatedPokeDex.write('%s %d %s \n'%(Name,Index,Type))                   #Writing new txt file


