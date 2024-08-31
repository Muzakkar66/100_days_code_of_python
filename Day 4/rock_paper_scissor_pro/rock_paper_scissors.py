import random

print("Welcome to the rock paper game\n")
print("Game rules\n"
        "1. Rock wins against scissors."
        "2. Scissors win against paper."
        "3. Paper wins against rock.")
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

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

user_chose = int(input("what do you choose? Type 0 for rock, 1 for paper and 2 for scissor."))
print(game_images[user_chose])

computer_choice = random.randint(0, 2) # range is from 0 to 2 because 0 for rock, 1 for paper and 2 for scissor
print(game_images[computer_choice])
print("computer choice:", computer_choice)

if user_chose == 0 and computer_choice == 2:
        print("You Win!")
elif computer_choice == 0 and user_chose == 2 :
        print("ou lose!")
elif user_chose > computer_choice:
        print("You lose!")
elif user_chose == computer_choice:
        print("Tie, Try again!")
elif user_chose >= 3 or user_chose < 0:
        print("You typed Invalid number, You lose!")

