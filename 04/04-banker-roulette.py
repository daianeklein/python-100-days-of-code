# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a 
# List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

import random

names_string = input("Give me evebody's names, separated by a comma: ")
names_string = names_string.split(',')

random_number = random.randint(0, (len(names_string) - 1))
random_name = names_string[random_number]

print(f'{random_name} is going o buy the meal today!')


