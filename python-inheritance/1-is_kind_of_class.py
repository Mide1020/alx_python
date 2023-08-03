"""
instance class inheritance task
"""


def is_kind_of_class(obj, a_class):
    """
    checks if the object is an instance of a_class or any subclass of a_class
    """
    if type(obj) == a_class or issubclass(type(obj), a_class):
        return True
    else:
        return False
