import random 

# ASCII Art for the game
Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

#Computer
choices = [Rock,Paper,Scissors]
computer_choice = random.randint(1,3)

#User
user_choice = int(input("What would you choose? \n\tType 1 for Rock, 2 for Paper, 3 for Scissors: "))
print("Playing")

#Result
print(f"Player Choice \n{choices[user_choice-1]}")
print(f"Computer Choice \n{choices[computer_choice-1]}")
    
#Decision Making
if user_choice == computer_choice:
    print('Draw')
elif user_choice == 1 and computer_choice== 2:
    print('You lose')
elif user_choice== 1 and computer_choice == 3:
    print('You Win')
elif user_choice == 2 and computer_choice == 1:
    print('You Win')
elif user_choice == 2 and computer_choice == 3:
    print('You Lose')
elif user_choice == 3 and computer_choice == 1:
    print('You Lose')
elif user_choice == 3 and computer_choice == 2:
    print('You Win')
else:
    print('None')
    
