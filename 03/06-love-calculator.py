# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers 
# to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names_combined = name1.lower() + name2.lower()

count_list_true = []
count_list_love = []

for i in 'true':
    count_list_true.append(names_combined.count(i))

for j in 'love':
    count_list_love.append(names_combined.count(j))

true_count_words = sum(count_list_true)
love_count_words = sum(count_list_love)

print(true_count_words, love_count_words)


# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."


score = str(true_count_words) + str(love_count_words)
score = int(score)

if score < 11 and score > 90:
    print(f'Your Score is {score}, you go together like coke and mentos')
elif score > 39 and score < 51:
    print(f'Your score is {score}, you are alright together')
else:
    print(f'Your score is {score}')