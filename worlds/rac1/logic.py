import logging
from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.rac1.constants.items import RAC1ITEM
from worlds.rac1.constants.options import RAC1OPTION
from worlds.rac1.data.items import RAC1ItemData

if TYPE_CHECKING:
    from worlds.rac1 import RacWorld

rac_logger = logging.getLogger(RAC1OPTION.GAME_TITLE_FULL)
rac_logger.setLevel(logging.DEBUG)


def can_improved_jump(state: CollectionState, world: 'RacWorld') -> bool:
    rac_logger.debug("Jump logic just got checked")
    return (state.has_any_count(world.progressive_convert[RAC1ITEM.HELI_PACK], world.player)
            or state.has_any_count(world.progressive_convert[RAC1ITEM.THRUSTER_PACK], world.player))


def can_heli_high_jump(state: CollectionState, world: 'RacWorld') -> bool:  # relevant for eudora gold bolt
    return state.has_any_count(world.progressive_convert[RAC1ITEM.HELI_PACK], world.player)


def can_glide(state: CollectionState, world: 'RacWorld') -> bool:  # gliding is not possible without the heli pack
    return state.has_any_count(world.progressive_convert[RAC1ITEM.HELI_PACK], world.player)


def can_ground_pound(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.THRUSTER_PACK], world.player)


def has_hydro_pack(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.HYDRO_PACK], world.player)


def has_sonic(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.SONIC_SUMMONER], world.player)


def has_o2_mask(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.O2_MASK], world.player)


def has_pilots_helmet(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.PILOTS_HELMET], world.player)


def has_devastator(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.DEVASTATOR], world.player)


