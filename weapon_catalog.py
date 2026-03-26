from weapon import Weapon
from assets import get_resource
import os

class WeaponCatalog:
    def __init__(self):
        self.weapons = {}
        for entry in os.scandir("./res/weapons"):
            weapon = Weapon(get_resource(f"weapons/{entry.name}"))
            self.weapons[weapon.id] = weapon

    def format(self, weapon_ids: list):
        return "[" + ",".join(str(self.weapons[id]) for id in weapon_ids) + "]"

weapon_catalog = WeaponCatalog()