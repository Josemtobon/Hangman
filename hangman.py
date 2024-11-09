"""
Starts hangman game.
"""

import os
import funcs

os.system("clear")
word = funcs.get_word()
underscores = funcs.word_underscores(word)
state = 0

while underscores != word and state < 7:
    while True:
        funcs.show_hangman(state)
        print("        " + underscores)
        attempt = input("\nMake a try: ")
        os.system('clear')
        if len(attempt) == len(word) or len(attempt) == 1:
            break
    underscores, state = funcs.update_underscores(word, attempt, underscores, state)
    os.system('clear')

if state == 7:
    funcs.show_hangman(state)
    print("        " + word)
    print("\nYou die!!!")
else:
    funcs.show_hangman(state)
    print("        " + underscores)
    print("\nYou win!!!")
