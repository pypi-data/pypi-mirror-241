"""
File in charge of containing the input field screen
"""

import asciimatics.widgets as WIG
from asciimatics.event import Event
from asciimatics.exceptions import NextScene
from asciimatics_overlay_ov import AsciiMaticsOverlayMain
from asciimatics_overlay_ov.widgets import FrameNodes


class InputField(WIG.Frame, AsciiMaticsOverlayMain, FrameNodes):
    """ A simple input field """

    def __init__(self, screen):
        super(InputField, self).__init__(
            screen,
            screen.height,
            screen.width,
            has_border=True,
            title="Input Field"
        )
        self.frame_node = FrameNodes()
        self.asciimatics_overlay = AsciiMaticsOverlayMain(Event, screen)
        self.error = self.frame_node.error
        self.success = self.frame_node.success
        self.data_nodes = {
            "text": "",
            "text2": ""
        }
        self.layout = WIG.Layout([100])
        self.add_layout(self.layout)
        self.layout2 = None
        self.place_content_on_screen()
        self.fix()

    def place_content_on_screen(self) -> None:
        """ Create the welcome screen """
        self.layout.add_widget(
            self.add_label(
                "Input demos",
                align=self.frame_node.label_center
            ),
            0
        )
        self.data_nodes["text"] = self.frame_node.add_input(
            label="Sample input:",
            on_change=self._get_usr_input,
            name="text"
        )
        self.layout.add_widget(self.data_nodes["text"], 0)
        self.data_nodes["text2"] = self.frame_node.add_textbox(
            height=2,
            label="Sample textbox:",
            name="text2",
            as_string=True,
            line_wrap=True,
            on_change=self._get_usr_input,
            readonly=False
        )
        self.layout.add_widget(self.data_nodes["text2"], 0)
        self.layout2 = WIG.Layout([30, 60])
        self.add_layout(self.layout2)
        self.layout2.add_widget(
            self.add_label(
                text="You have entered:",
                height=1,
                align=self.frame_node.label_left
            )
        )

        self.layout2.add_widget(
            self.add_label(
                text="",
                height=10,
                align=self.frame_node.label_center,
                name="Input_data"
            ),
            1
        )
        self.layout.add_widget(
            self.add_button(
                text="Exit",
                on_click=self._exit,
                name=None
            ),
            0
        )

    def _get_usr_input(self) -> None:
        """ Get the input of the user for both boxes """
        input_a = self.get_text_input(self.find_widget("text"))
        input_b = self.get_text_input(self.find_widget("text2"))
        input_c = self.find_widget("Input_data")
        if input_a != self.error and input_b != self.error:
            self.apply_text_to_display(
                input_c,
                f"{input_a}\n{input_b}"
            )

    def _reset_input(self) -> None:
        """ Reset the content of the boxes using pre-built functions """
        self.apply_text_to_input_box(self.find_widget("text"), "")
        self.apply_text_to_input_box(self.find_widget("text2"), "")
        self.apply_text_to_display(self.find_widget("Input_data"), "")

    def _exit(self):
        self._reset_input()
        raise NextScene("Main")
