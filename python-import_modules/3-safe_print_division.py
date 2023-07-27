def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))

result = 3-safe_print_division(10, 2)
