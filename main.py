import constants as c
import sys
import PasswordGenerator as pg
from Logger import LoggerType, custom_print
from utils import check_bool_str

def run():
    if len(sys.argv) > 1:    
        launch_quick_mode()
    else:
        launch_cli_mode()
        

def launch_quick_mode():
    if sys.argv[1].lower() == c.QUICK_COMMAND:
        # Set default values for quick mode
        length = pg.DEFAULT_LENGTH
        include_uppercase = pg.DEFAULT_INCLUDE_UPPERCASE
        include_digits = pg.DEFAULT_INCLUDE_DIGITS
        include_special_chars = pg.DEFAULT_INCLUDE_SPECIAL_CHARS
        
        # Process additional arguments for customization
        if len(sys.argv) > 1:
            for arg in sys.argv[2:]:
                user_entry = arg.lower()
                if user_entry.startswith(c.LENGTH_COMMAND):
                    try:
                        length = int(user_entry[len(c.LENGTH_COMMAND):])
                    except ValueError:
                        custom_print(f"Invalid length value. Using default length ({length})." , LoggerType.WARNING)

                elif user_entry.startswith(c.UPPERCASE_COMMAND):
                    user_input_value = check_bool_str(user_entry[len(c.UPPERCASE_COMMAND):])
                    if user_input_value == None:
                        custom_print(f"Invalid value for uppercase letters. Using default setting ({include_uppercase}).", LoggerType.WARNING)
                    else:
                        include_uppercase = user_input_value

                # ADD check_bool_str instead of try catch
                elif user_entry.startswith(c.NUMBERS_COMMAND):
                    user_input_value = check_bool_str(user_entry[len(c.NUMBERS_COMMAND):])
                    if user_input_value == None:
                        custom_print(f"Invalid value for numbers. Using default setting ({include_digits}).", LoggerType.WARNING)
                    else:
                        include_digits = user_input_value

                elif user_entry.startswith(c.SYMBOLS_CHAR):
                    user_input_value = check_bool_str(user_entry[len(c.SYMBOLS_CHAR):])
                    if user_input_value == None:
                        custom_print(f"Invalid value for special characters. Using default setting ({include_special_chars}).", LoggerType.WARNING)
                    else:
                        include_special_chars = user_input_value

                else:
                    custom_print(f"Unknown argument: {arg}. Ignoring.", LoggerType.WARNING)

        password_generator = pg.PasswordGenerator(
            length=length,
            include_uppercase=include_uppercase,
            include_digits=include_digits,
            include_special_chars=include_special_chars
        )
        custom_print(password_generator.generate(), LoggerType.SUCCESS)

    else:
        custom_print(c.QUICK_ERROR_MESSAGE, LoggerType.ERROR)


def launch_cli_mode():
    print(c.ASCII_ART)

if __name__ == "__main__":
    run()


