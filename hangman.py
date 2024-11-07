"""
Starts hangman game.
"""

import os
import funcs

os.system("clear")
word = funcs.get_word()
underscores = funcs.word_underscores(word)
state = 0

while underscores != word and state < 6:
    funcs.show_hangman(state)
    print(underscores)
    attempt = input("Make a try: ")
    while len(attempt) != len(word) and len(attempt) != 1:
        os.system("clear")
        funcs.show_hangman(state)
        print("You can only use words of the same lengt as the real word or letters.")
        print(underscores)
        attempt = input("Try again: ")
    underscores, state = funcs.update_underscores(word, attempt, underscores, state)
    os.system('clear')

if state == 6:
    funcs.show_hangman(state)
    print(word)
    print("\nYou die!!!")
else:
    funcs.show_hangman(state)
    print(underscores)
    print("\nYou win!")
