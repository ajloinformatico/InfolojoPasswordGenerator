from .constants import ACCEPTED_TRUE_VALUES, UNACCEPTED_TRUE_VALUES


def check_bool_str(value: str) -> bool:
    """
    Converts a string to a boolean value. It returns True for accepted true values, False for unaccepted true values, and None for invalid inputs.
    Accepted true values are defined in constants.py as ACCEPTED_TRUE_VALUES, and unaccepted true values are defined as UNACCEPTED_TRUE_VALUES.
    """
    if value.lower() in ACCEPTED_TRUE_VALUES:
        return True
    elif value.lower() in UNACCEPTED_TRUE_VALUES:
        return False
    else:
        return None


def check_int_str(value: str) -> int:
    """
    Converts a string to an integer value. It returns the integer if the string is a valid integer, and None for invalid inputs.
    Accepted integer values are defined as strings that can be successfully converted to integers using the int() function.
    """ 
    try:
        return int(value)
    except ValueError:
        return None