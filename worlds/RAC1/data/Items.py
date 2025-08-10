from dataclasses import dataclass
from typing import Sequence

from BaseClasses import Item


@dataclass
class ItemData(Item):
    item_id: int
    name: str
    pool: str


HELI_PACK = ItemData(2, "Heli Pack", "Packs")
THRUSTER_PACK = ItemData(3, "Thruster Pack", "Packs")
HYDRO_PACK = ItemData(4, "Hydro Pack", "Packs")
SONIC_SUMMONER = ItemData(5, "Sonic Summoner", "Helmets")
O2_MASK = ItemData(6, "O2 Mask", "Helmets")
PILOTS_HELMET = ItemData(7, "Pilots Helmet", "Helmets")
# WRENCH = ItemData(8, "Wrench", "?")
SUCK_CANNON = ItemData(9, "Suck cannon", "Weapons")
BOMB_GLOVE = ItemData(10, "Bomb glove", "Weapons")
DEVASTATOR = ItemData(11, "Devastator", "Weapons")
SWINGSHOT = ItemData(12, "Swingshot", "Gadgets")
VISIBOMB = ItemData(13, "Visibomb", "Weapons")
TAUNTER = ItemData(14, "Taunter", "Weapons")
BLASTER = ItemData(15, "Blaster", "Weapons")
PYROCITOR = ItemData(16, "Pyrocitor", "Weapons")
MINE_GLOVE = ItemData(17, "Mine glove", "Weapons")
WALLOPER = ItemData(18, "Walloper", "Weapons")
TESLA_CLAW = ItemData(19, "Tesla claw", "Weapons")
GLOVE_OF_DOOM = ItemData(20, "Glove of doom", "Weapons")
MORPH_O_RAY = ItemData(21, "Morph-o-ray", "Weapons")
HYDRODISPLACER = ItemData(22, "Hydrodisplacer", "Gadgets")
RYNO = ItemData(23, "RYNO", "Weapons")
DRONE_DEVICE = ItemData(24, "Drone device", "Weapons")
DECOY_GLOVE = ItemData(25, "Decoy glove", "Weapons")
TRESPASSER = ItemData(26, "Trespasser", "Gadgets")
METAL_DETECTOR = ItemData(27, "Metal Detector", "Gadgets")
MAGNEBOOTS = ItemData(28, "Magneboots", "Boots")
GRINDBOOTS = ItemData(29, "Grindboots", "Boots")
HOVERBOARD = ItemData(30, "Hoverboard", "ExtraItems")
HOLOGUISE = ItemData(31, "Hologuise", "Gadgets")
PDA = ItemData(32, "PDA", "Gadgets")
MAP_O_MATIC = ItemData(33, "Map-o-Matic", "ExtraItems")
BOLT_GRABBER = ItemData(34, "Bolt Grabber", "ExtraItems")
PERSUADER = ItemData(35, "Persuader", "ExtraItems")

ZOOMERATOR = ItemData(48, "Zoomerator", "ExtraItems")
RARITANIUM = ItemData(49, "Raritanium", "ExtraItems")
CODEBOT = ItemData(50, "Codebot", "ExtraItems")
PREMIUM_NANOTECH = ItemData(52, "Premium nanotech", "ExtraItems")
ULTRA_NANOTECH = ItemData(53, "Ultra nanotech", "ExtraItems")

GOLDEN_SUCK_CANNON = ItemData(59, "Golden Suck Cannon", "GoldenWeapons")
GOLDEN_BOMB_GLOVE = ItemData(60, "Golden Bomb glove", "GoldenWeapons")
GOLDEN_DEVASTATOR = ItemData(61, "Golden Devastator", "GoldenWeapons")
GOLDEN_BLASTER = ItemData(65, "Golden Blaster", "GoldenWeapons")
GOLDEN_PYROCITOR = ItemData(66, "Golden Pyrocitor", "GoldenWeapons")
GOLDEN_MINE_GLOVE = ItemData(67, "Golden Mine glove", "GoldenWeapons")
GOLDEN_TESLA_CLAW = ItemData(69, "Golden Tesla claw", "GoldenWeapons")
GOLDEN_GLOVE_OF_DOOM = ItemData(70, "Golden Glove of doom", "GoldenWeapons")
GOLDEN_MORPH_O_RAY = ItemData(71, "Golden Morph-o-ray", "GoldenWeapons")
GOLDEN_DECOY_GLOVE = ItemData(75, "Golden Decoy glove", "GoldenWeapons")

