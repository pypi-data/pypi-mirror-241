"""
File in charge of containing the list fields screen
"""

from functools import partial
import asciimatics.widgets as WIG
from asciimatics.event import Event
from asciimatics.exceptions import NextScene
from asciimatics_overlay_ov import AsciiMaticsOverlayMain
from asciimatics_overlay_ov.widgets import FrameNodes
from .list_data import LIST_DATA


class ListFields(WIG.Frame, AsciiMaticsOverlayMain, FrameNodes):
    """ A demo of the dropdown info """

    def __init__(self, screen):
        super(ListFields, self).__init__(
            screen,
            screen.height,
            screen.width,
            has_border=True,
            title="List Fields"
        )
        self.frame_node = FrameNodes()
        self.asciimatics_overlay = AsciiMaticsOverlayMain(Event, screen)
        self.error = self.frame_node.error
        self.success = self.frame_node.success
        self.data_nodes = {
            "text": "",
            "text2": ""
        }
        self.layout = WIG.Layout([90, 1])
        self.add_layout(self.layout)
        self.layout2 = None
        self.layout3 = None
        self.place_content_on_screen()
        self.fix()

    def _generate_random_data_for_the_input(self) -> list[tuple[str, int]]:
        """ Generate random data for the input """
        random_data = []
        for _ in enumerate(LIST_DATA):
            random_data.append(
                (f"Name: {_[1]}", _[0])
            )
        return random_data

    def add_test_controls(self) -> None:
        """ Add the controls for the test """
        self.layout2 = WIG.Layout([50, 50])
        self.add_layout(self.layout2)
        self.layout2.add_widget(
            self.add_label(
                text="Your current selection:",
                height=1,
                align=self.frame_node.label_left
            ),
            0
        )
        self.layout2.add_widget(
            self.add_label(
                text="",
                height=1,
                align=self.frame_node.label_left,
                name="user_listbox_current_selection"
            ),
            1
        )
        self.layout3 = WIG.Layout([40, 60])
        self.add_layout(self.layout3)
        self.layout3.add_widget(
            self.add_label(
                text="Your current choice:",
                height=1,
                align=self.frame_node.label_left
            ),
            0
        )
        self.layout3.add_widget(
            self.add_label(
                text="",
                height=1,
                align=self.frame_node.label_left,
                name="user_listbox_current_choice"
            ),
            1
        )

    def place_content_on_screen(self) -> None:
        """ Create the welcome screen """
        random_data = self._generate_random_data_for_the_input()
        self.layout.add_widget(
            self.add_label(
                "Input demos lists",
                align=self.frame_node.label_center
            ),
            0
        )
        self.layout.add_widget(
            self.add_listbox(
                input_data=random_data,

                on_change=partial(
                    self._display_new_selection,
                    "my_listbox", "user_listbox_current_selection"
                ),
                on_select=partial(
                    self._display_new_selection,
                    "my_listbox", "user_listbox_current_choice"
                ),
                height=5
            ),
            0
        )
        self.add_test_controls()
        self.layout.add_widget(
            self.add_button(
                text="Exit",
                on_click=self._exit,
                label=None,
                name=None
            ),
            0
        )

    def _display_new_selection(self, source, destination) -> None:
        """ Display the new selection """
        self.apply_text_to_display(
            self.find_widget(destination),
            self.get_text_input(self.find_widget(source))
        )

    def _exit(self):
        raise NextScene("Main")
