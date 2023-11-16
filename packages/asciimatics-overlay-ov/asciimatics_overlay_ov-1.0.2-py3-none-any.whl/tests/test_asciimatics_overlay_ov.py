# tests/test_ask_question.py
import unittest.mock
from sys import stderr
import asciimatics.screen as SCR
import asciimatics.event as EVE
from asciimatics_overlay_ov import AsciimaticsOverlay


def print_debug(string: str = "") -> None:
    """ Print debug messages """
    debug = False
    if debug is True:
        print(f"DEBUG: {string}", file=stderr)


class TestAsciimaticsOverlay(AsciimaticsOverlay):
    """ The class in charge of testing asciimatics overlay """

    def __init__(self) -> None:
        # ---- status code ----
        self.success = 0
        self.error = 84
        # ---- class attributes ----
        self.screen = SCR.Screen
        self.event = EVE.Event
        # ---- class inheritance ----
        super(AsciimaticsOverlay, self).__init__(
            self.screen,
            self.event
        )

    def initialise_window(self) -> int:
        """ Initialise the window """
        self.screen = SCR.Screen.open()
        self.event = EVE.Event()
        self.update_initial_pointers(self.event, self.screen)
        return self.success

    def de_initialise_window(self) -> int:
        """ De-initialise the window """
        self.screen.close(restore=True)
        self.event = None
        return self.success


TAOI = TestAsciimaticsOverlay()


def test_window_initialisation() -> None:
    """ Try to initialise the window """
    status1 = TAOI.initialise_window()
    status2 = TAOI.de_initialise_window()

    assert status1 == TAOI.success
    assert status2 == TAOI.success


def test_hello_world() -> None:
    """ Try to display a Hello World using the mvprintw """
    status1 = TAOI.initialise_window()
    try:
        TAOI.mvprintw("Hello World!", 0, 0)
    except Exception as err:
        print(f"Error = {err}")
        assert False
    status3 = TAOI.de_initialise_window()

    assert status1 == TAOI.success
    assert status3 == TAOI.success


def test_double_array_output() -> None:
    """ Try to display a double array """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.print_array(["Hello", "World"], " ", 0, 0)
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()

    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def print_array_colour() -> None:
    """ Try to display an array with colour output """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.print_array_colour(
            [
                {
                    "text": "Hello",
                    "posx": 0,
                    "posy": 0,
                    "colour": 7,
                    "attr": 0,
                    "bg": 0,
                    "transparent": False
                },
                {
                    "text": "World",
                    "posx": 0,
                    "posy": 0,
                    "colour": 7,
                    "attr": 0,
                    "bg": 0,
                    "transparent": False
                }
            ],
            " ",
            0,
            0
        )
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()

    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_print_double_array() -> None:
    """ Try to display a double array """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.print_double_array(
            [
                [
                    "Hello",
                    "World"
                ],
                [
                    "Hello",
                    "World"
                ]
            ],
            " ",
            0,
            0
        )
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()

    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_print_double_array_colour() -> None:
    """ Try to display a double array with colour """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.print_double_array_colour(
            [
                [
                    {
                        "text": "Hello",
                        "posx": 0,
                        "posy": 0,
                        "colour": 7,
                        "attr": 0,
                        "bg": 0,
                        "transparent": False
                    },
                    {
                        "text": "World",
                        "posx": 0,
                        "posy": 0,
                        "colour": 7,
                        "attr": 0,
                        "bg": 0,
                        "transparent": False
                    }
                ],
                [
                    {
                        "text": "Hello",
                        "posx": 0,
                        "posy": 0,
                        "colour": 7,
                        "attr": 0,
                        "bg": 0,
                        "transparent": False
                    },
                    {
                        "text": "World",
                        "posx": 0,
                        "posy": 0,
                        "colour": 7,
                        "attr": 0,
                        "bg": 0,
                        "transparent": False
                    }
                ]
            ],

            " ",
            0,
            0,
            7,
            0,
            TAOI.colour_cyan,
            False
        )
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()

    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_print_array_cloud_points() -> None:
    """Test the function to print array of cloud points."""
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.print_array_cloud_points(
            [
                {
                    "character": "Hello",
                    "posx": 0,
                    "posy": 0,
                    "colour": 7,
                    "attr": 0,
                    "bg": 0,
                    "transparent": False
                },
                {
                    "character": "World",
                    "posx": 0,
                    "posy": 1,
                    "colour": 7,
                    "attr": 0,
                    "bg": 0,
                    "transparent": False
                },
                {
                    "character": "Hello",
                    "posx": 0,
                    "posy": 2,
                    "colour": 7,
                    "attr": 0,
                    "bg": 0,
                    "transparent": False
                },
                {
                    "character": "World",
                    "posx": 0,
                    "posy": 3,
                    "colour": 7,
                    "attr": 0,
                    "bg": 0,
                    "transparent": False
                }
            ],
            0,
            0,
            7,
            0,
            TAOI.colour_cyan,
            False
        )
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()

    assert status1 == TAOI.success
    print("status 2")
    assert status2 == TAOI.success
    print("status 3")
    assert status3 == TAOI.success