PROGRESSIVE_PACK = ItemData(80, "Progressive Pack", "Packs")
PROGRESSIVE_HELMET = ItemData(81, "Progressive Helmet", "Helmets")
PROGRESSIVE_SUCK = ItemData(82, "Progressive Suck Cannon", "Weapons")
PROGRESSIVE_BOMB = ItemData(83, "Progressive Bomb glove", "Weapons")
PROGRESSIVE_DEVASTATOR = ItemData(84, "Progressive Devastator", "Weapons")
PROGRESSIVE_BLASTER = ItemData(85, "Progressive Blaster", "Weapons")
PROGRESSIVE_PYROCITOR = ItemData(86, "Progressive Pyrocitor", "Weapons")
PROGRESSIVE_MINE = ItemData(87, "Progressive Mine glove", "Weapons")
PROGRESSIVE_TESLA = ItemData(88, "Progressive Tesla claw", "Weapons")
PROGRESSIVE_DOOM = ItemData(89, "Progressive Glove of doom", "Weapons")
PROGRESSIVE_MORPH = ItemData(90, "Progressive Morph-o-ray", "Weapons")
PROGRESSIVE_DECOY = ItemData(91, "Progressive Decoy glove", "Weapons")
PROGRESSIVE_BOOT = ItemData(92, "Progressive Boots", "Boots")
PROGRESSIVE_HOVERBOARD = ItemData(93, "Progressive Hoverboard", "ExtraItems")
PROGRESSIVE_TRADE = ItemData(94, "Progressive Raritanium", "ExtraItems")
PROGRESSIVE_NANOTECH = ItemData(95, "Progressive Nanotech", "ExtraItems")

NOVALIS_INFOBOT = ItemData(101, "Novalis", "Infobots")
ARIDIA_INFOBOT = ItemData(102, "Aridia", "Infobots")
KERWAN_INFOBOT = ItemData(103, "Kerwan", "Infobots")
EUDORA_INFOBOT = ItemData(104, "Eudora", "Infobots")
RILGAR_INFOBOT = ItemData(105, "Rilgar", "Infobots")
BLARG_INFOBOT = ItemData(106, "Blarg", "Infobots")
UMBRIS_INFOBOT = ItemData(107, "Umbris", "Infobots")
BATALIA_INFOBOT = ItemData(108, "Batalia", "Infobots")
GASPAR_INFOBOT = ItemData(109, "Gaspar", "Infobots")
ORXON_INFOBOT = ItemData(110, "Orxon", "Infobots")
POKITARU_INFOBOT = ItemData(111, "Pokitaru", "Infobots")
HOVEN_INFOBOT = ItemData(112, "Hoven", "Infobots")
GEMLIK_INFOBOT = ItemData(113, "Gemlik", "Infobots")
OLTANIS_INFOBOT = ItemData(114, "Oltanis", "Infobots")
QUARTU_INFOBOT = ItemData(115, "Quartu", "Infobots")
KALEBO_INFOBOT = ItemData(116, "Kalebo III", "Infobots")
FLEET_INFOBOT = ItemData(117, "Drek's Fleet", "Infobots")
VELDIN_INFOBOT = ItemData(118, "Veldin", "Infobots")

