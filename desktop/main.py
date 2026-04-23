import constants as c
import sys
import PasswordGenerator as pg
import quick_launch
import cli_launch
from Logger import LoggerType, custom_input, custom_print
from utils import check_bool_str, check_int_str

def run():
    """
    App entry point. If there are command line arguments, it will run the quick launch mode, otherwise it will run the CLI mode.
    """
    if len(sys.argv) > 1:    
        quick_launch.run(force=False)
    else:
        cli_launch.run()

if __name__ == "__main__":
    run()
