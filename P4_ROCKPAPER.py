# ROCK PAPER AND SCISSORS
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors =  """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_ascii = [rock,paper,scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))
print(game_ascii[user_input])

print("Computer Chose:")
computer_choice = random.randint(0,2)
print(game_ascii[computer_choice])

if user_input >= 3 or user_input < 0:
    print("Invalid Input, You Lose")
elif user_input == computer_choice:
    print("It's a DRAW")
elif user_input == 0 and computer_choice == 2:
    print("You Win!")
elif user_input == 2 and computer_choice == 0:
    print("You Lose!")
elif user_input > computer_choice:
    print("You Win!")
elif user_input < computer_choice:
    print("You Lose!")


# else:
#     print("You typed an invalid input")