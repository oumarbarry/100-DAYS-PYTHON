from art import logo
from subprocess import call

import os
import random

def score(cards: list[int]) -> int:
    if sum(cards) == 21 and len(cards) == 2: return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1) 
    return sum(cards)

def compare(user_score: int, computer_score: int) -> None:
    if user_score == computer_score \
        or (user_score > 21 and computer_score > 21):
        print("Drawww 😒")
    elif user_score == 0:
        print("You win with a blackjack 👑🤩")
    elif computer_score == 0:
        print("You lose, opponent has a blackjack 😑")
    elif user_score > 21:
        print("You went over. You lose 😕")
    elif computer_score > 21:
        print("Opponent went over. You win 😎")
    elif user_score > computer_score:
        print("You win 😁")
    elif user_score < computer_score:
        print("You lose 😤")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    if input("Do you want to play a game of blackjack ? Type 'y' or 'n': ") == 'y':
        my_cards = [ random.choice(cards) for _ in range(2) ]
        computer_cards = [ random.choice(cards) for _ in range(2) ]
    else: break
    
    call('clear' if os.name == 'posix' else 'cls')
    print(logo)
    
    while True:
        print(f"\tYour cards: {my_cards}, current score: {score(my_cards)}")
        print(f"\tComputer's first card: {computer_cards[0]}")
        
        if 1 <= score(my_cards) <= 21 or score(computer_cards) != 0:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                my_cards.append( random.choice(cards) )
            else: break
        else: break
    
    while score(computer_cards) < 17 and score(computer_cards) != 0: 
        computer_cards.append( random.choice(cards) )
    
    print(f"Your final hand: {my_cards}, final score: {score(my_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {score(computer_cards)}")

    compare(score(my_cards), score(computer_cards))