TAKE_AIM = ItemData(200, "Take Aim: Skill Point", "Skillpoint")
SWING_IT = ItemData(201, "Swing it!: Skill Point", "Skillpoint")
TRANSPORTED = ItemData(202, "Transported: Skill Point", "Skillpoint")
STRIKE_A_POSE = ItemData(203, "Strike a pose: Skill Point", "Skillpoint")
BLIMPY = ItemData(204, "Blimpy: Skill Point", "Skillpoint")
QWARKTASTIC = ItemData(205, "Qwarktastic: Skill Point", "Skillpoint")
ANY_TEN = ItemData(206, "Any Ten: Skill Point", "Skillpoint")
TRICKY = ItemData(207, "Tricky: Skill Point", "Skillpoint")
CLUCK_CLUCK = ItemData(208, "Cluck, Cluck: Skill Point", "Skillpoint")
SPEEDY = ItemData(209, "Speedy: Skill Point", "Skillpoint")
GIRL_TROUBLE = ItemData(210, "Girl Trouble: Skill Point", "Skillpoint")
JUMPER = ItemData(211, "Jumper: Skill Point", "Skillpoint")
ACCURACY_COUNTS = ItemData(212, "Accuracy Counts: Skill Point", "Skillpoint")
EAT_LEAD = ItemData(213, "Eat Lead: Skill Point", "Skillpoint")
DESTROYED = ItemData(214, "Destroyed: Skill Point", "Skillpoint")
GUNNER = ItemData(215, "Gunner: Skill Point", "Skillpoint")
SNIPER = ItemData(216, "Sniper: Skill Point", "Skillpoint")
HEY_OVER_HERE = ItemData(217, "Hey, Over Here!: Skill Point", "Skillpoint")
ALIEN_INVASION = ItemData(218, "Alien Invasion: Skill Point", "Skillpoint")
BURIED_TREASURE = ItemData(219, "Buried Treasure: Skill Point", "Skillpoint")
PEST_CONTROL = ItemData(220, "Pest Control: Skill Point", "Skillpoint")
WHIRLYBIRDS = ItemData(221, "Whirlybirds: Skill Point", "Skillpoint")
SITTING_DUCKS = ItemData(222, "Sitting Ducks: Skill Point", "Skillpoint")
SHATTERED_GLASS = ItemData(223, "Shattered Glass: Skill Point", "Skillpoint")
BLAST_EM = ItemData(224, "Blast Em!: Skill Point", "Skillpoint")
HEAVY_TRAFFIC = ItemData(225, "Heavy Traffic: Skill Point", "Skillpoint")
MAGICIAN = ItemData(226, "Magician: Skill Point", "Skillpoint")
SNEAKY = ItemData(227, "Sneaky: Skill Point", "Skillpoint")
CAREFUL_CRUISE = ItemData(228, "Careful Cruise: Skill Point", "Skillpoint")
GOING_COMMANDO = ItemData(229, "Going Commando: Skill Point", "Skillpoint")


@dataclass
class CollectableData(ItemData):
    max_capacity: int = 0x7F


# Collectables
GOLD_BOLT = CollectableData(301, "Gold Bolt", "GoldBolts", 40)


WEAPONS: Sequence[ItemData] = [
    TAUNTER,
    VISIBOMB,
    WALLOPER,
    DRONE_DEVICE,
]

NON_PROGRESSIVE_WEAPONS: Sequence[ItemData] = [
    SUCK_CANNON,
    BOMB_GLOVE,
    DEVASTATOR,
    BLASTER,
    PYROCITOR,
    MINE_GLOVE,
    TESLA_CLAW,
    GLOVE_OF_DOOM,
    MORPH_O_RAY,
    RYNO,
    DECOY_GLOVE,
]

