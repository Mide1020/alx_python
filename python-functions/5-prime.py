def is_prime(number):
    if number <=1:
        return False
    number = int(input(enter a number))
    for i in range(2,number):
        if number % i == 0:
            return False
