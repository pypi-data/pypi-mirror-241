"""
File in charge of displaying content on the screen
"""

from asciimatics.screen import Screen as SC


class Display:
    """ Class in charge of displaying content on the screen """

    def __init__(self, screen: SC) -> None:
        self.my_asciimatics_overlay_main_screen = screen

    def mvprintw(self, text: str, posx: int, posy: int, width: int = 0, parent_screen: SC = None) -> None:
        """ Display a string at a specific location """
        if parent_screen is None:
            self.my_asciimatics_overlay_main_screen.print_at(
                text,
                posx,
                posy,
                width
            )
        else:
            parent_screen.print_at(
                text,
                posx,
                posy,
                width
            )

    def mvprintw_colour(self, text: str, posx: int, posy: int, colour: int = 7, attr: int = 0, bg: int = 0, transparent: bool = False, parent_screen: SC = None) -> None:
        """ Display a string at a specific location with a specific colour """
        if parent_screen is None:
            self.my_asciimatics_overlay_main_screen.print_at(
                text,
                posx,
                posy,
                colour,
                attr,
                bg,
                transparent
            )
        else:
            parent_screen.print_at(
                text,
                posx,
                posy,
                colour,
                attr,
                bg,
                transparent
            )

    def print_array(self, array: list, seperator: str, posx: int, posy: int, colour: int = 7, attr: int = 0, bg: int = 0, transparent: bool = False, parent_screen: SC = None) -> None:
        """ Display an array at a specific location with a specific colour """
        if parent_screen is None:
            self.my_asciimatics_overlay_main_screen.print_at(
                seperator.join(array),
                posx,
                posy,
                colour,
                attr,
                bg,
                transparent
            )
        else:
            parent_screen.print_at(
                seperator.join(array),
                posx,
                posy,
                colour,
                attr,
                bg,
                transparent
            )

    def print_array_colour(self, array: list[dict], seperator: str, posx: int, posy: int, colour: int = 7, attr: int = 0, bg: int = 0, transparent: bool = False, parent_screen: SC = None) -> None:
        """ Display an array at a specific location with a specific colour """
        display_function = None
        if parent_screen is None:
            display_function = self.my_asciimatics_overlay_main_screen.print_at
        else:
            display_function = parent_screen.print_at
        default_list = {
            "seperator": seperator,
            "posx": posx,
            "posy": posy,
            "colour": colour,
            "attr": attr,
            "bg": bg,
            "transparent": transparent
        }
        for index, item in enumerate(array):
            for key, value in default_list.items():
                if hasattr(item, key) is False and key == "posx":
                    item[key] = posx + index
                if hasattr(item, key) is False:
                    item[key] = value
            display_function(
                item["text"],
                item["posx"],
                item["posy"],
                item["colour"],
                item["attr"],
                item["bg"],
                item["transparent"]
            )

    def print_double_array(self, array: list[list], seperator: str, posx: int, posy: int, colour: int = 7, attr: int = 0, bg: int = 0, transparent: bool = False, parent_screen: SC = None) -> None:
        """ Display a double array at a specific location with a specific colour """
        display_function = None
        if parent_screen is None:
            display_function = self.my_asciimatics_overlay_main_screen.print_at
        else:
            display_function = parent_screen.print_at

        result = ""
        for i in array:
            result += seperator.join(i)
            result += "\n"
        display_function(
            result,
            posx,
            posy,
            colour,
            attr,
            bg,
            transparent
        )

    def print_double_array_colour(self, array: list[list[dict]], seperator: str, posx: int, posy: int, colour: int = 7, attr: int = 0, bg: int = 0, transparent: bool = False, parent_screen: SC = None) -> None:
        """ Display a double array at a specific location with a specific colour """
        for index, item in enumerate(array):
            self.print_array_colour(
                item,
                seperator,
                posx,
                posy+index,
                colour,
                attr,
                bg,
                transparent,
                parent_screen
            )

    def print_array_cloud_points(self, array: list[dict], iposx: int = 0, iposy: int = 0, colour: int = 7, attr: int = 0, bg: int = 0, transparent: bool = False, parent_screen: SC = None) -> None:
        """ Display a double array at a specific location with a specific colour """
        display_function = None
        if parent_screen is None:
            display_function = self.my_asciimatics_overlay_main_screen.print_at
        else:
            display_function = parent_screen.print_at
        new_posx = 0
        new_posy = 0
        new_character = ""
        new_colour = colour
        new_attr = attr
        new_bg = bg
        new_transparent = transparent
        prev_y = 0
        for line, character in enumerate(array):
            if "posx" in character:
                new_posx = character["posx"]+iposx
            else:
                new_posx = line + iposx
            if "posy" in character:
                new_posy = character["posy"] + iposy
                prev_y = character["posy"]
            else:
                new_posy = prev_y + iposy
            if "character" in character:
                new_character = character["character"]
            else:
                new_character = " "
            if "colour" in character:
                new_colour = character["colour"]
            else:
                new_colour = colour
            if "attr" in character:
                new_attr = character["attr"]
            else:
                new_attr = attr
            if "bg" in character:
                new_bg = character["bg"]
            else:
                new_bg = bg
            if "transparent" in character:
                new_transparent = character["transparent"]
            else:
                new_transparent = transparent
            display_function(
                new_character,
                new_posx,
                new_posy,
                new_colour,
                new_attr,
                new_bg,
                new_transparent
            )

    def print_double_array_cloud_points(self, array: list[list[dict]], iposx: int = 0, iposy: int = 0, colour: int = 7, attr: int = 0, bg: int = 0, transparent: bool = False, parent_screen: SC = None) -> None:
        """ Display a double array at a specific location with a specific colour """
        display_function = None
        if parent_screen is None:
            display_function = self.my_asciimatics_overlay_main_screen.print_at
        else:
            display_function = parent_screen.print_at
        new_posx = 0
        new_posy = 0
        new_character = ""
        new_colour = colour
        new_attr = attr
        new_bg = bg
        new_transparent = transparent
        for index, item in enumerate(array):
            for line, character in enumerate(item):
                if "posx" in character:
                    new_posx = character["posx"]+iposx
                else:
                    new_posx = line + iposx
                if "posy" in character:
                    new_posy = character["posy"] + iposy
                else:
                    new_posy = index + iposy
                if "character" in character:
                    new_character = character["character"]
                else:
                    new_character = " "
                if "colour" in character:
                    new_colour = character["colour"]
                else:
                    new_colour = colour
                if "attr" in character:
                    new_attr = character["attr"]
                else:
                    new_attr = attr
                if "bg" in character:
                    new_bg = character["bg"]
                else:
                    new_bg = bg
                if "transparent" in character:
                    new_transparent = character["transparent"]
                else:
                    new_transparent = transparent
                display_function(
                    new_character,
                    new_posx,
                    new_posy,
                    new_colour,
                    new_attr,
                    new_bg,
                    new_transparent
                )

    def _print_sides_of_checker_board(self, width: int, height: int, iposx: int = 0, iposy: int = 0, seperator_character_horizontal: str = "-", seperator_character_vertical: str = "|", fg: int = 7, bg: int = 6, transparent: bool = False, add_spacing: bool = True, parent_screen: SC = None) -> None:
        """ Print the borders (and characters) for the checker board """
        print(f"In _print_sides_of_checker_board")
        alphabet = [
            "A", "B", "C", "D", "E", "F",
            "G", "H", "I", "J", "K",
            "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"
        ]
        alphabet_length = len(alphabet)-1
        current_id = alphabet[0]
        display_function = None
        print(
            f"alphabet = {alphabet}, alphabet_length = {alphabet_length}"
        )
        print(
            f"current_id = {current_id}, display_function = {display_function}"
        )
        if parent_screen is None:
            display_function = self.my_asciimatics_overlay_main_screen.print_at
        else:
            display_function = parent_screen.print_at
        x_offset = (len(str(width))+1)
        if add_spacing is True:
            x_offset *= 2
        for i in range(x_offset, (width+x_offset)):
            print(
                f"i = {i}, width = {width}, alphabet_length = {alphabet_length}")
            if i > alphabet_length:
                current_id = str(i-x_offset)[1:]
            else:
                current_id = alphabet[i-x_offset]
            display_function(
                current_id,
                i+iposx,
                iposy,
                fg,
                0,
                bg,
                transparent
            )
            display_function(
                seperator_character_horizontal,
                i+iposx,
                iposy+1,
                fg,
                0,
                bg,
                transparent
            )
            if add_spacing is True:
                display_function(
                    " ",
                    i+iposx,
                    iposy,
                    fg,
                    0,
                    bg,
                    transparent
                )
                display_function(
                    seperator_character_horizontal,
                    i+iposx,
                    iposy+1,
                    fg,
                    0,
                    bg,
                    transparent
                )
                i += 1

        y_offset = len(str(height))+1
        for i in range(y_offset, (height+y_offset)):
            print(f"i = {i}, height = {height}")
            display_function(
                i-y_offset,
                iposx,
                i+iposy,
                fg,
                0,
                bg,
                transparent
            )
            display_function(
                seperator_character_vertical,
                iposx+1,
                i+iposy,
                fg,
                0,
                bg,
                transparent
            )
        print("Out of _print_sides_of_checker_board")

    def print_checker_board(self, data_array: list[list[str, int, float]], width: int = 30, height: int = 30, iposx: int = 0, iposy: int = 0, seperator_character_vertical: str = "|", seperator_character_horizontal: str = "-", even_bg_colour: int = 7, even_fg_colour: int = 6, uneven_bg_colour: int = 6, uneven_fg_colour: int = 7, border_fg: int = 7, border_bg: int = 6, transparent_even: bool = False, transparent_uneven: bool = False, border_transparent: bool = False, attr_even: int = 0, attr_uneven: int = 0, add_spacing: bool = True, parent_screen: SC = None) -> None:
        """ Display a checker board """
        line = 0
        character = 0
        display_function = None
        has_character = True
        if len(data_array) > 0:
            has_line = True
        else:
            has_line = False
        print(f"has_line = {has_line}, has_character = {has_character}")
        current_display = ""
        if parent_screen is None:
            display_function = self.my_asciimatics_overlay_main_screen.print_at
        else:
            display_function = parent_screen.print_at
        print(f"parent_screen = {parent_screen}")
        self._print_sides_of_checker_board(
            width,
            height,
            iposx,
            iposy,
            seperator_character_horizontal,
            seperator_character_vertical,
            border_fg,
            border_bg,
            border_transparent,
            add_spacing,
            parent_screen
        )
        border_width = len(str(width))+1
        iposx += border_width
        width -= border_width
        iposy += border_width
        height -= border_width
        line = 0
        character = 0
        print(f"border_width = {border_width}, iposx = {iposx}")
        print(f"iposy = {iposy}, width = {width}, height = {height}")
        while line < height:
            character = 0
            if has_line is True and len(data_array[line]) == 0:
                has_character = False
            else:
                has_character = True
            print(
                f"line = {line}, character = {character}, height = {height}, has_character = {has_character}")
            while character < width:
                if has_character is False or has_line is False or len(current_display[line]) == 0:
                    current_display = "."
                else:
                    current_display = data_array[line][character][0]
                print(
                    f"line = {line}, character = {character}, height = {height}, has_character = {has_character}")
                if character % 2 == 0:
                    display_function(
                        current_display,
                        line*width+iposx,
                        character*height+iposy,
                        even_fg_colour,
                        attr_even,
                        even_bg_colour,
                        transparent_even
                    )
                else:
                    display_function(
                        current_display,
                        line*width+iposx,
                        character*height+iposy,
                        uneven_fg_colour,
                        attr_uneven,
                        uneven_bg_colour,
                        transparent_uneven
                    )
                character += 1
            line += 1
