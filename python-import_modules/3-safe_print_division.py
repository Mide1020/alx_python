def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    finally:
        result = safe_print_division(10, 2)
        print("Inside result: {}".format(result))


