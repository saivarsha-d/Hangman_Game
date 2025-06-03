import random
from inputs import hangman,word_list,logo

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for letter in chosen_word:
    placeholder += "_"

correct_letters = []
lives = 6

while True:
    print(f"\nWord to guess: {placeholder}")
    user_guess = input("Guess a letter: ").lower()

    if user_guess in correct_letters or user_guess in placeholder:
        print(f"You've already guessed {user_guess}")

    else:
        if user_guess not in chosen_word:
            lives -= 1
            print(f"You guessed {user_guess}, that's not in the word. You lost a life.")
        elif user_guess not in correct_letters:
            correct_letters.append(user_guess)

    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display+= letter
        else:
            display += "_"
    placeholder = display

    print(hangman[lives])
    print(f"************************** {lives}/6 LIVES LEFT **************************")


    if display == chosen_word:
        print("************************** You Won! **************************")
        break


    if lives == 0:
        print(f"************************** It was {chosen_word}, You Lost! **************************")
        break