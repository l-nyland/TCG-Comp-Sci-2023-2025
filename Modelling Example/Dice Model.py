#Dice Model
import random

ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

def dice():
    roll = random.randint(1, 6)
    return roll

for i in range(10000):
    roll = dice()
    if roll == 1:
        ones += 1
    elif roll == 2:
        twos +=1
    elif roll == 3:
        threes +=1
    elif roll == 4:
        fours += 1
    elif roll ==5:
        fives += 1
    else:
        sixes += 1

print(ones, twos, threes, fours, fives, sixes)


    