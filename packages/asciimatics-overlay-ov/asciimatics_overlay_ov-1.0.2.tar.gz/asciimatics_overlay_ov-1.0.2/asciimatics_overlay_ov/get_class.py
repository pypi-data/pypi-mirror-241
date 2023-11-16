"""
File in charge of containing the actions that are used for gathering information withing the running program
"""

from asciimatics.event import Event as EV
from asciimatics.screen import Screen as SC


class Get:
    """ The class in charge of getting elements """

    def __init__(self, event: EV, screen: SC) -> None:
        self.my_asciimatics_overlay_main_event = event
        self.my_asciimatics_overlay_main_screen = screen

    def get_event(self) -> EV:
        """ Get the event """
        return self.my_asciimatics_overlay_main_event

    def get_screen(self) -> SC:
        """ Get the screen """
        return self.my_asciimatics_overlay_main_screen

    def get_screen_width(self) -> int:
        """ Get the screen width """
        return self.my_asciimatics_overlay_main_screen.width

    def get_screen_height(self) -> int:
        """ Get the screen height """
        return self.my_asciimatics_overlay_main_screen.height

    def get_screen_dimensions(self) -> tuple:
        """ Get the screen dimensions """
        return (self.my_asciimatics_overlay_main_screen.width, self.my_asciimatics_overlay_main_screen.height)

    def get_screen_center(self) -> tuple:
        """ Get the screen center """
        return (self.my_asciimatics_overlay_main_screen.width // 2, self.my_asciimatics_overlay_main_screen.height // 2)

    def get_screen_center_x(self) -> int:
        """ Get the screen center x """
        return self.my_asciimatics_overlay_main_screen.width // 2

    def get_screen_center_y(self) -> int:
        """ Get the screen center y """
        return self.my_asciimatics_overlay_main_screen.height // 2

    def get_screen_center_left(self) -> int:
        """ Get the screen center left """
        return self.my_asciimatics_overlay_main_screen.width // 4

    def get_screen_center_right(self) -> int:
        """ Get the screen center right """
        return self.my_asciimatics_overlay_main_screen.width // 4 * 3

    def get_screen_center_top(self) -> int:
        """ Get the screen center top """
        return self.my_asciimatics_overlay_main_screen.height // 4

    def get_screen_center_bottom(self) -> int:
        """ Get the screen center bottom """
        return self.my_asciimatics_overlay_main_screen.height // 4 * 3

    def get_screen_center_top_left(self) -> tuple:
        """ Get the screen center top left """
        return (self.my_asciimatics_overlay_main_screen.width // 4, self.my_asciimatics_overlay_main_screen.height // 4)

    def get_screen_center_top_right(self) -> tuple:
        """ Get the screen center top right """
        return (self.my_asciimatics_overlay_main_screen.width // 4 * 3, self.my_asciimatics_overlay_main_screen.height // 4)

    def get_screen_center_bottom_left(self) -> tuple:
        """ Get the screen center bottom left """
        return (self.my_asciimatics_overlay_main_screen.width // 4, self.my_asciimatics_overlay_main_screen.height // 4 * 3)

    def get_screen_center_bottom_right(self) -> tuple:
        """ Get the screen center bottom right """
        return (self.my_asciimatics_overlay_main_screen.width // 4 * 3, self.my_asciimatics_overlay_main_screen.height // 4 * 3)
    # --------------------------

    def get_event_type(self) -> str:
        """ Get the event type """
        return self.my_asciimatics_overlay_main_event.type

    def get_event_key_code(self) -> int or None:
        """ Get the event key code """
        return self.my_asciimatics_overlay_main_screen.get_key()

    def get_posx(self) -> int:
        """ Get the x position of the mouse """
        return self.my_asciimatics_overlay_main_event.x

    def get_posy(self) -> int:
        """ Get the y position of the mouse """
        return self.my_asciimatics_overlay_main_event.y

    def get_posxy(self) -> tuple:
        """ Get the position of the mouse """
        return (self.my_asciimatics_overlay_main_event.x, self.my_asciimatics_overlay_main_event.y)

    def get_maxxy(self) -> tuple:
        """ Get the maximum position of the mouse """
        return (self.my_asciimatics_overlay_main_screen.width, self.my_asciimatics_overlay_main_screen.height)

    def get_maxyx(self) -> tuple:
        """ Get the maximum position of the mouse """
        return (self.my_asciimatics_overlay_main_screen.height, self.my_asciimatics_overlay_main_screen.width)
