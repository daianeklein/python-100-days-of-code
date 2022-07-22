# Instructions
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
# https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

# Warning you should round the result to the nearest whole number. The interpretation message needs 
# to include the words in bold from the interpretations above. e.g. underweight, normal weight, 
# overweight, obese, clinically obese.


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = float((weight / (height ** 2)))
bmi = round(bmi, 2)

if bmi < 18.6:
    print(f'Your BMI is {bmi}, you are underweight!')
elif bmi >= 18.5 and bmi < 26:
    print(f'Your BMI is {bmi}, you have normal weight!')
elif bmi >= 25 and bmi < 31:
    print(f'Your BMI is {bmi}, you are slightly overweight!')
elif bmi >= 30 and bmi < 36:
    print(f'Your BMI is {bmi}, you are obese')
else:
    print(f'Your BMI is {bmi}, you are clinically obese')