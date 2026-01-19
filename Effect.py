from enum import Enum
from random import randint

from Alien import Alien

class EffectType(Enum):
    DAMAGE1 = "Cause 1 Damage"
    DAMAGE2 = "Cause 2 Damage"
    NOTHING = "Nothing"

BadEffects = [
    EffectType.NOTHING,
]

def getRandomEffect():
    match(randint(0,2)):
        case 0:
            return EffectType.DAMAGE1
        case 1:
            return EffectType.DAMAGE2
        case 2:
            return EffectType.NOTHING

def doEffect(effecType: EffectType, target: Alien):
    match (effecType):
        case EffectType.DAMAGE1:
            target.takeDamage(1)
        case EffectType.DAMAGE2:
            target.takeDamage(2)
        case _:
            pass


