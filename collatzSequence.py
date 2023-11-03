#This is the Collartz Sequence whereby a number is evaluated multiple times until it returns 1 as its final answer.
# Mathematicians call it 'the simplest impossible math problem'.

import sys

def collatz(number):
    global newNumber
    if number % 2 == 0:
        newNumber = number // 2
        return newNumber
    else: 
        print(3 * number + 1)
        newNumber = 3 * number + 1
        return newNumber

try:
    #user input must not be zero
    while True:
        userInput = int(input('Enter a number: '))
        if userInput == 0:
            print('Invalid argument! Try again.')
            continue
        else: 
            collatz(userInput)
            break
        
    #program re-evaluates itself until it arrives at 1
    while newNumber != 1:
        collatz(newNumber)
        print(newNumber)

except ValueError:
    print('Value must be an integer.')
    sys.exit()
