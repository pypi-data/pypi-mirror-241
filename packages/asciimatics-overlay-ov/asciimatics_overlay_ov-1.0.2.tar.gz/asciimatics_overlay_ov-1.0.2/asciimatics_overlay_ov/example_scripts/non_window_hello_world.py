"""
File in charge of acting as the main script of the library when it is called as a standalone
"""
from random import randint
from time import sleep
import asciimatics.widgets as WIG
from asciimatics.event import Event
from asciimatics.exceptions import NextScene
from asciimatics_overlay_ov import AsciiMaticsOverlayMain
from asciimatics_overlay_ov.widgets import FrameNodes


class NonWindowHelloWorld(WIG.Frame, AsciiMaticsOverlayMain, FrameNodes):
    """ The class in charge of displaying a filebrowser in a window """

    def __init__(self, screen):
        super(NonWindowHelloWorld, self).__init__(
            screen,
            screen.height,
            screen.width,
            has_border=True,
            title="TTY Hello World"
        )
        self.frame_node = FrameNodes()
        self.quotes = [
            "Carpe Diem",
            "Think big",
            "Dream big",
            "Love wins",
            "Be yourself",
            "Stay curious",
            "Never give up",
            "Less is more",
            "Do it now",
            "Live fully",
            "Stay positive",
            "Learn, adapt, overcome",
            "Embrace the journey",
            "Create, not consume",
            "Seek inner peace",
            "Follow your heart",
            "Chase your dreams",
            "Keep it simple",
            "Stay humble",
            "Work hard, play hard",
            "Find your passion",
            "Love unconditionally",
            "Hope never dies",
            "Time heals all",
            "Believe in yourself",
            "Spread love, not hate",
            "Make it happen",
            "Smile, be happy"
        ]
        self.event = Event()
        self.amom = AsciiMaticsOverlayMain(self.event, screen)
        self.amom.update_initial_pointers(self.event, screen)
        self.main_loop = True
        self.colour_data = self._get_colour_data()
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
                text="Here is a tty Hello World !",
                height=1,
                align=self.frame_node.label_center,
                name=None
            )
        )
        self.layout.add_widget(
            self.add_label(
                text="Warning: Risk of epilepsy, proceed at your own risk!",
                height=1,
                align=self.frame_node.label_center,
                name=None
            )
        )
        self.layout.add_widget(
            self.add_label(
                text="Press Q to exit !",
                height=1,
                align=self.frame_node.label_center,
                name=None
            )
        )
        self.layout.add_widget(
            self.add_button(
                text="Start animation",
                on_click=self._funk_up_the_display,
                name="start_button"
            ),
            0
        )
        self.layout.add_widget(
            self.add_button(
                text="Exit",
                on_click=self._goodbye_message,
                name="exit_button"
            ),
            0
        )

    def _get_colour_data(self) -> list:
        """ Get a set of available colours for automating"""
        colour_options = list(self.amom.human_bind)
        colour_options_length = len(colour_options) - 1
        return colour_options, colour_options_length

    def _get_random_colour(self) -> str:
        """ Get a random colour from the available ones """
        colour_options, colour_options_length = self.colour_data
        choice = randint(0, colour_options_length)
        return colour_options[choice]

    def _make_transparent(self) -> bool:
        """ Check if the colour is transparent """
        choice = randint(0, 10) % 2
        return bool(choice)

    def _is_quit_key_pressed(self) -> bool:
        """ Check if the key to stop the animation was pressed """
        pressed_key = self.amom.get_event_key_code()
        if self.amom.is_it_this_key(pressed_key, "q") is True or self.amom.is_it_this_key(pressed_key, "Q") is True:
            return True
        return False

    def _goodbye_message(self) -> int:
        line_top = "                                "
        line_center = "  Goodbye, see you next time !  "
        line_bottom = "                                "
        center_screen_x = self.amom.get_screen_center_x()
        center_screen_y = self.amom.get_screen_center_y()
        center_colour_fg = self.amom.pick_colour(
            self._get_random_colour()
        )
        center_colour_bg = self.amom.pick_colour(
            self._get_random_colour()
        )
        if center_colour_fg == center_colour_bg:
            if center_colour_fg == 0:
                center_colour_bg = 1
            else:
                center_colour_bg -= 1
        padding_top = 4
        padding_bottom = 4
        for i in range(1, padding_top+1):
            self.amom.mvprintw_colour(
                line_top,
                center_screen_x,
                center_screen_y-i,
                center_colour_fg,
                0,
                center_colour_bg,
                False
            )
        self.amom.mvprintw_colour(
            line_center,
            center_screen_x,
            center_screen_y,
            center_colour_fg,
            0,
            center_colour_bg,
            False
        )
        for i in range(1, padding_bottom+1):
            self.amom.mvprintw_colour(
                line_bottom,
                center_screen_x,
                center_screen_y+i,
                center_colour_fg,
                0,
                center_colour_bg,
                False
            )
        self.amom.my_asciimatics_overlay_main_screen.refresh()
        sleep(2)
        self._exit()

    def _funk_up_the_display(self) -> int:
        """ Update the display with funny text """
        screen_width = self.amom.get_screen_width()
        screen_height = self.amom.get_screen_height()-1
        quotes_length = len(self.quotes)-1
        while self.main_loop is True:
            x = randint(0, screen_width)
            y = randint(0, screen_height)
            random_foreground = self.amom.pick_colour(
                self._get_random_colour()
            )
            random_background = self.amom.pick_colour(
                self._get_random_colour()
            )
            random_content = self.quotes[randint(0, quotes_length)]
            random_transparent = self._make_transparent()
            self.amom.mvprintw_colour(
                random_content,
                x,
                y,
                random_foreground,
                0,
                random_background,
                random_transparent
            )
            if self._is_quit_key_pressed() is True:
                self._goodbye_message()
                break
            self.amom.my_asciimatics_overlay_main_screen.refresh()

    def _exit(self) -> None:
        raise NextScene("Main")
