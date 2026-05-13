import sys
from core import (
    PasswordGenerator,
    LoggerType,
    custom_print,
    DEFAULT_LENGTH,
    DEFAULT_INCLUDE_UPPERCASE,
    DEFAULT_INCLUDE_DIGITS,
    DEFAULT_INCLUDE_SPECIAL_CHARS,
    check_bool_str,
    check_int_str,
    QUICK_COMMAND,
    LENGTH_COMMAND,
    UPPERCASE_COMMAND,
    NUMBERS_COMMAND,
    SYMBOLS_CHAR,
    QUICK_ERROR_MESSAGE
)


def check_quick_command_or_force(force: bool) -> bool:
    """
    skip quick command if this script file is launched from quick_launch.py
    return True when force is True or check first arg to load script from main.py if main.py -q is launched
    """
    if force:
        return True
    else:
        return sys.argv[1].lower() == QUICK_COMMAND


def run(force: bool):
    """
    Quick launch mode entry point. It checks for the quick command or force flag, and if valid, it generates a password based on the provided arguments or defaults.
    Default arguments:
        - length: 12
        - include_uppercase: True
        - include_digits: True
        - include_special_chars: True   
    """

    if check_quick_command_or_force(force):
        # Set default values for quick mode
        length = DEFAULT_LENGTH
        include_uppercase = DEFAULT_INCLUDE_UPPERCASE
        include_digits = DEFAULT_INCLUDE_DIGITS
        include_special_chars = DEFAULT_INCLUDE_SPECIAL_CHARS
        
        # Process additional arguments for customization
        if len(sys.argv) > 1:
            for arg in sys.argv[2:]:
                user_entry = arg.lower()
                
                # Check length to load a custom password length or load default.
                if user_entry.startswith(LENGTH_COMMAND):
                    user_input_value = check_int_str(user_entry[len(LENGTH_COMMAND):])
                    if user_input_value == None:
                        custom_print(f"Invalid length value. Using default length ({length})." , LoggerType.WARNING)
                    else:
                        length = user_input_value

                # check bool values for uppercase, digits and special characters to load custom settings or load defaults. Use check_bool_str instead of try catch to validate the input and return None for invalid inputs.
                elif user_entry.startswith(UPPERCASE_COMMAND):
                    user_input_value = check_bool_str(user_entry[len(UPPERCASE_COMMAND):])
                    if user_input_value == None:
                        custom_print(f"Invalid value for uppercase letters. Using default setting ({include_uppercase}).", LoggerType.WARNING)
                    else:
                        include_uppercase = user_input_value

                # check bool values for digits and special characters to load custom settings or load defaults. Use check_bool_str instead of try catch to validate the input and return None for invalid inputs.
                elif user_entry.startswith(NUMBERS_COMMAND):
                    user_input_value = check_bool_str(user_entry[len(NUMBERS_COMMAND):])
                    if user_input_value == None:
                        custom_print(f"Invalid value for numbers. Using default setting ({include_digits}).", LoggerType.WARNING)
                    else:
                        include_digits = user_input_value

                # check bool values for special characters to load custom settings or load defaults. Use check_bool_str instead of try catch to validate the input and return None for invalid inputs.
                elif user_entry.startswith(SYMBOLS_CHAR):
                    user_input_value = check_bool_str(user_entry[len(SYMBOLS_CHAR):])
                    if user_input_value == None:
                        custom_print(f"Invalid value for special characters. Using default setting ({include_special_chars}).", LoggerType.WARNING)
                    else:
                        include_special_chars = user_input_value

                else:
                    custom_print(f"Unknown argument: {arg}. Ignoring.", LoggerType.WARNING)

        password_generator = PasswordGenerator(
            length=length,
            include_uppercase=include_uppercase,
            include_digits=include_digits,
            include_special_chars=include_special_chars
        )
        custom_print(password_generator.generate(), LoggerType.SUCCESS)

    else:
        custom_print(QUICK_ERROR_MESSAGE, LoggerType.ERROR)

if __name__ == "__main__":
    run(force=True)