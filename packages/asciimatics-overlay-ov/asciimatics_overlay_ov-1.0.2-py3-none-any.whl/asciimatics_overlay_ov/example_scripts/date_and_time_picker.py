"""
File in charge of containing the date and time picker screen
"""

from datetime import datetime
from functools import partial
import asciimatics.widgets as WIG
from asciimatics.event import Event
from asciimatics.exceptions import NextScene
from asciimatics_overlay_ov import AsciiMaticsOverlayMain
from asciimatics_overlay_ov.widgets import FrameNodes


class DateAndTime(WIG.Frame, AsciiMaticsOverlayMain, FrameNodes):
    """ The class in charge of displaying date and time picker in a window """

    def __init__(self, screen):
        super(DateAndTime, self).__init__(
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
        self.layout = WIG.Layout([100])
        self.add_layout(self.layout)
        self.layout2 = None
        self.layout3 = None
        self.layout4 = None
        self.layout5 = None
        self.current_date = None
        self.current_time = None
        self.reset_data = {
            "display_time": "",
            "display_date": "",
            "time_picker": "",
            "date_picker": ""
        }
        self.place_content_on_screen()
        self.fix()

    def _add_chosen_time_line(self) -> None:
        """ Add the line informing the user of the line they chose """
        self.layout2 = WIG.Layout([60, 30])
        self.add_layout(self.layout2)
        self.layout2.add_widget(
            self.add_label(
                text="The time you have chosen:",
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
                name="time_choices"
            ),
            1
        )

    def _add_chosen_date_line(self) -> None:
        """ Add the line informing the user of the line they chose """
        self.layout3 = WIG.Layout([60, 30])
        self.add_layout(self.layout3)
        self.layout3.add_widget(
            self.add_label(
                text="The date you have chosen:",
                height=1,
                align=self.frame_node.label_left
            ),
            0
        )

        self.layout3.add_widget(
            self.add_label(
                text="",
                height=1,
                align=self.frame_node.label_center,
                name="date_choices"
            ),
            1
        )

    def create_date_range(self, starting_date: int = 1999, date_range_length: int = 10) -> list[int]:
        """ Create a range of dates """
        return list(range(starting_date, starting_date + date_range_length+1))

    def _add_date_and_time(self) -> None:
        """ Add the date and time picker """
        self.layout4 = WIG.Layout([20, 40, 40])
        self.add_layout(self.layout4)
        self.layout4.add_widget(
            self.add_label(
                text="Date:",
                height=1,
                align=self.frame_node.label_left,
                name=None

            ),
            0
        )
        self.layout4.add_widget(
            self.add_datepicker(
                label=None,
                name="date_picker",
                year_range=self.create_date_range(1800, 400),
                on_change=partial(
                    self._update_usr_input,
                    "date_picker",
                    "date_choices"
                )
            ),
            1
        )
        self.layout4.add_widget(
            self.add_timepicker(
                label=None,
                name="time_picker",
                seconds=True,
                on_change=partial(
                    self._update_usr_input,
                    "time_picker",
                    "time_choices"
                )
            ),
            2
        )

    def _add_control_buttons(self) -> None:
        """ Add the control buttons """
        self.layout5 = WIG.Layout([50, 50])
        self.add_layout(self.layout5)
        self.layout5.add_widget(
            self.add_button(
                text="Exit",
                on_click=self._exit,
                name=None
            ),
            0
        )
        self.layout5.add_widget(
            self.add_button(
                text="Reset",
                on_click=partial(
                    self._reset_layout,
                    display_widgets=[
                        "time_choices",
                        "date_choices"  # ,
                        # "time_picker",
                        # "date_picker"
                    ],
                    value=[
                        self.current_time,
                        self.current_date  # ,
                        # self.current_time,
                        # self.current_date
                    ]
                ),
                name=None
            ),
            1
        )

    def place_content_on_screen(self) -> None:
        """ Create the welcome screen """
        self.current_date = datetime.now().date()
        self.current_time = datetime.now().time()
        self.current_date = self.convert_datetime_to_datepicker(
            self.current_date
        )
        self.current_time = self.convert_datetime_to_timepicker(
            self.current_time
        )
        # print("TYPE(Current_Time)")
        # print(f"type(self.current_time) = {type(self.current_time)}")
        # print("TYPE(Current_Date)")
        # print(f"type(self.current_date) = {type(self.current_date)}")
        # self.reset_data = {
        #     "display_time": self.current_time,
        #     "display_date": self.current_date,
        #     "time_picker": self.current_time,
        #     "date_picker": self.current_date
        # }
        self.layout.add_widget(
            self.add_label(
                "Date/Time demos",
                align=self.frame_node.label_center
            ),
            0
        )
        self._add_chosen_date_line()
        self._add_chosen_time_line()
        self._add_date_and_time()
        # self.current_date = self.find_widget("date_picker")._value
        # self.current_time = self.find_widget("time_picker")._value
        # self.reset_data = {
        #     "display_time": self.current_time,
        #     "display_date": self.current_date,
        #     "time_picker": self.current_time,
        #     "date_picker": self.current_date
        # }
        self._add_control_buttons()
        # print("CURRENT_DATE")
        # print(
        #     f"self.current_date = {self.current_date}, type(self.current_date) = {type(self.current_date)}")
        # print("CURRENT_TIME")
        # print(
        #     f"self.current_time = {self.current_time}, type(self.current_time) = {type(self.current_time)}")
        # tc = self.find_widget('time_choices')
        # dc = self.find_widget('date_choices')
        # print("FIND_WIDGET(Time_Choices)")
        # print(
        #     f"self.find_widget('time_choices') = {tc}, type(self.find_widget('time_choices')) = {type(tc._value)}")
        # print("FIND_WIDGET(Date_Choices)")
        # print(
        #     f"self.find_widget('date_choices') = {dc}, type(self.find_widget('date_choices')) = {type(dc._value)}")
        # print("tc")
        # for i in dir(tc):
        #     print(f"tc.{i} = {getattr(tc, i)}")
        # print("dc")
        # for i in dir(dc):
        #     print(f"dc.{i} = {getattr(dc, i)}")
        # self._reset_layout(
        #     display_widgets=[
        #         "time_choices",
        #         "date_choices"
        #     ],
        #     value=[
        #         self.current_time,
        #         self.current_date
        #     ]
        # )

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
        #     display_widgets=[
        #         "time_choices",
        #         "date_choices",
        #         "time_picker"  # ,
        #         # "date_picker"
        #     ],
        #     value=[
        #         self.current_time,
        #         self.current_date,
        #         self.current_time,
        #         self.current_date
        #     ]
        # )
        raise NextScene("Main")
