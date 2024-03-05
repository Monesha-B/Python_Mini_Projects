
from replit import clear

from ASCII_ART_Bid_game import logo

print(logo)


def find_highest_bidder(bidders_and_amount):
    highest_amount = 0
    winner = ""
    for bidder in bidders_and_amount:
        bid_amount = int(bidders_and_amount[bidder])
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_amount}")

bids = {}
bidding_finished = True
while bidding_finished:
    name = input("Enter the name of the bidder: ")
    amount = input("Enter the bidding the ammount: $")
    bids[name] = amount
    continue_bidding = input("Is anyone still there to bid? type 'yes'/'no': ")
    if continue_bidding == "no":
        bidding_finished = False
        find_highest_bidder(bidders_and_amount= bids)
    elif continue_bidding == "yes":
        clear()
    

# from replit import clear

# from ASCII_ART_Bid_game import logo

# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()
  



