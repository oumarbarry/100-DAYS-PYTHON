from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text: str, shift: int, direction: str):
    positions = []
    if direction == 'encode':
        positions = [ alphabet.index(t)+shift if t.isalpha() else t for t in text ]
        for i, p in enumerate(positions): 
            if type(p)==int and p>25 : positions[i]-=26
    elif direction == 'decode':
        positions = [ alphabet.index(t)-shift if t.isalpha() else t for t in text ]
        for i, p in enumerate(positions):
            if type(p)==int and p<0: positions[i]+=26

    result = "".join([ alphabet[p] if type(p)==int else p for p in positions ])
    print(f"The {direction}d text is {result}")

print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caesar(text, shift, direction)
    
    if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n") == 'no':
        print("Goodbye!"); break