from enum import Enum


class Crew(Enum):
    CAPTAIN = "Captain Zog"
    ENGINEER = "Engineer Dro"
    MEDIC = "Medic Lep"
    COOK = "Cook Bel"

class SpaceMan():
    def __init__(self, crewmember):
        match (crewmember):
            case Crew.CAPTAIN:
                self.name = "Captain Zog"
            case Crew.ENGINEER:
                self.name = "Engineer Dro"
            case Crew.MEDIC:
                self.name = "Medic Lep"
            case Crew.COOK:
                self.name = "Cook Bel"

