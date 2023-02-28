def check_prime_number(number):
    if (number % number == 0) & (number % 1 == 0):
        print('It is a prime number')
    else:
        print('It is not a prime number')

check_prime_number(73)