def has_swingshot(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has(RAC1ITEM.SWINGSHOT, world.player)


def has_visibomb(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has(RAC1ITEM.VISIBOMB, world.player)


def has_taunter(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has(RAC1ITEM.TAUNTER, world.player)


def has_blaster(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has(RAC1ITEM.BLASTER, world.player)


def has_morph(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.MORPH_O_RAY], world.player)


def has_hydrodisplacer(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has(RAC1ITEM.HYDRODISPLACER, world.player)


def has_trespasser(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has(RAC1ITEM.TRESPASSER, world.player)


def has_7500_bolts(state: CollectionState, world: 'RacWorld') -> bool:
    return has_metal_detector(state, world) or has_bolts(state, world, 7500)


def has_10k_bolts(state: CollectionState, world: 'RacWorld') -> bool:
    return has_metal_detector(state, world) or has_bolts(state, world, 10000)


def has_15k_bolts(state: CollectionState, world: 'RacWorld') -> bool:
    return has_metal_detector(state, world) or has_bolts(state, world, 15000)


def has_20k_bolts(state: CollectionState, world: 'RacWorld') -> bool:
    return has_metal_detector(state, world) or has_bolts(state, world, 20000)


def has_30k_bolts(state: CollectionState, world: 'RacWorld') -> bool:
    return has_metal_detector(state, world) or has_bolts(state, world, 30000)


def has_40k_bolts(state: CollectionState, world: 'RacWorld') -> bool:
    return has_metal_detector(state, world) or has_bolts(state, world, 40000)


def has_60k_bolts(state: CollectionState, world: 'RacWorld') -> bool:
    return has_metal_detector(state, world) or has_bolts(state, world, 60000)


def has_150k_bolts(state: CollectionState, world: 'RacWorld') -> bool:
    return has_metal_detector(state, world) or has_bolts(state, world, 150000)


def can_buy(state: CollectionState, world: 'RacWorld', bolts: int) -> bool:
    match world.options.vendor_logic.value:
        case 0:
            logic = True
        case 1:
            logic = has_metal_detector(state, world) or has_bolts(state, world, bolts)
        case _:
            logic = has_metal_detector(state, world)
    return logic


def has_metal_detector(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has(RAC1ITEM.METAL_DETECTOR, world.player)
            and (
                    early_metal_spots(state, world)
                    or blarg_metal_spots(state, world)
                    or rilgar_metal_spots(state, world)
                    or umbris_metal_spots(state, world)
                    or gaspar_metal_spots(state, world)
                    or orxon_metal_spots(state, world)
                    or gemlik_metal_spots(state, world)
                    or oltanis_metal_spots(state, world)
                    or kalebo_metal_spots(state, world)
                    or fleet_metal_spots(state, world)
                    or veldin_metal_spots(state, world)
            ))


def early_metal_spots(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any([
        RAC1ITEM.NOVALIS,
        RAC1ITEM.KERWAN,
        RAC1ITEM.ARIDIA,
        RAC1ITEM.EUDORA,
        RAC1ITEM.BATALIA,
        RAC1ITEM.POKITARU,
        RAC1ITEM.HOVEN,
        RAC1ITEM.QUARTU,
    ], world.player)


def has_bolts(state: CollectionState, world: 'RacWorld', count: int) -> bool:
    # 500,
    # 1000 * 3,
    # 2000 * 5,
    # 2500 * 3,
    # 4000 * 2,
    # 7500 * 5,
    # 10000 * 5,
    # 15000,
    # 20000 * 3
    # 30000 * 2,
    # 40000,
    # 60000 * 2,
    # 150000
    lookup: dict[int, int] = {
        500: 500,
        1000: 1500,
        2000: 5500,
        2500: 16000,
        4000: 25000,
        7500: 36500,
        10000: 75000,
        15000: 130000,
        20000: 150000,
        30000: 220000,
        40000: 290000,
        60000: 350000,
        150000: 560000,
    }

    total = 0
    for item in [
        RAC1ItemData.BOLT_PACK_1,
        RAC1ItemData.BOLT_PACK_10,
        RAC1ItemData.BOLT_PACK_100,
        RAC1ItemData.BOLT_PACK_250,
        RAC1ItemData.BOLT_PACK_500,
        RAC1ItemData.BOLT_PACK_750,
        RAC1ItemData.BOLT_PACK_1000,
        RAC1ItemData.BOLT_PACK_2000,
        RAC1ItemData.BOLT_PACK_3000,
        RAC1ItemData.BOLT_PACK_4000,
        RAC1ItemData.BOLT_PACK_5000,
        RAC1ItemData.BOLT_PACK_6000,
        RAC1ItemData.BOLT_PACK_7000,
        RAC1ItemData.BOLT_PACK_8000,
        RAC1ItemData.BOLT_PACK_9000,
        RAC1ItemData.BOLT_PACK_10000,
        RAC1ItemData.BOLT_PACK_12500,
        RAC1ItemData.BOLT_PACK_15000,
        RAC1ItemData.BOLT_PACK_17500,
        RAC1ItemData.BOLT_PACK_20000,
        RAC1ItemData.BOLT_PACK_25000,
        RAC1ItemData.BOLT_PACK_30000,
        RAC1ItemData.BOLT_PACK_40000,
        RAC1ItemData.BOLT_PACK_50000,
        RAC1ItemData.BOLT_PACK_75000,
        RAC1ItemData.BOLT_PACK_100000
    ]:
        if state.prog_items[world.player].get(item.item_id) is not None:
            total += (state.prog_items[world.player].get(item.item_id)
                      * item.quantity * world.options.pack_size_bolts.value)
        for planet, bolts in {
            RAC1ITEM.NOVALIS: 4800,
            RAC1ITEM.KERWAN: 2250,
            RAC1ITEM.EUDORA: 4500,
            RAC1ITEM.BLARG: 2250,
            RAC1ITEM.RILGAR: 325,
            RAC1ITEM.BATALIA: 3000,
            RAC1ITEM.GASPAR: 7850,
            RAC1ITEM.ORXON: 4750,
            RAC1ITEM.POKITARU: 2430,
            RAC1ITEM.HOVEN: 2600,
            RAC1ITEM.OLTANIS: 4150,
        }.items():
            total += state.has(planet, world.player) * bolts * world.options.pack_size_bolts.value
    return total >= lookup[count]


def has_magneboots(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.MAGNEBOOTS], world.player)


def has_grindboots(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.GRINDBOOTS], world.player)


def has_hoverboard(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.HOVERBOARD], world.player)


def has_hologuise(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has(RAC1ITEM.HOLOGUISE, world.player)


def has_pda(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has(RAC1ITEM.PDA, world.player)


def has_zoomerator(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.ZOOMERATOR], world.player)


def has_raritanium(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has_any_count(world.progressive_convert[RAC1ITEM.RARITANIUM], world.player)


def has_codebot(state: CollectionState, world: 'RacWorld') -> bool:
    return state.has(RAC1ITEM.CODEBOT, world.player)


def has_explosive_weapon(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has_any_count(world.progressive_convert[RAC1ITEM.BOMB_GLOVE], world.player)
            or state.has_any_count(world.progressive_convert[RAC1ITEM.MINE_GLOVE], world.player)
            or state.has_any_count(world.progressive_convert[RAC1ITEM.DEVASTATOR], world.player)
            or state.has_any([RAC1ITEM.VISIBOMB, RAC1ITEM.RYNO], world.player))


def has_long_range_weapon(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has_any_count(world.progressive_convert[RAC1ITEM.DEVASTATOR], world.player)
            or state.has(RAC1ITEM.VISIBOMB, world.player))


def has_medium_range_weapon(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has_any_count(world.progressive_convert[RAC1ITEM.BLASTER], world.player)
            or state.has_any_count(world.progressive_convert[RAC1ITEM.DEVASTATOR], world.player)
            or state.has_any([RAC1ITEM.VISIBOMB, RAC1ITEM.RYNO], world.player))


def has_short_range_weapon(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has_any_count(world.progressive_convert[RAC1ITEM.PYROCITOR], world.player)
            or state.has_any_count(world.progressive_convert[RAC1ITEM.BLASTER], world.player)
            or state.has_any_count(world.progressive_convert[RAC1ITEM.SUCK_CANNON], world.player)
            or state.has_any_count(world.progressive_convert[RAC1ITEM.DEVASTATOR], world.player)
            or state.has_any_count(world.progressive_convert[RAC1ITEM.TESLA_CLAW], world.player)
            or state.has_any([RAC1ITEM.VISIBOMB, RAC1ITEM.RYNO], world.player))


def has_40_gold_bolts(state: CollectionState, world: 'RacWorld') -> bool:
    lookup: dict[int, tuple[str, int]] = {
        1: (RAC1ITEM.GOLD_BOLT_1, 40),
        2: (RAC1ITEM.GOLD_BOLT_2, 20),
        3: (RAC1ITEM.GOLD_BOLT_3, 14),
        4: (RAC1ITEM.GOLD_BOLT_4, 10),
        5: (RAC1ITEM.GOLD_BOLT_5, 8),
        6: (RAC1ITEM.GOLD_BOLT_6, 7),
        7: (RAC1ITEM.GOLD_BOLT_7, 6),
        8: (RAC1ITEM.GOLD_BOLT_8, 5),
        9: (RAC1ITEM.GOLD_BOLT_9, 5),
        10: (RAC1ITEM.GOLD_BOLT_10, 4),
        11: (RAC1ITEM.GOLD_BOLT_11, 4),
        12: (RAC1ITEM.GOLD_BOLT_12, 4),
        13: (RAC1ITEM.GOLD_BOLT_13, 4),
        14: (RAC1ITEM.GOLD_BOLT_14, 3),
        15: (RAC1ITEM.GOLD_BOLT_15, 3),
        16: (RAC1ITEM.GOLD_BOLT_16, 3),
        17: (RAC1ITEM.GOLD_BOLT_17, 3),
        18: (RAC1ITEM.GOLD_BOLT_18, 3),
        19: (RAC1ITEM.GOLD_BOLT_19, 3),
        20: (RAC1ITEM.GOLD_BOLT_20, 2),
        21: (RAC1ITEM.GOLD_BOLT_21, 2),
        22: (RAC1ITEM.GOLD_BOLT_22, 2),
        23: (RAC1ITEM.GOLD_BOLT_23, 2),
        24: (RAC1ITEM.GOLD_BOLT_24, 2),
        25: (RAC1ITEM.GOLD_BOLT_25, 2),
        26: (RAC1ITEM.GOLD_BOLT_26, 2),
        27: (RAC1ITEM.GOLD_BOLT_27, 2),
        28: (RAC1ITEM.GOLD_BOLT_28, 2),
        29: (RAC1ITEM.GOLD_BOLT_29, 2),
        30: (RAC1ITEM.GOLD_BOLT_30, 2),
        31: (RAC1ITEM.GOLD_BOLT_31, 2),
        32: (RAC1ITEM.GOLD_BOLT_32, 2),
        33: (RAC1ITEM.GOLD_BOLT_33, 2),
        34: (RAC1ITEM.GOLD_BOLT_34, 2),
        35: (RAC1ITEM.GOLD_BOLT_35, 2),
        36: (RAC1ITEM.GOLD_BOLT_36, 2),
        37: (RAC1ITEM.GOLD_BOLT_37, 2),
        38: (RAC1ITEM.GOLD_BOLT_38, 2),
        39: (RAC1ITEM.GOLD_BOLT_39, 2),
        40: (RAC1ITEM.GOLD_BOLT_40, 1),
    }
    item, count = lookup[world.options.pack_size_gold_bolts.value]
    if state.count(item, world.player) < count:
        rac_logger.debug(f"Missing gold bolt packs from world, expected {count} but only had "
                         f"{state.count(item, world.player)}. Can reach {state.prog_items}")
    return state.has(item, world.player, count)


# TODO: Trick/Glitch logic

# Novalis
def novalis_cave_gb_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return has_explosive_weapon(state, world)  # Tricks


def novalis_underwater_caves_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return has_hydro_pack(state, world)  # Tricks


def novalis_gold_weapon_10k(state: CollectionState, world: 'RacWorld') -> bool:
    return has_40_gold_bolts(state, world) and has_10k_bolts(state, world)


def novalis_gold_weapon_20k(state: CollectionState, world: 'RacWorld') -> bool:
    return has_40_gold_bolts(state, world) and has_20k_bolts(state, world)


def novalis_gold_weapon_30k(state: CollectionState, world: 'RacWorld') -> bool:
    return has_40_gold_bolts(state, world) and has_30k_bolts(state, world)


def novalis_gold_weapon_60k(state: CollectionState, world: 'RacWorld') -> bool:
    return has_40_gold_bolts(state, world) and has_60k_bolts(state, world)


# Aridia
def aridia_trespasser_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return has_swingshot(state, world)  # Tricks


def aridia_laser_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return has_magneboots(state, world)  # Tricks


def aridia_cave_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return has_explosive_weapon(state, world)  # Tricks


# Kerwan
def kerwan_train_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return can_improved_jump(state, world)  # Tricks


def kerwan_course_gb_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return can_glide(state, world)  # Tricks


# Eudora
def eudora_suck_cannon_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return can_glide(state, world)  # Tricks


def eudora_henchman_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_swingshot(state, world)
            and has_trespasser(state, world)
            and can_improved_jump(state, world))


def eudora_skillpoint_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return has_short_range_weapon(state, world)


# Rilgar
def rilgar_hoverboard_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_hoverboard(state, world)
            and can_improved_jump(state, world))


def rilgar_bouncer_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_swingshot(state, world)
            and can_improved_jump(state, world)
            and has_hydrodisplacer(state, world))


def rilgar_underwater_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (rilgar_bouncer_rule(state, world)
            and has_o2_mask(state, world))


def rilgar_ryno_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return can_improved_jump(state, world) and has_150k_bolts(state, world)


def rilgar_metal_spots(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has(RAC1ITEM.RILGAR, world.player)
            and can_improved_jump(state, world))


# Blarg
def blarg_outside_gold_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_o2_mask(state, world)
            and has_trespasser(state, world))


def blarg_metal_spots(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has(RAC1ITEM.BLARG, world.player)
            and (
                    state.has(RAC1ITEM.SWINGSHOT, world.player)
                    or blarg_outside_gold_bolt_rule(state, world)
            ))


# Umbris
def umbris_snagglebeast_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_swingshot(state, world)
            and can_glide(state, world)
            and has_hydrodisplacer(state, world))


