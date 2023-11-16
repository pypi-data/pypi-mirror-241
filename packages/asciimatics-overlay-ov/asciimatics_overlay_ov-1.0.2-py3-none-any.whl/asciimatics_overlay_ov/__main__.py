"""
File in charge of acting as the main script of the library when it is called as a standalone
"""
from time import sleep
from random import randint
from asciimatics.event import Event
from asciimatics.screen import Screen
from asciimatics_overlay_ov import AsciimaticsOverlay
import example_scripts as ES


print("Hello world")

if __name__ == "__main__":
    SUCCESS = 0
    ERROR = 1
    SCREEN = None
    LAST_SCENE = None
    WII = ES.Main(
        success=SUCCESS,
        error=ERROR,
        screen=SCREEN,
        last_scene=LAST_SCENE
    )
    try:
        STATUS = WII.run()
    except Exception as err:
        print(f"Error: {err}")
        exit(ERROR)