def test_get_event() -> None:
    """ Test the function to get event """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_event()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()

    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen() -> None:
    """ Test the function to get screen """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()

    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_width() -> None:
    """ Test the function to get screen width """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_width()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()

    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_height() -> None:
    """ Test the function to get screen height """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_height()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()

    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_dimensions() -> None:
    """ Test the function to get screen dimensions """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_dimensions()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_center() -> None:
    """ Test the function to get screen center """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_center()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_center_x() -> None:
    """ Test the function to get screen center x """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_center_x()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error

    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_center_y() -> None:
    """ Test the function to get screen center y """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_center_y()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error

    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_center_left() -> None:
    """ Test the function to get screen center left """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_center_left()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error

    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_center_right() -> None:
    """ Test the function to get screen center right """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_center_right()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error

    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_center_top() -> None:
    """ Test the function to get screen center top """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_center_top()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error

    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_center_bottom() -> None:
    """ Test the function to get screen center bottom """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_center_bottom()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error

    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_center_top_left() -> None:
    """ Test the function to get screen center top left """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_center_top_left()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error

    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_screen_center_top_right() -> None:
    """ Test the function to get screen center top right """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_center_top_right()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error

    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_center_bottom_left() -> None:
    """ Test the function to get screen center bottom left """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_center_bottom_left()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_center_bottom_right() -> None:
    """ Test the function to get screen center bottom right """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_screen_center_bottom_right()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_get_event_type() -> None:
    """ Test the function to get event type """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_event_type()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.error
    assert status3 == TAOI.success


def test_get_event_key_code() -> None:
    """ Test the function to get event type """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.get_event_key_code()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.error
    assert status3 == TAOI.success


def test_is_mouse_button_pressed() -> None:
    """ Test the function to check if a mouse button is pressed """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.is_mouse_button_pressed()
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.error
    assert status3 == TAOI.success


def test_is_it_this_mouse_button() -> None:
    """ Test the function to check if a mouse button is pressed """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.is_it_this_mouse_button(1)
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.error
    assert status3 == TAOI.success


def test_pick_colour() -> None:
    """ Test the function to pick a colour """
    status1 = TAOI.initialise_window()
    status2 = TAOI.error
    try:
        TAOI.pick_colour("cyan")
        status2 = TAOI.success
    except Exception as err:
        print(f"Error = {err}")
        status2 = TAOI.error
    status3 = TAOI.de_initialise_window()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
    assert status3 == TAOI.success


def test_screen_initialisation() -> None:
    """ Test the function to initialise the screen """
    status1 = TAOI.create_game_screen()
    status2 = TAOI.destroy_game_screen()
    assert status1 == TAOI.success
    assert status2 == TAOI.success
