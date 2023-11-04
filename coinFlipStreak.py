# This is a program that randomizes a coin flip and checks how many times a streak of 6 heads or 6 tails occurs in a row and records it after every 100 coin flips for 10000 times and gives a percentage of how many times a streak would occur.
import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # creates a list of 100 'heads' or 'tails' values.
    coinFlips = []
    for i in range(100):
        coinFlips.append(random.randint(0, 1))      # 0 ='heads' and 1 = tails

    # checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(coinFlips) -5):
        if all(coinFlips[i + j] == coinFlips[i] for j in range(6)):
            numberOfStreaks +=1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
