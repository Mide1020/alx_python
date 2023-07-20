#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

Last_digit = abs(number) %10
string = ""

if number < 0:
    Last_digit = -Last_digit

    if Last_digit > 5:
        string = "greater than 5"
    elif Last_digit == 0:
        string = "0"
    else:
        string = "less than 6 and not 0"

        print("last digit of {} is {} and is {}".format(number, Last_digit, string))
