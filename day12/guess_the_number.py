from art import LOGO

import random

print(LOGO)
print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number between 1 and 100.")

gold = random.randint(1, 100)
# print(f"number to guess: {gold}")

if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy': 
    level = 10
else: 
    level = 5

print(f"You have { level } attempts remaining to guess the number.")

while level!=0:
    user = int(input("Make a guess: "))
    if user == gold:
        print(f"You got it! The answer was {gold} 👑🤩"); break
    elif user > gold:
        print("Too high 🥶.\nGuess again.")
    elif user < gold:
        print("Too low 🔥.\nGuess again.")
    
    level-=1

if level == 0: print(f"You've run out of guesses, you lose.")
