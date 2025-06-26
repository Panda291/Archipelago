from dataclasses import dataclass
from typing import Dict, Sequence, Set

from BaseClasses import Item


@dataclass
class ItemData(Item):
    item_id: int
    name: str


HELI_PACK = ItemData(2, "Heli Pack")
THRUSTER_PACK = ItemData(3, "Thruster Pack")
HYDRO_PACK = ItemData(4, "Hydro Pack")
SONIC_SUMMONER = ItemData(5, "Sonic Summoner")
O2_MASK = ItemData(6, "O2 Mask")
PILOTS_HELMET = ItemData(7, "Pilots Helmet")
# WRENCH = ItemData(8, "Wrench")
SUCK_CANNON = ItemData(9, "Suck cannon")
BOMB_GLOVE = ItemData(10, "Bomb glove")
DEVASTATOR = ItemData(11, "Devastator")
SWINGSHOT = ItemData(12, "Swingshot")
VISIBOMB = ItemData(13, "Visibomb")
TAUNTER = ItemData(14, "Taunter")
BLASTER = ItemData(15, "Blaster")
PYROCITOR = ItemData(16, "Pyrocitor")
MINE_GLOVE = ItemData(17, "Mine glove")
WALLOPER = ItemData(18, "Walloper")
TESLA_CLAW = ItemData(19, "Tesla claw")
GLOVE_OF_DOOM = ItemData(20, "Glove of doom")
MORPH_O_RAY = ItemData(21, "Morph-o-ray")
HYDRODISPLACER = ItemData(22, "Hydrodisplacer")
RYNO = ItemData(23, "RYNO")
DRONE_DEVICE = ItemData(24, "Drone device")
DECOY_GLOVE = ItemData(25, "Decoy glove")
TRESPASSER = ItemData(26, "Trespasser")
METAL_DETECTOR = ItemData(27, "Metal Detector")
MAGNEBOOTS = ItemData(28, "Magneboots")
GRINDBOOTS = ItemData(29, "Grindboots")
HOVERBOARD = ItemData(30, "Hoverboard")
HOLOGUISE = ItemData(31, "Hologuise")
PDA = ItemData(32, "PDA")
MAP_O_MATIC = ItemData(33, "Map-o-Matic")
BOLT_GRABBER = ItemData(34, "Bolt Grabber")
PERSUADER = ItemData(35, "Persuader")

ZOOMERATOR = ItemData(48, "Zoomerator")
RARITANIUM = ItemData(49, "Raritanium")
CODEBOT = ItemData(50, "Codebot")
PREMIUM_NANOTECH = ItemData(52, "Premium nanotech")
ULTRA_NANOTECH = ItemData(53, "Ultra nanotech")

GOLDEN_SUCK_CANNON = ItemData(59, "Golden Suck Cannon")
GOLDEN_BOMB_GLOVE = ItemData(60, "Golden Bomb glove")
GOLDEN_DEVASTATOR = ItemData(61, "Golden Devastator")
GOLDEN_BLASTER = ItemData(65, "Golden Blaster")
GOLDEN_PYROCITOR = ItemData(66, "Golden Pyrocitor")
GOLDEN_MINE_GLOVE = ItemData(67, "Golden Mine glove")
GOLDEN_TESLA_CLAW = ItemData(69, "Golden Tesla claw")
GOLDEN_GLOVE_OF_DOOM = ItemData(70, "Golden Glove of doom")
GOLDEN_MORPH_O_RAY = ItemData(71, "Golden Morph-o-ray")
GOLDEN_DECOY_GLOVE = ItemData(75, "Golden Decoy glove")