def umbris_pressure_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_swingshot(state, world)
            and can_glide(state, world))


def umbris_jump_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_swingshot(state, world)
            and can_glide(state, world)
            and has_hydrodisplacer(state, world))


def umbris_metal_spots(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has(RAC1ITEM.UMBRIS, world.player)
            and umbris_pressure_bolt_rule(state, world))


# Gaspar
def gaspar_skillpoint_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_visibomb(state, world)
            or (
                    has_swingshot(state, world)
                    and has_medium_range_weapon(state, world)
            ))


def gaspar_metal_spots(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has(RAC1ITEM.GASPAR, world.player)
            and (
                    has_swingshot(state, world)
                    or can_improved_jump(state, world)
            ))


# Orxon
def orxon_nanotech_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_o2_mask(state, world)
            and can_glide(state, world))


def orxon_ultra_nanotech_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return orxon_nanotech_rule(state, world) and has_30k_bolts(state, world)


def orxon_visibomb_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return has_o2_mask(state, world) and has_15k_bolts(state, world)


def orxon_visibomb_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (orxon_ratchet_infobot_rule(state, world)
            and has_visibomb(state, world))


def orxon_ratchet_infobot_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_o2_mask(state, world)
            and can_glide(state, world)
            and has_swingshot(state, world)
            and has_magneboots(state, world))


