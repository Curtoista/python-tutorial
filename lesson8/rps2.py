import sys
import random
from enum import Enum

class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3
    
play_again = True

while play_again:

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.SCISSORS.value)
    # sys.exit()

    
    player_choice = input(
        "\nEnter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit("Invalid Choice, please enter 1, 2, or 3.")

    comp_choice = random.choice("123")

    computer = int(comp_choice)

    #This is how i edited the code to print the names instead of the numbers. The tutorial is going to have me use Enum but i wanted to try it this way first.

    # if player == 1:
    #     playerrps = "Rock"
    # elif player == 2:
    #     playerrps = "Paper"
    # elif player == 3:
    #     playerrps = "Scissors"

    # if computer == 1:
    #     comprps = "Rock"
    # elif computer == 2:
    #     comprps = "Paper"
    # elif computer == 3:
    #     comprps = "Scissors"

    # print('')
    # print("You chose " + playerrps + ".")
    # print("Python chose " + comprps + ".")
    # print("")

    
    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")
    


    if player == 1 and computer == 3:
        print("🪨  beats ✂️ , you win! 😄")
    elif player == 2 and computer == 1:
        print("🧻 covers 🪨 , you win! 😄")
    elif player == 3 and computer == 2:
        print("✂️ cuts 🧻 , you win! 😄")
    elif player == computer:
        print("Tie game, please go again! 🤬")
    elif player == 1 and computer == 2:
        print("🧻 covers 🪨 , you lose! 😢")
    elif player == 2 and computer == 3:
        print("✂️ cuts 🧻 , you lose! 😢")
    else:
        print("🪨 beats ✂️ , you lose! 😢")

    play_again = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if play_again.lower() == "y":
        continue
    else:
        print("\n🥳🥳🥳🥳🥳")
        print("Thanks for playing!\n")
        play_again = False
        # break also works


sys.exit("Bye! 👋")