import random
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
choices = [rock, paper, scissors]

user_turn = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(choices[user_turn])

computer_turn = random.randint(0,2)
print("Computer chose:\n")
print(choices[computer_turn])

if user_turn == 0 and computer_turn == 2:
  print("You won")
elif user_turn == 2 and computer_turn == 1:
  print("You won")
elif user_turn == 1 and computer_turn == 0:
  print("You won")
elif user_turn == computer_turn:
  print("It's a draw")
else:
  print("You lost")

exit()