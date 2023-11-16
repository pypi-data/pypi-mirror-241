"""
File in charge of containing the hello world screen
"""

import asciimatics.widgets as WIG
from asciimatics.event import Event
from asciimatics.exceptions import NextScene
from asciimatics_overlay_ov import AsciiMaticsOverlayMain
from asciimatics_overlay_ov.widgets import FrameNodes


class HelloWorld(WIG.Frame, AsciiMaticsOverlayMain, FrameNodes):
    """ A simple hello world window """

    def __init__(self, screen):
        super(HelloWorld, self).__init__(
            screen,
            screen.height,
            screen.width,
            has_border=True,
            title="Hello World"
        )
        self.frame_node = FrameNodes()
        self.asciimatics_overlay = AsciiMaticsOverlayMain(Event, screen)
        self.layout = WIG.Layout([1, 1])  # Define a layout with three columns
        self.add_layout(self.layout)
        self.place_content_on_screen()
        self.fix()

    def place_content_on_screen(self) -> None:
        """ Create the welcome screen """
        self.layout.add_widget(
            self.add_label(
                "Hello World !",
                align=self.frame_node.label_center,
                name=None
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Exit",
                on_click=self._exit,
                name=None
            ),
            0
        )

    def _exit(self):
        raise NextScene("Main")