PROGRESSIVE_WEAPONS: Sequence[ItemData] = [
    PROGRESSIVE_SUCK,
    PROGRESSIVE_BOMB,
    PROGRESSIVE_DEVASTATOR,
    PROGRESSIVE_BLASTER,
    PROGRESSIVE_PYROCITOR,
    PROGRESSIVE_MINE,
    PROGRESSIVE_TESLA,
    PROGRESSIVE_DOOM,
    PROGRESSIVE_MORPH,
    PROGRESSIVE_DECOY,
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

PROGRESSIVE_GOLDEN_WEAPONS: Sequence[ItemData] = [
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

GADGETS: Sequence[ItemData] = [
    HYDRODISPLACER,
    TRESPASSER,
    METAL_DETECTOR,
    HOLOGUISE,
    PDA,
    SWINGSHOT,
]

PACKS: Sequence[ItemData] = [
    HELI_PACK,
    THRUSTER_PACK,
    HYDRO_PACK,
]

PROGRESSIVE_PACKS: Sequence[ItemData] = [
    *[PROGRESSIVE_PACK] * 3,
]

HELMETS: Sequence[ItemData] = [
    SONIC_SUMMONER,
    O2_MASK,
    PILOTS_HELMET,
]

PROGRESSIVE_HELMETS: Sequence[ItemData] = [
    *[PROGRESSIVE_HELMET] * 3,
]

BOOTS: Sequence[ItemData] = [
    MAGNEBOOTS,
    GRINDBOOTS,
]

PROGRESSIVE_BOOTS: Sequence[ItemData] = [
    *[PROGRESSIVE_BOOT] * 2,
]

EXTRA_ITEMS: Sequence[ItemData] = [
    MAP_O_MATIC,
    BOLT_GRABBER,
    CODEBOT,
]

NON_PROGRESSIVE_HOVERBOARDS: Sequence[ItemData] = [
    HOVERBOARD,
    ZOOMERATOR,
]

PROGRESSIVE_HOVERBOARDS: Sequence[ItemData] = [
    *[PROGRESSIVE_HOVERBOARD] * 2,
]

NON_PROGRESSIVE_TRADES: Sequence[ItemData] = [
    PERSUADER,
    RARITANIUM,
]

PROGRESSIVE_TRADES: Sequence[ItemData] = [
    *[PROGRESSIVE_TRADE] * 2,
]

NON_PROGRESSIVE_NANOTECHS: Sequence[ItemData] = [
    PREMIUM_NANOTECH,
    ULTRA_NANOTECH,
]

PROGRESSIVE_NANOTECHS: Sequence[ItemData] = [
    *[PROGRESSIVE_NANOTECH] * 2,
]

GOLD_BOLTS: Sequence[CollectableData] = [
    *[GOLD_BOLT] * 40,
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

ALL: Sequence[ItemData] = [*WEAPONS, *NON_PROGRESSIVE_WEAPONS, *PROGRESSIVE_WEAPONS, *GOLDEN_WEAPONS,
                           *PROGRESSIVE_GOLDEN_WEAPONS, *GADGETS, *PACKS, *PROGRESSIVE_PACKS, *HELMETS,
                           *PROGRESSIVE_HELMETS, *BOOTS, *PROGRESSIVE_BOOTS, *EXTRA_ITEMS,
                           *NON_PROGRESSIVE_HOVERBOARDS, *PROGRESSIVE_HOVERBOARDS, *NON_PROGRESSIVE_TRADES,
                           *PROGRESSIVE_TRADES, *NON_PROGRESSIVE_NANOTECHS, *PROGRESSIVE_NANOTECHS, *GOLD_BOLTS,
                           *PLANETS, *SKILLPOINTS]

ALL_WEAPONS: Sequence[ItemData] = [*WEAPONS, *NON_PROGRESSIVE_WEAPONS, *PROGRESSIVE_WEAPONS, *GOLDEN_WEAPONS,
                                   *PROGRESSIVE_GOLDEN_WEAPONS]
ALL_PACKS: Sequence[ItemData] = [*PACKS, *PROGRESSIVE_PACKS]
ALL_HELMETS: Sequence[ItemData] = [*HELMETS, *PROGRESSIVE_HELMETS]
ALL_BOOTS: Sequence[ItemData] = [*BOOTS, *PROGRESSIVE_BOOTS]
ALL_EXTRA_ITEMS: Sequence[ItemData] = [*EXTRA_ITEMS, *NON_PROGRESSIVE_HOVERBOARDS, *PROGRESSIVE_HOVERBOARDS,
                                       *NON_PROGRESSIVE_TRADES, *PROGRESSIVE_TRADES, *NON_PROGRESSIVE_NANOTECHS,
                                       *PROGRESSIVE_NANOTECHS]


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
    # if item_name != GOLD_BOLT.name:
    #     assert len(matching) < 2, f"Multiple item data with name '{item_name}'. Please report."
    return matching[0]


def get_item_groups() -> dict[str, set[str]]:
    groups: dict[str, set[str]] = {
        "Weapons": {w.name for w in ALL_WEAPONS},
        "Gadgets": {g.name for g in GADGETS},
        "Packs": {p.name for p in ALL_PACKS},
        "Helmets": {h.name for h in ALL_HELMETS},
        "Boots": {b.name for b in ALL_BOOTS},
        "ExtraItems": {e.name for e in ALL_EXTRA_ITEMS},
        "GoldBolts": {c.name for c in GOLD_BOLTS},
        "Infobots": {i.name for i in PLANETS},
        "Skillpoints": {s.name for s in SKILLPOINTS},
    }
    return groups
