from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text: str, shift: int, direction: str):
    positions = []
    if direction == 'code':
        positions = [ alphabet.index(t)+shift if t.isalpha() else t for t in text ]
        for i, p in enumerate(positions): 
            if type(p)==int and p>25 : positions[i]-=26
    elif direction == 'decode':
        positions = [ alphabet.index(t)-shift if t.isalpha() else t for t in text ]
        for i, p in enumerate(positions):
            if type(p)==int and p<0: positions[i]+=26

    result = "".join([ alphabet[p] if type(p)==int else p for p in positions ])
    print(f"Le texte est: {result}")

print(logo)

while True:
    direction = input("Entre 'code' pour crypter ou 'decode' pour decrypter un message: ")
    text = input("\nEntre un message: ").lower()
    shift = int(input("\nEntre la cle de chiffrement: ")) % 26

    caesar(text, shift, direction)
    
    if input("Tape 'oui' pour continuer, ou 'non' pour quitter.\n").lower() == 'non':
        print("Goodbye! :)"); break