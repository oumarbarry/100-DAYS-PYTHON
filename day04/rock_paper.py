import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand = [rock, paper, scissors]

print("Type 0 for Rock, 1 for paper or 2 for Paper.")
user = int(input("What do you choose ? "))
if user in [0,1,2]:
    print(hand[user])
else:
    print("**Bad choice**")

computer = random.randint(0, len(hand)-1)
print(f"\n\nComputer choose:\n{hand[computer]}")

if (user==0 and computer==2) \
    or (user==2 and computer==1) \
        or (user==1 and computer==0):
            print("YOU WIIIN 👑")
elif user==computer:
    print("EQUALITY")
else:
    print("You lose")
