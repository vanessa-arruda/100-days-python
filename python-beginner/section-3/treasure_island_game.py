print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("*********************************************")
print("TREASURE ISLAND GAME - YOUR UNIQUE ADVENTURE!")
print("*********************************************\n\n")


username = str(input("What's your name?\n"))

print(
    f"""
{username} is an adventurer that has just arrived in Treasure Island dungeon's gate.
Your mission is to find the treasure! The decision is in your hands now...
Are you brave and lucky enough to go in?
"""
)

is_entering = input("Will you enter the dungeon? 'Yes' or 'No'\n").upper()
if is_entering == "YES":
    print("You unsheath your sword and go in! For GLORY and for GOLD!")
    print(
        """
        .
        .
        .
        """
    )
    first_move = input("Where do you want to go? 'LEFT' or 'RIGHT'?\n").upper()

    if first_move == "LEFT":
        print(
            """
            You start moving left in the dark durty corridor...
            After a while, you end up at a cave that's sorrounded by a dark river... and a huge golden door on the other side of it.
            On the left side you are able to see three doors guarded by 2 big armed orcs.
            You could wait for them to move away from the smaller doors or try to swim the river to go to the golden door.
            """
        )
        second_move = input("What will you do? 'SWIM' or 'WAIT'?\n").upper()
        if second_move == "WAIT":
            print(
                """
                  You decided to wait... the orcs are leaving in the direction of another corridor...
                  You can choose a door to open and go inside!
                  You see each door has a different color. What will you do?
                  """
            )
            third_move = input("Open the RED, YELLOW or BLUE door?\n").upper()
            if third_move == "RED":
                print(
                    f"""
                      As {username} opens the {third_move} door and enters the room, an explosion happens.
                      {username} gets burned by fire.
                      Game Over!
                      """
                )
            elif third_move == "BLUE":
                print(
                    f"""
                      As {username} opens the {third_move} door and enters the room, the door immediatelly gets locked.
                      {username} gets eaten by beasts.
                      Game Over!
                      """
                )
            elif third_move == "YELLOW":
                print("You found the right door! You found the treasure! You Win!")
            else:
                print("That was a wrong choice - Game Over!")

        else:
            print(
                """
                  You go into the river's direction and start swimming... you didn't notice a giant Trout was there, starving...
                  The giant Trout eats you alive!

                  YOU ARE DEAD!
                  Game over.
                  """
            )
    else:
        print(
            """
              As you go further into the right path, it gets darker and darker..
              You suddenly loose all vision and FELL IN A HOLE... it was deep.
              YOU DIED.
              Game over.
              """
        )
else:
    print(
        "After sometime looking at the gate's, you get strongly afraid and decide to leave and return other day. Game ended."
    )
