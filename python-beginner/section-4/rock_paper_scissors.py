import random

# global variables
hand_choice = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
}


def get_computer_choice() -> str:
    return random.choice(list(hand_choice.keys()))


def get_user_choice() -> str:
    return str(input("Type your choice: Rock, paper or scissors? ")).lower()


def game_match():
    # Game presentation
    print(
        """--------LET'S PLAY ROCK, PAPER, SCISSORS!---------

        _______            _______               _______
    ---'   ____)___    ---'   ____)____      ---'   ____)____
             (_____)              ______)              ______)
             (_____)              _______)         ___________)
             (____)              _______)         (____)
    ---._____(___)     ---.__________)       ---._(___)
    \n"""
    )
    print("--------------------------------------------------")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print()
    print(f"You chose: {user_choice}!")
    print(hand_choice[user_choice])
    print(f"Computer chose: {computer_choice}!")
    print(hand_choice[computer_choice])

    if user_choice == "scissors" and computer_choice == "rock":
        print("You LOST! ROCK breaks SCISSORS!")
    elif user_choice == "rock" and computer_choice == "paper":
        print("You LOST! PAPER covers ROCK!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You WIN! ROCK breaks SCISSORS!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You WIN! PAPER covers ROCK!")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("You LOST! SCISSORS cut PAPER!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You WIN! SCISSORS cut PAPER!")
    else:
        print("It's a tie!")


game_match()
