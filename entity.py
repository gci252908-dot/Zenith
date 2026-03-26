from weapon_catalog import weapon_catalog

BASE_HEALTH = 20
BASE_STRENGTH = 1

class Entity:
    def __init__(self,stats: dict):
        self.display_name = stats.get("display","unknown")
        self.id = stats.get("id","unknown")
        self.health = stats.get("health",BASE_HEALTH)
        self.weapons = stats.get("weapons",[])
        self.strength = stats.get("strength",BASE_STRENGTH)
        self.currency = 0

        self.alive = self.health > 0

    def dealt_damage(self):
        """ Returns dealt damage from the entity based on its strength and held weapon. """
        return 0

    def damage(self,amount: int | float):
        """ Damages the entity by a given amount. """
        if not isinstance(amount, (int,float)):
            raise ValueError("Attempt to deal damage by a non-numeric value!")
        self.health -= amount
        self.alive = self.health > 0

    def __str__(self) -> str:
        stats = ""
        stats += f"/c#66DEFFName: {self.display_name}\n"
        stats += f"/cREDHealth: {self.health}\n"
        stats += f"/cGREENShmeckles: {self.currency}\n"
        stats += f"Weapons: {weapon_catalog.format(self.weapons)}\n"
        return stats