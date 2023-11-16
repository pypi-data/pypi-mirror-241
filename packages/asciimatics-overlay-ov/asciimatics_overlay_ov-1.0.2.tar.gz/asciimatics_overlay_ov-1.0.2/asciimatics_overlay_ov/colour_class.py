"""
File in charge of managing the colours for asciimatics
"""


class Colour:
    """ The class in charge of managing the colours for asciimatics """

    your_selected_colour = 0

    def __init__(self, colour_name: str = None) -> None or int:
        self.windows_bind = dict()
        self.linux_bind = dict()
        self.human_bind = dict()
        self.colour_default = -1
        self.colour_black = 0
        self.colour_red = 1
        self.colour_green = 2
        self.colour_yellow = 3
        self.colour_blue = 4
        self.colour_magenta = 5
        self.colour_cyan = 6
        self.colour_white = 7
        self._create_windows_bind()
        self._create_linux_bind()
        self._create_human_bind()
        self.your_selected_colour = -1
        if colour_name is not None:
            self.your_selected_colour = self.pick_colour(colour_name)

    def _create_linux_bind(self) -> None:
        """ Create the linux bind """
        self.linux_bind = {
            "default": self.colour_default,
            "0": self.colour_default,
            "00": self.colour_default,
            "30": self.colour_black,
            "34": self.colour_blue,
            "32": self.colour_green,
            "36": self.colour_cyan,
            "31": self.colour_red,
            "35": self.colour_magenta,
            "33": self.colour_yellow,
            "37": self.colour_white,
            "90": self.colour_black,
            "94": self.colour_blue,
            "92": self.colour_green,
            "96": self.colour_cyan,
            "91": self.colour_red,
            "95": self.colour_magenta,
            "93": self.colour_yellow,
            "97": self.colour_white
        }

    def _create_windows_bind(self) -> None:
        """ Create the windows bind """
        self.windows_bind = {
            "default": -1,
            "0": self.colour_black,
            "1": self.colour_blue,
            "2": self.colour_green,
            "3": self.colour_cyan,
            "4": self.colour_red,
            "5": self.colour_magenta,
            "6": self.colour_yellow,
            "7": self.colour_white,
            "8": self.colour_black,
            "9": self.colour_blue,
            "A": self.colour_green,
            "B": self.colour_cyan,
            "C": self.colour_red,
            "D": self.colour_magenta,
            "E": self.colour_yellow,
            "F": self.colour_white
        }

    def _create_human_bind(self) -> None:
        """ Create the human bind """
        self.human_bind = {
            "default": self.colour_default,
            "black": self.colour_black,
            "blue": self.colour_blue,
            "green": self.colour_green,
            "cyan": self.colour_cyan,
            "red": self.colour_red,
            "magenta": self.colour_magenta,
            "yellow": self.colour_yellow,
            "white": self.colour_white
        }

    def pick_colour(self, colour_name: str) -> int:
        """ Pick a colour from the human bind """
        if colour_name in self.human_bind:
            self.your_selected_colour = self.human_bind[colour_name]
            return self.your_selected_colour
        if colour_name in self.windows_bind:
            self.your_selected_colour = self.windows_bind[colour_name]
            return self.your_selected_colour
        if colour_name in self.linux_bind:
            self.your_selected_colour = self.linux_bind[colour_name]
            return self.your_selected_colour
        self.your_selected_colour = self.human_bind["default"]
        return self.your_selected_colour
