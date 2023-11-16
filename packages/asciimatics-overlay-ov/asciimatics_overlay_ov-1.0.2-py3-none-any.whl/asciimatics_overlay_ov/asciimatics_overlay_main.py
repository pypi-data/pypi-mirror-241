"""
File in charge of containing the code for the rebind
"""

from asciimatics.event import Event
from asciimatics.screen import Screen as SC
from .is_class import Is
from .screen_class import MyScreen
from .get_class import Get
from .display_class import Display
from .colour_class import Colour
from .widgets import FrameNodes


class AsciiMaticsOverlayMain(Is, MyScreen, Get, Display, Colour, FrameNodes):
    """ The class in charge of simplifying the usage of some functionalities from asciimatics """

    def __init__(self, event: Event = None, screen: SC = None, success: int = 0, error: int = 84) -> None:
        self.success = success
        self.error = error
        if event is None or screen is None:
            return
        self.__version__ = '1.0.2'
        # ---- Basic input ----
        self.my_asciimatics_overlay_main_event = event
        self.my_asciimatics_overlay_main_screen = screen
        # ---- Initialise the inherited classes ----
        super(Is, self).__init__(self.my_asciimatics_overlay_main_event)
        super(MyScreen, self).__init__(
            self.my_asciimatics_overlay_main_event,
            self.my_asciimatics_overlay_main_screen
        )
        super(Get, self).__init__(self.my_asciimatics_overlay_main_screen)
        super(Colour, self).__init__()
        super(Display, self).__init__()
        super(FrameNodes, self).__init__()
        # ---- Initialise the node classes version ----
        self.is_ = Is(self.my_asciimatics_overlay_main_event)
        self.screen_ = MyScreen(
            self.my_asciimatics_overlay_main_screen,
            self.success,
            self.error
        )
        self.get_ = Get(
            self.my_asciimatics_overlay_main_event,
            self.my_asciimatics_overlay_main_screen
        )
        self.display_ = Display(self.my_asciimatics_overlay_main_screen)
        self.colour_ = Colour()
        self.frame_nodes_ = FrameNodes(self.success, self.error)

    def update_initial_pointers(self, event: Event = None, screen: SC = None, success: int = None, error: int = None) -> int:
        """ Update the initial pointers, this is usefull when you wish to inherit this class """
        if event is None and self.my_asciimatics_overlay_main_event is not None:
            event = self.my_asciimatics_overlay_main_event
        elif self.my_asciimatics_overlay_main_event is None:
            raise Exception(
                "my_asciimatics_overlay_main_event or event must contain an instance of the Event class."
            )

        if screen is None:
            screen = self.my_asciimatics_overlay_main_screen
        elif self.my_asciimatics_overlay_main_screen is None:
            raise Exception(
                "my_asciimatics_overlay_main_screen or screen must contain an instance of the Screen class."
            )
        self.my_asciimatics_overlay_main_event = event
        self.my_asciimatics_overlay_main_screen = screen
        self.is_.my_asciimatics_overlay_main_event = event
        self.screen_.my_asciimatics_overlay_main_screen = screen
        self.get_.my_asciimatics_overlay_main_event = event
        if success is not None:
            self.success = success
            self.screen_.success = success
            self.frame_nodes_.success = success
        if error is not None:
            self.error = error
            self.screen_.error = error
            self.frame_nodes_.error = error
        return 0

    def update_event_pointer(self, event: Event) -> int:
        """ Update the event pointer """
        self.my_asciimatics_overlay_main_event = event
        self.is_.my_asciimatics_overlay_main_event = self.my_asciimatics_overlay_main_event
        self.get_.my_asciimatics_overlay_main_event = self.my_asciimatics_overlay_main_event
        return 0
