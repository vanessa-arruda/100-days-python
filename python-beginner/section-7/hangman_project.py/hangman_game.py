import random
from hangman_wordlist import words_list
from hangman_logo import hangman


def get_word(word_list: list) -> str:
    return random.choice(words_list).lower()


def guess_a_letter() -> str:
    guess = ""
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Guess a letter: ").lower()
    return guess


def game() -> str:
    print("-------------------------------------------")
    print("-------- Let's play HANGMAN GAME!! --------")
    print("-------------------------------------------")
    print(f"{hangman[0]}\n")

    chosen_word = get_word(words_list)
    print(f"There are a total of {len(chosen_word)} characters:\n")

    # print(chosen_word)
    placeholder = "_ " * len(chosen_word)
    print(f"{placeholder}\n")

    game_over = False
    correct_letters = []
    live_counter = 6
    hangman_idx = 0

    while not game_over:
        print()
        print(f"****** You have {live_counter} lives left! ******\n")
        display = ""
        guess = guess_a_letter()

        if guess in correct_letters:
            print(f"You've already guessed {guess}. Try again!")

        if guess not in chosen_word:
            live_counter -= 1
            hangman_idx += 1
            print(hangman[hangman_idx])

        for letter in chosen_word:
            if guess == letter:
                display += letter + " "
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter + " "
            else:
                display += "_ "

        print(display)
        if "_ " not in display:
            print()
            print("You won! Congratulations!")
            game_over = True
        elif live_counter <= 0:
            print()
            print("Game over! You've run out of lives.")
            game_over = True

    return


game()
