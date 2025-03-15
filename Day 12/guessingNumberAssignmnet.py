import random
from art import logo

game_on = True

def diff():
    '''for choosing your difficulty, easy = 10 attempts, hard = 5 attempts'''
    still_going = True
    
    while still_going:
        attempts = 0
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == 'hard':
            attempts += 5
            still_going = False
            return attempts
        elif difficulty == 'easy':
            attempts += 10
            still_going = False
            return attempts
            
# selecting the number
def random_number():
    '''Chooses the random Number'''
    number_to_guess = random.randint(0, 100)
    return number_to_guess

def checking_number(number, random_num):
    '''This will check the number if it is close the the subjected random number'''
    if random_num == number:
        print("Congraulations! You guessed the correct answer")
        return True
    elif number > random_num:
        print("Too High")
        return False
    elif number < random_num:
        print("Too Low")
        return False  

def game():
    '''This will start the guessing game'''
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100: ")
    ran_num = random_number()

    attempts = diff()

    while  attempts > 0:
        my_num = int(input("What is your number: (1 - 100): "))
        if checking_number(my_num, ran_num):
            break
        print(f"Attemps left {attempts-1}")
        attempts -= 1

    if attempts == 0:
        print(f"GG try again mate, right answer {ran_num}")
        
# game start       
while game_on:
    decision = input("Would you like to play? (Y/N): ").upper()
    if decision == 'Y':
        print("\n"*20)
        game()
    elif decision == 'N':
        print("Thank You for playing the game")
        game_on = False
    else: 
        print("Please enter a valid option (Y/N): ")
        
# missing docstring josh huhu

