"""
File in charge of containing the radiobuttons screen
"""

from random import randint
from functools import partial
import asciimatics.widgets as WIG
from asciimatics.event import Event
from asciimatics.exceptions import NextScene
from asciimatics_overlay_ov import AsciiMaticsOverlayMain
from asciimatics_overlay_ov.widgets import FrameNodes
from .list_data import LIST_DATA, LIST_DATA_LENGTH


class Radiobuttons(WIG.Frame, AsciiMaticsOverlayMain, FrameNodes):
    """ The class in charge of displaying Radiobuttons in a window """

    def __init__(self, screen):
        super(Radiobuttons, self).__init__(
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
        self.radio_options = list()
        self.layout = WIG.Layout([100])
        self.add_layout(self.layout)
        self.layout2 = None
        self.layout3 = None
        self.layout4 = None
        self.place_content_on_screen()
        self.fix()

    def _create_checkboxes(self, desired_layout: WIG.Layout) -> None:
        """ Add a series of checkboxes to the screen """
        max_placable_boxes = randint(1, 10)
        current_destination = "usr_choices"
        self.radio_options = list()
        for i in range(max_placable_boxes):
            self.radio_options.append(
                (
                    f"{LIST_DATA[randint(0, LIST_DATA_LENGTH)]}",
                    i
                )
            )

        desired_layout.add_widget(
            self.add_radiobuttons(
                options=self.radio_options,
                label=None,
                name="radiobuttons",
                on_change=partial(
                    self._update_usr_input,
                    "radiobuttons",
                    f"{current_destination}"
                )
            ),
            0
        )

    def _add_chosen_data_line(self) -> None:
        """ Add the line informing the user of the line they chose """
        self.layout2 = WIG.Layout([30, 60])
        self.add_layout(self.layout2)
        self.layout2.add_widget(
            self.add_label(
                text="You have chosen:",
                height=1,
                align=self.frame_node.label_left
            ),
            0
        )

        self.layout2.add_widget(
            self.add_label(
                text="",
                height=1,
                align=self.frame_node.label_center,
                name="usr_choices"
            ),
            1
        )

    def place_content_on_screen(self) -> None:
        """ Create the welcome screen """
        self.layout.add_widget(
            self.add_label(
                "Input demos",
                align=self.frame_node.label_center
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Remove checkboxes",
                on_click=partial(
                    self._remove_layout,
                    self.layout4,
                    "usr_choices"
                )
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Reset Layout",
                on_click=partial(
                    self._reset_layout,
                    "usr_choices"
                )
            )
        )
        self._add_chosen_data_line()
        self.layout3 = WIG.Layout([33, 33, 33])
        self.add_layout(self.layout3)
        self.layout3.add_widget(
            self.add_button(
                text="Exit",
                on_click=self._exit,
                name=None
            ),
            1
        )
        self.layout4 = WIG.Layout([100])
        self.add_layout(self.layout4)
        self._create_checkboxes(self.layout4)

    def _update_usr_input(self, checkbox_name: str, destination: str) -> None:
        """ Update the choice of the user based on their selection """
        checkbox_input = self.find_widget(checkbox_name)
        checkbox_input_value = self.get_text_input(checkbox_input)
        destination_var = self.find_widget(destination)
        self.apply_text_to_display(
            destination_var,
            f"{self.radio_options[checkbox_input_value][0]}"
        )

    def _remove_layout(self, chosen_layout: WIG.Layout, display_widget: str) -> None:
        """ Remove the checkboxes contained in the layout """
        if chosen_layout is None:
            chosen_layout = self.layout4
        chosen_layout.clear_widgets()
        destination_var = self.find_widget(display_widget)
        self.apply_text_to_display(destination_var, "")
        self.fix()

    def _reset_layout(self, display_widget: str = "usr_choices") -> None:
        """ Reset the current selection and options """
        self._remove_layout(self.layout4, display_widget)
        self._create_checkboxes(self.layout4)
        destination_var = self.find_widget(display_widget)
        self.apply_text_to_display(destination_var, "")
        self.fix()

    def _exit(self):
        raise NextScene("Main")
