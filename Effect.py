from enum import Enum
from random import randint

class EffectType(Enum):
    DAMAGE1 = "Cause 1 Damage"
    DAMAGE2 = "Cause 2 Damage"
    NOTHING = "No"

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

def doEffect(effectType: EffectType, target):
    match (effectType):
        case EffectType.DAMAGE1:
            target.takeDamage(1)
            print(f"{target.name} takes 1 damage")
        case EffectType.DAMAGE2:
            target.takeDamage(2)
            print(f"{target.name} takes 2 damage")
        case _:
            pass


