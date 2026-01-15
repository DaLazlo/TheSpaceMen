from Enum import Enum

from Effects import Effect

class WeaponType(Enum):
    PISTOL = "Captain's Pistol"
    EXTINGUISHER = "Fire Extinguisher"


class Weapon():
    def __init__(self, weapontype):
        self.name = ""
        self.effect = Effect()
        match weapontype:
            case PISTOL:
                self.name = "Captain's Pistol"
            case EXTINGUISHER:
                self.name = "Fire Extinguisher"
        

