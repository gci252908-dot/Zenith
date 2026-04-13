DEFAULT_DURABILITY = 15
DEFAULT_VALUE = 1
DEFAULT_DAMAGE = 1

class Weapon:
    def __init__(self,stats):
        self.display_name = stats.get("display","Unknown Weapon")
        self.description = stats.get("description","A super secret unknown weapon...")
        self.durability = stats.get("durability",DEFAULT_DURABILITY)
        self.value = stats.get("value",DEFAULT_VALUE)
        self.damage = stats.get("damage",DEFAULT_DAMAGE)
        self.id = stats.get("id","")
        if self.id == "": raise ValueError("ID for weapon cannot be blank!")
        self.types = stats.get("types",["melee"])

    def __str__(self):
        return self.display_name