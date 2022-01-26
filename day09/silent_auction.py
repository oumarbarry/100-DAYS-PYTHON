from subprocess import call
from typing import Dict
from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

bids: Dict[str, int] = {}

while True:
    name = input("What's your name ? ")
    bid = int(input("What's your bid ? $"))
    bids[name] = bid

    keep = input("Are there any other bidders? Type 'yes' or 'no': ")
    if keep == 'yes': 
        call('clear' if os.name =='posix' else 'cls')
    else:
        winner_bid = max([ v for v in bids.values()])
        for name, bid in bids.items():
            if bid == winner_bid: print(f"The winner is {name} with a bid of {bid}")
        break