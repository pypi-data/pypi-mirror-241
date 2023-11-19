from colorama import Fore

def colorize(text: str, color: Fore = Fore.GREEN) -> str:
    """
    Colorizes the text with the specified color.

    :param text: Text to be colorized.
    :param color: Color to use (from the colorama module, e.g., Fore.GREEN).
    :return: Colorized text.
    """
    reset_color = "\033[0m"
    return f"{color}{text}{reset_color}"

def colorize_error(text: str) -> str:
    """
    Colorizes error text in red.

    :param text: Error text.
    :return: Colorized error text.
    """
    return colorize(text, Fore.RED)

def colorize_warning(text: str) -> str:
    """
    Colorizes warning text in yellow.

    :param text: Warning text.
    :return: Colorized warning text.
    """
    return colorize(text, Fore.YELLOW)

def colorize_info(text: str) -> str:
    """
    Colorizes informational text in blue.

    :param text: Informational text.
    :return: Colorized informational text.
    """
    return colorize(text, Fore.BLUE)