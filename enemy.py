class Enemy:
    def __init__(self,stats: dict):
        self.display = stats["display"]
        self.id = stats["id"]
        self.health = stats["health"]
        self.weapons = stats["weapons"]
        self.strength = stats["strength"]

        self.alive = self.health > 0

    def dealt_damage(self):
        """ Returns dealt damage from the enemy based on its strength and held weapon. """
        return 0

    def damage(self,amount: int | float):
        """ Damages the enemy by a given amount. """
        if not isinstance(amount, (int,float)):
            raise ValueError("Attempt to deal damage by a non-numeric value!")
        self.health -= amount
        self.alive = self.health > 0