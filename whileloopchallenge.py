#!/usr/bin/env python3
"""Number guessing game!"""

import random

def main():
    num= random.randint(1,100)
    x=1
    while x<=5:
    
        guess= input("Guess a number between 1 and 100, enter q to quit at anytime: ")
         
        if guess.lower == 'q':
            break
        try:
            guess = int(guess)
            x+=1
            if guess > num:
                    print("Too high!")

            elif guess < num:
                    print("Too low!")

            else:
                print("Correct!")
                break
        except ValueError:
            print("Please type in an appropriate number")        
main()
