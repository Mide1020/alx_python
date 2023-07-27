#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
        return result
result = safe_print_division(10, 0)
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 10
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))