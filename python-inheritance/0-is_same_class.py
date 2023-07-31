def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The specified class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class; otherwise False.
    """
    return type(obj) == a_class


# Test cases
a = 1
print(is_same_class(a, int))  # Output: True

a = True
print(is_same_class(a, int))  # Output: False

a = 3.14
print(is_same_class(a, int))  # Output: False

a = True
print(is_same_class(a, object))  # Output: True

a = None
print(is_same_class(a, object))  # Output: True

a = None
print(is_same_class(a, list))  # Output: False

a = [1, 2, 3]
print(is_same_class(a, list))  # Output: True

a = [1, 2, 3]
print(is_same_class(a, object))  # Output: True