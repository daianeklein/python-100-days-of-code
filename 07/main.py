import random

word_list = ['school', 'balloon', 'student', 'elephant']
word_chosen = random.choice(word_list)
print(word_chosen)

word_display = []
len_word_chosen = len(word_chosen)
for _ in range(len_word_chosen):
    word_display += '_'

print(word_display)

while '_' in word_display:
    letter_guessed = input('choose a letter: ').lower()

    for position in range(len(word_chosen)):
        letter = word_chosen[position]
        if letter == letter_guessed:
            word_display[position] = letter_guessed
            print(word_display)

print(word_chosen)


