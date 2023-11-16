"""
File in charge of containing binders for the Screen interraction
"""

from asciimatics.screen import Screen as SC
from asciimatics_overlay_ov.colour_class import Colour


class MyScreen:
    """ The class in wharge of containing the binders for the Screen insterractions """

    def __init__(self, screen: SC = None, success: int = 0, error: int = 84) -> None:
        self.success = success
        self.error = error
        self.my_asciimatics_overlay_main_screen = screen

    def destroy_game_screen(self) -> int:
        """ Destroy the game screen """
        self.my_asciimatics_overlay_main_screen.close()
        return self.success

    def create_game_screen(self) -> int:
        """ Create the game screen """
        self.my_asciimatics_overlay_main_screen = SC.open()
        return self.success

    def clear_screen(self) -> int:
        """ Clear the screen """
        self.my_asciimatics_overlay_main_screen.clear()
        return self.success

    def refresh_screen(self) -> int:
        """ Refresh the screen """
        self.my_asciimatics_overlay_main_screen.refresh()
        return self.success

    def set_screen_title(self, title: str) -> int:
        """ Set the screen title """
        if isinstance(title, str) is True:
            self.my_asciimatics_overlay_main_screen.set_title(title)
            return self.success
        if isinstance(title, (list, tuple, float, int, object)) is False:
            print("Title must be of type 'string'")
            return self.error
        content = ""
        if isinstance(title, (list, tuple)) is True:
            content = ""
            for i in title:
                content += f"{i} "
        else:
            content = f"{title}"
        self.my_asciimatics_overlay_main_screen.set_title(content)
        return self.success

    def set_screen_colour(self, fg: Colour.your_selected_colour = -1, attr: any = None, bg: Colour.your_selected_colour = -1) -> int:
        """
        Set the colour of the screen
        colour: New colour to use.
        Change current colour if required.

        :param colour: New colour to use.
        :param attr: New attributes to use.
        :param bg: New background colour to use.
        """
        self.my_asciimatics_overlay_main_screen._change_colours(
            colour=fg,
            attr=attr,
            bg=bg
        )
        return self.success
