import os #importing this to use the clear screen function

from ascii import logo
print(logo)

bids = {}
bidders = False
   
def highest_bidder(bids_record):
    highest = 0
    winner = ''
    for bidder in bids_record:
        bid_amount = bids_record[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest}")
        
print("Welcome to silent auction.")

while not bidders:
    user_name = input("Enter the name of the bidder: ")
    user_bid = int(input("Enter the price you want to bid: "))
    bids[user_name] = user_bid
    should_continue = input("Type 'yes' if there are any more bidders else 'no': ")
    if should_continue == 'no':
        bidders = True
        highest_bidder(bids)
    elif should_continue == 'yes':
        os.system('cls')