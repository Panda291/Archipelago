from ..Logic import *
from typing import Optional, NamedTuple, Dict, Callable, TYPE_CHECKING, Any, Sequence


class LocationData(NamedTuple):
    location_id: Optional[int]
    name: str
    access_rule: Optional[Callable[[CollectionState, int], bool]] = None


# Novalis
NOVALIS_PLUMBER = LocationData(1, "Novalis: Plumber - Infobot")
NOVALIS_MAYOR   = LocationData(2, "Novalis: Mayor - Infobot")
NOVALIS_VENDOR_PYROCITOR = LocationData(3, "Novalis: Vendor - Pyrocitor")
NOVALIS_SEWER_GOLD_BOLT = LocationData(4, "Novalis: Sewer - Gold Bolt")
NOVALIS_CAVES_GOLD_BOLT = LocationData(5, "Novalis: Caves - Gold Bolt", has_explosive_weapon)
NOVALIS_UNDERWATER_CAVES_GOLD_BOLT = LocationData(6, "Novalis: Underwater Caves - Gold Bolt", novalis_underwater_caves_rule)

# Aridia
ARIDIA_HOVERBOARD = LocationData(7, "Aridia: Save Skid Mc Marks")
ARIDIA_TRESSPASSER = LocationData(8, "Aridia: Find the tresspasser", can_swingshot)
ARIDIA_SONIC_SUMMONER = LocationData(9, "Aridia: Trade the platinum zoomerator for the sonic summoner", has_zoomerator)
ARIDIA_TRESSPASSER_GOLD_BOLT = LocationData(10, "Aridia: Gold Bolt below tresspasser", can_swingshot)
ARIDIA_ISLAND_GOLD_BOLT = LocationData(11, "Aridia: Gold bolt on island", can_improved_jump)
ARIDIA_MAGNEBOOTS_GOLD_BOLT = LocationData(12, "Aridia: Gold bolt near mortar turret", has_magneboots)
ARIDIA_SANDSHARK_GOLD_BOLT = LocationData(13, "Aridia: Gold bolt hidden in sandshark area", has_explosive_weapon)

# Kerwan
KERWAN_SWINGSHOT = LocationData(14, "Kerwan: Buy the swingshot from Helga")
KERWAN_HELIPACK  = LocationData(15, "Kerwan: Buy the helipack from Al")
KERWAN_TRAIN_INFOBOT = LocationData(16, "Kerwan: Get the infobot after the train section", can_improved_jump)
KERWAN_VENDOR_BLASTER = LocationData(17, "Kerwan: Buy the blaster from the vendor")
KERWAN_BELOW_SHIP_GOLD_BOLT = LocationData(18, "Kerwan: Get the gold bolt below your ship", can_improved_jump)
KERWAN_TRAIN_STATION_GOLD_BOLT = LocationData(19, "Kerwan: Get the gold bolt just before the flying train section", can_improved_jump)
KERWAN_LONE_TOWER_GOLD_BOLT = LocationData(20, "Kerwan: Get the gold bolt on the lone tower", can_improved_jump)

# Eudora
EUDORA_HENCHMAN = LocationData(21, "Eudora: Get the infobot after the swingshot section", can_swingshot)
EUDORA_SUCK_CANNON = LocationData(22, "Eudora: get the suck cannon", can_improved_jump)
EUDORA_VENDOR_GLOVE_OF_DOOM = LocationData(23, "Eudora: Buy the glove of doom from the vendor")
EUDORA_GOLD_BOLT = LocationData(24, "Eudora: Get the gold bolt near your ship", can_heli_high_jump)

# Rilgar
RILGAR_QUARK_INFOBOT = LocationData(25, "Rilgar: Pay the bouncer to meet Captain Quark", can_swingshot)
RILGAR_PLATINUM_ZOOMERATOR = LocationData(26, "Rilgar: Win the hoverboard race", rilgar_hoverboard_rule)
RILGAR_MINE_GLOVE = LocationData(27, "Rilgar: buy the mine glove from the vendor")
RILGAR_RYNO = LocationData(28, "Rilgar: Buy the RYNO", can_improved_jump)
RILGAR_MAZE_GOLD_BOLT = LocationData(29, "Rilgar: Get the gold bolt in the maze", can_improved_jump)
RILGAR_WATERWORKS_GOLD_BOLT = LocationData(30, "Rilgar: Get the gold bolt in the flooded area", has_o2_mask)

