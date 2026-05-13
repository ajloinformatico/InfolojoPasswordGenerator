import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import QUICK_COMMAND, GUI_COMMAND
import cli
import quick
import desktop_ui


def run():
    """
    App entry point. If there are command line arguments, it will run the quick launch mode.
    If -gui flag is provided, it will run the GUI mode.
    Otherwise, it will run the CLI mode.
    """
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == GUI_COMMAND:
            desktop_ui.run()
        else:
            quick.run(force=False)
    else:
        cli.run()


if __name__ == "__main__":
    run()