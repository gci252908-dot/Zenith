from letter_options import get_next_letter,reset
from catalogs import zone_catalog
from player import Player

def test_letters():
    assert(get_next_letter().lower() == "a")
    assert(get_next_letter().lower() == "b")
    assert(get_next_letter().lower() == "c")
    reset()
    assert(get_next_letter().lower() == "a")

def test_catalogs():
    assert(zone_catalog.zones["nightring_city"] != None)
    assert(zone_catalog.zones["nightring_jail"] != None)

def test_player():
    assert(Player().id == "player")