"""
File in charge of containing a window containing popup windows
"""

from functools import partial
import asciimatics.widgets as WIG
from asciimatics.event import Event
from asciimatics.exceptions import NextScene
from asciimatics_overlay_ov import AsciiMaticsOverlayMain
from asciimatics_overlay_ov.widgets import FrameNodes


class Popup(WIG.Frame, AsciiMaticsOverlayMain, FrameNodes):
    """ The class in charge of displaying a window containing popup windows """

    def __init__(self, screen):
        super(Popup, self).__init__(
            screen,
            screen.height//2,
            screen.width//2,
            has_border=True,
            title="Popup"
        )
        self.frame_node = FrameNodes()
        self.asciimatics_overlay = AsciiMaticsOverlayMain(Event, screen)
        self.error = self.frame_node.error
        self.success = self.frame_node.success
        self.layout = WIG.Layout([100], fill_frame=True)
        self.add_layout(self.layout)
        self.place_content_on_screen()
        self.fix()

    def place_content_on_screen(self) -> None:
        """ Create the welcome screen """
        self.layout.add_widget(
            self.add_label(
                text="Here are a selection of popup-windows :-)",
                height=1,
                align=self.frame_node.label_center,
                name=None
            )
        )
        self.layout.add_widget(
            self.add_button(
                text="Simple popup",
                on_click=self._simple_popup,
                label=None,
                box=True,
                name=None
            )
        )
        self.layout.add_widget(
            self.add_button(
                text="Menu popup",
                on_click=self._menu_popup,
                label=None,
                box=True,
                name=None
            )
        )
        self.layout.add_widget(
            self.add_button(
                text="Exit",
                on_click=self._exit,
                name="exit_button"
            ),
            0
        )

    def _display_sample_text(self, sample_text: str, fg: int, bg: int, posy: int, posx: int) -> None:
        """ The sample text to show """
        print("In display sample text")
        print(f"sample_text = {sample_text}")
        print(f"fg = {fg}")
        print(f"bg = {bg}")
        print(f"posy = {posy}")
        print(f"posx = {posx}")
        print(f"dir(self) = {dir(self)}")
        for i in dir(self):
            print(f"self.{i} = {getattr(self, i)}")
        print(f"dir(self.scene) = {dir(self.scene)}")
        print(f"dir(self.screen) = {dir(self.screen)}")
        self.screen.print_at(
            f"You chose ({sample_text})",
            posx,
            posy,
            fg,
            0,
            bg,
            False
        )
        # self.mvprintw_colour(
        #     f"You chose ({sample_text})",
        #     posx,
        #     posy,
        #     fg,
        #     0,
        #     bg,
        #     True
        # )
        print("After display sample text")

    def _simple_popup(self) -> None:
        """ Display a simple popup """
        self.scene.add_effect(
            self.add_popup_dialog(
                screen=self.screen,
                text="Hello World !",
                buttons=["Exit"],
                # on_close=partial(
                #     self.mvprintw_colour,
                #     "You closed (simple popup)",
                #     (self.screen.width // 2),
                #     (self.screen.height//2),
                #     self.asciimatics_overlay.colour_black,
                #     0,
                #     self.asciimatics_overlay.colour_cyan,
                #     True
                # ),
                has_shadow=True,
                theme="warning"
            )
        )
        self.fix()

    def _menu_popup(self) -> None:
        """ Display a menu popup """
        # self.scene.screen = self.screen
        self.scene.the_sample_text = self._display_sample_text
        self.scene.asciimatics_overlay = self.asciimatics_overlay
        self.scene.the_screen = self._screen
        self.scene.the_fg = (self.scene.asciimatics_overlay.colour_black)
        self.scene.the_bg = (self.scene.asciimatics_overlay.colour_green)
        self.scene.the_posx = 0  # (self.scene.the_screen.width // 2)
        self.scene.the_posy = 0  # (self.scene.the_screen.height//2)
        # print(f"dir(self.scene) = {dir(self.scene)}")
        # for i in dir(self.scene):
        #     print(f"self.scene.{i} = {getattr(self.scene, i)}")
        self.scene.add_effect(
            self.add_popup_menu(
                screen=self.screen,
                menu_items=[
                    (
                        "Sample text1",
                        partial(
                            self.scene.the_sample_text,
                            "Sample text1",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text2",
                        partial(
                            print,
                            "dir(Content of display_sample_text) = ",
                            partial(
                                dir,
                                partial(
                                    self.scene.the_sample_text,
                                    "Sample text2",
                                    self.scene.the_fg,
                                    self.scene.the_bg,
                                    self.scene.the_posx,
                                    self.scene.the_posy
                                )
                            )
                        )
                    ),
                    (
                        "Sample text3",
                        partial(
                            self.scene.the_sample_text,
                            "Sample text3",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text4",
                        partial(
                            self.scene.the_sample_text,
                            "Sample text4",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text5",
                        partial(
                            self.scene.the_sample_text,
                            "Sample text5",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text6",
                        partial(
                            self.scene.the_sample_text,
                            "Sample text6",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text7",
                        partial(
                            self.scene.the_sample_text,
                            "Sample text7",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text8",
                        partial(
                            self.scene.the_sample_text,
                            "Sample text8",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text9",
                        partial(
                            self.scene.the_sample_text,
                            "Sample text9",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text10",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text10",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text11",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text11",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text12",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text12",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text13",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text13",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text14",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text14",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text15",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text15",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text16",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text16",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text17",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text17",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text18",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text18",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text19",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text19",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text20",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text20",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text21",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text21",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text22",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text22",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text23",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text23",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text24",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text24",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text25",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text25",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text26",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text26",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text27",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text27",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    ),
                    (
                        "Sample text28",
                        partial
                        (
                            self.scene.the_sample_text,
                            "Sample text28",
                            self.scene.the_fg,
                            self.scene.the_bg,
                            self.scene.the_posx,
                            self.scene.the_posy
                        )
                    )
                ],
                posx=(self.screen.width // 2),
                posy=(self.screen.height // 2)
            )
        )
        self.fix()

    def _reset_layout(self, display_widgets: list[str] or str = "", value: list[str] or str = "") -> None:
        """ Reset the current selection and options """
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
        raise NextScene("Main")