def orxon_sniper_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_o2_mask(state, world)
            and can_glide(state, world)
            and (
                    has_devastator(state, world)
                    or has_blaster(state, world)
                    or has_visibomb(state, world)
            ))


def orxon_hey_over_here_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_o2_mask(state, world)
            and can_glide(state, world)
            and has_magneboots(state, world)
            and has_taunter(state, world))


def orxon_metal_spots(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has(RAC1ITEM.ORXON, world.player)
            and has_o2_mask(state, world))


# Pokitaru
def pokitaru_ship_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_pilots_helmet(state, world)
            and can_ground_pound(state, world))


def pokitaru_persuader_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_raritanium(state, world)
            and has_trespasser(state, world)
            and has_hydrodisplacer(state, world))


def pokitaru_gold_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_swingshot(state, world)
            and can_ground_pound(state, world))


# Hoven
def hoven_infobot_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_short_range_weapon(state, world)
            and can_improved_jump(state, world))


def hoven_raritanium_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_swingshot(state, world)
            and can_improved_jump(state, world))


# Gemlik
def gemlik_quark_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_magneboots(state, world)
            and can_improved_jump(state, world)
            and has_long_range_weapon(state, world)
            and has_trespasser(state, world)
            and has_swingshot(state, world))


def gemlik_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_visibomb(state, world)
            and can_improved_jump(state, world)
            and has_trespasser(state, world))


