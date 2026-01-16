from enum import Enum

from Effect import Effect

class WeaponType(Enum):
    PISTOL = "Captain's Pistol"
    EXTINGUISHER = "Fire Extinguisher"


class Weapon():
    def __init__(self, weapontype):
        self.name = ""
        self.effect = Effect()
        match weapontype:
            case WeaponType.PISTOL:
                self.name = "Captain's Pistol"
            case WeaponType.EXTINGUISHER:
                self.name = "Fire Extinguisher"
        

