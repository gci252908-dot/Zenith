from pyterminal import PyTerminal
from src.resources.assets import LOGO_ART
from src.world.game import Game

class Zenith:
    def __init__(self):        
        self.engine = PyTerminal(init_func=self.init, end_func=self.end)
        self.game = Game()

    def init(self, engine):
        engine.get_input(LOGO_ART + "\n\nPress enter to play...") # Hacky but works :)

    def update(self, _delta):
        """ Moves over to the next update of the game loop """
        self.game.reset_frame()
        self.game.update(self.engine,_delta)

    def draw(self, delta):
        """ Draw the game's frame. """
        self.engine.draw(self.game.frame)
        #self.engine.quit()

    def end(self):
        """End of game message."""
        #self.engine.draw("/cYELLOWExample ended")
        #self.engine.draw("/cGREENThanks for checking it out")

    def run_game(self):
        """Start the game loop."""
        self.engine.run_loop(self.update, self.draw, fps=5)
game = Zenith()
game.run_game()