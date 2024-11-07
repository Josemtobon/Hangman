import requests

def get_word():
    """
    Obtain a random word with Random-Words-API
    https://github.com/mcnaveen/Random-Words-API
    """
    response = requests.get("https://random-word-api.herokuapp.com/word")
    if response.status_code == 200:
        word = response.json()[0]
        return word
    else:
        print("Was not possible get a word")

def print_underscores(word):
    pass


def show_hangman():
    states = [
        """
           ------
           |    |
           |
           |
           |
           |
        =========
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        =========
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        =========
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        =========
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        =========
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        =========
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        =========
        """
    ]
    print(states[-1])
