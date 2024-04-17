#Dice Model 2
import random

freq = [0, 0, 0, 0, 0, 0]

def dice():
    roll = random.randint(1, 6)
    return roll

trials = int(input('How many times do you want to roll the dice?'))

ex_freq = trials/6

print('We expect each number to appear', ex_freq, 'times')
             
             
for i in range(trials):
    roll = dice()
    freq[roll-1] +=1
    
print(freq)




    