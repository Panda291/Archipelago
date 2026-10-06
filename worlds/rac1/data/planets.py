from typing import NamedTuple, Sequence

from worlds.rac1 import RAC1ITEM
from worlds.rac1.data.locations import LocationData, RAC1LocationData
from worlds.rac1.constants.locations.planets import RAC1PLANET
from worlds.rac1.constants.pools import RAC1POOL


class PlanetData(NamedTuple):
    name: str
    number: int
    locations: Sequence[LocationData] = []


class RAC1PlanetData:
    GENERAL = PlanetData(RAC1PLANET.GENERAL, 0, [
        RAC1LocationData.HOVERBOARD_TRICKY
    ])

    NOVALIS = PlanetData(RAC1PLANET.NOVALIS, 1, [
        RAC1LocationData.NOVALIS_PLUMBER,
        RAC1LocationData.NOVALIS_MAYOR,
        RAC1LocationData.NOVALIS_VENDOR_PYROCITOR,
        RAC1LocationData.NOVALIS_SEWER_GOLD_BOLT,
        RAC1LocationData.NOVALIS_CAVES_GOLD_BOLT,
        RAC1LocationData.NOVALIS_UNDERWATER_CAVES_GOLD_BOLT,
        RAC1LocationData.NOVALIS_GOLD_WEAPON_1,
        RAC1LocationData.NOVALIS_GOLD_WEAPON_2,
        RAC1LocationData.NOVALIS_GOLD_WEAPON_3,
        RAC1LocationData.NOVALIS_GOLD_WEAPON_4,
        RAC1LocationData.NOVALIS_GOLD_WEAPON_5,
        RAC1LocationData.NOVALIS_GOLD_WEAPON_6,
        RAC1LocationData.NOVALIS_GOLD_WEAPON_7,
        RAC1LocationData.NOVALIS_GOLD_WEAPON_8,
        RAC1LocationData.NOVALIS_GOLD_WEAPON_9,
        RAC1LocationData.NOVALIS_GOLD_WEAPON_10,
        RAC1LocationData.NOVALIS_SKILLPOINT,
    ])

    ARIDIA = PlanetData(RAC1PLANET.ARIDIA, 2, [
        RAC1LocationData.ARIDIA_HOVERBOARD,
        RAC1LocationData.ARIDIA_TRESPASSER,
        RAC1LocationData.ARIDIA_SONIC_SUMMONER,
        RAC1LocationData.ARIDIA_TRESPASSER_GOLD_BOLT,
        RAC1LocationData.ARIDIA_ISLAND_GOLD_BOLT,
        RAC1LocationData.ARIDIA_MAGNEBOOTS_GOLD_BOLT,
        RAC1LocationData.ARIDIA_SANDSHARK_GOLD_BOLT,
        RAC1LocationData.ARIDIA_SWING_IT,
        RAC1LocationData.ARIDIA_TRANSPORTED,
    ])

    KERWAN = PlanetData(RAC1PLANET.KERWAN, 3, [
        RAC1LocationData.KERWAN_SWINGSHOT,
        RAC1LocationData.KERWAN_HELIPACK,
        RAC1LocationData.KERWAN_TRAIN_INFOBOT,
        RAC1LocationData.KERWAN_VENDOR_BLASTER,
        RAC1LocationData.KERWAN_BELOW_SHIP_GOLD_BOLT,
        RAC1LocationData.KERWAN_TRAIN_STATION_GOLD_BOLT,
        RAC1LocationData.KERWAN_LONE_TOWER_GOLD_BOLT,
        RAC1LocationData.KERWAN_STRIKE_A_POSE,
        RAC1LocationData.KERWAN_BLIMPY,
        RAC1LocationData.KERWAN_QWARKTASTIC,
    ])

    EUDORA = PlanetData(RAC1PLANET.EUDORA, 4, [
        RAC1LocationData.EUDORA_HENCHMAN,
        RAC1LocationData.EUDORA_SUCK_CANNON,
        RAC1LocationData.EUDORA_VENDOR_GLOVE_OF_DOOM,
        RAC1LocationData.EUDORA_GOLD_BOLT,
        RAC1LocationData.EUDORA_ANY_TEN,
    ])

    RILGAR = PlanetData(RAC1PLANET.RILGAR, 5, [
        RAC1LocationData.RILGAR_QUARK_INFOBOT,
        RAC1LocationData.RILGAR_PLATINUM_ZOOMERATOR,
        RAC1LocationData.RILGAR_MINE_GLOVE,
        RAC1LocationData.RILGAR_RYNO,
        RAC1LocationData.RILGAR_MAZE_GOLD_BOLT,
        RAC1LocationData.RILGAR_WATERWORKS_GOLD_BOLT,
        RAC1LocationData.RILGAR_CLUCK_CLUCK,
        RAC1LocationData.RILGAR_SPEEDY,
    ])

    BLARG = PlanetData(RAC1PLANET.BLARG, 6, [
        RAC1LocationData.BLARG_HYDRODISPLACER,
        RAC1LocationData.BLARG_EXPLOSION_INFOBOT,
        RAC1LocationData.BLARG_GRINDBOOTS,
        RAC1LocationData.BLARG_VENDOR_TAUNTER,
        RAC1LocationData.BLARG_OUTSIDE_GOLD_BOLT,
        RAC1LocationData.BLARG_SWARMER_GOLD_BOLT,
        RAC1LocationData.BLARG_GIRL_TROUBLE,
    ])

    UMBRIS = PlanetData(RAC1PLANET.UMBRIS, 7, [
        RAC1LocationData.UMBRIS_SNAGGLEBEAST_INFOBOT,
        RAC1LocationData.UMBRIS_PRESSURE_PUZZLE_GOLD_BOLT,
        RAC1LocationData.UMBRIS_JUMP_DOWN_GOLD_BOLT,
    ])

    BATALIA = PlanetData(RAC1PLANET.BATALIA, 8, [
        RAC1LocationData.BATALIA_VENDOR_DEVASTATOR,
        RAC1LocationData.BATALIA_GRINDRAIL_INFOBOT,
        RAC1LocationData.BATALIA_COMMANDER_INFOBOT,
        RAC1LocationData.BATALIA_METAL_DETECTOR,
        RAC1LocationData.BATALIA_CLIFFSIDE_GOLD_BOLT,
        RAC1LocationData.BATALIA_TRESPASSER_GOLD_BOLT,
        RAC1LocationData.BATALIA_JUMPER,
        RAC1LocationData.BATALIA_ACCURACY_COUNTS,
        RAC1LocationData.BATALIA_EAT_LEAD,
    ])

    GASPAR = PlanetData(RAC1PLANET.GASPAR, 9, [
        RAC1LocationData.GASPAR_VENDOR_WALLOPER,
        RAC1LocationData.GASPAR_PILOT_HELMET,
        RAC1LocationData.GASPAR_SWINGSHOT_GOLD_BOLT,
        RAC1LocationData.GASPAR_VOLCANO_GOLD_BOLT,
        RAC1LocationData.GASPAR_DESTROYED,
        RAC1LocationData.GASPAR_GUNNER,
    ])

    ORXON = PlanetData(RAC1PLANET.ORXON, 10, [
        RAC1LocationData.ORXON_VENDOR_VISIBOMB,
        RAC1LocationData.ORXON_CLANK_INFOBOT,
        RAC1LocationData.ORXON_RATCHET_INFOBOT,
        RAC1LocationData.ORXON_CLANK_MAGNEBOOTS,
        RAC1LocationData.ORXON_PREMIUM_NANOTECH,
        RAC1LocationData.ORXON_ULTRA_NANOTECH,
        RAC1LocationData.ORXON_CLANK_GOLD_BOLT,
        RAC1LocationData.ORXON_VISIBOMB_GOLD_BOLT,
        RAC1LocationData.ORXON_SNIPER,
        RAC1LocationData.ORXON_HEY_OVER_HERE,
    ])

    POKITARU = PlanetData(RAC1PLANET.POKITARU, 11, [
        RAC1LocationData.POKITARU_VENDOR_DECOY_GLOVE,
        RAC1LocationData.POKITARU_O2_MASK,
        RAC1LocationData.POKITARU_SEWER_PERSUADER,
        RAC1LocationData.POKITARU_THRUSTER_PACK,
        RAC1LocationData.POKITARU_GOLD_BOLT,
        RAC1LocationData.POKITARU_ALIEN_INVASION,
        RAC1LocationData.POKITARU_BURIED_TREASURE,
    ])

    HOVEN = PlanetData(RAC1PLANET.HOVEN, 12, [
        RAC1LocationData.HOVEN_VENDOR_DRONE_DEVICE,
        RAC1LocationData.HOVEN_TURRET_INFOBOT,
        RAC1LocationData.HOVEN_HYDRO_PACK,
        RAC1LocationData.HOVEN_RARITANIUM,
        RAC1LocationData.HOVEN_WATER_GOLD_BOLT,
        RAC1LocationData.HOVEN_WALLJUMP_GOLD_BOLT,
        RAC1LocationData.HOVEN_PEST_CONTROL,
        RAC1LocationData.HOVEN_WHIRLYBIRDS,
    ])

    GEMLIK = PlanetData(RAC1PLANET.GEMLIK, 13, [
        RAC1LocationData.GEMLIK_QUARK_FIGHT,
        RAC1LocationData.GEMLIK_GOLD_BOLT,
        RAC1LocationData.GEMLIK_SITTING_DUCKS,
    ])

    OLTANIS = PlanetData(RAC1PLANET.OLTANIS, 14, [
        RAC1LocationData.OLTANIS_VENDOR_TESLA_CLAW,
        RAC1LocationData.OLTANIS_INFOBOT,
        RAC1LocationData.OLTANIS_PDA,
        RAC1LocationData.OLTANIS_MORPH_O_RAY,
        RAC1LocationData.OLTANIS_MAIN_GOLD_BOLT,
        RAC1LocationData.OLTANIS_MAGNET_GOLD_BOLT_1,
        RAC1LocationData.OLTANIS_MAGNET_GOLD_BOLT_2,
        RAC1LocationData.OLTANIS_FINAL_GOLD_BOLT,
        RAC1LocationData.OLTANIS_SHATTERED_GLASS,
        RAC1LocationData.OLTANIS_BLAST_EM,
    ])

    QUARTU = PlanetData(RAC1PLANET.QUARTU, 15, [
        RAC1LocationData.QUARTU_GIANT_CLANK_INFOBOT,
        RAC1LocationData.QUARTU_BOLT_GRABBER,
        RAC1LocationData.QUARTU_INFILTRATE_INFOBOT,
        RAC1LocationData.QUARTU_MOM_GOLD_BOLT,
        RAC1LocationData.QUARTU_CODEBOT_GOLD_BOLT,
    ])

    KALEBO = PlanetData(RAC1PLANET.KALEBO, 16, [
        RAC1LocationData.KALEBO_HOLOGUISE,
        RAC1LocationData.KALEBO_MAP_O_MATIC,
        RAC1LocationData.KALEBO_GRIND_GOLD_BOLT,
        RAC1LocationData.KALEBO_BREAK_ROOM_GOLD_BOLT,
        RAC1LocationData.KALEBO_HEAVY_TRAFFIC,
        RAC1LocationData.KALEBO_MAGICIAN,
    ])

    FLEET = PlanetData(RAC1PLANET.FLEET, 17, [
        RAC1LocationData.FLEET_INFOBOT,
        RAC1LocationData.FLEET_CODEBOT,
        RAC1LocationData.FLEET_WATER_GOLD_BOLT,
        RAC1LocationData.FLEET_ROBOT_GOLD_BOLT,
        RAC1LocationData.FLEET_SNEAKY,
        RAC1LocationData.FLEET_CAREFUL_CRUISE,
    ])

    VELDIN = PlanetData(RAC1PLANET.VELDIN, 18, [
        RAC1LocationData.VELDIN_TAUNTER_GOLD_BOLT,
        RAC1LocationData.VELDIN_HALFWAY_GOLD_BOLT,
        RAC1LocationData.VELDIN_GRIND_GOLD_BOLT,
        RAC1LocationData.VELDIN_DREK,
        RAC1LocationData.VELDIN_GOING_COMMANDO,
    ])

