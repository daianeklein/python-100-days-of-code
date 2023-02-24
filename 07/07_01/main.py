from hangman_stages import logo
from hangman_stages import stages
from hangman_words import word_list
import random

word_chosen = random.choice(word_list)
word_length = len(word_chosen)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess_word_by_user = input('Guess a letter: ').lower()

    if guess_word_by_user in display:
        print('You have guessed the letter: {guess_word_by_user}')

#check guessed letter
    for position in range(word_length):
        letter = word_chosen[position]
        if letter == guess_word_by_user:
            display[position] = letter

# check if user is wrong
    if guess_word_by_user not in word_chosen:
        print(f"You guessed {guess_word_by_user}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You Lose')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # check if the user has got all letters
    if "_" not in display:
        end_of_game = True
        print('You win!')


    print(stages[lives])

