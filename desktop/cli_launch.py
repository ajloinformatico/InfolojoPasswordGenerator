import PasswordGenerator as pg
from Logger import LoggerType, custom_input, custom_print
import constants as c
from utils import check_bool_str, check_int_str


def run():
    finish_cli_mode = False

    print(c.ASCII_ART)

    if not c.DEBUG_MODE:
        return

    custom_print("Welcome to the Infolojo Password Generator CLI!", LoggerType.SUCCESS)
    custom_print("This tool allows you to generate secure passwords with customizable options.", LoggerType.REGULAR)
    custom_print("You can choose to include uppercase letters, numbers, and special characters, as well as specify the desired length of your password.", LoggerType.REGULAR)
    custom_print("Let's get started!", LoggerType.SUCCESS)
    
    
    while not finish_cli_mode:
        length = pg.DEFAULT_LENGTH
        include_uppercase = pg.DEFAULT_INCLUDE_UPPERCASE
        include_digits = pg.DEFAULT_INCLUDE_DIGITS
        include_special_chars = pg.DEFAULT_INCLUDE_SPECIAL_CHARS
        
        # region length password 
        length_input = check_int_str(custom_input("Enter the desired password length (default is 12): "))
        if (length_input == None):
            custom_print(f"Invalid input for length. Using default length ({length}).", LoggerType.WARNING)
        else:
            length = length_input
        # endregion length password



        include_uppercase_input = custom_input("Include uppercase letters? (true/false, default is true): ")
        include_uppercase = check_bool_str(include_uppercase_input) if include_uppercase_input else pg.DEFAULT_INCLUDE_UPPERCASE

        include_digits_input = custom_input("Include numbers? (true/false, default is true): ")
        include_digits = check_bool_str(include_digits_input) if include_digits_input else pg.DEFAULT_INCLUDE_DIGITS

        include_special_chars_input = custom_input("Include special characters? (true/false, default is true): ")
        include_special_chars = check_bool_str(include_special_chars_input) if include_special_chars_input else pg.DEFAULT_INCLUDE_SPECIAL_CHARS

        password_generator = pg.PasswordGenerator(
            length=length,
            include_uppercase=include_uppercase,
            include_digits=include_digits,
            include_special_chars=include_special_chars
        )
        custom_print(password_generator.generate(), LoggerType.SUCCESS)

        continue_input = custom_input("Do you want to generate another password? (yes/no): ")
        if continue_input.lower() not in ['yes', 'y']:
            finish_cli_mode = True
            custom_print("Thank you for using the Infolojo Password Generator CLI! Goodbye!", LoggerType.SUCCESS)

if __name__ == "__main__":
    run()
    