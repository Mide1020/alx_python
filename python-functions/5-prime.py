def is_prime(number):

    if number <=1:
        return True
    
    for i in range(number):
        if number % i == 0:
            return False
