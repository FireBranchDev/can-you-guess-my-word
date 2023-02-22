#!/usr/bin/env python3

"""Can You Guess My Word

Can You Guess My Word is a cli version of the popular Wordle game.
The game will randomly pick a word that the user must guess within
the maximum number of attempts. For each guess the player will be
given feedback to whether the letter is in the correct spot,
in the word or not in the word at all.
"""

import doctest

from play import play


def main(test=False):
    """main entry point for Can You Guess My Word"""
    if test:
        return doctest.testmod()

    continue_game = True
    while continue_game:
        play()
        print("\nDo you want to play again?")

        answer = input("y/n: ")
        continue_game = answer.lower() == "y"

    print("Thanks for playing, hope to see you again")


if __name__ == "__main__":
    print(main(test=False))
