# I was reading this article by Tim Urban - Your Life in Weeks and realised just how 
# little time we actually have.
# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, 
# months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time 
# left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly, even the positions of 
# the commas and full stops.

#There are 365 days in a year, 52 weeks in a year and 12 months in a year.

age = input('What is your current age?\n')
years_difference = (90 - int(age))
weeks = 60 * 52
days = years_difference * 365
months = years_difference * 12

print(90 - int(age))
print(weeks)
print(days)

print(f"You have {days} days, {weeks} weeks, and {months} months left")

a = int("5") / int(2.7)

print(type(a))









