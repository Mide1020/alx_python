#!/usr/bin/python
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result

if __name__ == "__main__":
    # Example usage:
    a = 10
    b = 2
    safe_print_division(a, b)
