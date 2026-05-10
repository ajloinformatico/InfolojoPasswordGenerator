import PasswordGenerator as pg
from Logger import LoggerType, custom_input, custom_print
import constants as c
from utils import check_bool_str, check_int_str


def run():
    """
    Entry point for the CLI mode of the password generator.

    This function displays a welcome message, prompts the user for password
    configuration options (length, uppercase letters, numbers, special characters),
    and generates a secure password based on the provided settings.

    Default values are used if the user provides no input or invalid input:
        - Length: 12 characters
        - Include uppercase: true
        - Include numbers: true
        - Include special characters: true

    If no character types are selected, defaults are applied to ensure at least
    one character type is included.

    After generating a password, the user is prompted to generate another one.
    The loop continues until the user chooses to exit.

    Returns:
        None: Outputs the generated password directly to the console.
    """
    print(c.ASCII_ART)
    custom_print("Welcome to the Infolojo Password Generator CLI!", LoggerType.SUCCESS)
    custom_print("This tool allows you to generate secure passwords with customizable options.", LoggerType.REGULAR)
    custom_print("You can choose to include uppercase letters, numbers, and special characters, as well as specify the desired length of your password.", LoggerType.REGULAR)
    custom_print("Let's get started!", LoggerType.SUCCESS)
    print()

    while True:
        length = pg.DEFAULT_LENGTH
        include_uppercase = pg.DEFAULT_INCLUDE_UPPERCASE
        include_digits = pg.DEFAULT_INCLUDE_DIGITS
        include_special_chars = pg.DEFAULT_INCLUDE_SPECIAL_CHARS

        custom_print("--- Password Configuration ---", LoggerType.REGULAR)
        custom_print("Enter the desired password length (press Enter for 12): ", LoggerType.REGULAR)
        length_input = custom_input()
        if length_input:
            length_value = check_int_str(length_input)
            if length_value is not None:
                length = length_value
            else:
                custom_print(f"Invalid input. Using default length ({pg.DEFAULT_LENGTH}).", LoggerType.WARNING)

        custom_print("Include uppercase letters? (true/false, press Enter for true): ", LoggerType.REGULAR)
        uppercase_input = custom_input()
        if uppercase_input:
            value = check_bool_str(uppercase_input)
            if value is not None:
                include_uppercase = value
            else:
                custom_print(f"Invalid input. Using default (true).", LoggerType.WARNING)

        custom_print("Include numbers? (true/false, press Enter for true): ", LoggerType.REGULAR)
        digits_input = custom_input()
        if digits_input:
            value = check_bool_str(digits_input)
            if value is not None:
                include_digits = value
            else:
                custom_print(f"Invalid input. Using default (true).", LoggerType.WARNING)

        custom_print("Include special characters? (true/false, press Enter for true): ", LoggerType.REGULAR)
        special_input = custom_input()
        if special_input:
            value = check_bool_str(special_input)
            if value is not None:
                include_special_chars = value
            else:
                custom_print(f"Invalid input. Using default (true).", LoggerType.WARNING)

        if not include_uppercase and not include_digits and not include_special_chars:
            custom_print("You must include at least one character type. Using defaults.", LoggerType.WARNING)
            include_uppercase = True
            include_digits = True
            include_special_chars = True

        print()
        password_generator = pg.PasswordGenerator(
            length=length,
            include_uppercase=include_uppercase,
            include_digits=include_digits,
            include_special_chars=include_special_chars
        )
        custom_print(password_generator.generate(), LoggerType.SUCCESS)

        print()
        custom_print("Do you want to generate another password? (yes/no): ", LoggerType.REGULAR)
        continue_input = custom_input()
        if not check_bool_str(continue_input.lower()):
            print("THANK YOU FOR USING THE INFOLOJO PASSWORD CLI! Goodbye!")
            break


if __name__ == "__main__":
    run()