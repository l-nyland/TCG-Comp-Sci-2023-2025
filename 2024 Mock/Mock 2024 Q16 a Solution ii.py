# Question 16(a)
# Name and School:3
import random

# i)
#player_choice = input('Choose one of rock, paper, scissors:')
#print('You have chosen', player_choice)

def play_round(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'
#ii)
    
options = ['rock', 'paper', 'scissors']
player_win = 0
comp_win = 0
ties = 0

for i in range(0, 3):
    player_choice = 'scissors'
    
    computer_choice = options[random.randint(0, 2)]
    
    x = play_round(player_choice, computer_choice)
    
    print(x)
    
    if x == 'player':
        player_win = player_win + 1
    elif x == 'computer':
        comp_win = comp_win + 1
    else:
        ties = ties + 1
        
print('\t\t Outcome')
print('Player win \t', player_win)
print('Computer win \t', comp_win)
print('Tie \t\t', ties)
    
    


    