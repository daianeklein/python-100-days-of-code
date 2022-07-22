#You are going to write a virtual coin toss program. 
# It will randomly tell the user "Heads" or "Tails".

import random

random_number = random.randint(1,10)
print(f'The number is {random_number}')


if random_number % 2 == 0:
    print('Heads!')
else:
    print('Tails!')

