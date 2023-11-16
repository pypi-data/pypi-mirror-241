from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    """
    Color codes used in logging
    """
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    BROWN = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    GREY = '\033[0;37m'

    DARK_GREY = '\033[1;30m'
    LIGHT_RED = '\033[1;31m'
    LIGHT_GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    LIGHT_BLUE = '\033[1;34m'
    LIGHT_PURPLE = '\033[1;35m'
    LIGHT_CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'

    RESET = "\033[0m"


class StrColor:
    """
    Add colors to your messages in console logs
    """

    def __init__(self):
        self.colors = Colors()
        self.reset = self.colors.LIGHT_BLUE

    def brand(self, msg):
        return f"{self.colors.LIGHT_PURPLE}{msg}{self.reset}"

    def info(self, msg):
        return f"{self.colors.WHITE}{msg}{self.reset}"

    def passed(self, msg):
        return f"{self.colors.LIGHT_GREEN}{'PASS' : <8}{self.colors.LIGHT_CYAN}{msg}{self.reset}"

    def failed(self, msg):
        return f"{self.colors.LIGHT_RED}{'FAIL' : <8}{self.colors.LIGHT_CYAN}{msg}{self.reset}"

    def error(self, msg):
        return f"{self.colors.YELLOW}{'ERROR' : <8}{self.colors.LIGHT_CYAN}{msg}{self.reset}"

    def exception(self, msg):
        return f"{self.colors.RED}{msg}{self.reset}"


str_color = StrColor()
