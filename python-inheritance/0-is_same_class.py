def is_same_class(obj, a_class):
    """
    This function returns True if the object is exactly an instance of the specified class, otherwise False.

    Usage:
    is_same_class(obj, a_class)

    Parameters:
    obj: An object.
    a_class: A class.

    Returns:
    True if obj is exactly an instance of a_class, otherwise False.
    """
    # Check if the type of obj is equal to a_class
    if type(obj) == a_class:
        return True
    else:
      return False