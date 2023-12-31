#!/usr/bin/python
import random

# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10  # Calculate the absolute value first

# Determine if the last digit should be negative based on the original number
if number < 0:
    last_digit = -last_digit

# Print the result based on the last digit
print("Last digit of", number, "is", last_digit, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
