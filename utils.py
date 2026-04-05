import constants as c

def check_bool_str(value: str) -> bool:
    if value.lower() in c.ACCEPTED_TRUE_VALUES:
        return True
    elif value.lower() in c.UNACCEPTED_TRUE_VALUES:
        return False
    else:
        return None
