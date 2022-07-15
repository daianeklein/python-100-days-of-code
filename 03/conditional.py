print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride")


# modulo
print(7 % 3) # 1
print(7 % 5) # 2
print(12 % 10) # 2
print(12 % 3) # 0
print(12 % 5) # 2
print(12 % 6) # 0
print(12 % 7) # 5
print(12 % 8) # 4
print(16 % 3) # 1


# Code exercise
# Instructions
# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# e.g. 86 is even because 86 ÷ 2 = 43
# 43 does not have any decimal places. Therefore the division is clean.
# e.g. 59 is odd because 59 ÷ 2 = 29.5
# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

number = int(input('Which number do you want to check?:\n'))

if (number % 2) == 0:
    print("This is a even number!")
else:
    print("This is an odd number!")

# identacao / nested
print("Welcome to the rollercoaster")
age = int(input("What is your height in cm? "))

if age >= 120:
    print("You can ride a rollercoaster!")
    age = int(input('What is your age?: '))
    if age < 12:
        print("Please, pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride")

    