PLANET_NAME_TO_ITEM: dict[str, str] = {
    RAC1PLANET.VELDIN: RAC1ITEM.VELDIN,
    RAC1PLANET.NOVALIS: RAC1ITEM.NOVALIS,
    RAC1PLANET.ARIDIA: RAC1ITEM.ARIDIA,
    RAC1PLANET.KERWAN: RAC1ITEM.KERWAN,
    RAC1PLANET.EUDORA: RAC1ITEM.EUDORA,
    RAC1PLANET.BLARG: RAC1ITEM.BLARG,
    RAC1PLANET.RILGAR: RAC1ITEM.RILGAR,
    RAC1PLANET.UMBRIS: RAC1ITEM.UMBRIS,
    RAC1PLANET.BATALIA: RAC1ITEM.BATALIA,
    RAC1PLANET.ORXON: RAC1ITEM.ORXON,
    RAC1PLANET.GASPAR: RAC1ITEM.GASPAR,
    RAC1PLANET.POKITARU: RAC1ITEM.POKITARU,
    RAC1PLANET.HOVEN: RAC1ITEM.HOVEN,
    RAC1PLANET.GEMLIK: RAC1ITEM.GEMLIK,
    RAC1PLANET.OLTANIS: RAC1ITEM.OLTANIS,
    RAC1PLANET.QUARTU: RAC1ITEM.QUARTU,
    RAC1PLANET.KALEBO: RAC1ITEM.KALEBO,
    RAC1PLANET.FLEET: RAC1ITEM.FLEET,
}

