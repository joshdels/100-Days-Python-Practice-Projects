import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_additions = True
player_cards = []
computer_cards = []

def draw():
    draw_cards = random.choice(cards)
    return draw_cards

def player_check(total_player_cards):
    # add debugging phase
    # print("running player_check") # add debugging phase
    # why it wont run! to print, found the mistake, global and local variables
    # first mistake nako is and sum() kay naa sa global not knowing gina update diay siya every run
    # print(total_player_cards)
    # global card_conditions
    if total_player_cards == 21:
        print("Black Jack, You win!")
        return False
    elif total_player_cards > 21:
        print("Bust! You lose")
        return False
    return True

def computer_check(total_computer_cards, total_player_cards):
    # add debugging phase
    # print("running computer_check") # add debugging phase
    while total_computer_cards < 17:
        computer_cards.append(draw())
        total_computer_cards= sum(computer_cards)
    #check conditions mate
    if total_computer_cards == 21:  
        print("Dealer has blackjack! Dealers Win!")  
    elif total_player_cards == total_computer_cards:
        print("Draw")
    elif total_computer_cards > 21:
        print("You win!")
    elif total_computer_cards > total_player_cards:
        print("Dealer wins")
    elif total_computer_cards < total_player_cards:
        print("You win!")
        #it could be improved by replacing print into return :)
        
    print(f"dealer has {computer_cards} total of {total_computer_cards}")
    print(f"player has {player_cards} total of {total_player_cards}")
    
# intial setup  
def blackjack():
    global card_additions
    
    

    choice = input("Do you want to play Blackjack? (Y/N) ").lower()
    
    if choice == 'y':
        # im thinking this can be optimized
        print(logo)
        player_cards.append(draw())
        player_cards.append(draw())
        computer_cards.append(draw())
        computer_cards.append(draw())
        print(f"You got, {player_cards} a total of {sum(player_cards)}") 
        print(f"Dealer have, {computer_cards[0]}")
        
        # add cards? 
        while card_additions:
            total_player_cards= sum(player_cards)
            card_additions = player_check(total_player_cards)
            
            if not card_additions:
                break
            add_cards = input("Would you add cards or proceed to check? (Y/N) ").lower()
            # new learning here, i need to global the condition variable then
            # use the if not then break, super cool

            if add_cards == 'y':
                player_cards.append(draw())
                print(f"{player_cards} a total of {sum(player_cards)}")
            elif add_cards == 'n':
                total_computer_cards = sum(computer_cards)
                total_player_cards= sum(player_cards)
                computer_check(total_computer_cards, total_player_cards)
                card_additions = False
                blackjack()
                
    elif choice == 'n':
        print("Thanks for playing Blackjack") 

blackjack() 
    
    
#TODO 1 want to play?
#TODO 2 show cards
#TODO 3 get another player card?
#TODO 4 show computer card
#TODO 4.1 if efficient draw computer card
#TODO 5 if no show all the cards 

'''
Rules
    Over 21
    jack queen king = 10
    ace special 1 or 11
    first draw only one card can be seen
    dealer smaller < 17 must take another card
'''

'''
Reflection:
    missing 11 and 1 ideas, by adding and removing sa initial stage hahah, 
    i did not comprehen well in the instruction hehehe
    then my ending phase is quite ugly :(
'''