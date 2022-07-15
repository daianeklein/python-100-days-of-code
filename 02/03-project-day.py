# Tip Calculator
# Instructions
# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print('Welcome to the tip calculator!')

total_bill = input('What was the total bill?\n')
percentage = input('What percentage tip would you like to give?\n')
people = input('How many people to split the bill? ')

total_per_person = (float(total_bill) + (int(percentage) / 100)) / int(people)
total_per_person = round(total_per_person, 2)

print(f'Each person should pay $: {total_per_person}')


