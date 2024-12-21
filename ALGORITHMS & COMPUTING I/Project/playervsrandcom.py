# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:48:27 2017

@author: Joleen
"""

import numpy as np
import random
#in this case player 2 is computer player

def printmat(my_mat,s): #define function to print the board out with plaer 1 as 'X' and player 2 as 'O' and blank face as '-'
    for a in range(s): #ranging through every rows
        for b in range(s): #ranging through evert columns
            if my_mat[a,b]==1: #player 2's symbol 
                print(" X", end=" ") #printing the X for player 1 piece
            elif my_mat[a,b]==0: #blank face
                print(" -", end=" ") #printing the background
            else: #player 1's symbol
                print(" O", end=" ") #printing the O for player 2 piece
        print("\n") #print next line
    return #Return nothing

def win(my_mat, s, playernum): #define a function to check for win condition
    """check if the board win
    returns my_mat
    """
    p1win = 0 #initialise player1win = 0
    p2win = 0 #initialise player2win = 0
    for i in range(s): #this for loop loops over every element in a row or colum
        sumrow = np.sum(my_mat[i])  #sums the number of entries in a row  
        sumcol = np.sum(my_mat[:,i])  #sums the number of entries in a column
        if sumrow == s or sumcol == s: #if the sum of the row or column equals to the size of the board
            p2win = 1 #player 2 wins as player 2 piece is 1
        elif sumrow == -s or sumcol == -s: #if the sum of the row or column equals to the negative number of the size of the board
            p1win = 1 #player 1 wins as player 1 piece is -1
        
    sumdiagonal = np.sum(np.diag(my_mat)) #sums the number of entries in the diagonal
    sumantidiag= np.sum(np.diag(np.flipud(my_mat))) #sums the number of entries in the anti diagonal
    if sumdiagonal == s or sumantidiag == s: #if the sum of the diagonal equals to the size of the board
        p2win = 1 #player 2 wins as player 2 piece is 1
    elif sumdiagonal == -s or sumantidiag == -s: #if the sum of the diagonal equals to the negative number of the size of the board
        p1win = 1 #player 1 wins as player 1 piece is -1
    
    if playernum==1 and p1win ==1 and p2win ==1: #player 2 wins if he was the last one to make a move such that player 1 and 2 both win simultaneously
        print('Player 2 win')#printing player 2 win 
    elif playernum ==2 and p1win ==1 and p2win ==1:#player 1 wins if he was the last one to make a move such that player 1 and 2 both win simultaneously
        print('Player 1 win')#printing player 1 win
    elif p1win==1: #if the condition is met
        print('Player 1 win') #print player 1 win
    elif p2win==1: #else if the condition of p2win == 1 
        print('Player 2 win') #print player 2 win
    if p1win == 1 or p2win == 1: #someone has won
        return 1 #someone has won
    return 0 #game continue on

def comdirection(): #define the function for computer direction
    direction = random.randint(1, 4) #randomly choose an integer between 1 to 4 inclusive
    if direction == 1: #if the number is 1 set the direction as up
        return 'UP'#return UP
    elif direction == 2: #if the number is 2 set the direction as down
        return 'DOWN'#return DOWN
    elif direction == 3: #if the number is 3 set the direction as left
        return 'LEFT'#return LEFT
    else: #if the number is 4 set the direction as right
        return 'RIGHT'#return RIGHT


def movecom (r, c, my_mat, s, playernum): #define function for player and computer moves
    """when a player selects row r and column c, it will change the matrix board into the player1 piece.
    Returns the matrix board
    """
    if playernum == 1:#player 1
        while my_mat [r, c] == 1 or (r >= 1) and (r <= s-2) and (c <= s-2) and (c >= 1) or (r < 0) or (c < 0) or (r > s) or (c > s):#error check
            print('invalid move, you can only choose the row and column that has a blank face or your own symbol on the outer boundary')#remind user
            r = int(input('Please select a row from the outer boundary:'))#prompt user to input row that they want to select
            c = int(input('Please select a column from the outer boundary:'))#prompt user to input column that they want to select
    else: #computer player (As player 2)
        while my_mat [r, c] == -1 or (r >= 1) and (r <= s-2) and (c <= s-2) and (c >= 1) or (r < 0) or (c < 0) or (r > s) or (c > s):#Error check
            r = random.randint(0, s-1)#randomly generate valid rows move
            c = random.randint(0, s-1)#randomly generate valid columns move
        
    if [r,c]==[0,0]:    #TOP LEFT CORNER
        if playernum == 1:#player 1
            direction=input('Please push UP or LEFT (case sensitive):')#prompt user to select direction
            while direction != 'UP' and direction != 'LEFT':#user cannot select up and left
                print('Please think clearly and try again')#remind user
                direction=input('Please push UP or LEFT (case sensitive):')#reprompt user to input direction
        else:#computer player
            direction=comdirection()#calling the comdirection function to determine its direction
            while direction != 'UP' and direction != 'LEFT':#computer cannot select up(1) or left(3)
                direction=comdirection()#recall the comdirection function
        if direction == 'UP': #if player chooses up direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,0] #assign the entries onto the first column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1):#this for loop loops over every s-1
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first row and first column) shift the remaining elements to replace the removed entry position
            if playernum == 1:#player 1
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position
            else:#computer player
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position
            for y in range(s):#this for loop loops over every s
                my_mat[y,0]=my_column2[y] #replace the first column of my_mat with my_column2
        
        else:   #if player choose to move in the left direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[0,:] #assign the entries onto the first row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first row and first column) shift the remaining entries to replace the removed entry position
            if playernum == 1:#player 1
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position 
            else:#computer player
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position 
            for y in range(s):#this for loop loops over every s
                my_mat[0,y]=my_column2[y] #replace the first row of my_mat with my_column2

        
    elif [r, c] == [0, s-1]: #TOP RIGHT CORNER CASE
        if playernum == 1:#player 1
            direction=input('Please push UP or RIGHT (case sensitive):')#prompt user for direction
            while direction != 'UP' and direction != 'RIGHT':#user cannot select these
                print('Please think clearly and try again')#remind user
                direction=input('Please push UP or RIGHT (case sensitive):')#reprompt user
        else:#computer player
            direction=comdirection()#calling the comdirection function to determine its direction
            while direction != 'UP' and direction != 'RIGHT':#computer cannot choose these
                direction=comdirection()#recall the function
        if direction == 'UP': #if player chooses up direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,s-1] #assign the entries onto the last column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first row and last column) shift the remaining elements to replace the removed entry position
            if playernum == 1:#player 1
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position
            else:#computer player
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position
            for y in range(s):#this for loop loops over every s
                my_mat[y,s-1]=my_column2[y] #replace the last column of my_mat with my_column2
        
        else:   #if player choose to move in the right direction 
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[0,:] #assign the entries onto the first row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                my_column1[x]=my_column[x] #after removing the first piece(from the first row and last column) shift the remaining entries to replace the removed entry position
            if playernum == 1:#player 1
                my_column2 = np.concatenate([np.array([-1]), my_column1]) #join back the piece as the first position 
            else:#computer player
                my_column2 = np.concatenate([np.array([1]), my_column1]) #join back the piece as the first position 
            for y in range(s):#this for loop loops over every s
                my_mat[0,y]=my_column2[y] #replace the first row of my_mat with my_column2
         
    elif [r, c] == [s-1, 0]: #BOTTOM LEFT CORNER CASE
        if playernum == 1:#player 1
            direction=input('Please push DOWN or LEFT (case sensitive):')#prompt user to select direction
            while direction != 'DOWN' and direction != 'LEFT':#user cannot select these choices
                print('Please think clearly and try again')#remind user
                direction=input('Please push DOWN or LEFT (case sensitive):')#reprompt user
        else:#computer player
            direction = comdirection()#calling the comdirection function
            while direction != 'DOWN' and direction != 'LEFT':#computer cannot select these
                direction = comdirection()#recall the function
        if direction == 'DOWN': #if player chooses down direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,0] #assign the entries onto the first column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                my_column1[x]=my_column[x] #after removing the first piece(from the first column and last row) shift the remaining elements to replace the removed entry position
            if playernum == 1:#player 1
                my_column2 = np.concatenate([np.array([-1]),my_column1]) #join back the piece as the first position 
            else:#computer player
                my_column2 = np.concatenate([np.array([1]),my_column1]) #join back the piece as the first position 
            for y in range(s):#this for loop loops over every s
                my_mat[y,0]=my_column2[y] #replace the first column of my_mat with my_column2
        
        else:   #if player choose to move in the left direction 
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[s-1,:] #assign the entries onto the last row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first column and last row) shift the remaining entries to replace the removed entry position
            if playernum == 1 :#player 1
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position 
            else:#computer player
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position 
            for y in range(s):#this for loop loops over every s
                my_mat[s-1,y]=my_column2[y] #replace the last row of my_mat with my_column2
    
    elif [r, c] == [s-1, s-1]: #BOTTOM RIGHT CORNER CASE
        if playernum == 1:#player 1
            direction=input('Please push DOWN or RIGHT (case sensitive):')
            while direction != 'DOWN' and direction != 'RIGHT':
                print('Please think clearly and try again')
                direction=input('Please push DOWN or RIGHT (case sensitive):')
        else:#computer player
            direction = comdirection()#calling the comdirection function
            while direction != 'DOWN' and direction != 'RIGHT':#computer cannot select these directions
                direction = comdirection()#recall the function
        if direction == 'DOWN': #if player chooses down direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,s-1] #assign the entries onto the last column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                my_column1[x]=my_column[x] #after removing the first piece(from the last row and last column) shift the remaining elements to replace the removed entry position
            if playernum == 1:#player 1
                my_column2 = np.concatenate([np.array([-1]),my_column1]) #join back the piece as the first position 
            else:#computer player
                my_column2 = np.concatenate([np.array([1]),my_column1]) #join back the piece as the first position 
            for y in range(s):#this for loop loops over every s
                my_mat[y,s-1]=my_column2[y] #replace the last column of my_mat with my_column2
        
        else:   #if player choose to move in the right direction 
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[s-1,:] #assign the entries onto the last row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                my_column1[x]=my_column[x] #after removing the first piece(from the last row and last column) shift the remaining entries to replace the removed entry position
            if playernum == 1:#player 1
                my_column2 = np.concatenate([np.array([-1]), my_column1]) #join back the piece as the first position 
            else:#computer player
                my_column2 = np.concatenate([np.array([1]), my_column1]) #join back the piece as the first position  
            for y in range(s):#this for loop loops over every s
                my_mat[s-1,y]=my_column2[y] #replace the last row of my_mat with my_column2
            
            
#TOP EDGE SIDES
    elif r == 0 and c != 0 and c != (s-1):#error check
        if playernum == 1:#player 1
            direction=input('Please push UP or LEFT or RIGHT (case sensitive):')#prompt user for direction
            while direction == 'DOWN': #player cannot choose down
                print('Please think clearly and try again')#remind user
                direction=input('Please push UP or LEFT or RIGHT (case sensitive):') #if the user input correctly, will break the while loop automatically
        else:#computer player
            direction = comdirection()#calling the comdirection function
            while direction == 'DOWN':#error check
                direction = comdirection()#recalling the function
        if direction == 'UP':#select up direction
            my_column = np.linspace(0,0,s)#making the new vector with s entries 
            my_column = my_mat[:,c] #equating my_column with c column of the my_mat.   Can also use my_mat[r,:] but in general if push vertically use column more easier, if its push horizontally use row better
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1):#this for loop loops over every s-1                                             
                my_column1[x]=my_column[x+1] #Index of my_column1 eg [1] = my_column eg [2], Hence the link is x+1
            if playernum == 1:#player 1
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #adding np.array([-1]) to the end of my_column1
            else:#computer player
                my_column2 = np.concatenate([my_column1,np.array([1])]) #adding np.array([1]) to the end of my_column1
            for y in range(s): #this for loop loops over every s                                                 #Running through every s
                my_mat[y,c]=my_column2[y] #replace the y row, c column of the my_mat with my_column2
        
        elif direction == 'LEFT':#select left direction
            my_column = np.linspace(0,0,s)#making the new vector with s entries 
            my_column = my_mat[r,:] #equating my_column with r row of the my_mat. In general if push horizontally use row easier, if push vertically use column easier
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1):#this for loop loops over every s-1  
                if x < c: #for x < c your index of my_column1 and my_column will be the same
                    my_column1[x]=my_column[x]
                else: #else when x > c your index of my_column1 eg=2 will be the index of my_column eg=3, so the pattern for index is x+1
                    my_column1[x]=my_column[x+1]
            if playernum == 1:#player 1
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #Because you are inserting np.array[-1] at the end of my_column1)
            else:#computer player
                my_column2 = np.concatenate([my_column1,np.array([1])]) #Because you are inserting np.array[1] at the end of my_column1)
            for y in range(s):#this for loop loops over every s
                my_mat[r,y]=my_column2[y] #replacing the r row with y column of my_mat with entire my_column2
        
        
        else:
            my_column = np.linspace(0,0,s)#making the new vector with s entries
            my_column = my_mat[r,:]#equating my_column with r row of the my_mat. In general if push horizontally use row easier, if push vertically use column easier
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1):#this for loop loops over every s-1
                if x < c:#for x < c your index of my_column1 and my_column will be the same
                    my_column1[x]=my_column[x]
                else:#else when x > c your index of my_column1 eg=2 will be the index of my_column eg=3, so the pattern for index is x+1
                    my_column1[x]=my_column[x+1]
            if playernum == 1:#player 1
                my_column2=np.concatenate([np.array([-1]),my_column1])#join back the piece as the first position 
            else:#computer player
                my_column2=np.concatenate([np.array([1]),my_column1])#join back the piece as the first position 
            for y in range(s):#this for loop loops over every s
                my_mat[r,y]=my_column2[y]#replacing the r row with y column of my_mat with entire my_column2
        
                
#BOTTOM EDGE SIDES
    elif r == s-1 and c != 0 and c != (s-1):#error check
        if playernum == 1:#player 1
            direction=input('Please push DOWN or LEFT or RIGHT (case sensitive):')#prompt user
            while direction == 'UP':#cannot select up direction
                print('Please think clearly and try again')#remind user
                direction=input('Please push DOWN or LEFT or RIGHT (case sensitive):')#reprompt user
        else:#computer player
            direction = comdirection()#call function
            while direction == 'UP':#computer cannot select up direction
                direction = comdirection()#recall function
        if direction == 'DOWN':#select down direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,c] 
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1):#this for loop loops over every s-1
                my_column1[x]=my_column[x]#after removing the first piece(from the first column and last row) shift the remaining entries to replace the removed entry position
            if playernum == 1:#player 1
                my_column2 = np.concatenate([np.array([-1]),my_column1])
            else:#comuter player
                my_column2 = np.concatenate([np.array([1]),my_column1])
            for y in range(s):#this for loop loops over every s
                my_mat[y,c] = my_column2[y]#replace the y row, c column of the my_mat with my_column2
         
        elif direction == 'LEFT':#select left direction
            my_column = np.linspace(0,0,s)#making the new vector with s entries
            my_column = my_mat[r,:]#equating my_column with r row of the my_mat. In general if push horizontally use row easier, if push vertically use column easier
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1):#this for loop loops over every s-1
                if x < c:#for x < c your index of my_column1 and my_column will be the same
                    my_column1[x] = my_column[x]
                else:#else when x > c your index of my_column1 eg=2 will be the index of my_column eg=3, so the pattern for index is x+1
                    my_column1[x] = my_column[x+1]
            if playernum == 1:#player 1
                my_column2 = np.concatenate([my_column1,np.array([-1])])#Because you are inserting np.array[1] at the end of my_column1)
            else:#computer player
                my_column2 = np.concatenate([my_column1,np.array([1])])#Because you are inserting np.array[1] at the end of my_column1)

            for y in range(s):#this for loop loops over every s
                my_mat[r,y] = my_column2[y]#replacing the r row with y column of my_mat with entire my_column2
         
        else:#selects right direction
            my_column = np.linspace(0,0,s)#making the new vector with s entries
            my_column = my_mat[r,:]#equating my_column with r row of the my_mat. In general if push horizontally use row easier, if push vertically use column easier
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                if x < c:#for x < c your index of my_column1 and my_column will be the same
                    my_column1[x] = my_column[x]
                else:#else when x > c your index of my_column1 eg=2 will be the index of my_column eg=3, so the pattern for index is x+1
                    my_column1[x] = my_column[x+1]
            if playernum == 1:#player 1
                my_column2 = np.concatenate([np.array([-1]),my_column1])#join back the piece as the first position 
            else:#computer player
                my_column2 = np.concatenate([np.array([1]),my_column1])#join back the piece as the first position 
            for y in range(s): #this for loop loops over every s
                my_mat[r,y] = my_column2[y]#replacing the r row with y column of my_mat with entire my_column2
          
#LEFT EDGE SIDE
    elif c == 0 and r != 0 and r != (s-1):#error check
        if playernum == 1:#player 1
            direction=input('Please push LEFT or UP or DOWN (case sensitive): ')#prompt user for direction
            while direction == 'RIGHT':#cannot choose this
                print('Please think clearly and try again')#remind user
                direction=input('Please push LEFT or UP or DOWN (case sensitive):')#reprompt user
        else:#computer player
            direction = comdirection()#calling function
            while direction == 'RIGHT':#cannot select right direction
                direction = comdirection()#recall function
        if direction == 'LEFT':#selects left direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[r,:] #equating my_column with r row of the my_mat. In general if push horizontally use row easier, if push vertically use column easier
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1):#this for loop loops over every s-1
                my_column1[x]=my_column[x+1]
            if playernum == 1:#player 1
                my_column2 = np.concatenate([my_column1,np.array([-1])])#Because you are inserting np.array[1] at the end of my_column1)
            else:#computer player
                my_column2 = np.concatenate([my_column1,np.array([1])])#Because you are inserting np.array[1] at the end of my_column1)
            for y in range(s):#this for loop loops over every s
                my_mat[r,y] = my_column2[y]#replacing the r row with y column of my_mat with entire my_column2
                
         
        elif direction == 'UP':#selects up direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,c] #equating my_column with c column of the my_mat.   Can also use my_mat[r,:] but in general if push vertically use column more easier, if its push horizontally use row better
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                if x < r:#for x < r your index of my_column1 and my_column will be the same
                    my_column1[x] = my_column[x]
                else: #else when x > r your index of my_column1 eg=2 will be the index of my_column eg=3, so the pattern for index is x+1
                    my_column1[x] = my_column[x+1]
            if playernum == 1:#player 1
                my_column2 = np.concatenate([my_column1,np.array([-1])])#Because you are inserting np.array[1] at the end of my_column1)
            else:#computer player
                my_column2 = np.concatenate([my_column1,np.array([1])])#Because you are inserting np.array[1] at the end of my_column1)
            for y in range(s): #this for loop loops over every s
                my_mat[y,c] = my_column2[y]#replace the y row, c column of the my_mat with my_column2
        
        
        else:#down direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,c] #equating my_column with c column of the my_mat.   Can also use my_mat[r,:] but in general if push vertically use column more easier, if its push horizontally use row better
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                if x < r:#for x < r your index of my_column1 and my_column will be the same
                    my_column1[x] = my_column[x]
                else: #else when x > r your index of my_column1 eg=2 will be the index of my_column eg=3, so the pattern for index is x+1
                    my_column1[x] = my_column[x+1]
            if playernum == 1:#player 1
                my_column2 = np.concatenate([np.array([-1]),my_column1])#join back the piece as the first position
            else:#computer player
                my_column2 = np.concatenate([np.array([1]),my_column1])#join back the piece as the first position
            for y in range(s): #this for loop loops over every s
                my_mat[y,c] = my_column2[y]#replace the y row, c column of the my_mat with my_column2
        
#RIGHT EDGE SIDE
    elif c == (s-1) and r != 0 and r != (s-1):#error check
        if playernum == 1:#player 1
            direction=input('Please push RIGHT or UP or DOWN (case sensitive): ')#prompt user for direction
            while direction == 'LEFT':#cannot choose left
                print('Please think clearly and try again')#remind user
                direction=input('Please push RIGHT or UP or DOWN (case sensitive):')#repromt user
        else:#computer player
            direction = comdirection()#calling the function
            while direction == 'LEFT':#cannot select this direction
                direction = comdirection()#recall the function
        if direction == 'RIGHT':#selects right direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[r,:] #equating my_column with r row of the my_mat. In general if push horizontally use row easier, if push vertically use column easier
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1):#this for loop loops over every s-1
                my_column1[x]=my_column[x]#after removing the first piece(from the first column and last row) shift the remaining elements to replace the removed entry position
            if playernum == 1:#player 1
                my_column2 = np.concatenate([np.array([-1]),my_column1])#join back the piece as the first position
            else:#computer player
                my_column2 = np.concatenate([np.array([1]),my_column1])#join back the piece as the first position
            for y in range(s):#this for loop loops over every s
                my_mat[r,y] = my_column2[y]#replacing the r row with y column of my_mat with entire my_column2
                       
         
        elif direction == 'UP':#selects up direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,c] #equating my_column with c column of the my_mat.   Can also use my_mat[r,:] but in general if push vertically use column more easier, if its push horizontally use row better
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                if x < r:#for x < r your index of my_column1 and my_column will be the same
                    my_column1[x] = my_column[x]
                else:#else when x > r your index of my_column1 eg=2 will be the index of my_column eg=3, so the pattern for index is x+1
                    my_column1[x] = my_column[x+1]
            if playernum == 1:#player 1
                my_column2 = np.concatenate([my_column1,np.array([-1])])#Because you are inserting np.array[1] at the end of my_column1)
            else:#computer player
                my_column2 = np.concatenate([my_column1,np.array([1])])#Because you are inserting np.array[1] at the end of my_column1)
            for y in range(s): #this for loop loops over every s
                my_mat[y,c] = my_column2[y]#replace the y row, c column of the my_mat with my_column2
        
        
        else:#selects down direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,c] #equating my_column with c column of the my_mat.   Can also use my_mat[r,:] but in general if push vertically use column more easier, if its push horizontally use row better
            my_column1 = np.linspace(0,0,s-1)#making the new vector with s-1 entries
            for x in range(s-1): #this for loop loops over every s-1
                if x < r:#for x < r your index of my_column1 and my_column will be the same
                    my_column1[x] = my_column[x]
                else:#else when x > r your index of my_column1 eg=2 will be the index of my_column eg=3, so the pattern for index is x+1
                    my_column1[x] = my_column[x+1]
            if playernum == 1:#player 1
                my_column2 = np.concatenate([np.array([-1]),my_column1])#join back the piece as the first position
            else:#computer player
                my_column2 = np.concatenate([np.array([1]),my_column1])#join back the piece as the first position
            for y in range(s): #this for loop loops over every s
                my_mat[y,c] = my_column2[y]#replace the y row, c column of the my_mat with my_column2
    return my_mat#returning matrix


def AIrandomplayer(my_mat,s): #random computer player
    r=-1
    c=-1    
    while my_mat [r, c] == -1 or (r >= 1) and (r <= s-2) and (c <= s-2) and (c >= 1) or (r < 0) or (c < 0) or (r > s) or (c > s):
            r = random.randint(0, s-1)
            c = random.randint(0, s-1)
    movecom(r, c, my_mat, s, 2)#calling function
    printmat(my_mat,s)
    return my_mat

choice = input('Do you want to choose your board size? (please choose YES or NO)(case sensitive): ')

#error check for choice
while choice != 'YES' and choice != 'NO': 
    print('invalid choice')
    choice = input('Do you want to choose your board size? (please choose YES or NO)(case sensitive): ')


#creating the default board
if choice == 'NO':
    s = 5 #board size is 5
    my_mat = np.zeros([s, s])#creating the matrix
    printmat(my_mat,s)

#board based on player's choice    
elif choice == 'YES':
    s = (int(input('Please enter the size of the board:')))#prompt user
    #error check
    while s <= 2: 
        print('Please input a board size of at least 3')#remind user to create at least size 3
        s = (int(input('Please enter the size of the board:')))#reprompt user again
    my_mat = np.zeros([s,s])#create matrix
    printmat(my_mat,s)


wincon=-1#initializing wincon=-1
while wincon!=0:#wincon is always true unless break
    print('Player 1 turn \nYour piece is O') 
    while True:#always true
        try:#catching error
            x = input('Please select a row from the outer boundary:')
            y = input('Please select a column from the outer boundary:')
            r=int(x)
            c=int(y)
            if my_mat[r,c] == 1:
                print('Please select your own symbol or a blank face')
                #error check
            elif (r >= 1) and ((r <= s-2) and (c <= s-2) and (c >= 1)) or (r < 0) or (c < 0) or (r >= s) or (c >= s) :
                print('error, please select only the outer boundary blocks')
            else:
                break
        except:
            print("Please input an integer, only select from the outer boundaries and you can only choose your own symbol or a blank face. \n")
    
    movecom(r, c, my_mat, s, 1)#calling function
    printmat(my_mat,s)
    if win(my_mat, s, 1) != 0: #if value = 1, will break, there is a winner for player
        break
    print('Computer turn')
    AIrandomplayer(my_mat, s)#calling function
    if win(my_mat, s, 1) != 0: #there is a winner for computer
        break
    
