from subprocess import call
import os
import random
import data

chosen_word = random.choice(data.words)
display = ["_"]*len(chosen_word)
score = 6

print(data.logo) 

while True:
    guess = input("\nGuess a letter: ").lower()
    
    call('clear' if os.name =='posix' else 'cls')
    
    if guess in display:
        print(f"You've already guessed {guess}.")

    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
    
    if guess not in chosen_word:
        score -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
                
    print("".join(display))
    print( data.stages[score] )
    
    if "_" not in display:
        print("You win 👑"); break
    elif score == 0:
        print("You lose"); break
