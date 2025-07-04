from typing import Sequence

from .Locations import *


class PlanetData(NamedTuple):
    name: str
    number: int
    locations: Sequence[LocationData] = []


NOVALIS = PlanetData("Novalis", 1, [
    NOVALIS_PLUMBER,
    NOVALIS_MAYOR,
    NOVALIS_VENDOR_PYROCITOR,
    NOVALIS_SEWER_GOLD_BOLT,
    NOVALIS_CAVES_GOLD_BOLT,
    NOVALIS_UNDERWATER_CAVES_GOLD_BOLT,
])

ARIDIA = PlanetData("Aridia", 2, [
    ARIDIA_HOVERBOARD,
    ARIDIA_TRESPASSER,
    ARIDIA_SONIC_SUMMONER,
    ARIDIA_TRESPASSER_GOLD_BOLT,
    ARIDIA_ISLAND_GOLD_BOLT,
    ARIDIA_MAGNEBOOTS_GOLD_BOLT,
    ARIDIA_SANDSHARK_GOLD_BOLT,
])

KERWAN = PlanetData("Kerwan", 3, [
    KERWAN_SWINGSHOT,
    KERWAN_HELIPACK,
    KERWAN_TRAIN_INFOBOT,
    KERWAN_VENDOR_BLASTER,
    KERWAN_BELOW_SHIP_GOLD_BOLT,
    KERWAN_TRAIN_STATION_GOLD_BOLT,
    KERWAN_LONE_TOWER_GOLD_BOLT,
])

EUDORA = PlanetData("Eudora", 4, [
    EUDORA_HENCHMAN,
    EUDORA_SUCK_CANNON,
    EUDORA_VENDOR_GLOVE_OF_DOOM,
    EUDORA_GOLD_BOLT,
])

RILGAR = PlanetData("Rilgar", 5, [
    RILGAR_QUARK_INFOBOT,
    RILGAR_PLATINUM_ZOOMERATOR,
    RILGAR_MINE_GLOVE,
    RILGAR_RYNO,
    RILGAR_MAZE_GOLD_BOLT,
    RILGAR_WATERWORKS_GOLD_BOLT,
])

BLARG = PlanetData("Blarg", 6, [
    BLARG_HYDRODISPLACER,
    BLARG_EXPLOSION_INFOBOT,
    BLARG_GRINDBOOTS,
    BLARG_VENDOR_TAUNTER,
    BLARG_OUTSIDE_GOLD_BOLT,
    BLARG_SWARMER_GOLD_BOLT,
])

UMBRIS = PlanetData("Umbris", 7, [
    UMBRIS_SNAGGLEBEAST_INFOBOT,
    UMBRIS_PRESSURE_PUZZLE_GOLD_BOLT,
    UMBRIS_JUMP_DOWN_GOLD_BOLT,
])

BATALIA = PlanetData("Batalia", 8, [
    BATALIA_VENDOR_DEVASTATOR,
    BATALIA_GRINDRAIL_INFOBOT,
    BATALIA_COMMANDER_INFOBOT,
    BATALIA_METAL_DETECTOR,
    BATALIA_CLIFFSIDE_GOLD_BOLT,
    BATALIA_TRESPASSER_GOLD_BOLT,
])

GASPAR = PlanetData("Gaspar", 9, [
    GASPAR_VENDOR_WALLOPER,
    GASPAR_PILOT_HELMET,
    GASPAR_SWINGSHOT_GOLD_BOLT,
    GASPAR_VOLCANO_GOLD_BOLT,
])

ORXON = PlanetData("Orxon", 10, [
    ORXON_VENDOR_VISIBOMB,
    ORXON_CLANK_INFOBOT,
    ORXON_RATCHET_INFOBOT,
    ORXON_CLANK_MAGNEBOOTS,
    ORXON_PREMIUM_NANOTECH,
    ORXON_ULTRA_NANOTECH,
    ORXON_CLANK_GOLD_BOLT,
    ORXON_VISIBOMB_GOLD_BOLT,
])

POKITARU = PlanetData("Pokitaru", 11, [
    POKITARU_VENDOR_DECOY_GLOVE,
    POKITARU_O2_MASK,
    POKITARU_SEWER_PERSUADER,
    POKITARU_THRUSTER_PACK,
    POKITARU_GOLD_BOLT,
])

HOVEN = PlanetData("Hoven", 12, [
    HOVEN_VENDOR_DRONE_DEVICE,
    HOVEN_TURRET_INFOBOT,
    HOVEN_HYDRO_PACK,
    HOVEN_RARITANIUM,
    HOVEN_WATER_GOLD_BOLT,
    HOVEN_WALLJUMP_GOLD_BOLT,
])

GEMLIK = PlanetData("Gemlik", 13, [
    GEMLIK_QUARK_FIGHT,
    GEMLIK_GOLD_BOLT,
])

OLTANIS = PlanetData("Oltanis", 14, [
    OLTANIS_VENDOR_TESLA_CLAW,
    OLTANIS_INFOBOT,
    OLTANIS_PDA,
    OLTANIS_MORPH_O_RAY,
    OLTANIS_MAIN_GOLD_BOLT,
    OLTANIS_MAGNET_GOLD_BOLT_1,
    OLTANIS_MAGNET_GOLD_BOLT_2,
    OLTANIS_FINAL_GOLD_BOLT,
])

QUARTU = PlanetData("Quartu", 15, [
    QUARTU_GIANT_CLANK_INFOBOT,
    QUARTU_BOLT_GRABBER,
    QUARTU_INFILTRATE_INFOBOT,
    QUARTU_MOM_GOLD_BOLT,
    QUARTU_CODEBOT_GOLD_BOLT,
])

KALEBO = PlanetData("Kalebo III", 16, [
    KALEBO_HOLOGUISE,
    KALEBO_MAP_O_MATIC,
    KALEBO_GRIND_GOLD_BOLT,
    KALEBO_BREAK_ROOM_GOLD_BOLT,
])

FLEET = PlanetData("Drek's Fleet", 17, [
    FLEET_INFOBOT,
    FLEET_CODEBOT,
    FLEET_WATER_GOLD_BOLT,
    FLEET_ROBOT_GOLD_BOLT,
])

VELDIN = PlanetData("Veldin", 18, [
    VELDIN_TAUNTER_GOLD_BOLT,
    VELDIN_HALFWAY_GOLD_BOLT,
    VELDIN_GRIND_GOLD_BOLT,
    VELDIN_DREK,
])

LOGIC_PLANETS: Sequence[PlanetData] = [
    NOVALIS,
    ARIDIA,
    KERWAN,
    EUDORA,
    RILGAR,
    BLARG,
    UMBRIS,
    BATALIA,
    GASPAR,
    ORXON,
    POKITARU,
    HOVEN,
    GEMLIK,
    OLTANIS,
    QUARTU,
    KALEBO,
    FLEET,
    VELDIN
]

ALL_LOCATIONS: Sequence[LocationData] = [
    location
    for locations in [planet.locations for planet in LOGIC_PLANETS]
    for location in locations
]
