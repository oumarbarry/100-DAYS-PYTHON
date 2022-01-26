
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password?\n")) 
num_numbers = int(input(f"How many numbers would you like?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))

#1rst solution
password = ""
for _ in range(0, num_letters):
    password += random.choice(letters)

for i in range(0, num_numbers):
    password += random.choice(numbers)

for _ in range(0, num_symbols):
    password += random.choice(symbols)

password = "".join( random.sample(password, len(password)) )

#2nd solution
""" 
password = []
for _ in range(0, num_letters):
    password.append( random.choice(letters) )
for i in range(0, num_numbers):
    password.append( random.choice(numbers) )
for _ in range(0, num_symbols):
    password.append( random.choice(symbols) )

random.shuffle(password)
password = "".join( password )
"""

print(f"Here is your password: {password}")