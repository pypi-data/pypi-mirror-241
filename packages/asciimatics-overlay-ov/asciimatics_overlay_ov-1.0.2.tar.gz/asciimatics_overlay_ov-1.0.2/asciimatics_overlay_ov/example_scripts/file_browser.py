"""
File in charge of containing a filebrowser screen
"""

import os
from functools import partial
import asciimatics.widgets as WIG
from asciimatics.event import Event
from asciimatics.exceptions import NextScene
from asciimatics_overlay_ov import AsciiMaticsOverlayMain
from asciimatics_overlay_ov.widgets import FrameNodes


class FileBrowser(WIG.Frame, AsciiMaticsOverlayMain, FrameNodes):
    """ The class in charge of displaying a filebrowser in a window """

    def __init__(self, screen):
        super(FileBrowser, self).__init__(
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
        self.layout = WIG.Layout([100], fill_frame=True)
        self.add_layout(self.layout)
        self.layout2 = None
        self.layout3 = None
        self.layout4 = None
        self.place_content_on_screen()
        self.fix()

    def place_content_on_screen(self) -> None:
        """ Create the welcome screen """
        self.layout.add_widget(
            self.add_label(
                text="Here is a beautiful filebrowser :-)",
                height=1,
                align=self.frame_node.label_center,
                name=None
            )
        )
        self.layout.add_widget(
            self.add_divider(
                draw_line=True,
                height=1,
                line_char="#"
            )
        )
        self.layout.add_widget(
            self.add_filebrowser(
                height=WIG.Widget.FILL_FRAME,
                root=os.path.abspath("."),
                name="filebrowser",
                on_select=partial(
                    self._update_usr_input,
                    "filebrowser",
                    "filebrowser_choice_output"
                ),
                on_change=partial(
                    self._update_usr_input,
                    "filebrowser",
                    "filebrowser_output"
                ),
                file_filter=".*.txt$|.*.py$"
            )
        )
        self.layout.add_widget(
            self.add_divider(
                draw_line=True,
                height=1,
                line_char="#"
            )
        )

        self.layout2 = WIG.Layout([20, 80])
        self.add_layout(self.layout2)
        self.layout2.add_widget(
            self.add_label(
                text="You have chosen:",
                height=1,
                align=self.frame_node.label_center,
                name=None
            ),
            0
        )
        self.layout2.add_widget(
            self.add_label(
                text="",
                height=1,
                align=self.frame_node.label_center,
                name="filebrowser_output"
            ),
            1
        )
        self.layout3 = WIG.Layout([20, 80])
        self.add_layout(self.layout3)
        self.layout3.add_widget(
            self.add_label(
                text="You have selected:",
                height=1,
                align=self.frame_node.label_center,
                name=None
            ),
            0
        )
        self.layout3.add_widget(
            self.add_label(
                text="",
                height=1,
                align=self.frame_node.label_center,
                name="filebrowser_choice_output"
            ),
            1
        )
        self.layout4 = WIG.Layout([100])
        self.add_layout(self.layout4)
        self.layout4.add_widget(
            self.add_divider(
                draw_line=True,
                height=1,
                line_char="#"
            ),
            0
        )
        self.layout4.add_widget(
            self.add_button(
                text="Exit",
                on_click=self._exit,
                name="exit_button"
            ),
            0
        )

    def _update_usr_input(self, object_name: str, destination: str) -> None:
        """ Update the choice of the user based on their selection """
        object_name = self.find_widget(object_name)
        data = self.get_widget_value(object_name)
        destination_var = self.find_widget(destination)
        self.apply_text_to_display(destination_var, f"{data}")

    def _reset_layout(self, display_widgets: list[str] or str = "", value: list[str] or str = "") -> None:
        """ Reset the current selection and options """
        print(f"Reset layout ({display_widgets}, {value})")
        if isinstance(value, str) is True and isinstance(display_widgets, list) is True:
            data = list()
            for i in value:
                data.append(value)
        else:
            data = value
        if isinstance(display_widgets, list) is True:
            for index, display_widget in enumerate(display_widgets):
                destination_var = self.find_widget(display_widget)
                status = self.apply_text_to_display(
                    destination_var,
                    data[index]
                )
                if status != self.success:
                    status2 = self.apply_text_to_input_box(
                        destination_var, data[index])
                    if status2 != self.success:
                        raise Exception(f"Failed to reset {display_widget}")
        else:
            destination_var = self.find_widget(display_widget)
            self.apply_text_to_display(destination_var, value)
        self.fix()

    def _exit(self):
        # self._reset_layout(
        #     display_widgets=[],
        #     value=[]
        # )
        raise NextScene("Main")