# Blarg
BLARG_HYDRODISPLACER = LocationData(31, "Blarg: Get the hydrodisplacer as Clank")
BLARG_EXPLOSION_INFOBOT = LocationData(32, "Blarg: Get the Infobot from the exploding ship")
BLARG_GRINDBOOTS = LocationData(33, "Blarg: Buy the grind boots from the scientist")
BLARG_VENDOR_TAUNTER = LocationData(34, "Blarg: Buy the taunter from the vendor")
BLARG_OUTSIDE_GOLD_BOLT = LocationData(35, "Blarg: Get the gold bolt outside as Ratchet", has_o2_mask)
BLARG_SWARMER_GOLD_BOLT = LocationData(36, "Blarg: Get the gold bolt from the swarmer nest")

# Umbris
UMBRIS_SNAGGLEBEAST_INFOBOT = LocationData(37, "Umbris: Defeat the Snagglebeast and claim the infobot", umbris_snagglebeast_rule)
UMBRIS_PRESSURE_PUZZLE_GOLD_BOLT = LocationData(38, "Umbris: Get the gold bolt from solving the pressure plate puzzle", umbris_pressure_bolt_rule)
UMBRIS_JUMP_DOWN_GOLD_BOLT = LocationData(39, "Umbris: Get the gold bolt from jumping down onto it", umbris_jump_bolt_rule)

# Batalia
BATALIA_VENDOR_DEVESTATOR = LocationData(40, "Batalia: Buy the devastator from the vendor")
BATALIA_GRINDRAIL_INFOBOT = LocationData(41, "Batalia: Buy the infobot at the end of the grindrail", can_grind)
BATALIA_COMMANDER_INFOBOT = LocationData(42, "Batalia: Get the infobot from the commander")
BATALIA_METAL_DETECTOR = LocationData(43, "Batalia: Get the metal detector from the plumber", has_magneboots)
BATALIA_CLIFFSIDE_GOLD_BOLT = LocationData(44, "Batalia: Get the gold bolt at the cliffside")
BATALIA_TRESSPASSER_GOLD_BOLT = LocationData(45, "Batalia: Get the gold bolt behind the tresspasser lock", has_tresspasser)

# Gaspar
GASPAR_VENDOR_WALLOPER = LocationData(46, "Gaspar: Buy the walloper from the vendor")
GASPAR_PILOT_HELMET = LocationData(47, "Gaspar: Get the pilot helmet")
GASPAR_SWINGSHOT_GOLD_BOLT = LocationData(48, "Gaspar: Get the gold bolt from the swingshot sidepath", can_swingshot)
GASPAR_VOLCANO_GOLD_BOLT = LocationData(49, "Gaspar: Get the gold bolt after a path through the volcano", can_improved_jump)

# Orxon
ORXON_VENDOR_VISIBOMB = LocationData(50, "Orxon: Buy the visibomb gun from the vendor", has_o2_mask)
ORXON_CLANK_INFOBOT = LocationData(51, "Orxon: Get the infobot in the clank section")
ORXON_CLANK_MAGNEBOOTS = LocationData(52, "Orxon: Get the magneboots in the clank section")
ORXON_PREMIUM_NANOTECH = LocationData(53, "Orxon: Buy the premium nanotech", orxon_nanotech_rule)
ORXON_ULTRA_NANOTECH = LocationData(54, "Orxon: Buy the ultra nanotech", orxon_nanotech_rule)
ORXON_CLANK_GOLD_BOLT = LocationData(55, "Orxon: Get the gold bolt in the clank section as ratchet", has_o2_mask)
ORXON_VISIBOMB_GOLD_BOLT = LocationData(56, "Orxon: Get the gold bolt requiring the visibomb", orxon_visibomb_bolt_rule)

# Pokitaru
POKITARU_VENDOR_DECOY_GLOVE = LocationData(57, "Pokitaru: Buy the decoy glove from the vendor")
POKITARU_SHIP_INFOBOT = LocationData(58, "Pokitaru: Destroy all ships using the pilot's helmet", pokitaru_ship_rule)
POKITARU_SEWER_PERSUADER = LocationData(59, "Pokitaru: Trade raritanium for the persuader", pokitaru_persuader_rule)
POKITARU_THRUSTER_PACK = LocationData(60, "Pokitaru: Buy the thruster pack")
POKITARU_GOLD_BOLT = LocationData(61, "Pokitaru: Get the gold bolt on the waterfalls", can_ground_pound)

