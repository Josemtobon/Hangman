"""
Functions to play hangman.
"""

import random

def get_word():
    """
    Choose a random word.
    """
    animal_list = [
        "Aardvark", "Albatross", "Alligator", "Alpaca", "Ant", "Anteater",
        "Antelope", "Ape", "Armadillo", "Donkey", "Baboon", "Badger", "Barracuda",
        "Bat", "Bear", "Beaver", "Bee", "Bison", "Boar", "Buffalo", "Butterfly",
        "Camel", "Capybara", "Caribou", "Cassowary", "Cat", "Caterpillar", "Cattle",
        "Chamois", "Cheetah", "Chicken", "Chimpanzee", "Chinchilla", "Chough",
        "Clam", "Cobra", "Cockroach", "Cod", "Cormorant", "Coyote", "Crab", "Crane",
        "Crocodile", "Crow", "Curlew", "Deer", "Dinosaur", "Dog", "Dogfish",
        "Dolphin", "Dotterel", "Dove", "Dragonfly", "Duck", "Dugong", "Dunlin",
        "Eagle", "Echidna", "Eel", "Eland", "Elephant", "Elk", "Emu", "Falcon",
        "Ferret", "Finch", "Fish", "Flamingo", "Fly", "Fox", "Frog", "Gaur",
        "Gazelle", "Gerbil", "Giraffe", "Gnat", "Gnu", "Goat", "Goldfinch",
        "Goldfish", "Goose", "Gorilla", "Goshawk", "Grasshopper", "Grouse",
        "Guanaco", "Gull", "Hamster", "Hare", "Hawk", "Hedgehog", "Heron",
        "Herring", "Hippopotamus", "Hornet", "Horse", "Human", "Hummingbird",
        "Hyena", "Ibex", "Ibis", "Jackal", "Jaguar", "Jay", "Jellyfish",
        "Kangaroo", "Kingfisher", "Koala", "Kookaburra", "Kouprey", "Kudu",
        "Lapwing", "Lark", "Lemur", "Leopard", "Lion", "Llama", "Lobster",
        "Locust", "Loris", "Louse", "Lyrebird", "Magpie", "Mallard", "Manatee",
        "Mandrill", "Mantis", "Marten", "Meerkat", "Mink", "Mole", "Mongoose",
        "Monkey", "Moose", "Mosquito", "Mouse", "Mule", "Narwhal", "Newt",
        "Nightingale", "Octopus", "Okapi", "Opossum", "Oryx", "Ostrich", "Otter",
        "Owl", "Ox", "Oyster", "Panther", "Parrot", "Partridge", "Peafowl",
        "Pelican", "Penguin", "Pheasant", "Pig", "Pigeon", "Pony", "Porcupine",
        "Porpoise", "Quail", "Quelea", "Quetzal", "Rabbit", "Raccoon", "Rail",
        "Ram", "Rat", "Raven", "Red deer", "Red panda", "Reindeer", "Rhinoceros",
        "Rook", "Salamander", "Salmon", "Sand Dollar", "Sandpiper", "Sardine",
        "Scorpion", "Seahorse", "Seal", "Shark", "Sheep", "Shrew", "Skunk", "Snail",
        "Snake", "Sparrow", "Spider", "Spoonbill", "Squid", "Squirrel", "Starling",
        "Stingray", "Stinkbug", "Stork", "Swallow", "Swan", "Tapir", "Tarsier",
        "Termite", "Tiger", "Toad", "Trout", "Turkey", "Turtle", "Viper", "Vulture",
        "Wallaby", "Walrus", "Wasp", "Weasel", "Whale", "Wildcat", "Wolf",
        "Wolverine", "Wombat", "Woodcock", "Woodpecker", "Worm", "Wren", "Yak",
        "Zebra"
    ]

    return random.choice(animal_list)


def word_underscores(word):
    """
    Transforms the word into underscores and prints the result.
    """
    underscores = "_" * len(word)

    return underscores


def update_underscores(word, attempt, underscores, state):
    """
    Replace underscores by coincidences.
    """
    lower_word = word.lower()
    lower_attempt = attempt.lower()
    attempt_length = len(attempt)
    underscores_list = list(underscores)
    state_list = []

    for i, c in enumerate(lower_word):
        if attempt_length == 1:
            if c in lower_attempt:
                underscores_list[i] = c
                state_list.append(True)
            else:
                state_list.append(False)
        elif attempt_length == len(word):
            if c == lower_attempt[i]:
                underscores_list[i] = c
                state_list.append(True)
            else:
                state_list.append(False)

    if not any(state_list):
        state += 1

    if underscores_list[0] != "_":
        underscores_list[0] = underscores_list[0].upper()

    new_underscores = ''.join(underscores_list)

    return new_underscores, state


def show_hangman(state):
    """
    Prints hangman on each try.
    """
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
    print(states[state])
