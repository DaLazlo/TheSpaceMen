from enum import Enum
from random import randint

class EffectType(Enum):
    DAMAGE1 = "Cause 1 Damage"
    DAMAGE2 = "Cause 2 Damage"
    GROW = "Grows"
    NOTHING = "No"

BadEffects = [
    EffectType.NOTHING,
    EffectType.GROW,
]

def getRandomEffect():
    match(randint(0,3)):
        case 0:
            return EffectType.DAMAGE1
        case 1:
            return EffectType.DAMAGE2
        case 2:
            return EffectType.NOTHING
        case 3:
            return EffectType.GROW

def doEffect(effectType: EffectType, target):
    match (effectType):
        case EffectType.DAMAGE1:
            target.takeDamage(1)
        case EffectType.DAMAGE2:
            target.takeDamage(2)
        case _:
            pass