NOVALIS_INFOBOT = ItemData(101, "Novalis")
ARIDIA_INFOBOT = ItemData(102, "Aridia")
KERWAN_INFOBOT = ItemData(103, "Kerwan")
EUDORA_INFOBOT = ItemData(104, "Eudora")
RILGAR_INFOBOT = ItemData(105, "Rilgar")
BLARG_INFOBOT = ItemData(106, "Blarg")
UMBRIS_INFOBOT = ItemData(107, "Umbris")
BATALIA_INFOBOT = ItemData(108, "Batalia")
GASPAR_INFOBOT = ItemData(109, "Gaspar")
ORXON_INFOBOT = ItemData(110, "Orxon")
POKITARU_INFOBOT = ItemData(111, "Pokitaru")
HOVEN_INFOBOT = ItemData(112, "Hoven")
GEMLIK_INFOBOT = ItemData(113, "Gemlik")
OLTANIS_INFOBOT = ItemData(114, "Oltanis")
QUARTU_INFOBOT = ItemData(115, "Quartu")
KALEBO_INFOBOT = ItemData(116, "Kalebo III")
FLEET_INFOBOT = ItemData(117, "Drek's Fleet")
VELDIN_INFOBOT = ItemData(118, "Veldin")

TAKE_AIM = ItemData(200, "Take Aim: Skill Point")
SWING_IT = ItemData(201, "Swing it!: Skill Point")
TRANSPORTED = ItemData(202, "Transported: Skill Point")
STRIKE_A_POSE = ItemData(203, "Strike a pose: Skill Point")
BLIMPY = ItemData(204, "Blimpy: Skill Point")
QWARKTASTIC = ItemData(205, "Qwarktastic: Skill Point")
ANY_TEN = ItemData(206, "Any Ten: Skill Point")
TRICKY = ItemData(207, "Tricky: Skill Point")
CLUCK_CLUCK = ItemData(208, "Cluck, Cluck: Skill Point")
SPEEDY = ItemData(209, "Speedy: Skill Point")
GIRL_TROUBLE = ItemData(210, "Girl Trouble: Skill Point")
JUMPER = ItemData(211, "Jumper: Skill Point")
ACCURACY_COUNTS = ItemData(212, "Accuracy Counts: Skill Point")
EAT_LEAD = ItemData(213, "Eat Lead: Skill Point")
DESTROYED = ItemData(214, "Destroyed: Skill Point")
GUNNER = ItemData(215, "Gunner: Skill Point")
SNIPER = ItemData(216, "Sniper: Skill Point")
HEY_OVER_HERE = ItemData(217, "Hey, Over Here!: Skill Point")
ALIEN_INVASION = ItemData(218, "Alien Invasion: Skill Point")
BURIED_TREASURE = ItemData(219, "Buried Treasure: Skill Point")
PEST_CONTROL = ItemData(220, "Pest Control: Skill Point")
WHIRLYBIRDS = ItemData(221, "Whirlybirds: Skill Point")
SITTING_DUCKS = ItemData(222, "Sitting Ducks: Skill Point")
SHATTERED_GLASS = ItemData(223, "Shattered Glass: Skill Point")
BLAST_EM = ItemData(224, "Blast Em!: Skill Point")
HEAVY_TRAFFIC = ItemData(225, "Heavy Traffic: Skill Point")
MAGICIAN = ItemData(226, "Magician: Skill Point")
SNEAKY = ItemData(227, "Sneaky: Skill Point")
CAREFUL_CRUISE = ItemData(228, "Careful Cruise: Skill Point")
GOING_COMMANDO = ItemData(229, "Going Commando: Skill Point")


@dataclass
class CollectableData(ItemData):
    max_capacity: int = 0x7F


# Collectables
GOLD_BOLT = CollectableData(301, "Gold Bolt", 40)

EQUIPMENT: Sequence[ItemData] = [
    HELI_PACK,
    THRUSTER_PACK,
    HYDRO_PACK,
    SONIC_SUMMONER,
    O2_MASK,
    PILOTS_HELMET,
    TAUNTER,
    HYDRODISPLACER,
    TRESPASSER,
    METAL_DETECTOR,
    MAGNEBOOTS,
    GRINDBOOTS,
    HOVERBOARD,
    HOLOGUISE,
    PDA,
    MAP_O_MATIC,
    BOLT_GRABBER,
    PERSUADER,
    ZOOMERATOR,
    RARITANIUM,
    CODEBOT,
    PREMIUM_NANOTECH,
    ULTRA_NANOTECH,
    SWINGSHOT,
    DRONE_DEVICE,
]