# def gemlik_gold_weapon_rule(state: CollectionState, world: 'RacWorld') -> bool:
#     return (gemlik_quark_rule(state, world)
#             and has_40_gold_bolts(state, world)
#             and has_bolts(state, world))


def gemlik_metal_spots(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has(RAC1ITEM.GEMLIK, world.player)
            and gemlik_quark_rule(state, world))


# Oltanis
def oltanis_main_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_grindboots(state, world)
            and has_swingshot(state, world))


def oltanis_final_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_grindboots(state, world)
            and has_swingshot(state, world)
            and has_magneboots(state, world))


def oltanis_metal_spots(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has(RAC1ITEM.OLTANIS, world.player)
            and (
                    has_swingshot(state, world)
                    or has_magneboots(state, world)
            ))


# Quartu
def quartu_infiltrate_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_hologuise(state, world)
            and has_swingshot(state, world)
            and can_ground_pound(state, world))


def quartu_codebot_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_codebot(state, world)
            and has_swingshot(state, world))


def quartu_bolt_grabber_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_hydro_pack(state, world)
            and has_o2_mask(state, world))


# Kalebo III
def kalebo_switch_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has_any_count(world.progressive_convert[RAC1ITEM.BOMB_GLOVE], world.player)
            or state.has_any_count(world.progressive_convert[RAC1ITEM.BLASTER], world.player)
            or state.has_any_count(world.progressive_convert[RAC1ITEM.DEVASTATOR], world.player)
            or state.has_any_count(world.progressive_convert[RAC1ITEM.TESLA_CLAW], world.player)
            or state.has_any([RAC1ITEM.VISIBOMB, RAC1ITEM.RYNO], world.player))


def kalebo_hologuise_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_hoverboard(state, world)
            and has_swingshot(state, world)
            and has_grindboots(state, world)
            and kalebo_switch_rule(state, world))


def kalebo_metal_spots(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has(RAC1ITEM.KALEBO, world.player)
            and kalebo_switch_rule(state, world)
            and (has_swingshot(state, world)
                 or can_improved_jump(state, world)))


# Drek's Fleet
def fleet_infobot_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_magneboots(state, world)
            and has_pilots_helmet(state, world)
            and has_hologuise(state, world)
            and has_swingshot(state, world))


def fleet_water_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_o2_mask(state, world)
            and has_hydro_pack(state, world))


def fleet_second_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_magneboots(state, world)
            and has_pilots_helmet(state, world)
            and has_hologuise(state, world)
            and has_swingshot(state, world))


def fleet_metal_spots(state: CollectionState, world: 'RacWorld') -> bool:
    return (state.has(RAC1ITEM.FLEET, world.player)
            and (
                    has_hologuise(state, world)
                    or fleet_water_rule(state, world)
            ))


# Veldin
def veldin_global_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (has_trespasser(state, world)
            and has_magneboots(state, world)
            and has_hydrodisplacer(state, world)
            and can_ground_pound(state, world))


def veldin_grind_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (veldin_global_rule(state, world)
            and has_grindboots(state, world)
            and has_swingshot(state, world))


def veldin_halfway_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return veldin_global_rule(state, world)


def veldin_taunter_bolt_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (veldin_global_rule(state, world)
            and has_taunter(state, world))


def veldin_metal_spots(state: CollectionState, world: 'RacWorld') -> bool:
    return (veldin_global_rule(state, world)
            and has_swingshot(state, world))


def veldin_defeat_drek_rule(state: CollectionState, world: 'RacWorld') -> bool:
    return (veldin_global_rule(state, world)
            and has_swingshot(state, world))
