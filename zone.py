class Option:
    def __init__(self,text,letter):
        self.text = text
        self.letter = letter
    
    def __str__(self):
        return f"{self.letter}: {self.text}"

class Area:
    def __init__(self, dat, zone):
        self.id = dat["id"]
        self.entry = (self.id == "entry")
        self.desc = dat.get("desc", "")
        self.condition = dat.get("condition", None)
        self.zone = zone

        self.options = [
            Option(text, letter)
            for text, letter in dat.get("options", {}).items()
        ]

    def which_option(self,key):
        for option in self.options:
            if option.letter.lower() == key.lower():
                return option
        return None
    
    def __str__(self):
        return f"""
{self.desc}
{"\n".join(str(option) for option in self.options)}
        """.strip()

    def get_next(self,letter):
        for id,area in self.zone.areas.items():
            if area.id.lower() == letter.lower():
                return area
        return None

class Zone:
    def __init__(self,dat):
        self.display = dat["display"]
        self.id = dat["id"]
        self.areas = {}

def parse(data):
    zone = Zone(data)
    zone.areas = {a["id"]: Area(a,zone) for a in data["areas"]}
    return zone