"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
guess the number, then tell them whether they guessed too low, too high, or exactly right.
    Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random as rd
min, max=1, 9
guessed = 0
attempts = 0
exit = 'Go On'
start_again = 1

while exit!='exit':
    if start_again==1:
        generated = rd.randint(min,max)
        print("The random number is generated, now please guess the number")
        guessed = 0
        attempts = 0
        start_again=0
    else:
        guessed = int(input())
        attempts += 1
        if guessed==generated:
            print("Exactly Right")
            print("You took ",attempts," attempt/attempts to guess the number.")
            print("Press 'ENTER' to play again,type 'exit' to exit !")
            start_again=1
            exit = input()
        elif guessed>generated:
            print("High")
            print("Please guess the number again!")
        elif guessed<generated:
            print("Low")
            print("Please guess the number again!")