# Hoven
HOVEN_VENDOR_DRONE_DEVICE = LocationData(62, "Hoven: Buy the drone device from the vendor")
HOVEN_TURRET_INFOBOT = LocationData(63, "Hoven: Destroy the ship and get the infobot", can_improved_jump)
HOVEN_HYDRO_PACK = LocationData(64, "Hoven: Buy the hydropack", has_hydrodisplacer)
HOVEN_RARITANIUM = LocationData(65, "Hoven: Get the raritanium")
HOVEN_WATER_GOLD_BOLT = LocationData(66, "Hoven: Get the gold bolt in the hydrodisplacer section", has_hydrodisplacer)
HOVEN_WALLJUMP_GOLD_BOLT = LocationData(67, "Hoven: Get the gold bolt at the top of the moving wall jump")

# Gemlik
GEMLIK_QUARK_FIGHT = LocationData(68, "Gemlik: Defeat Captain Quark", gemlik_quark_rule)
GEMLIK_GOLD_BOLT = LocationData(69, "Gemlik: Get the gold bolt after shooting its tower with the visibomb", has_visibomb)

# Oltanis
OLTANIS_VENDOR_TESLA_CLAW = LocationData(70, "Oltanis: Buy the tesla claw from the vendor")
OLTANIS_INFOBOT = LocationData(71, "Oltanis: Buy the infobot after traversing the grindrail", can_grind)
OLTANIS_PDA = LocationData(72, "Oltanis: Buy the PDA from Steve", has_magneboots)
OLTANIS_MORPH_O_RAY = LocationData(73, "Oltanis: Get the Morph-o-Ray", can_swingshot)
OLTANIS_MAIN_GOLD_BOLT = LocationData(74, "Oltanis: Get the gold bolt from swingshotting along the main path", oltanis_main_bolt_rule)
OLTANIS_MAGNET_GOLD_BOLT_1 = LocationData(75, "Oltanis: Get the gold bolt by dropping down the ice on the magneboot path", has_magneboots)
OLTANIS_MAGNET_GOLD_BOLT_2 = LocationData(76, "Oltanis: Get the gold bolt by ledge hanging on the magneboot path", has_magneboots)
OLTANIS_FINAL_GOLD_BOLT = LocationData(77, "Oltanis: Get the gold bolt after completing all objectives", oltanis_final_bolt_rule)

# Quartu
QUARTU_GIANT_CLANK_INFOBOT = LocationData(78, "Quartu: Get the infobot after the giant clank fight", can_swingshot)
QUARTU_BOLT_GRABBER = LocationData(79, "Quartu: Get the bolt grabber after the underwater section", quartu_bolt_grabber_rule)
QUARTU_INFILTRATE_INFOBOT = LocationData(80, "Quartu: Get the infobot from clank's mother", quartu_infiltrate_rule)
QUARTU_MOM_GOLD_BOLT = LocationData(81, "Quartu: Get the gold bolt behind clank's mother", quartu_infiltrate_rule)
QUARTU_CODEBOT_GOLD_BOLT = LocationData(82, "Quartu: Get the gold bolt behind the codebot door", quartu_codebot_rule)

# Kalebo III
KALEBO_HOLOGUISE = LocationData(83, "Kalebo III: Win the hoverboard race", kalebo_hologuise_rule)
KALEBO_MAP_O_MATIC = LocationData(84, "Kalebo III: Buy the map-o-matic after the grindrail", can_grind)
KALEBO_GRIND_GOLD_BOLT = LocationData(85, "Kalebo III: Get the gold bolt on the grindrail", can_grind)
KALEBO_BREAK_ROOM_GOLD_BOLT = LocationData(86, "Kalebo III: Get the gold bolt in the employee break room", can_grind)

# Drek's Fleet
FLEET_INFOBOT = LocationData(87, "Drek's Fleet: Get the infobot from the main ship", fleet_infobot_rule)
FLEET_WATER_GOLD_BOLT = LocationData(88, "Drek's Fleet: Get the gold bolt after the water section", fleet_water_rule)
FLEET_ROBOT_GOLD_BOLT = LocationData(89, "Drek's Fleet: Get the gold bolt along the sidepath with robot guards", fleet_second_bolt_rule)

# Veldin
VELDIN_TAUNTER_GOLD_BOLT = LocationData(90, "Veldin: Get the gold bolt using the taunted to lure the horny toad", has_taunter)
VELDIN_HALFWAY_GOLD_BOLT = LocationData(91, "Veldin: Get the gold bolt with better description pending")
VELDIN_GRIND_GOLD_BOLT = LocationData(92, "Veldin: Get the gold bolt after a short grindrail", veldin_grind_bolt_rule)
VELDIN_DREK = LocationData(None, "Veldin: Defeat Chairman Drek", veldin_defeat_drek_rule)