from entity import Entity

BASE_STATS = {
    "id": "player",
    "weapons": ["wooden_stick"]
}

class Player(Entity):
    def __init__(self):
        super().__init__(BASE_STATS)

    def set_name(self,name):
        self.display_name = name