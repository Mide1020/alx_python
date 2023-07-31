def is_same_class(obj, a_class):
    """
    This function checks if an object is exactly an instance of a specified class.

    Args:
    obj: Any object.
    a_class: Any class.

    Returns:
    True if the object is exactly an instance of the specified class, otherwise False.
    """
    return type(obj) is a_class