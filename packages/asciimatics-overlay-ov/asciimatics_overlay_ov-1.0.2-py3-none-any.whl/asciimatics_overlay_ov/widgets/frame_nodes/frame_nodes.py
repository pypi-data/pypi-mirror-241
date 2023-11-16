from datetime import datetime
import asciimatics.widgets as WIG
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.widgets import Frame
from asciimatics_overlay_ov.colour_class import Colour


class FrameNodes:
    """ The class in charge of containing functions that will ease the implementation process """

    def __init__(self, success: int = 0, error: int = 84) -> None:
        self.label_left = "<"
        self.label_right = ">"
        self.label_center = "^"
        self.success = success
        self.error = error

    def add_listbox(self, input_data: list[tuple[str, int]], on_change: object, on_select: object, height: int = WIG.Widget.FILL_FRAME, name: str = "my_listbox", center: bool = False, scrollbar: bool = True, label: str = None) -> WIG.ListBox:
        """
        Add a listbox to the layout
        :param input_data: The options for each row in the widget.
        :param on_change: Optional function to call when selection changes.
        :param on_select: Optional function to call when the user actually selects an entry from
        :param height: The required number of input lines for this ListBox.
        :param name: The name for the ListBox.
        :param centre: Whether to centre the selected line in the list.
        :param scrollbar: Whether to add a scrollbar or not to the box
        :param label: An optional label for the widget.
        :return: A new ListBox instance.

        The options are a list of tuples, where the first value is the string to be displayed to the user and the second is an interval value to identify the entry to the program.
        For example:
            input_data=[("First option", 1), ("Second option", 2)]
        """
        return WIG.ListBox(
            height=height,
            options=input_data,
            centre=center,
            name=name,
            add_scroll_bar=scrollbar,
            on_change=on_change,
            on_select=on_select,
            label=label
        )

    def add_textbox(self, height: int = 1, label: str = "Place Question", name: str = None, as_string: bool = True, line_wrap: bool = True, on_change: object = None, readonly: bool = False) -> WIG.TextBox:
        """
        Add a textbox to the layout
        :param height: The required number of input lines for this TextBox.
        :param label: An optional label for the widget.
        :param name: The name for the TextBox.
        :param as_string: Use string with newline separator instead of a list
            for the value of this widget.
        :param line_wrap: Whether to wrap at the end of the line.
        :param on_change: Optional function to call when text changes.
        :param readonly: Whether the widget prevents user input to change values. Default is False.
        :return: A TextBox instance
        """
        return WIG.TextBox(
            height=height,
            label=label,
            name=name,
            as_string=as_string,
            line_wrap=line_wrap,
            on_change=on_change,
            readonly=readonly
        )

    def add_input(self, label: str = "Hello World !", name: str = None, on_change: object = None, hide_char: str = None, max_length: int = None, readonly: bool = False) -> WIG.Text:
        """
        Add an input to the layout
        :param label: An optional label for the widget.
        :param name: The name for the widget.
        :param on_change: Optional function to call when text changes.
        :param hide_char: Character to use instead of what the user types - e.g. to hide passwords.
        :param max_length: Optional maximum length of the field. If set, the widget will limit
            data entry to this length.
        :param readonly: Whether the widget prevents user input to change values. Default is False.
        :return: A new Text instance.
        """
        return WIG.Text(
            label=label,
            name=name,
            on_change=on_change,
            hide_char=hide_char,
            max_length=max_length,
            readonly=readonly
        )

    def add_button(self, text: str, on_click: object, label: str = None, box: bool = True, name: str = None) -> WIG.Button:
        """
        Add a button to the layout
        :param text: The text for the button.
        :param on_click: The function to invoke when the button is clicked.
        :param label: An optional label for the widget.
        :param box: Whether to wrap the text with chevrons.
        :param name: The name of this widget.
        :return: A new Button object.
        """
        return WIG.Button(
            text=text,
            on_click=on_click,
            label=label,
            add_box=box,
            name=name
        )

    def add_label(self, text: str, height: int = 1, align: str = "<", name: str = None) -> WIG.Label:
        """
        Add a label to the layout 
        :param label: The text to be displayed for the Label.
        :param height: Optional height for the label. Defaults to 1 line.
        :param align: Optional alignment for the Label. Defaults to left aligned.
            Options are "<" = left, ">" = right and "^" = centre
        :param name: The name of this widget.
        :return: a Label instance
        """
        return WIG.Label(
            label=text,
            height=height,
            align=align,
            name=name
        )

    def add_checkbox(self, text: str = "Description", label: str = None, name: str = None, on_change: object = None) -> WIG.CheckBox:
        """
        Add a checkbox to the interface
        :param text: The text to explain this specific field to the user.
        :param label: An optional label for the widget.
        :param name: The internal name for the widget.
        :param on_change: Optional function to call when text changes.
        :return: a CheckBox instance
        """
        return WIG.CheckBox(
            text=text,
            label=label,
            name=name,
            on_change=on_change
        )

    def add_datepicker(self, label: str = None, name: str = "Pick a date", year_range: str = None, on_change: object = None) -> WIG.DatePicker:
        """
        Add a datepicker to the interface
        :param label: An optional label for the widget.
        :param name: The internal name for the widget.
        :param year_range: Optional range of years to display. Defaults to 10 years either side of the current year.
        :param on_change: Optional function to call when text changes.
        :return: a DatePicker instance
        """
        return WIG.DatePicker(
            label=label,
            name=name,
            year_range=year_range,
            on_change=on_change
        )

    def add_divider(self, draw_line: bool = True, height: int = 1, line_char: str = None) -> WIG.Divider:
        """
        Add a divider to the layout
        :param draw_line: Whether to draw a line in the centre of the gap.
        :param height: The required vertical gap.
        :param line_char: Optional character to use for drawing the line.
        :return: a Divider instance
        """
        return WIG.Divider(
            draw_line=draw_line,
            height=height,
            line_char=line_char
        )

    def add_dropdownlist(self, options: list[tuple[str, int]], label: str = None, name: str = None, on_change: object = None, fit: bool = False) -> WIG.DropdownList:
        """
        Add a dropdown list
        :param options: The options for each row in the widget.
        :param label: An optional label for the widget.
        :param name: The name for the ListBox.
        :param on_change: Optional function to call when selection changes.
        :param fit: Shrink width of dropdown to fit the width of options. Default False.
        :return: a DropdownList instance
        The options are a list of tuples, where the first value is the string to be displayed to the user and the second is an interval value to identify the entry to the program.
        For example:
            options=[("First option", 1), ("Second option", 2)]
        """
        return WIG.DropdownList(
            options=options,
            label=label,
            name=name,
            on_change=on_change,
            fit=fit
        )

    def add_filebrowser(self, height: int = 10, root: str = ".", name: str = "File browser", on_select: object = None, on_change: object = None, file_filter: str = ".*.txt$") -> WIG.FileBrowser:
        """
        Add a file browser to the layout
        :param height: The desired height for this widget.
        :param root: The starting root directory to display in the widget.
        :param name: The name of this widget.
        :param on_select: Optional function that gets called when user selects a file (by pressing enter or double-clicking).
        :param on_change: Optional function that gets called on any movement of the selection.
        :param file_filter: Optional RegEx string that can be passed in to filter the files to be displayed.

        Most people will want to use a filter to find files with a particular extension.
        In this case, you must use a regex that matches to the end of the line - e.g. use ".*.txt$" to find files ending with ".txt".
        This ensures that you don't accidentally pick up files containing the filter.
        :return: a FileBrowser instance
        """
        return WIG.FileBrowser(
            height=height,
            root=root,
            name=name,
            on_select=on_select,
            on_change=on_change,
            file_filter=file_filter
        )

    def add_frame(self, screen: Screen, height: int = 10, width: int = 10, data: any = None, on_load: object = None, has_border: bool = True, hover_focus: bool = False, name: str = None, title: str = "Frame", posx: int = 0, posy: int = 0, has_shadow: bool = False, reduce_cpu: bool = False, is_modal: bool = False, can_scroll: bool = True) -> WIG.Frame:
        """
        Add a frame to the layout
        :param screen: The Screen that owns this Frame.
        :param height: The desired height of the Frame.
        :param width: The desired width of the Frame.
        :param data: optional data dict to initialize any widgets in the frame.
        :param on_load: optional function to call whenever the Frame reloads.
        :param has_border: Whether the frame has a border box. Defaults to True.
        :param hover_focus: Whether hovering a mouse over a widget (i.e. mouse move events) should change the input focus. Defaults to false.
        :param name: Optional name to identify this Frame. This is used to reset data as needed from on old copy after the screen resizes.
        :param title: Optional title to display if has_border is True.
        :param posx: Optional x position for the top left corner of the Frame.
        :param posy: Optional y position for the top left corner of the Frame.
        :param has_shadow: Optional flag to indicate if this Frame should have a shadow when drawn.
        :param reduce_cpu: Whether to minimize CPU usage (for use on low spec systems).
        :param is_modal: Whether this Frame is "modal" - i.e. will stop all other Effects from receiving input events.
        :param can_scroll: Whether a scrollbar should be available on the border, or not.
        :return: a Frame instance
        """
        return WIG.Frame(
            screen=screen,
            height=height,
            width=width,
            data=data,
            on_load=on_load,
            has_border=has_border,
            hover_focus=hover_focus,
            name=name,
            title=title,
            x=posx,
            y=posy,
            has_shadow=has_shadow,
            reduce_cpu=reduce_cpu,
            is_modal=is_modal,
            can_scroll=can_scroll
        )

    def add_layout(self, columns: list[int], fill_frame: bool = True) -> WIG.Layout:
        """
        Add a layout to the frame
        :param columns: A list of numbers specifying the width of each column in this layout.
        :param fill_frame: Whether this Layout should attempt to fill the rest of the Frame.
        :return: a Layout instance
        Defaults to False.
        The Layout will automatically normalize the units used for the columns, e.g. converting [2, 6, 2] to [20%, 60%, 20%] of the available canvas.
        """
        return WIG.Layout(
            columns=columns,
            fill_frame=fill_frame
        )

    def add_multicolumnlistbox(self, options: list[tuple[str, int]], height: int = 10, columns: list[int] = None, titles: list[str] = None, label: str = None, name: str = None, add_scroll_bar: bool = False, on_change: object = None, on_select: object = None, space_delimiter: str = " ") -> WIG.MultiColumnListBox:
        """
        Add a multi column listbox to the layout
        :param options: The options for each row in the widget.
        :param height: The required number of input lines for this ListBox.
        :param columns: A list of widths and alignments for each column.
        :param titles: Optional list of titles for each column. Must match the length of columns.
        :param label: An optional label for the widget.
        :param name: The name for the ListBox.
        :param add_scroll_bar: Whether to add optional scrollbar for large lists.
        :param parser: Optional parser to colour text.
        :param on_change: Optional function to call when selection changes.
        :param on_select: Optional function to call when the user actually selects an entry from
        :param space_delimiter: Optional parameter to define the delimiter between columns. (The default value is blank space.)
        :return: a MultiColumnListBox instance

        The columns parameter is a list of integers or strings. If it is an integer, this is the absolute width of the column in characters. If it is a string, it must be of the format "[<align>]<width>[%]" where:
        <align> is the alignment string ("<" = left, ">" = right, "^" = centre)
        <width> is the width in characters
        % is an optional qualifier that says the number is a percentage of the width of the widget.
        Column widths need to encompass any space required between columns, so for example, if your column is 5 characters, allow 6 for an extra space at the end. It is not possible to do this when you have a right-justified column next to a left-justified column, so this widget will automatically space them for you.

        An integer value of 0 is interpreted to be use whatever space is left available after the rest of the columns have been calculated. There must be only one of these columns.
        The number of columns is for this widget is determined from the number of entries in the columns parameter. The options list is then a list of tuples of the form ([val1, val2, ... , valn], index). For example, this data provides 2 rows for a 3 column widget:
            options=[(["One", "row", "here"], 1), (["Second", "row", "here"], 2)]
        The options list may be None and then can be set later using the options property on this widget.
        """
        return WIG.MultiColumnListBox(
            height=height,
            columns=columns,
            options=options,
            titles=titles,
            label=label,
            name=name,
            add_scroll_bar=add_scroll_bar,
            on_change=on_change,
            on_select=on_select,
            space_delimiter=space_delimiter
        )

    def add_radiobuttons(self, options: list[tuple[str, int]], label: str = None, name: str = None, on_change: object = None) -> WIG.RadioButtons:
        """
        Add a radio button to the layout
        :param options: The options for each row in the widget.
        :param label: An optional label for the widget.
        :param name: The name for the ListBox.
        :param on_change: Optional function to call when selection changes.
        :param readonly: Whether the widget prevents user input to change values. Default is False.
        :return: a RadioButtons instance
        """
        return WIG.RadioButtons(
            options=options,
            label=label,
            name=name,
            on_change=on_change
        )

    def add_popup_dialog(self, screen: Screen, text: str = "Sample text", buttons: list[str] = None, on_close: object = None, has_shadow: bool = False, theme: str = "Warning") -> WIG.PopUpDialog:
        """
        Add a PopUp dialog to your window
        :param screen: The Screen that owns this dialog.
        :param text: The message text to display.
        :param buttons: A list of button names to display. This may be an empty list.
        :param on_close: Optional function to invoke on exit.
        :param has_shadow: optional flag to specify if dialog should have a shadow when drawn.
        :param theme: optional colour theme for this pop-up. Defaults to the warning colours.

        The theme options are:
            * "default"
            * "monochrome"
            * "green"
            * "bright"
            * "tlj256"
            * "warning"

        The on_close method (if specified) will be called with one integer parameter that corresponds to the index of the button passed in the array of available buttons.

        Note that on_close must be a static method to work across screen resizing. Either it is static (and so the dialog will be cloned) or it is not (and the dialog will disappear when the screen is resized).
        :return: a PopUpDialog instance
        """
        return WIG.PopUpDialog(
            screen=screen,
            text=text,
            buttons=buttons,
            on_close=on_close,
            has_shadow=has_shadow,
            theme=theme
        )

    def add_popup_menu(self, screen: Screen, menu_items: list[tuple[str, object]], posx: int = 0, posy: int = 0) -> WIG.PopupMenu:
        """
        Add a PopUp menu to your window
        :param screen: The Screen being used for this pop-up.
        :param menu_items: a list of items to be displayed in the menu.
        :param x: The X coordinate for the desired pop-up.
        :param y: The Y coordinate for the desired pop-up.

        The menu_items parameter is a list of 2-tuples, which define the text to be displayed in the menu and the function to call when that menu item is clicked.
        For example:
            menu_items = [("Open", file_open), ("Save", file_save), ("Close", file_close)]
        :return: a PopUpMenu instance
        """
        return WIG.PopupMenu(
            screen=screen,
            menu_items=menu_items,
            x=posx,
            y=posy
        )

    def add_timepicker(self, label: str = "Time picker", name: str = None, seconds: bool = False, on_change: object = None) -> WIG.TimePicker:
        """
        Add a time picker to your window
        :param label: An optional label for the widget.
        :param name: The name for the widget.
        :param seconds: Whether to include selection of seconds or not.
        :param on_change: Optional function to call when the selected time changes.
        :return: a TimePicker instance
        """
        return WIG.TimePicker(
            label=label,
            name=name,
            seconds=seconds,
            on_change=on_change
        )

    def add_verticaldivider(self, height: int = WIG.Widget.FILL_COLUMN) -> WIG.VerticalDivider:
        """
        Add a vertical divider to your window
        :param height: The required height of the divider.
        :return: a VerticalDivider instance
        """
        return WIG.VerticalDivider(height=height)

    # def add_widget(self, name: str = None, tab_stop: bool = True, disabled: bool = False, on_focus: object = None, on_blur: object = None) -> None:
    #     """
    #     Add a widget to the layout
    #     :param name: The name of this Widget.
    #     :param tab_stop: Whether this widget should take focus or not when tabbing around the Frame.
    #     :param disabled: Whether this Widget should be disabled or not.
    #     :param on_focus: Optional callback whenever this widget gets the focus.
    #     :param on_blur: Optional callback whenever this widget loses the focus.
    #     :return: a Widget instance
    #     """
    #     return WIG.Widget(
    #         name=name,
    #         tab_stop=tab_stop,
    #         disabled=disabled,
    #         on_focus=on_focus,
    #         on_blur=on_blur
    #     )

    def convert_datetime_to_timepicker(self, datetime_time: datetime.time, include_seconds: bool = True) -> str:
        """ Convert the datetime element to the timepicker format """
        if include_seconds is True:
            return datetime_time.strftime("%H:%M:%S")
        else:
            return datetime_time.strftime("%H:%M")

    def convert_datetime_to_datepicker(self, datetime_date: datetime.date) -> str:
        """ Convert the datetime element to the datepicker format """
        return datetime_date.strftime("%d/%b/%Y")

    def change_screen_background(self, screen: Screen, bg: int = 0) -> None:
        """
        Change the background colour of a scene
        :param screen: The Screen being used for the Scene.
        :param bg: Optional colour for the background.
        """
        WIG.Background(
            screen=screen,
            bg=bg
        )

    def _tmp(self) -> None:
        print(dir(WIG))

    def get_text_input(self, text_box: object) -> str or int:
        """
        Get the text from a text box
        :param text_box: The text box to get the text from
        :return: The text from the text box
        """
        if text_box is None:
            print(
                "get_text_input: 'text_box' cannot be equal to 'None'"
            )
            return self.error
        if hasattr(text_box, "_value") is True:
            return text_box._value
        if hasattr(text_box, "value") is True:
            return text_box.value

        print(
            "get_text_input: 'text_box' does not have the 'value' attribute"
        )
        return self.error

    def get_widget_value(self, widget: object) -> str or int:
        """
        Get the value from a widget
        :param widget: The widget to get the value from
        :return: The value from the widget
        """
        if widget is None:
            print(
                "get_widget_input: 'widget' cannot be equal to 'None'"
            )
            return self.error
        if hasattr(widget, "value") is True:
            return widget.value
        print(
            "get_widget_input: 'widget' does not have the 'value' attribute"
        )
        return self.error

    def get_widget_value_by_name(self, your_self: Frame, widget_name: str) -> str or int:
        """
        Get the value of a widget
        :param widget_name: The name of the widget to get the value from
        :return: The value of the widget
        """
        if widget_name is None:
            print(
                "get_widget_value: 'widget_name' cannot be equal to 'None'"
            )
            return self.error
        target_widget = your_self.find_widget(widget_name)
        if hasattr(target_widget, "value") is True:
            return target_widget.value
        print(
            "get_widget_value: 'widget_name' does not have the 'value' attribute"
        )
        return self.error

    def apply_text_to_display(self, label: object, text: str = "sample text") -> int:
        """
        Apply text to a label
        :param label: The label to apply the text to
        :param text: The text to apply to the label
        :return: 0 if success, 1 if error (these are based on the self.success and self.error of the class)
        """
        if label is None:
            print(
                "apply_text_to_display: 'label' cannot be equal to 'None'"
            )
            return self.error
        if isinstance(text, (int, str, float, object)) is False:
            print(
                "apply_text_to_display: Text type has to be of type (string, int or float)"
            )
            return self.error
        if hasattr(label, "text") is True:
            if isinstance(text, (int, float)) is True:
                label.text = f"{text}"
            else:
                label.text = text
            return self.success
        print(
            "apply_text_to_display: 'label' does not have the 'text' attribute"
        )
        return self.error

    def apply_text_to_input_box(self, text_box: object, text: str) -> int:
        """
        Apply text to an input box
        :param text_box: The input box to apply the text to
        :param text: The text to apply to the input box
        :return: 0 if success, 1 if error (these are based on the self.success and self.error of the class)
        """
        if text_box is None:
            print(
                "apply_text_to_input_box: 'text_box' cannot be equal to 'None'"
            )
            return self.error
        if isinstance(text, (int, str, float, object)) is False:
            print(
                "apply_text_to_input_box: Text type has to be of type (string, int or float)"
            )
            return self.error

        if hasattr(text_box, "_value") is True:
            if isinstance(text, (int, float)) is True:
                text_box._value = f"{text}"
            else:
                text_box._value = text
            return self.success
        if hasattr(text_box, "value") is True:
            if isinstance(text, (int, float)) is True:
                text_box.value = f"{text}"
            else:
                text_box.value = text
            return self.success
        print(
            "apply_text_to_input_box: 'text_box' does not have the 'value' attribute"
        )
        return self.error

    def get_and_apply_text_to_display(self, input_source: object, output_source: object) -> int:
        """
        Get the text from an input source and apply it to an output source
        :param input_source: The input source to get the text from
        :param output_source: The output source to apply the text to
        """
        text = self.get_text_input(input_source)
        return self.apply_text_to_display(output_source, text)

    def get_and_apply_text_to_input_box(self, input_source: object, output_source: object) -> int:
        """
        Get the text from an input source and apply it to an output source
        :param input_source: The input source to get the text from
        :param output_source: The output source to apply the text to
        """
        text = self.get_text_input(input_source)
        return self.apply_text_to_input_box(output_source, text)

    def set_scene_colour(self, scene: Scene, fg: int = -1, bg: int = -1) -> int:
        """
        Set the colour of a scene
        :param scene: The scene to set the colour of
        :param fg: The foreground colour
        :param bg: The background colour
        :return: 0 if success, 1 if error (these are based on the self.success and self.error of the class)
        """
        if scene is None:
            print(
                "set_scene_colour: 'scene' cannot be equal to 'None'"
            )
            return self.error
        if isinstance(fg, int) is False:
            print(
                "set_scene_colour: 'fg' has to be of type 'int'"
            )
            return self.error
        if isinstance(bg, int) is False:
            print(
                "set_scene_colour: 'bg' has to be of type 'int'"
            )
            return self.error
        scene.set_theme(
            fg=fg,
            bg=bg
        )
        return self.success
