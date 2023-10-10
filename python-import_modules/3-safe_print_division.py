#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        operation = "{} / {} = {:.1f}".format(a, b, result)
    except ZeroDivisionError:
        result = None
        operation = "{} / {} = None".format(a, b)
    finally:
        print("Inside result: {:.1f}".format(result))
        if result is not None:
            print(operation)

# Example usage:
a = 10
b = 2
safe_print_division(a, b)
