"""
same class inheritance task
"""


def is_same_class(obj, a_class):
    """
    Checks if the class the object is the same as the class of the class.

    """
    if obj.__class__.__name__ == a_class.__name__:
        return True
    else:
        return type(obj) == a_class
    