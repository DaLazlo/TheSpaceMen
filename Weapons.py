from enum import Enum

from Effect import Effect, EffectType

class WeaponType(Enum):
    PISTOL = "Captain's Pistol"
    EXTINGUISHER = "Fire Extinguisher"
    CLEAVER = "Butcher's Cleaver"
    SYRINGE = "Doctor's Syringe"


class Weapon():
    def __init__(self, weapontype):
        self.name = ""
        self.effect = None
        match weapontype:
            case WeaponType.PISTOL:
                self.name = "Captain's Pistol"
            case WeaponType.EXTINGUISHER:
                self.name = "Fire Extinguisher"
            case WeaponType.CLEAVER:
                self.name = "Butcher's Cleaver"
            case WeaponType.SYRINGE:
                self.name = "Doctor's Syringe"
        