LOGIC_PLANETS: Sequence[PlanetData] = [
    RAC1PlanetData.GENERAL,
    RAC1PlanetData.NOVALIS,
    RAC1PlanetData.ARIDIA,
    RAC1PlanetData.KERWAN,
    RAC1PlanetData.EUDORA,
    RAC1PlanetData.RILGAR,
    RAC1PlanetData.BLARG,
    RAC1PlanetData.UMBRIS,
    RAC1PlanetData.BATALIA,
    RAC1PlanetData.GASPAR,
    RAC1PlanetData.ORXON,
    RAC1PlanetData.POKITARU,
    RAC1PlanetData.HOVEN,
    RAC1PlanetData.GEMLIK,
    RAC1PlanetData.OLTANIS,
    RAC1PlanetData.QUARTU,
    RAC1PlanetData.KALEBO,
    RAC1PlanetData.FLEET,
    RAC1PlanetData.VELDIN,
]

ALL_LOCATIONS: Sequence[LocationData] = [
    location
    for locations in [planet.locations for planet in LOGIC_PLANETS]
    for location in locations
]

location_table_by_name: dict[str, LocationData] = {location.name: location for location in ALL_LOCATIONS}
location_groups: dict[str, set[str]] = {
    RAC1PLANET.NOVALIS: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.NOVALIS),
    RAC1PLANET.ARIDIA: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.ARIDIA),
    RAC1PLANET.KERWAN: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.KERWAN),
    RAC1PLANET.EUDORA: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.EUDORA),
    RAC1PLANET.RILGAR: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.RILGAR),
    RAC1PLANET.BLARG: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.BLARG),
    RAC1PLANET.UMBRIS: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.UMBRIS),
    RAC1PLANET.BATALIA: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.BATALIA),
    RAC1PLANET.GASPAR: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.GASPAR),
    RAC1PLANET.ORXON: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.ORXON),
    RAC1PLANET.POKITARU: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.POKITARU),
    RAC1PLANET.HOVEN: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.HOVEN),
    RAC1PLANET.GEMLIK: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.GEMLIK),
    RAC1PLANET.OLTANIS: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.OLTANIS),
    RAC1PLANET.QUARTU: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.QUARTU),
    RAC1PLANET.KALEBO: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.KALEBO),
    RAC1PLANET.FLEET: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.FLEET),
    RAC1PLANET.VELDIN: set(loc.name for loc in ALL_LOCATIONS if loc.planet in RAC1PlanetData.VELDIN),
    RAC1POOL.WEAPONS: set(loc.name for loc in ALL_LOCATIONS if loc.pools.issubset(RAC1POOL.WEAPONS) and len(loc.pools)),
    RAC1POOL.GOLD_WEAPONS: set(
        loc.name for loc in ALL_LOCATIONS if loc.pools.issubset(RAC1POOL.GOLD_WEAPONS) and len(loc.pools)),
    RAC1POOL.GADGETS: set(loc.name for loc in ALL_LOCATIONS if loc.pools.issubset(RAC1POOL.GADGETS) and len(loc.pools)),
    RAC1POOL.PACKS: set(loc.name for loc in ALL_LOCATIONS if loc.pools.issubset(RAC1POOL.PACKS) and len(loc.pools)),
    RAC1POOL.HELMETS: set(loc.name for loc in ALL_LOCATIONS if loc.pools.issubset(RAC1POOL.HELMETS) and len(loc.pools)),
    RAC1POOL.BOOTS: set(loc.name for loc in ALL_LOCATIONS if loc.pools.issubset(RAC1POOL.BOOTS) and len(loc.pools)),
    RAC1POOL.EXTRA_ITEMS: set(
        loc.name for loc in ALL_LOCATIONS if loc.pools.issubset(RAC1POOL.EXTRA_ITEMS) and len(loc.pools)),
    RAC1POOL.GOLD_BOLTS: set(
        loc.name for loc in ALL_LOCATIONS if loc.pools.issubset(RAC1POOL.GOLD_BOLTS) and len(loc.pools)),
    RAC1POOL.INFOBOTS: set(
        loc.name for loc in ALL_LOCATIONS if loc.pools.issubset(RAC1POOL.INFOBOTS) and len(loc.pools)),
    RAC1POOL.SKILLPOINT: set(
        loc.name for loc in ALL_LOCATIONS if loc.pools.issubset(RAC1POOL.SKILLPOINT) and len(loc.pools)),
}