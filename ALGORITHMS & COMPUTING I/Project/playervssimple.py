# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:25:10 2017

@author: Joleen
"""


import numpy as np
import random
#in this case player 2 is computer player

def printmat(my_mat,s): #define function to print the board out with plaer 1 as 'X' and player 2 as 'O' and blank face as '-'
    for a in range(s):
        for b in range(s):
            if my_mat[a,b]==1: #player 2's symbol 
                print(" X", end=" ")
            elif my_mat[a,b]==0: #blank face
                print(" -", end=" ")
            else: #player 1's symbol
                print(" O", end=" ")
        print("\n")
    return 


def goingtowincom(my_mat, s):
    a = []
    for i in range(s):
        for j in range(s):
            a.append((j, i))
            if np.count_nonzero(my_mat[j][i]==1) == s-1:
                return a
            else:
                return False


def win(my_mat, s, playernum): #define a function to check for win condition
    """check if the board win
    returns my_mat
    """
    p1win = 0 
    p2win = 0
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
        print('Player 2 win')
    elif playernum ==2 and p1win ==1 and p2win ==1:#player 1 wins if he was the last one to make a move such that player 1 and 2 both win simultaneously
        print('Player 1 win')
    elif p1win==1: #if the condition is met
        print('Player 1 win') #print player 1 win
    elif p2win==1: #else if the condition of p2win == 1 
        print(' ')   
    #print player 2 win 
    if playernum==1 and p1win ==1 and p2win ==1: #player 2 wins if he was the last one to make a move such that player 1 and 2 both win simultaneously
        return 2
    elif playernum ==2 and p1win ==1 and p2win ==1:#player 1 wins if he was the last one to make a move such that player 1 and 2 both win simultaneously
        return 1
    elif p1win==1: #if the condition is met
        return 1
    elif p2win==1: #else if the condition of p2win == 1 
        return 2
    return 0


def comdirection(): #define the function for computer direction
    direction = random.randint(1, 4) #randomly choose an integer between 1 to 4 inclusive
    if direction == 1: #if the number is 1 set the direction as up
        return 'UP'
    elif direction == 2: #if the number is 2 set the direction as down
        return 'DOWN'
    elif direction == 3: #if the number is 3 set the direction as left
        return 'LEFT'
    else: #if the number is 4 set the direction as right
        return 'RIGHT'


def movecom (r, c, my_mat, s, playernum): #define function for player and computer moves
    """when a player selects row r and column c, it will change the matrix board into the player1 piece.
    Returns the matrix board
    """
    if playernum == 1:
        while my_mat [r, c] == 1 or (r >= 1) and (r <= s-2) and (c <= s-2) and (c >= 1) or (r < 0) or (c < 0) or (r > s) or (c > s):
            print('invalid move, you can only choose the row and column that has a blank face or your own symbol on the outer boundary')
            r = int(input('Please select a row from the outer boundary:'))
            c = int(input('Please select a column from the outer boundary:'))
    else:
        while my_mat [r, c] == -1 or (r >= 1) and (r <= s-2) and (c <= s-2) and (c >= 1) or (r < 0) or (c < 0) or (r > s) or (c > s):
            r = random.randint(0, s-1)
            c = random.randint(0, s-1)
        
    if [r,c]==[0,0]:    #TOP LEFT CORNER
        if playernum == 1:
            direction=input('Please push UP or LEFT (case sensitive):')
            while direction != 'UP' and direction != 'LEFT':
                print('Please think clearly and try again')
                direction=input('Please push UP or LEFT (case sensitive):')
        else:
            direction=comdirection()
            while direction != 'UP' and direction != 'LEFT':
                direction=comdirection()
        if direction == 'UP': #if player chooses up direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,0] #assign the entries onto the first column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first row and first column) shift the remaining elements to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position
            for y in range(s):
                my_mat[y,0]=my_column2[y] #replace the first column of my_mat with my_column2
        
        else:   #if player choose to move in the left direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[0,:] #assign the entries onto the first row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first row and first column) shift the remaining entries to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position 
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position 
            for y in range(s):
                my_mat[0,y]=my_column2[y] #replace the first row of my_mat with my_column2

        
    elif [r, c] == [0, s-1]: #TOP RIGHT CORNER CASE
        if playernum == 1:
            direction=input('Please push UP or RIGHT (case sensitive):')
            while direction != 'UP' and direction != 'RIGHT':
                print('Please think clearly and try again')
                direction=input('Please push UP or RIGHT (case sensitive):')
        else:
            direction=comdirection()
            while direction != 'UP' and direction != 'RIGHT':
                direction=comdirection()
        if direction == 'UP': #if player chooses up direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,s-1] #assign the entries onto the last column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first row and last column) shift the remaining elements to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position
            for y in range(s):
                my_mat[y,s-1]=my_column2[y] #replace the last column of my_mat with my_column2
        
        else:   #if player choose to move in the right direction 
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[0,:] #assign the entries onto the first row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x] #after removing the first piece(from the first row and last column) shift the remaining entries to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]), my_column1]) #join back the first piece as the last position 
            else:
                my_column2 = np.concatenate([np.array([1]), my_column1]) #join back the first piece as the last position 
            for y in range(s):
                my_mat[0,y]=my_column2[y] #replace the first row of my_mat with my_column2
         
    elif [r, c] == [s-1, 0]: #BOTTOM LEFT CORNER CASE
        if playernum == 1:
            direction=input('Please push DOWN or LEFT (case sensitive):')
            while direction != 'DOWN' and direction != 'LEFT':
                print('Please think clearly and try again')
                direction=input('Please push DOWN or LEFT (case sensitive):')
        else:
            direction = comdirection()
            while direction != 'DOWN' and direction != 'LEFT':
                direction = comdirection()
        if direction == 'DOWN': #if player chooses down direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,0] #assign the entries onto the first column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x] #after removing the first piece(from the first column and last row) shift the remaining elements to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1]) #join back the first piece as the last position
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1]) #join back the first piece as the last position
            for y in range(s):
                my_mat[y,0]=my_column2[y] #replace the first column of my_mat with my_column2
        
        else:   #if player choose to move in the left direction 
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[s-1,:] #assign the entries onto the last row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first column and last row) shift the remaining entries to replace the removed entry position
            if playernum == 1 :
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position 
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position 
            for y in range(s):
                my_mat[s-1,y]=my_column2[y] #replace the last row of my_mat with my_column2
    
    elif [r, c] == [s-1, s-1]: #BOTTOM RIGHT CORNER CASE
        if playernum == 1:
            direction=input('Please push DOWN or RIGHT (case sensitive):')
            while direction != 'DOWN' and direction != 'RIGHT':
                print('Please think clearly and try again')
                direction=input('Please push DOWN or RIGHT (case sensitive):')
        else:
            direction = comdirection()
            while direction != 'DOWN' and direction != 'RIGHT':
                direction = comdirection()
        if direction == 'DOWN': #if player chooses down direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,s-1] #assign the entries onto the last column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x] #after removing the first piece(from the last row and last column) shift the remaining elements to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1]) #join back the first piece as the last position
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1]) #join back the first piece as the last position
            for y in range(s):
                my_mat[y,s-1]=my_column2[y] #replace the last column of my_mat with my_column2
        
        else:   #if player choose to move in the right direction 
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[s-1,:] #assign the entries onto the last row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x] #after removing the first piece(from the last row and last column) shift the remaining entries to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]), my_column1]) #join back the first piece as the last position 
            else:
                my_column2 = np.concatenate([np.array([1]), my_column1]) #join back the first piece as the last position 
            for y in range(s):
                my_mat[s-1,y]=my_column2[y] #replace the last row of my_mat with my_column2
            
            
#TOP EDGE SIDES
    elif r == 0 and c != 0 and c != (s-1):
        if playernum == 1:
            direction=input('Please push UP or LEFT or RIGHT (case sensitive):')
            while not (direction == 'UP' or direction =='LEFT' or direction =='RIGHT'):                                               #Error check
                print('Please think clearly and try again')
                direction=input('Please push UP or LEFT or RIGHT (case sensitive):') #if the user input correctly, will break the while loop automatically
        else:
            direction = comdirection()
            while direction == 'DOWN':                                               #Error check
                direction = comdirection()
        if direction == 'UP':
            my_column = np.linspace(0,0,s)
            my_column = my_mat[:,c]                                             #equating my_column with c column of the my_mat.
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):                                                
                my_column1[x]=my_column[x+1]                                    #Index of my_column1 eg [1] = my_column eg [2], Hence the link is x+1
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])             #adding np.array([-1]) to the end of my_column1
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])             #adding np.array([1]) to the end of my_column1
            for y in range(s):                                                  #Running through every s
                my_mat[y,c]=my_column2[y]                                       #replace the y row, c column of the my_mat with my_column2
        
        elif direction == 'LEFT':
            my_column = np.linspace(0,0,s)
            my_column = my_mat[r,:]                                             #equating my_column with r row of the my_mat. In general if push horizontally use row easier, if push vertically use column easier
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                if x < c:                                                       #for x < c your index of my_column1 and my_column will be the same
                    my_column1[x]=my_column[x]
                else:                                                           #else when x > c your index of my_column1 eg=2 will be the index of my_column eg=3, so the pattern for index is x+1
                    my_column1[x]=my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])             #inserting np.array[-1] at the end of my_column1
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])             #inserting np.array[1] at the end of my_column1
            for y in range(s):
                my_mat[r,y]=my_column2[y]                                       #replacing the r row with y column of my_mat with entire my_column2
        
        
        else:
            my_column = np.linspace(0,0,s)
            my_column = my_mat[r,:]
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                if x < c:
                    my_column1[x]=my_column[x]
                else:
                    my_column1[x]=my_column[x+1]
            if playernum == 1:
                my_column2=np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2=np.concatenate([np.array([1]),my_column1])
            for y in range(s):
                my_mat[r,y]=my_column2[y]
        
                
#BOTTOM EDGE SIDES
    elif r == s-1 and c != 0 and c != (s-1):
        if playernum == 1:
            direction=input('Please push DOWN or LEFT or RIGHT (case sensitive):')
            while not (direction == 'DOWN' or direction =='LEFT' or direction =='RIGHT'):
                print('Please think clearly and try again')
                direction=input('Please push DOWN or LEFT or RIGHT (case sensitive):')
        else:
            direction = comdirection()
            while direction == 'UP':
                direction = comdirection()
        if direction == 'DOWN':
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[:,c] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                my_column1[x]=my_column[x]
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1])
            for y in range(s):
                my_mat[y,c] = my_column2[y]
         
        elif direction == 'LEFT':
            my_column = np.linspace(0,0,s)
            my_column = my_mat[r,:]                                             #equating my_column with r row of the my_mat
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                if x < c:
                    my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])

            for y in range(s):
                my_mat[r,y] = my_column2[y]
         
        else:
            my_column = np.linspace(0,0,s)
            my_column = my_mat[r,:]
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1): 
                if x < c:
                     my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1])
            for y in range(s): 
                my_mat[r,y] = my_column2[y]
          
#LEFT EDGE SIDE
    elif c == 0 and r != 0 and r != (s-1):
        if playernum == 1:
            direction=input('Please push LEFT or UP or DOWN (case sensitive): ')
            while not (direction == 'UP' or direction =='LEFT' or direction =='DOWN'):
                print('Please think clearly and try again')
                direction=input('Please push LEFT or UP or DOWN (case sensitive):')
        else:
            direction = comdirection()
            while direction == 'RIGHT':
                direction = comdirection()
        if direction == 'LEFT':
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[r,:] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                my_column1[x]=my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])
            for y in range(s):
                my_mat[r,y] = my_column2[y]
                
         
        elif direction == 'UP':
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[:,c] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1): 
                if x < r:
                    my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])
            for y in range(s): 
                my_mat[y,c] = my_column2[y]
        
        
        else:
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[:,c] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1): 
                if x < r:
                    my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1])
            for y in range(s): 
                my_mat[y,c] = my_column2[y]
        
#RIGHT EDGE SIDE
    elif c == (s-1) and r != 0 and r != (s-1):
        if playernum == 1:
            direction=input('Please push RIGHT or UP or DOWN (case sensitive): ')
            while not (direction == 'UP' or direction =='DOWN' or direction =='RIGHT'):
                print('Please think clearly and try again')
                direction=input('Please push RIGHT or UP or DOWN (case sensitive):')
        else:
            direction = comdirection()
            while direction == 'LEFT':
                direction = comdirection()
        if direction == 'RIGHT':
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[r,:] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                my_column1[x]=my_column[x]
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1])
            for y in range(s):
                my_mat[r,y] = my_column2[y]
                       
         
        elif direction == 'UP':
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[:,c] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1): 
                if x < r:
                    my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])
            for y in range(s): 
                my_mat[y,c] = my_column2[y]
        
        
        else:
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[:,c] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1): 
                if x < r:
                    my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1])
            for y in range(s): 
                my_mat[y,c] = my_column2[y]  
    return my_mat



def movecom1 (r, c, d, my_mat, s, playernum): #define function for player and computer moves
    """when a player selects row r and column c, it will change the matrix board into the player1 piece.
    Returns the matrix board
    """
    if playernum == 1:
        while my_mat [r, c] == 1 or (r >= 1) and (r <= s-2) and (c <= s-2) and (c >= 1) or (r < 0) or (c < 0) or (r > s) or (c > s):
            print('invalid move, you can only choose the row and column that has a blank face or your own symbol on the outer boundary')
            r = int(input('Please select a row from the outer boundary:'))
            c = int(input('Please select a column from the outer boundary:'))
    else:
        while my_mat [r, c] == -1 or (r >= 1) and (r <= s-2) and (c <= s-2) and (c >= 1) or (r < 0) or (c < 0) or (r > s) or (c > s):
            r = random.randint(0, s-1)
            c = random.randint(0, s-1)
        
    if [r,c]==[0,0]:    #TOP LEFT CORNER
        if playernum == 1:
            direction=d
            while direction != 'UP' and direction != 'LEFT':
                print('Please think clearly and try again')
                direction=input('Please push UP or LEFT (case sensitive):')
        else:
            direction=d
            while direction != 'UP' and direction != 'LEFT':
                direction=comdirection()
        if direction == 'UP': #if player chooses up direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,0] #assign the entries onto the first column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first row and first column) shift the remaining elements to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position
            for y in range(s):
                my_mat[y,0]=my_column2[y] #replace the first column of my_mat with my_column2
        
        else:   #if player choose to move in the left direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[0,:] #assign the entries onto the first row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first row and first column) shift the remaining entries to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position 
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position 
            for y in range(s):
                my_mat[0,y]=my_column2[y] #replace the first row of my_mat with my_column2

        
    elif [r, c] == [0, s-1]: #TOP RIGHT CORNER CASE
        if playernum == 1:
            direction=d
            while direction != 'UP' and direction != 'RIGHT':
                print('Please think clearly and try again')
                direction=input('Please push UP or RIGHT (case sensitive):')
        else:
            direction=d
            while direction != 'UP' and direction != 'RIGHT':
                direction=comdirection()
        if direction == 'UP': #if player chooses up direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,s-1] #assign the entries onto the last column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first row and last column) shift the remaining elements to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position
            for y in range(s):
                my_mat[y,s-1]=my_column2[y] #replace the last column of my_mat with my_column2
        
        else:   #if player choose to move in the right direction 
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[0,:] #assign the entries onto the first row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x] #after removing the first piece(from the first row and last column) shift the remaining entries to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]), my_column1]) #join back the first piece as the last position 
            else:
                my_column2 = np.concatenate([np.array([1]), my_column1]) #join back the first piece as the last position 
            for y in range(s):
                my_mat[0,y]=my_column2[y] #replace the first row of my_mat with my_column2
         
    elif [r, c] == [s-1, 0]: #BOTTOM LEFT CORNER CASE
        if playernum == 1:
            direction=d
            while direction != 'DOWN' and direction != 'LEFT':
                print('Please think clearly and try again')
                direction=input('Please push DOWN or LEFT (case sensitive):')
        else:
            direction = d
            while direction != 'DOWN' and direction != 'LEFT':
                direction = comdirection()
        if direction == 'DOWN': #if player chooses down direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,0] #assign the entries onto the first column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x] #after removing the first piece(from the first column and last row) shift the remaining elements to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1]) #join back the first piece as the last position
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1]) #join back the first piece as the last position
            for y in range(s):
                my_mat[y,0]=my_column2[y] #replace the first column of my_mat with my_column2
        
        else:   #if player choose to move in the left direction 
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[s-1,:] #assign the entries onto the last row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x+1] #after removing the first piece(from the first column and last row) shift the remaining entries to replace the removed entry position
            if playernum == 1 :
                my_column2 = np.concatenate([my_column1,np.array([-1])]) #join back the first piece as the last position 
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])]) #join back the first piece as the last position 
            for y in range(s):
                my_mat[s-1,y]=my_column2[y] #replace the last row of my_mat with my_column2
    
    elif [r, c] == [s-1, s-1]: #BOTTOM RIGHT CORNER CASE
        if playernum == 1:
            direction=d
            while direction != 'DOWN' and direction != 'RIGHT':
                print('Please think clearly and try again')
                direction=input('Please push DOWN or RIGHT (case sensitive):')
        else:
            direction = d
            while direction != 'DOWN' and direction != 'RIGHT':
                direction = comdirection()
        if direction == 'DOWN': #if player chooses down direction
            my_column = np.linspace(0,0,s) #making the new vector with s entries
            my_column = my_mat[:,s-1] #assign the entries onto the last column
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x] #after removing the first piece(from the last row and last column) shift the remaining elements to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1]) #join back the first piece as the last position
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1]) #join back the first piece as the last position
            for y in range(s):
                my_mat[y,s-1]=my_column2[y] #replace the last column of my_mat with my_column2
        
        else:   #if player choose to move in the right direction 
            my_column = np.linspace(0,0,s) #making the new vector with s entries 
            my_column = my_mat[s-1,:] #assign the entries onto the last row 
            my_column1 = np.linspace(0,0,s-1) #making the new vector with s-1 entries
            for x in range(s-1): 
                my_column1[x]=my_column[x] #after removing the first piece(from the last row and last column) shift the remaining entries to replace the removed entry position
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]), my_column1]) #join back the first piece as the last position 
            else:
                my_column2 = np.concatenate([np.array([1]), my_column1]) #join back the first piece as the last position 
            for y in range(s):
                my_mat[s-1,y]=my_column2[y] #replace the last row of my_mat with my_column2
            
            
#TOP EDGE SIDES
    elif r == 0 and c != 0 and c != (s-1):
        if playernum == 1:
            direction=d
            while not (direction == 'UP' or direction == 'LEFT' or direction == 'RIGHT'):                                               #Error check
                print('Please think clearly and try again')
                direction=input('Please push UP or LEFT or RIGHT (case sensitive):') #if the user input correctly, will break the while loop automatically
        else:
            direction = d
            while direction == 'DOWN':                                               #Error check
                direction = comdirection()
        if direction == 'UP':
            my_column = np.linspace(0,0,s)
            my_column = my_mat[:,c]                                             #equating my_column with c column of the my_mat.
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):                                                
                my_column1[x]=my_column[x+1]                                    #Index of my_column1 eg [1] = my_column eg [2], Hence the link is x+1
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])             #adding np.array([-1]) to the end of my_column1
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])             #adding np.array([1]) to the end of my_column1
            for y in range(s):                                                  #Running through every s
                my_mat[y,c]=my_column2[y]                                       #replace the y row, c column of the my_mat with my_column2
        
        elif direction == 'LEFT':
            my_column = np.linspace(0,0,s)
            my_column = my_mat[r,:]                                             #equating my_column with r row of the my_mat. In general if push horizontally use row easier, if push vertically use column easier
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                if x < c:                                                       #for x < c your index of my_column1 and my_column will be the same
                    my_column1[x]=my_column[x]
                else:                                                           #else when x > c your index of my_column1 eg=2 will be the index of my_column eg=3, so the pattern for index is x+1
                    my_column1[x]=my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])             #inserting np.array[-1] at the end of my_column1
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])             #inserting np.array[1] at the end of my_column1
            for y in range(s):
                my_mat[r,y]=my_column2[y]                                       #replacing the r row with y column of my_mat with entire my_column2
        
        
        else:
            my_column = np.linspace(0,0,s)
            my_column = my_mat[r,:]
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                if x < c:
                    my_column1[x]=my_column[x]
                else:
                    my_column1[x]=my_column[x+1]
            if playernum == 1:
                my_column2=np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2=np.concatenate([np.array([1]),my_column1])
            for y in range(s):
                my_mat[r,y]=my_column2[y]
        
                
#BOTTOM EDGE SIDES
    elif r == s-1 and c != 0 and c != (s-1):
        if playernum == 1:
            direction=d
            while not (direction == 'DOWN' or direction == 'LEFT' or direction == 'RIGHT'):
                print('Please think clearly and try again')
                direction=input('Please push DOWN or LEFT or RIGHT (case sensitive):')
        else:
            direction = d
            while direction == 'UP':
                direction = comdirection()
        if direction == 'DOWN':
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[:,c] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                my_column1[x]=my_column[x]
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1])
            for y in range(s):
                my_mat[y,c] = my_column2[y]
         
        elif direction == 'LEFT':
            my_column = np.linspace(0,0,s)
            my_column = my_mat[r,:]                                             #equating my_column with r row of the my_mat
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                if x < c:
                    my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])

            for y in range(s):
                my_mat[r,y] = my_column2[y]
         
        else:
            my_column = np.linspace(0,0,s)
            my_column = my_mat[r,:]
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1): 
                if x < c:
                     my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1])
            for y in range(s): 
                my_mat[r,y] = my_column2[y]
          
#LEFT EDGE SIDE
    elif c == 0 and r != 0 and r != (s-1):
        if playernum == 1:
            direction=d
            while not (direction == 'UP' or direction == 'LEFT' or direction == 'DOWN'):
                print('Please think clearly and try again')
                direction=input('Please push LEFT or UP or DOWN (case sensitive):')
        else:
            direction = d
            while direction == 'RIGHT':
                direction = d
        if direction == 'LEFT':
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[r,:] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                my_column1[x]=my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])
            for y in range(s):
                my_mat[r,y] = my_column2[y]
                
         
        elif direction == 'UP':
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[:,c] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1): 
                if x < r:
                    my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])
            for y in range(s): 
                my_mat[y,c] = my_column2[y]
        
        
        else:
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[:,c] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1): 
                if x < r:
                    my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1])
            for y in range(s): 
                my_mat[y,c] = my_column2[y]
        
#RIGHT EDGE SIDE
    elif c == (s-1) and r != 0 and r != (s-1):
        if playernum == 1:
            direction=d
            while not (direction == 'UP' or direction == 'DOWN' or direction == 'RIGHT'):
                print('Please think clearly and try again')
                direction=input('Please push RIGHT or UP or DOWN (case sensitive):')
        else:
            direction = d
            while direction == 'LEFT':
                direction = comdirection()
        if direction == 'RIGHT':
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[r,:] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1):
                my_column1[x]=my_column[x]
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1])
            for y in range(s):
                my_mat[r,y] = my_column2[y]
                       
         
        elif direction == 'UP':
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[:,c] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1): 
                if x < r:
                    my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([my_column1,np.array([-1])])
            else:
                my_column2 = np.concatenate([my_column1,np.array([1])])
            for y in range(s): 
                my_mat[y,c] = my_column2[y]
        
        
        else:
            my_column = np.linspace(0,0,s) 
            my_column = my_mat[:,c] 
            my_column1 = np.linspace(0,0,s-1)
            for x in range(s-1): 
                if x < r:
                    my_column1[x] = my_column[x]
                else:
                    my_column1[x] = my_column[x+1]
            if playernum == 1:
                my_column2 = np.concatenate([np.array([-1]),my_column1])
            else:
                my_column2 = np.concatenate([np.array([1]),my_column1])
            for y in range(s): 
                my_mat[y,c] = my_column2[y]  
    return my_mat





def AIrandomplayer(my_mat,s): #random computer player
    r=-1
    c=-1    
    while my_mat [r, c] == -1 or (r >= 1) and (r <= s-2) and (c <= s-2) and (c >= 1) or (r < 0) or (c < 0) or (r > s) or (c > s):
            r = random.randint(0, s-1)
            c = random.randint(0, s-1)
    movecom(r, c, my_mat, s, 2)
    printmat(my_mat,s)
    return my_mat

def checkd_(r,c,d,s):                        #This function checks the validity of the direction with respect to the pieces of the board 
    if [r,c]==[0,0]:        #Top Left corner                  
        if d == 'UP':                        
            return d                         
        elif d == 'LEFT':                    
            return d                         
                                             
    elif [r, c] == [0, s-1]:#Top right corner
        if d == 'UP':
            return d
        elif d == 'RIGHT':
            return d
        
    elif [r, c] == [s-1, 0]: #Bottom left corner 
        if d == 'DOWN':
            return d
        elif d == 'LEFT':
            return d
        
    elif [r, c] == [s-1, s-1]: #Bottom right corner 
        if d == 'DOWN':
            return d
        elif d == 'RIGHT':
            return d 
        
    elif r == 0 and c != 0 and c != (s-1): ##Top edge 
        if d == 'UP':
            return d
        elif d == 'LEFT':
            return d
        elif d == 'RIGHT':
            return d
    
    elif r == s-1 and c != 0 and c != (s-1): #Bottom edge 
        if d == 'DOWN':
            return d
        elif d == 'LEFT':
            return d
        elif d == 'RIGHT':
            return d
        
    elif c == 0 and r != 0 and r != (s-1): #Left edge 
        if d == 'LEFT':
            return d
        elif d == 'UP':
            return d
        elif d == 'DOWN':
            return d
        
    elif c == (s-1) and r != 0 and r != (s-1): #Right edge 
        if d == 'RIGHT':
            return d
        elif d == 'UP':
            return d
        elif d == 'DOWN':
            return d
    else:
        return 0
    



def simple(my_mat,s):
    for i in range(s):
        r=i #Loop for row 
        for j in range(s):
            c=j #Loop for column 
            while not (my_mat [r, c] == -1 or (((r >= 1) and (r <= s-2)) and ((c <= s-2) and (c >= 1))) or (r < 0) or (c < 0) or (r > s) or (c > s)):
                dc='UP' #Set direction to UP
                direction=checkd_(r,c,dc,s)
                if direction!=0:
                    my_mat1=my_mat.copy()
                    my_mat1=movecom1 (r, c, direction, my_mat1, s, 2)
                    if win(my_mat1, s, 2)==2: 
                                                           
                        return (r,c,'UP')                                            
                                                                                 
                dc='RIGHT' #Loop for RIGHT                                                       
                direction=checkd_(r,c,dc,s)                                      
                if direction!=0:                                                 
                    my_mat1=my_mat.copy()                                        
                    my_mat1=movecom1 (r, c, direction, my_mat1, s, 2)
                    if win(my_mat1, s, 2)==2:                                                                           
                        return (r,c,'RIGHT')                                             
                                                                                
                dc='LEFT'   #Loop for LEFT                                                    
                direction=checkd_(r,c,dc,s)
                if direction!=0:
                    my_mat1=my_mat.copy()
                    my_mat1=movecom1 (r, c, direction, my_mat1, s, 2)
                    if win(my_mat1, s, 2)==2:
                        return (r,c,'LEFT') 
                
                dc='DOWN' #Loop for DOWN
                direction=checkd_(r,c,dc,s)
                if direction!=0:
                    my_mat1=my_mat.copy()
                    my_mat1=movecom1 (r, c, direction, my_mat1, s, 2)
                    if win(my_mat1, s, 2)==2:
                        return (r,c,'DOWN') 
                    
                break
    return 0 #return 0 when no winning move is possible 
    
                    
choice = input('Do you want to choose your board size? (please choose YES or NO)(case sensitive): ')

#error check for choice
while choice != 'YES' and choice != 'NO': 
    print('invalid choice')
    choice = input('Do you want to choose your board size? (please choose YES or NO)(case sensitive): ')


#creating the default board
if choice == 'NO':
    s = 5 
    my_mat = np.zeros([s, s])
    printmat(my_mat,s)

#board based on player's choice    
elif choice == 'YES':
    s = (int(input('Please enter the size of the board:')))
    #error check
    while s <= 2: 
        print('error')
        s = (int(input('Please enter the size of the board:')))
    my_mat = np.zeros([s,s])
    printmat(my_mat,s)


wincon=-1
while wincon!=0:
    print('Player 1 turn \nYour piece is O') 
    while True:
        try:
            x = input('Please select a row from the outer boundary:')
            y = input('Please select a column from the outer boundary:')
            r=int(x)
            c=int(y)
            if my_mat[r,c] == 1:
                print('Please select your own symbol or a blank face')
            elif (r >= 1) and ((r <= s-2) and (c <= s-2) and (c >= 1)) or (r < 0) or (c < 0) or (r >= s) or (c >= s) :
                print('error, please select only the outer boundary blocks')
            else:
                break
        except:
            print("Please input an integer, only select from the outer boundaries and you can only choose your own symbol or a blank face. \n")
     
    movecom(r, c, my_mat, s, 1)
    printmat(my_mat,s)
    if win(my_mat, s, 1) != 0:
        wincon=0
        print('The player has won')
        break
    print('Computer turn')
    a=[]  #Create a list to store the winning move
    a.append(simple(my_mat,s))  #append the winning move
    if simple(my_mat,s) == 0:  #If there is no winnning move, computer will make random move.
        AIrandomplayer(my_mat,s)
    else: #There is a winning move. Make the winning move
        r=a[0][0]   #Row
        c=a[0][1]   #Column 
        direction=a[0][2] #Direction of winning move 
        movecom1 (r, c, direction, my_mat, s, 2) #Makethe winning move 
        printmat(my_mat,s)
        print('The computer has won')
        break
    
    if win(my_mat, s, 2)==2:
        wincon=0
        break