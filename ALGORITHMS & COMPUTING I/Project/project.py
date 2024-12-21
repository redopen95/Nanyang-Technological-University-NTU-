#create menu
print('Menu Selection')
print('1) player vs player')
print('2) player vs computer')

game_play=int(input('Please select the game mode (1 or 2):')) #allow player to choose the game mode 

#error check for menu  
while game_play != 1 and game_play != 2: 
    print('Please choose either 1 or 2 only')
    game_play=input('Please select the game mode:')

#if player chooses 1
if game_play == 1:
    import playervsplayer
    print(playervsplayer)
    
#if player chooses 2 then allow the player to choose the level of difficulty
if game_play == 2:
    print('Please choose the level of difficulty')
    print('1) Easy')
    print('2) Normal')
    while True:
        lvl = 0
        try: #error check for level
            while lvl != 1 and lvl != 2: #error check for level
                print('Please choose either 1 or 2 only')
                lvl = int(input('Please choose the level of difficulty (1 or 2):'))
            break
        except: 
            print('Please input an integer either 1 or 2 only')
    if lvl == 1: #if player chooses 1, import the file for the player vs random computer
        import playervsrandcom
        print(playervsrandcom)
    else: #if player chooses 2, import the file for the player vs simple computer
        import playervssimple
        print(playervssimple)
    

    
    