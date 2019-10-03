import random

def guess(): 
    
    while True: 
        try:
            print('\nInput your number  in the box below ↓↓')
            player_input = int(input())                                 #player input 
            generate = random.randint(0,30)                             #random value generated 
        
        except:     # deal with error when a player's input is not a number 
            print('\nSorry you can only put a number. Attempt again by putting a number.') 
            continue
        
        if generate != player_input: 
            print('Oops wrong guess , retry again.\n')
            print(f'The random value is {generate} but the number you gave is {player_input}.')
            continue
        
        else:
            print('Congratulations!!!!!!!!  you had the right guess.')
            break 
            
print(guess())