"""
same class inheritance task
"""


def is_same_class(obj, a_class):
    """
    Checks if the class the object is the same as the class of the class.

    """
    if obj._class.__name_ == a_class._name_:
        return True
    else:
        return type(obj) == a_class