from enum import Enum
from assets import LOGO_ART
from player import Player
from pyterminal import PyTerminal

from catalogs import zone_catalog

class GAME_STATE(Enum):
    INITIAL_SETUP = 1
    PLAYING = 2

def choice_loop(terminal: PyTerminal, required: bool, prompt: str, empty: str):
    """ Repeatedly asks the user a prompt until they are satisfied with the answer. """
    decided = False
    result = ""
    while not decided:
        result = terminal.get_input(prompt)
        sure = terminal.get_input(f"You have selected {result}. Are you sure? ")
        if sure.lower().strip() in ["y", "yes","ye"]:
            decided = True
        if result == "":
            print(empty)
            if required: decided = False
    return result

class Game:
    """
    The main Game class for Zenith.

    - Handles per-frame game updates
    - Updates the text buffer for drawing
    """
    def __init__(self):
        self.gamestate = GAME_STATE.INITIAL_SETUP
        self.player = Player()
        self.frame = ""
        self.area = zone_catalog.zones["nightring"].areas["entry"]

    def change_state(self,gamestate) -> None:
        """ Swaps the state of the game. """
        if not isinstance(gamestate, GAME_STATE): raise ValueError("Non GAME_STATE passed to Game change_state")
        self.gamestate = gamestate

    def reset_frame(self) -> None:
        """ Resets the text frame of the game to avoid repeated draws. """
        self.frame = ""

    def add_to_frame(self,text: str) -> None:
        """ Appends text to the text frame for drawing. """
        if not type(text) is str:
            raise ValueError("Attempt to add a non-string value to add_to_frame")
        self.frame += text

    def parse_option(self,key):
        option = self.area.which_option(key)
        if option:
            self.area = self.area.get_next(key)


    def update(self, terminal: PyTerminal, _delta: float) -> None:
        """ A state-machine based update loop for the game. Fires every tick. """
        match self.gamestate:
            case GAME_STATE.INITIAL_SETUP:
                name = choice_loop(terminal,True,"Enter your name young peasant: ","Peasant, you must choose a name!")
                self.player.set_name(name)
                terminal.harsh_flush()
                self.change_state(GAME_STATE.PLAYING)
            case GAME_STATE.PLAYING:
                self.add_to_frame(str(self.player))
                self.add_to_frame(str(self.area))
                terminal.non_blocking_input("What do you choose?: ")
                if len(terminal.input_buffer) != 0:
                    self.parse_option(terminal.input_buffer[0])
                    terminal.cut_input()
