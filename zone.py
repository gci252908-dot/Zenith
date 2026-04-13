from letter_options import get_next_letter,reset

class Option:
    """ Represents an option the player can pick from a specific Area """
    def __init__(self,text,id,letter):
        self.text = text
        self.next_id = id
        self.letter = letter
    
    def __str__(self):
        return f"{self.letter}: {self.text}"

class Area:
    """ Represents a subcategory of a Zone, with options and a description """
    def __init__(self, dat, zone):
        self.id = dat["id"]
        self.entry = (self.id == "entry")
        self.desc = dat.get("desc", "")
        self.condition = dat.get("condition", None)
        self.zone = zone

        self.options = [
            Option(text, id,get_next_letter())
            for text, id in dat.get("options", {}).items()
        ]
        reset()

    def which_option(self,key):
        """ Returns which option in the current area the user has picked, or None if the user picked an invalid option """
        for option in self.options:
            if option.letter.lower() == key.lower():
                return option
        return None
    
    def __str__(self):
        return f"""
{self.desc}
{"\n".join(str(option) for option in self.options)}
        """.strip()

    def get_next(self,option,catalog):
        """ Grabs the next area to go to, either from the current Zone or from the next Zone to move to """
        last_id = None
        for id,area in self.zone.areas.items():
            if id.lower() == option.next_id.lower():
                return area
            last_id = option.next_id
        return catalog.zones[last_id.lower()].areas["entry"]

class Zone:
    def __init__(self,dat):
        self.display = dat["display"]
        self.id = dat["id"]
        self.areas = {}

def parse(data):
    """ Parses Zones from the JSON-data input from the catalog """
    zone = Zone(data)
    zone.areas = {a["id"]: Area(a,zone) for a in data["areas"]}
    return zone