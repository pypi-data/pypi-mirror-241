"""
File in charge of containing a few demo functions for the asciimatics library
"""


from asciimatics.event import Event
import asciimatics.widgets as WIG
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics_overlay_ov import AsciiMaticsOverlayMain
from asciimatics_overlay_ov.widgets import FrameNodes
from .hello_world import HelloWorld
from .inut_field import InputField
from .list_fields import ListFields
from .checkboxes import Checkboxes
from .radiobuttons import Radiobuttons
from .date_and_time_picker import DateAndTime
from .file_browser import FileBrowser
from .non_window_hello_world import NonWindowHelloWorld
from .popup import Popup
from .chess_test import ChessTest


class MainMenu(WIG.Frame, AsciiMaticsOverlayMain, FrameNodes):
    """ The class in charge of the main menu screen """

    def __init__(self, screen):
        super(MainMenu, self).__init__(
            screen,
            screen.height,
            screen.width,
            has_border=True,
            title="Main Menu"
        )
        self.asciimatics_overlay = AsciiMaticsOverlayMain(Event, screen)
        self.frame_node = FrameNodes()

        # Define a layout with three columns
        self.layout = WIG.Layout([1, 1, 1], fill_frame=True)
        self.add_layout(self.layout)

        self.change_screen_background(
            screen,
            self.asciimatics_overlay.colour_.colour_green
        )
        self.place_content_on_screen()

        self.fix()

    def place_content_on_screen(self) -> None:
        """ Create the main menu screen """
        self.layout.add_widget(
            self.add_button(
                text="Hello World",
                on_click=self._play,
                name=None
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Test input fields",
                on_click=self._test_input,
                name=None
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Test list fields",
                on_click=self._test_list_fields,
                name=None
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Test Checkboxes",
                on_click=self._test_checkboxes,
                name=None
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Test Radio Buttons",
                on_click=self._test_radiobuttons,
                name=None
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Test date and time picker",
                on_click=self._test_date_and_time_picker,
                name=None
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Test file browser",
                on_click=self._test_filebrowser,
                name=None
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="(Epilepsy warning) Non windowed hello world",
                on_click=self._test_non_windows_hello_world,
                name=None
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Test popup",
                on_click=self._test_popup,
                name=None
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Test chess",
                on_click=self._test_chess,
                name=None
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Quit",
                on_click=self._quit,
                name=None
            ),
            0
        )

    def _play(self) -> None:
        raise NextScene("HelloWorld")

    def _test_input(self) -> None:
        raise NextScene("InputField")

    def _test_filebrowser(self) -> None:
        raise NextScene("FileBrowser")

    def _test_list_fields(self) -> None:
        raise NextScene("ListFields")

    def _test_checkboxes(self) -> None:
        raise NextScene("Checkboxes")

    def _test_radiobuttons(self) -> None:
        raise NextScene("Radiobuttons")

    def _test_date_and_time_picker(self) -> None:
        raise NextScene("DateAndTime")

    def _test_non_windows_hello_world(self) -> None:
        raise NextScene("NonWindowHelloWorld")

    def _test_popup(self) -> None:
        raise NextScene("Popup")

    def _test_chess(self) -> None:
        raise NextScene("ChessTest")

    def _quit(self) -> None:
        raise StopApplication("User pressed quit")


class Main:
    """ The main class of the program """

    def __init__(self, success: int = 0, error: int = 1, screen: Screen = None, last_scene: Scene = None) -> None:
        self.success = success
        self.screen = screen
        self.error = error
        self.last_scene = last_scene

    def create_scenes(self, screen: Screen) -> int:
        """ Create the screens that will be used for the windows """
        scenes = [
            Scene([MainMenu(screen)], -1, name="Main"),
            Scene([HelloWorld(screen)], -1, name="HelloWorld"),
            Scene([InputField(screen)], -1, name="InputField"),
            Scene([ListFields(screen)], -1, name="ListFields"),
            Scene([Checkboxes(screen)], -1, name="Checkboxes"),
            Scene([Radiobuttons(screen)], -1, name="Radiobuttons"),
            Scene([DateAndTime(screen)], -1, name="DateAndTime"),
            Scene([FileBrowser(screen)], -1, name="FileBrowser"),
            Scene([NonWindowHelloWorld(screen)],
                  (-1), name="NonWindowHelloWorld"),
            Scene([Popup(screen)], -1, name="Popup"),
            Scene([ChessTest(screen)], -1, name="ChessTest")
        ]
        return scenes

    def main(self, screen: Screen) -> int:
        """ Create the main window """
        scenes = self.create_scenes(screen)
        screen.play(
            scenes,
            stop_on_resize=True,
            start_scene=self.last_scene,
            allow_int=True
        )
        return self.success

    def run(self) -> int:
        """ Run the program """
        if self.screen is None:
            try:
                Screen.wrapper(
                    self.main  # ,
                    # catch_interrupt=True,
                )
                return self.success
            except ResizeScreenError as e:
                self.last_scene = e.scene
        return self.error


if __name__ == "__main__":
    SUCCESS = 0
    ERROR = 1
    LAST_SCENE = None
    SCREEN = None
    MI = Main(SUCCESS, ERROR, SCREEN, LAST_SCENE)
    MI.run()
