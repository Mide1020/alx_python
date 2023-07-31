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
print(is_same_class(a, int))