WEAPONS: Sequence[ItemData] = [
    SUCK_CANNON,
    BOMB_GLOVE,
    DEVASTATOR,
    VISIBOMB,
    BLASTER,
    PYROCITOR,
    MINE_GLOVE,
    WALLOPER,
    TESLA_CLAW,
    GLOVE_OF_DOOM,
    MORPH_O_RAY,
    RYNO,
    DECOY_GLOVE,
]

GOLDEN_WEAPONS: Sequence[ItemData] = [
    GOLDEN_SUCK_CANNON,
    GOLDEN_BOMB_GLOVE,
    GOLDEN_DEVASTATOR,
    GOLDEN_BLASTER,
    GOLDEN_PYROCITOR,
    GOLDEN_MINE_GLOVE,
    GOLDEN_TESLA_CLAW,
    GOLDEN_GLOVE_OF_DOOM,
    GOLDEN_MORPH_O_RAY,
    GOLDEN_DECOY_GLOVE,
]

SKILLPOINTS: Sequence[ItemData] = [
    TAKE_AIM,
    SWING_IT,
    TRANSPORTED,
    STRIKE_A_POSE,
    BLIMPY,
    QWARKTASTIC,
    ANY_TEN,
    TRICKY,
    CLUCK_CLUCK,
    SPEEDY,
    GIRL_TROUBLE,
    JUMPER,
    ACCURACY_COUNTS,
    EAT_LEAD,
    DESTROYED,
    GUNNER,
    SNIPER,
    HEY_OVER_HERE,
    ALIEN_INVASION,
    BURIED_TREASURE,
    PEST_CONTROL,
    WHIRLYBIRDS,
    SITTING_DUCKS,
    SHATTERED_GLASS,
    BLAST_EM,
    HEAVY_TRAFFIC,
    MAGICIAN,
    SNEAKY,
    CAREFUL_CRUISE,
    GOING_COMMANDO,
]

PLANETS: Sequence[ItemData] = [
    NOVALIS_INFOBOT,
    ARIDIA_INFOBOT,
    KERWAN_INFOBOT,
    EUDORA_INFOBOT,
    RILGAR_INFOBOT,
    BLARG_INFOBOT,
    UMBRIS_INFOBOT,
    BATALIA_INFOBOT,
    GASPAR_INFOBOT,
    ORXON_INFOBOT,
    POKITARU_INFOBOT,
    HOVEN_INFOBOT,
    GEMLIK_INFOBOT,
    OLTANIS_INFOBOT,
    QUARTU_INFOBOT,
    KALEBO_INFOBOT,
    FLEET_INFOBOT,
    VELDIN_INFOBOT,
]

COLLECTABLES: Sequence[CollectableData] = [
    GOLD_BOLT,
]

EQUIPMENT_AND_WEAPONS: Sequence[ItemData] = [*EQUIPMENT, *WEAPONS]

ALL: Sequence[ItemData] = [*EQUIPMENT, *WEAPONS, *PLANETS, *COLLECTABLES, ]


def from_id(item_id: int) -> ItemData:
    matching = [item for item in ALL if item.item_id == item_id]
    if len(matching) == 0:
        raise ValueError(f"No item data for item id '{item_id}'")
    assert len(matching) < 2, f"Multiple item data with id '{item_id}'. Please report."
    return matching[0]


def from_name(item_name: str) -> ItemData:
    matching = [item for item in ALL if item.name == item_name]
    if len(matching) == 0:
        raise ValueError(f"No item data for '{item_name}'")
    assert len(matching) < 2, f"Multiple item data with name '{item_name}'. Please report."
    return matching[0]


def get_item_groups() -> Dict[str, Set[str]]:
    groups: Dict[str, Set[str]] = {
        "Weapons": {w.name for w in WEAPONS},
        "Infobots": {c.name for c in PLANETS},
        "Equipment": {e.name for e in EQUIPMENT},
        "Gold Bolts": {b.name for b in COLLECTABLES},
        "Gold Weapons": {g.name for g in GOLDEN_WEAPONS},
        "Skillpoints": {s.name for s in SKILLPOINTS},
    }
    return groups
