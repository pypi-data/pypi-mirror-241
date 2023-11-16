"""
The file in charge of groupping the is functions in charge of asserting states
"""
from asciimatics.event import Event


class Is:
    """ The class in charge of asserting states """

    def __init__(self, event: Event = None) -> None:
        self.my_asciimatics_overlay_main_event = event

    def is_key_pressed(self) -> bool:
        """ Check if a key is pressed """
        if self.my_asciimatics_overlay_main_event is not None:
            return True
        return False

    def is_it_this_key(self, input_key: int, wanted_key: str or int) -> bool:
        """ Check if the key pressed is the one passed as parameter """
        if isinstance(wanted_key, int) is True:
            if input_key == wanted_key:
                return True
            return False
        if input_key == ord(wanted_key):
            return True
        return False

    def is_mouse_button_pressed(self) -> bool:
        # Define the button_mask for each mouse button (left, middle, right)
        left_button_mask = 1
        middle_button_mask = 2
        right_button_mask = 4

        # Check if any mouse button is pressed
        if (self.my_asciimatics_overlay_main_event.buttons & left_button_mask) or (self.my_asciimatics_overlay_main_event.buttons & middle_button_mask) or (self.my_asciimatics_overlay_main_event.buttons & right_button_mask):
            return True
        else:
            return False

    def is_it_this_mouse_button(self, button: int):
        """
        Check if a specific mouse button is currently pressed in an asciimatics application.

        Args:
            screen (asciimatics.screen.Screen): The asciimatics screen object.
            button (int): The mouse button to check (1 for left, 2 for middle, 3 for right).

        Returns:
            bool: True if the specified mouse button is pressed, False otherwise.
        """
        # Get the current mouse event
        mouse_event = self.my_asciimatics_overlay_main_event.get_event()

        # Check if the event is a mouse event and the specified button is pressed
        if isinstance(mouse_event, self.my_asciimatics_overlay_main_event) and 1 <= button <= 3:
            return mouse_event.buttons & (1 << (button - 1)) != 0

        return False
