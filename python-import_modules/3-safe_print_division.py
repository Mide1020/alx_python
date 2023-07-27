def safe_print_division(a, b):
    try:
        result = a / b
        return result
        return None
    finally:
        print("Inside result: {}".format(result))
result = safe_print_division(10, 2)


