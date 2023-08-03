"""
subclass inheritance task
"""


def inherits_from(obj, a_class):
    """
    checks if the type of the given object is a subclass of the specified class
    """
    if issubclass(type(obj), a_class) and type(obj)!= a_class:
        return True
    else:
        return False