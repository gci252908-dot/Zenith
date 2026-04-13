from random import randint
from src.entities.entity import Entity

class Enemy(Entity):
    def __init__(self,stats: dict):
        super().__init__(stats)

        if stats["currency"]:
            currency = stats["currency"]
            self.currency = randint(currency[0],currency[1])