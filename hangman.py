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
    state = funcs.update_state(word, attempt, state)
    underscores = funcs.update_underscores(word, attempt, underscores)
    os.system('clear')

if state == 6:
    funcs.show_hangman(state)
    print(word)
    print("\nYou die!!!")
else:
    funcs.show_hangman(state)
    print(underscores)
    print("\nYou win!")
