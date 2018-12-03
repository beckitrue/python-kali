# Project A Play a Number Guessing Game or a Dice Game

import random


def guessing():
    # Guess a randomly generated number between 1 and 99
    # generate a random number
    n = random.randint(1, 99)
    # add a guess counter
    count = 1
    # the guessing loop logic
    guess = int(input("Guess a number between 1 and 99: "))
    while n != guess:
        count += 1
        if guess > n:
            print("High. Try again: ")
        else:
            print("Low. Try again: ")
        guess = int(input("Guess a number between 1 and 99: "))    
    print("Correct!! It took you {:d} guesses".format(count))
    # see if they want to play again
    again = input("Would you like to play again? ")
    if (again == 'yes') or (again == 'y'):
        guessing()
    else:
        print("Thanks for playing")
        return main()


def diceroll():
    # dice rolling game with 2 dice
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    print("your dice came up {:d} and {:d}".format(die_1, die_2))
    again = input("Would you like to play again? ")
    if (again == 'yes') or (again == 'y'):
        diceroll()
    else:
        print("Thanks for playing")
        return main()


def main():
    # ask the player to choose a game
    print("Let's play a game")
    game = int(input('''
        Pick a game.

        Choose [1] for the number game
        Choose [2] for the dice game
        Choose [0] to quit

        '''))
    if game == 1:
        guessing()
    elif game == 2:
        diceroll()
    elif game == 0:
        print("Thanks for playing\n")
        return
    else:
        print("Your input wasn't valid\n")
        main()
    return


main()
