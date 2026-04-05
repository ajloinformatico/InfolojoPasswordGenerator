ASCII_ART = r"""
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

                       >>>   INFOLOJO   <<<
"""

QUICK_ERROR_MESSAGE = r"""
Invalid command. Use -q for quick password generation or launch without arguments for CLI App.

For example:
python main.py -q will generate a password with default settings (12 characters, including uppercase letters, numbers, and special characters).


Use special flags for customization:
-l : Specify the length of the password (e.g., -l16 for a 16-character password)
-u : Include uppercase letters
-n : Include numbers
-s : Include special characters

For example:
python main.py -q -l=16 -u=true -n=true -s=false ) will generate a 16-character password with uppercase letters and numbers, but without special characters.
python main.py -q -l=20 -u=true -n=false -s=true ) will generate a 20-character password with uppercase letters and special characters, but without numbers.

"""


ACCEPTED_TRUE_VALUES = ['true', '1', 'yes']
UNACCEPTED_TRUE_VALUES = ['false', '0', 'no']
QUICK_COMMAND = "-q"
LENGTH_COMMAND = "-l="
UPPERCASE_COMMAND = "-u="
NUMBERS_COMMAND = "-n="
SYMBOLS_CHAR = "-s="