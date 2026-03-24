from enum import Enum
from assets import LOGO_ART
from player import Player

class GAME_STATE(Enum):
    INITIAL_SETUP = 1
    PLAYING = 2

def choice_loop(terminal,prompt):
    decided = False
    result = ""
    while not decided:
        result = terminal.get_input(prompt)
        sure = terminal.get_input(f"You have selected {result}. Are you sure? ")
        if sure.lower() in ["y", "yes","ye"]:
            decided = True
    return result


class Game:
    def __init__(self):
        self.gamestate = GAME_STATE.INITIAL_SETUP
        self.player = Player()

    def change_state(self,gamestate):
        if not isinstance(gamestate, GAME_STATE): raise RuntimeError("You passed a non-gamestate to change_state!")
        self.gamestate = gamestate

    def update(self,terminal,_delta):
        match self.gamestate:
            case GAME_STATE.INITIAL_SETUP:
                name = choice_loop(terminal,"Enter your name young peasant: ")
                self.player.name = name
                terminal.harsh_flush()
                self.change_state(GAME_STATE.PLAYING)
            case GAME_STATE.PLAYING:
                terminal.draw("/cRANDPoop fart!")