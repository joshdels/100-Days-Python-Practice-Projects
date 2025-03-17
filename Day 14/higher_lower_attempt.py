# This is my attemp of making the game of higher and lower, got to say so much stress ay pero nahuman man pud wahahah

import random
from game_data import data
from art import logo

choosen_data = []
current = []
previous = []
SCORE = 0
game_is_on = True

# data name exatractor maybe a function and remove data that is not related
def actor():
    '''This will choose random names that is not yet in the choosen dat'''
    while True:
        current_data = random.choice(data)
        if current_data not in choosen_data:
            choosen_data.append(current_data)
            return current_data

# compute 2 followers
# print(f"old_intial_previous {previous}")
# print(f"old_initial_current {current}")

#show

def assign(current, previous):
    '''This will assign the position of the data'''
    name_a = current[0]['name']
    follower_a = current[0]['follower_count']

    name_b = previous[0]['name']
    follower_b = previous[0]['follower_count']
    
    return name_a, follower_a, name_b, follower_b

def checking_names(name_a, follower_a, name_b, follower_b):
    '''This will evaluate the number of followers of 'Name A' or 'Name B' '''
    global SCORE

    # visualize comparison
    choice = input(f"\nIs {name_a} has higher than {name_b} or lower follower/s (higher/lower)? ").lower()
    # follower higher or lower
    
    # decide sila higher or lower
    if choice == 'higher':     
        if follower_a> follower_b:  
            follower_a = follower_a
            SCORE += 1
            return True
        else:
            print("You lose")
            print(f"{name_b} has {follower_b} followers and {name_a} has {follower_a} followers")
            return False
        
    elif choice == 'lower': 
        #bug naman
        if follower_b > follower_a:
            SCORE += 1
            follower_a = follower_b
            follower_b = follower_a  
            return True
        else:
            print("You lose")
            print(f"{name_b} has {follower_b} followers and {name_a} has {follower_a} followers")
            return False

def compute(name_a, follower_a, name_b, follower_b):
    '''This will compute followers and return the biggest followers'''
    global current
    global previous 
    
    #computation
    if follower_a > follower_b:
        print(f"{name_a} is the winner which has {follower_a} followers than {name_b} which has {follower_b} followers")
        previous = []
        previous.append(current[0]) # nara ang idol.
        current = []

    else:
        print(f"{name_b} is the winner which has {follower_b} followers than {name_a} which has {follower_a} followers")
        previous = []
        previous.append(current[0]) 
        current = [] 

    return previous, current

# to be continue nani hehe
def new_actor():
    '''This will select new actor'''
    current.append(actor())
    return current 


# game
def game():
    print(logo)

    current.append(actor())
    previous.append(actor())

    name_a, follower_a, name_b, follower_b = assign(current, previous)

    while checking_names(name_a, follower_a, name_b, follower_b):
        compute(name_a, follower_a, name_b, follower_b)
        print(f"Your current score: {SCORE}")
        new_actor()
        

game()

while game_is_on:
    choice = input("Would you play again? (Y/N): ")
    if choice == 'y':
        game()
    else:
        print("Thank you for playing")
        game_is_on = False
    
   
   


# name_a, follower_a, name_b, follower_b = assign(current, previous)
# compute(name_a, follower_a, name_b, follower_b)

#found a bug dyemmm! its like a demon bug


# next a goal is to add interaction to the choosing

