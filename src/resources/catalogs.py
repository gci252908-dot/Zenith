from src.world.weapon import Weapon
from src.world.zone import parse
import os
import json


def get_resource(relative_path: str) -> dict:
    """ Grabs a JSON resource from the res/ folder """
    with open(f"res/{relative_path}") as f:
        return json.load(f)

class WeaponCatalog:
    """ A catalog of weapons that exist in the game """
    def __init__(self):
        self.weapons = {}
        for entry in os.scandir("./res/weapons"):
            weapon = Weapon(get_resource(f"weapons/{entry.name}"))
            self.weapons[weapon.id] = weapon

    def format(self, weapon_ids: list):
        """ Formats a list of weapons for printing """
        return "[" + ",".join(str(self.weapons[id]) for id in weapon_ids) + "]"

class ZoneCatalog:
    def __init__(self):
        self.zones = {}
        for entry in os.scandir("./res/zones"):
            zone = parse(get_resource(f"zones/{entry.name}"))
            self.zones[zone.id.lower()] = zone

weapon_catalog = WeaponCatalog()
zone_catalog = ZoneCatalog()