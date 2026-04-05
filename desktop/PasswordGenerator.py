import random
import string

DEFAULT_LENGTH = 12
DEFAULT_INCLUDE_UPPERCASE = True
DEFAULT_INCLUDE_DIGITS = True
DEFAULT_INCLUDE_SPECIAL_CHARS = True

class PasswordGenerator:
    def __init__(self, length=12, include_uppercase=True, include_digits=True, include_special_chars=True):
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_digits = include_digits
        self.include_special_chars = include_special_chars



    def generate(self):
        characters = string.ascii_lowercase
        if self.include_uppercase:
            characters += string.ascii_uppercase
        if self.include_digits:
            characters += string.digits
        if self.include_special_chars:
            characters += string.punctuation

        password = ""
        
        for _ in range(self.length):
            password += random.choice(characters)
        
        return f"Generated password: {password}"
