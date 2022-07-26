# Instructions
# Make a rock, paper, scissors game.

# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a 
# corresponding variable: rock, paper, and scissors. This will make it easy to print them out to 
# the console.

# Start the game by asking the player:
# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:
# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.
# You can find the "official" rules of the game on the World Rock Paper Scissors Association 
# website.

import random

from click import option

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options = [rock, paper, scissors]

user_option = input("What do you choose? Type:\n0 for Rock,\n1 for Paper\n2 for Scissors\nYour choice: ")
user_option = int(user_option)

user_choice = options[user_option]
print(options[user_option])

#computer
random_int = random.randint(0, 2)

computer_choice = options[random_int]
print(computer_choice)

if user_choice == 0 and computer_choice == 1:
    print('You lost!')
elif user_choice == 1 and computer_choice == 0:
    print('Congrats! You won')
elif user_choice == 2 and computer_choice == 0:
    print('You lost!')
elif user_choice == 0 and computer_choice == 2:
    print('Congrats! You won')
elif user_choice == 1 and computer_choice == 2:
    print('You Lost!')
else:
    print('Congrats! Yoy won')
