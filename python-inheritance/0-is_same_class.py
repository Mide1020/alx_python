def is_same_class(obj, a_class):
    """
    This  function returns True if the object is exactly
 an instance of the specified class, 
 otherwise False 
    Usage:
is_same_class(obj, a_class)

    Parameters:
    obj: An object,
    a_class:Aclass.

    Returns:
    True if objj is exactly an instance of a_class, otherwise
    False
    """
    return type(obj) == a_class