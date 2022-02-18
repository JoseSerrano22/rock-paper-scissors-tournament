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

import random

signs = [rock, paper, scissors]

print("Welcome to the Ultimate Rock Paper Scissor Tournament!\n")

playerAction = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))

botAction = random.randint(0,2)

if(playerAction == 0 and botAction == 0):
  print(f"you choose:{signs[playerAction]}\n bot choose:{signs[botAction]}\n")
  print("Tie")

elif(playerAction == 0 and botAction == 1):
  print(f"you choose:{signs[playerAction]}\n bot choose:{signs[botAction]}\n")
  print("You Lose\n ¯\_(⊙︿⊙)_/¯")

elif(playerAction == 0 and botAction == 2):
  print(f"you choose:{signs[playerAction]}\n bot choose:{signs[botAction]}\n")
  print("Player Win\n ＼(＾O＾)／")

elif(playerAction == 1 and botAction == 1):
  print(f"you choose:{signs[playerAction]}\n bot choose:{signs[botAction]}\n")
  print("Tie")

elif(playerAction == 1 and botAction == 2):
  print(f"you choose:{signs[playerAction]}\n bot choose:{signs[botAction]}\n")
  print("You Lose\n ¯\_(⊙︿⊙)_/¯")

elif(playerAction == 1 and botAction == 0):
  print(f"you choose:{signs[playerAction]}\n bot choose:{signs[botAction]}\n")
  print("Player Win\n ＼(＾O＾)／")

elif(playerAction == 2 and botAction == 2):
  print(f"you choose:{signs[playerAction]}\n bot choose:{signs[botAction]}\n")
  print("Tie")

elif(playerAction == 2 and botAction == 0):
  print(f"you choose:{signs[playerAction]}\n bot choose:{signs[botAction]}\n")
  print("You Lose\n ¯\_(⊙︿⊙)_/¯")

elif(playerAction == 2 and botAction == 1):
  print(f"you choose:{signs[playerAction]}\n bot choose:{signs[botAction]}\n")
  print("Player Win\n ＼(＾O＾)／")
#ji 