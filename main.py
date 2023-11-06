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
import random
game_img=[rock,paper,scissors]
print("Welcome to ROCK, PAPER AND SCISSORS game!")
choice=int(input("Choose\n0 for rock\n1 for paper\n2 for scissors:\n"))
print("you choose")
print(game_img[choice])
comp_choice=random.randint(0,2)
print("computer choose:")
print(game_img[comp_choice])
if choice>=3 or choice<0:
 print("Typed an invalid number")
elif choice==0 and comp_choice==2:
 print("You WIN!")
elif choice==2 and comp_choice==0:
  print("You LOST")
elif comp_choice>choice:
  print("You LOST")
elif choice>comp_choice:
  print("You WIN!")
elif comp_choice==choice:
  print("It's a Draw")


