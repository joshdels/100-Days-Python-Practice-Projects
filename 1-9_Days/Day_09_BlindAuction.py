
adding_bidders = True
bidder_profile = {}

def bidder(auctioner, amount):
    '''This will add biders to the main profile'''
    individual = {auctioner: amount}
    bidder_profile.update(individual)

def check_winner(profiles):
    '''This will check who is the winner'''
    highest_bids = max(profiles.values()) #I make some short cuts dyemmm
    for bidder in profiles:
        if profiles[bidder] == highest_bids:
            print(f"Winner is: {bidder} with a winning of ${highest_bids}")

# auction conditions
while adding_bidders: 
    choice = input("Is there any bidders? (Y/N): ").lower()
    if choice == 'y':
        print("\n"*50)
        name = input("What is your name? ")
        bid = int(input("How much would you like to bid: $"))
        bidder(name, bid)
    elif choice =='n':
        print("No more bidders")
        check_winner(bidder_profile)
        adding_bidders = False

# for testing and checking
print("Final Bidders:", bidder_profile)        

'''
Notes:
    Work on the main simple principle
    before using shortcuts, more on fundamental
'''
        
    
        



    
    