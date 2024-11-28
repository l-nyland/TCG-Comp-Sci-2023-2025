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
p_w_rock = 0
p_w_paper = 0
p_w_scissors = 0
c_w_rock = 0
c_w_paper = 0
c_w_scissors = 0
tie_rock = 0
tie_paper = 0
tie_scissors = 0

n = int(input('How many times do you want to play?'))

for i in range(0, n):
    player_choice = options[random.randint(0,2)]
    computer_choice = options[random.randint(0, 2)]
    
    x = play_round(player_choice, computer_choice)
    if x == 'player':
        player_win = player_win + 1
        
        if player_choice == 'rock':
            p_w_rock = p_w_rock + 1
        elif player_choice == 'scissors':
            p_w_scissors = p_w_scissors + 1
        else:
            p_w_paper = p_w_paper +1
        
    elif x == 'computer':
        comp_win = comp_win + 1
        
        if computer_choice == 'rock':
            c_w_rock = c_w_rock + 1
        elif computer_choice == 'scissors':
            c_w_scissors = c_w_scissors + 1
        else:
            c_w_paper = c_w_paper +1
    else:
        ties = ties + 1
        
        if player_choice == 'rock':
            tie_rock = tie_rock + 1
        elif player_choice == 'scissors':
            tie_scissors = tie_scissors + 1
        else:
            tie_paper = tie_paper +1
        
print('\t\t Outcome \t Rock \t\t Paper \t\t Scissors')
print('Player win \t', player_win, '\t\t', p_w_rock, '\t\t', p_w_paper, '\t\t', p_w_scissors)
print('Computer win \t', comp_win, '\t\t', c_w_rock, '\t\t', c_w_paper, '\t\t', c_w_scissors)
print('Tie \t\t', ties,'\t\t', tie_rock, '\t\t', tie_paper, '\t\t', tie_scissors)


