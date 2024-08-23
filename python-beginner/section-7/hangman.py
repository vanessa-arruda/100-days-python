import random

# global variables
words_list = [
    "LION",
    "TIGER",
    "BANANA",
    "BOTTLE",
    "ORANGE",
    "STRIKE",
    "DECEPTION",
    "FEELINGS",
    "COMPLEXITY",
    "TURTLE",
    "JOURNEY",
    "DUNGEON",
    "STOMACH",
    "PLANET",
]

hangman = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]


def get_word(word_list: list) -> str:
    return random.choice(words_list).lower()


def guess_a_letter() -> str:
    guess = ""
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Guess a letter: ").lower()
    return guess


def check_guess() -> str:
    print("------- Let's play HANGMAN!! -------")
    print(hangman[0])
    print("* Guess the word: ")
    chosen_word = get_word(words_list)
    # print(chosen_word)
    placeholder = "_ " * len(chosen_word)
    print(f"{placeholder}\n")

    game_over = False
    correct_letters = []
    live_counter = 6
    hangman_idx = 0

    while not game_over:
        display = ""
        guess = guess_a_letter()

        if guess not in chosen_word:
            live_counter -= 1
            hangman_idx += 1
            print(hangman[hangman_idx])

        for letter in chosen_word:
            if guess == letter:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print(display)
        if "_" not in display:
            print("You won! Congratulations!")
            game_over = True
        elif live_counter <= 0:
            print("Game over! You've run out of lives.")
            game_over = True

    return


check_guess()
