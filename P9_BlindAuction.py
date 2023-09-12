logo = """               ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\ 
"""
print(logo)
print("Welcome to Secret Auction Program.\n")

import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


bid_log = {}
bidding_finished = False


def highest_bidder(bidding_record):
    highest_bid = 0
    # bidding_record = {"Naman": 123, "Aman": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        print(f"Winner is {winner} with a bid of {highest_bid}")


while not bidding_finished:
    name = input("What is your name?:")
    bid = int(input("What's your bid? "))
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    bid_log[name] = bid
    if bidders == "no":
        bidding_finished = True
        highest_bidder(bid_log)
    elif bidders == "yes":
        clear_console()
