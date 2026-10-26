from typing import TYPE_CHECKING

from BaseClasses import Item
from worlds.rac1.constants.items import RAC1ITEM
from worlds.rac1.constants.pools import RAC1POOL
from worlds.rac1.constants.progressive_orders import RAC1ORDER
from worlds.rac1.data.items import (ALL_BOOTS, ALL_EXTRA_ITEMS, ALL_HELMETS, ALL_ITEMS, ALL_PACKS, ALL_WEAPONS, GADGETS,
                                    GOLD_BOLTS, GOLD_WEAPONS, ITEM_POOL, ItemData, NON_PROGRESSIVE_NANOTECHS,
                                    NON_PROGRESSIVE_WEAPONS, PACKS, PLANETS, PROGRESSIVE_NANOTECHS, PROGRESSIVE_PACKS,
                                    PROGRESSIVE_WEAPONS, RAC1ItemData, STARTING_PLANETS)
from worlds.rac1.options import GoldWeaponProgression, NanotechProgression, PackProgression, RacOptions, ShuffleInfobots

if TYPE_CHECKING:
    from worlds.rac1 import RacWorld


def progression_rules(world: "RacWorld"):
    world.orders = {
        RAC1ORDER.SUCK_CANNON: [RAC1ItemData.SUCK_CANNON.item_id, RAC1ItemData.GOLD_SUCK_CANNON.item_id],
        RAC1ORDER.BOMB_GLOVE: [RAC1ItemData.BOMB_GLOVE.item_id, RAC1ItemData.GOLD_BOMB_GLOVE.item_id],
        RAC1ORDER.DEVASTATOR: [RAC1ItemData.DEVASTATOR.item_id, RAC1ItemData.GOLD_DEVASTATOR.item_id],
        RAC1ORDER.BLASTER: [RAC1ItemData.BLASTER.item_id, RAC1ItemData.GOLD_BLASTER.item_id],
        RAC1ORDER.PYROCITOR: [RAC1ItemData.PYROCITOR.item_id, RAC1ItemData.GOLD_PYROCITOR.item_id],
        RAC1ORDER.MINE_GLOVE: [RAC1ItemData.MINE_GLOVE.item_id, RAC1ItemData.GOLD_MINE_GLOVE.item_id],
        RAC1ORDER.TESLA_CLAW: [RAC1ItemData.TESLA_CLAW.item_id, RAC1ItemData.GOLD_TESLA_CLAW.item_id],
        RAC1ORDER.GLOVE_OF_DOOM: [RAC1ItemData.GLOVE_OF_DOOM.item_id, RAC1ItemData.GOLD_GLOVE_OF_DOOM.item_id],
        RAC1ORDER.MORPH_O_RAY: [RAC1ItemData.MORPH_O_RAY.item_id, RAC1ItemData.GOLD_MORPH_O_RAY.item_id],
        RAC1ORDER.DECOY_GLOVE: [RAC1ItemData.DECOY_GLOVE.item_id, RAC1ItemData.GOLD_DECOY_GLOVE.item_id],
        RAC1ORDER.PACKS: [RAC1ItemData.HELI_PACK.item_id, RAC1ItemData.THRUSTER_PACK.item_id,
                          RAC1ItemData.HYDRO_PACK.item_id],
        RAC1ORDER.NANOTECH: [RAC1ItemData.PREMIUM_NANOTECH.item_id, RAC1ItemData.ULTRA_NANOTECH.item_id],
    }
    world.progressive_convert = {
        RAC1ITEM.HELI_PACK: {RAC1ITEM.HELI_PACK: 1},
        RAC1ITEM.THRUSTER_PACK: {RAC1ITEM.THRUSTER_PACK: 1},
        RAC1ITEM.HYDRO_PACK: {RAC1ITEM.HYDRO_PACK: 1},
        RAC1ITEM.SUCK_CANNON: {RAC1ITEM.SUCK_CANNON: 1},
        RAC1ITEM.GOLD_SUCK_CANNON: {RAC1ITEM.SUCK_CANNON: 1, RAC1ITEM.GOLD_SUCK_CANNON: 1},
        RAC1ITEM.BOMB_GLOVE: {RAC1ITEM.BOMB_GLOVE: 1},
        RAC1ITEM.GOLD_BOMB_GLOVE: {RAC1ITEM.BOMB_GLOVE: 1, RAC1ITEM.GOLD_BOMB_GLOVE: 1},
        RAC1ITEM.DEVASTATOR: {RAC1ITEM.DEVASTATOR: 1},
        RAC1ITEM.GOLD_DEVASTATOR: {RAC1ITEM.DEVASTATOR: 1, RAC1ITEM.GOLD_DEVASTATOR: 1},
        RAC1ITEM.BLASTER: {RAC1ITEM.BLASTER: 1},
        RAC1ITEM.GOLD_BLASTER: {RAC1ITEM.BLASTER: 1, RAC1ITEM.GOLD_BLASTER: 1},
        RAC1ITEM.PYROCITOR: {RAC1ITEM.PYROCITOR: 1},
        RAC1ITEM.GOLD_PYROCITOR: {RAC1ITEM.PYROCITOR: 1, RAC1ITEM.GOLD_PYROCITOR: 1},
        RAC1ITEM.MINE_GLOVE: {RAC1ITEM.MINE_GLOVE: 1},
        RAC1ITEM.GOLD_MINE_GLOVE: {RAC1ITEM.MINE_GLOVE: 1, RAC1ITEM.GOLD_MINE_GLOVE: 1},
        RAC1ITEM.TESLA_CLAW: {RAC1ITEM.TESLA_CLAW: 1},
        RAC1ITEM.GOLD_TESLA_CLAW: {RAC1ITEM.TESLA_CLAW: 1, RAC1ITEM.GOLD_TESLA_CLAW: 1},
        RAC1ITEM.GLOVE_OF_DOOM: {RAC1ITEM.GLOVE_OF_DOOM: 1},
        RAC1ITEM.GOLD_GLOVE_OF_DOOM: {RAC1ITEM.GLOVE_OF_DOOM: 1, RAC1ITEM.GOLD_GLOVE_OF_DOOM: 1},
        RAC1ITEM.MORPH_O_RAY: {RAC1ITEM.MORPH_O_RAY: 1},
        RAC1ITEM.GOLD_MORPH_O_RAY: {RAC1ITEM.MORPH_O_RAY: 1, RAC1ITEM.GOLD_MORPH_O_RAY: 1},
        RAC1ITEM.DECOY_GLOVE: {RAC1ITEM.DECOY_GLOVE: 1},
        RAC1ITEM.GOLD_DECOY_GLOVE: {RAC1ITEM.DECOY_GLOVE: 1, RAC1ITEM.GOLD_DECOY_GLOVE: 1},
        RAC1ITEM.PREMIUM_NANOTECH: {RAC1ITEM.PREMIUM_NANOTECH: 1, RAC1ITEM.PROGRESSIVE_NANOTECH: 1},
        RAC1ITEM.ULTRA_NANOTECH: {RAC1ITEM.ULTRA_NANOTECH: 1, RAC1ITEM.PROGRESSIVE_NANOTECH: 2},
    }
    match world.options.progressive_weapons.value:
        case GoldWeaponProgression.option_normal:
            world.progressive_convert[RAC1ITEM.SUCK_CANNON] = {RAC1ITEM.SUCK_CANNON: 1,
                                                               RAC1ITEM.GOLD_SUCK_CANNON: 1}
            world.progressive_convert[RAC1ITEM.GOLD_SUCK_CANNON] = {RAC1ITEM.GOLD_SUCK_CANNON: 1}
            world.progressive_convert[RAC1ITEM.BOMB_GLOVE] = {RAC1ITEM.BOMB_GLOVE: 1,
                                                              RAC1ITEM.GOLD_BOMB_GLOVE: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BOMB_GLOVE] = {RAC1ITEM.GOLD_BOMB_GLOVE: 1}
            world.progressive_convert[RAC1ITEM.DEVASTATOR] = {RAC1ITEM.DEVASTATOR: 1,
                                                              RAC1ITEM.GOLD_DEVASTATOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DEVASTATOR] = {RAC1ITEM.GOLD_DEVASTATOR: 1}
            world.progressive_convert[RAC1ITEM.BLASTER] = {RAC1ITEM.BLASTER: 1,
                                                           RAC1ITEM.GOLD_BLASTER: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BLASTER] = {RAC1ITEM.GOLD_BLASTER: 1}
            world.progressive_convert[RAC1ITEM.PYROCITOR] = {RAC1ITEM.PYROCITOR: 1,
                                                             RAC1ITEM.GOLD_PYROCITOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_PYROCITOR] = {RAC1ITEM.GOLD_PYROCITOR: 1}
            world.progressive_convert[RAC1ITEM.MINE_GLOVE] = {RAC1ITEM.MINE_GLOVE: 1,
                                                              RAC1ITEM.GOLD_MINE_GLOVE: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MINE_GLOVE] = {RAC1ITEM.GOLD_MINE_GLOVE: 1}
            world.progressive_convert[RAC1ITEM.TESLA_CLAW] = {RAC1ITEM.TESLA_CLAW: 1,
                                                              RAC1ITEM.GOLD_TESLA_CLAW: 1}
            world.progressive_convert[RAC1ITEM.GOLD_TESLA_CLAW] = {RAC1ITEM.GOLD_TESLA_CLAW: 1}
            world.progressive_convert[RAC1ITEM.GLOVE_OF_DOOM] = {RAC1ITEM.GLOVE_OF_DOOM: 1,
                                                                 RAC1ITEM.GOLD_GLOVE_OF_DOOM: 1}
            world.progressive_convert[RAC1ITEM.GOLD_GLOVE_OF_DOOM] = {RAC1ITEM.GOLD_GLOVE_OF_DOOM: 1}
            world.progressive_convert[RAC1ITEM.MORPH_O_RAY] = {RAC1ITEM.MORPH_O_RAY: 1,
                                                               RAC1ITEM.GOLD_MORPH_O_RAY: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MORPH_O_RAY] = {RAC1ITEM.GOLD_MORPH_O_RAY: 1}
            world.progressive_convert[RAC1ITEM.DECOY_GLOVE] = {RAC1ITEM.DECOY_GLOVE: 1,
                                                               RAC1ITEM.GOLD_DECOY_GLOVE: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DECOY_GLOVE] = {RAC1ITEM.GOLD_DECOY_GLOVE: 1}
        case GoldWeaponProgression.option_progressive:
            world.progressive_convert[RAC1ITEM.SUCK_CANNON] = {RAC1ITEM.PROGRESSIVE_SUCK: 1}
            world.progressive_convert[RAC1ITEM.GOLD_SUCK_CANNON] = {RAC1ITEM.PROGRESSIVE_SUCK: 2}
            world.progressive_convert[RAC1ITEM.BOMB_GLOVE] = {RAC1ITEM.PROGRESSIVE_BOMB: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BOMB_GLOVE] = {RAC1ITEM.PROGRESSIVE_BOMB: 2}
            world.progressive_convert[RAC1ITEM.DEVASTATOR] = {RAC1ITEM.PROGRESSIVE_DEVASTATOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DEVASTATOR] = {RAC1ITEM.PROGRESSIVE_DEVASTATOR: 2}
            world.progressive_convert[RAC1ITEM.BLASTER] = {RAC1ITEM.PROGRESSIVE_BLASTER: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BLASTER] = {RAC1ITEM.PROGRESSIVE_BLASTER: 2}
            world.progressive_convert[RAC1ITEM.PYROCITOR] = {RAC1ITEM.PROGRESSIVE_PYROCITOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_PYROCITOR] = {RAC1ITEM.PROGRESSIVE_PYROCITOR: 2}
            world.progressive_convert[RAC1ITEM.MINE_GLOVE] = {RAC1ITEM.PROGRESSIVE_MINE: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MINE_GLOVE] = {RAC1ITEM.PROGRESSIVE_MINE: 2}
            world.progressive_convert[RAC1ITEM.TESLA_CLAW] = {RAC1ITEM.PROGRESSIVE_TESLA: 1}
            world.progressive_convert[RAC1ITEM.GOLD_TESLA_CLAW] = {RAC1ITEM.PROGRESSIVE_TESLA: 2}
            world.progressive_convert[RAC1ITEM.GLOVE_OF_DOOM] = {RAC1ITEM.PROGRESSIVE_DOOM: 1}
            world.progressive_convert[RAC1ITEM.GOLD_GLOVE_OF_DOOM] = {RAC1ITEM.PROGRESSIVE_DOOM: 2}
            world.progressive_convert[RAC1ITEM.MORPH_O_RAY] = {RAC1ITEM.PROGRESSIVE_MORPH: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MORPH_O_RAY] = {RAC1ITEM.PROGRESSIVE_MORPH: 2}
            world.progressive_convert[RAC1ITEM.DECOY_GLOVE] = {RAC1ITEM.PROGRESSIVE_DECOY: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DECOY_GLOVE] = {RAC1ITEM.PROGRESSIVE_DECOY: 2}
        case _:
            pass

    match world.options.progressive_packs.value:
        case PackProgression.option_progressive:
            world.progressive_convert[RAC1ITEM.HELI_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 1}
            world.progressive_convert[RAC1ITEM.THRUSTER_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 2}
            world.progressive_convert[RAC1ITEM.HYDRO_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 3}
        case PackProgression.option_progressive_reversed:
            world.orders[RAC1ORDER.PACKS].reverse()
            world.progressive_convert[RAC1ITEM.HELI_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 3}
            world.progressive_convert[RAC1ITEM.THRUSTER_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 2}
            world.progressive_convert[RAC1ITEM.HYDRO_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 1}
        case PackProgression.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.PACKS])
            world.progressive_convert[RAC1ITEM.HELI_PACK] = {
                RAC1ITEM.PROGRESSIVE_PACK: 1 + world.orders[RAC1ORDER.PACKS].index(RAC1ItemData.HELI_PACK.item_id)}
            world.progressive_convert[RAC1ITEM.THRUSTER_PACK] = {
                RAC1ITEM.PROGRESSIVE_PACK: 1 + world.orders[RAC1ORDER.PACKS].index(RAC1ItemData.THRUSTER_PACK.item_id)}
            world.progressive_convert[RAC1ITEM.HYDRO_PACK] = {
                RAC1ITEM.PROGRESSIVE_PACK: 1 + world.orders[RAC1ORDER.PACKS].index(RAC1ItemData.HYDRO_PACK.item_id)}
        case _:
            pass

    match world.options.progressive_nanotech.value:
        case NanotechProgression.option_progressive:
            world.progressive_convert[RAC1ITEM.PREMIUM_NANOTECH] = {RAC1ITEM.PROGRESSIVE_NANOTECH: 1}
            world.progressive_convert[RAC1ITEM.ULTRA_NANOTECH] = {RAC1ITEM.PROGRESSIVE_NANOTECH: 2}
        case NanotechProgression.option_progressive_reversed:
            world.orders[RAC1ORDER.NANOTECH].reverse()
            world.progressive_convert[RAC1ITEM.PREMIUM_NANOTECH] = {RAC1ITEM.PROGRESSIVE_NANOTECH: 2}
            world.progressive_convert[RAC1ITEM.ULTRA_NANOTECH] = {RAC1ITEM.PROGRESSIVE_NANOTECH: 1}
        case NanotechProgression.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.NANOTECH])
            world.progressive_convert[RAC1ITEM.PREMIUM_NANOTECH] = {
                RAC1ITEM.PROGRESSIVE_NANOTECH:
                    1 + world.orders[RAC1ORDER.NANOTECH].index(RAC1ItemData.PREMIUM_NANOTECH.item_id)}
            world.progressive_convert[RAC1ITEM.ULTRA_NANOTECH] = {
                RAC1ITEM.PROGRESSIVE_NANOTECH:
                    1 + world.orders[RAC1ORDER.NANOTECH].index(RAC1ItemData.ULTRA_NANOTECH.item_id)}
        case _:
            pass
    return


def get_pool(world: "RacWorld") -> list[Item]:
    _options = world.options
    pool: list[Item] = []
    for item in ITEM_POOL:
        if (item in PROGRESSIVE_WEAPONS and _options.progressive_weapons.value <
                GoldWeaponProgression.option_progressive):
            continue
        if (item in NON_PROGRESSIVE_WEAPONS and _options.progressive_weapons.value !=
                GoldWeaponProgression.option_normal):
            pool += [item]
        for item in GOLD_WEAPONS:
            pool += [item]
        if _options.progressive_packs.value > PackProgression.option_vanilla:
            for item in PROGRESSIVE_PACKS:
                pool += [item]
        else:
            for item in PACKS:
                pool += [item]
        if _options.progressive_nanotech.value > NanotechProgression.option_vanilla:
            for item in PROGRESSIVE_NANOTECHS:
                pool += [item]
        else:
            for item in NON_PROGRESSIVE_NANOTECHS:
                pool += [item]
        lookup: dict[int, tuple[ItemData, int]] = {
            1: (RAC1ItemData.GOLD_BOLT_1, 40),
            2: (RAC1ItemData.GOLD_BOLT_2, 30),
            3: (RAC1ItemData.GOLD_BOLT_3, 20),
            4: (RAC1ItemData.GOLD_BOLT_4, 15),
            5: (RAC1ItemData.GOLD_BOLT_5, 12),
            6: (RAC1ItemData.GOLD_BOLT_6, 10),
            7: (RAC1ItemData.GOLD_BOLT_7, 9),
            8: (RAC1ItemData.GOLD_BOLT_8, 8),
            9: (RAC1ItemData.GOLD_BOLT_9, 7),
            10: (RAC1ItemData.GOLD_BOLT_10, 6),
            11: (RAC1ItemData.GOLD_BOLT_11, 5),
            12: (RAC1ItemData.GOLD_BOLT_12, 5),
            13: (RAC1ItemData.GOLD_BOLT_13, 5),
            14: (RAC1ItemData.GOLD_BOLT_14, 4),
            15: (RAC1ItemData.GOLD_BOLT_15, 4),
            16: (RAC1ItemData.GOLD_BOLT_16, 4),
            17: (RAC1ItemData.GOLD_BOLT_17, 4),
            18: (RAC1ItemData.GOLD_BOLT_18, 4),
            19: (RAC1ItemData.GOLD_BOLT_19, 4),
            20: (RAC1ItemData.GOLD_BOLT_20, 3),
            21: (RAC1ItemData.GOLD_BOLT_21, 3),
            22: (RAC1ItemData.GOLD_BOLT_22, 3),
            23: (RAC1ItemData.GOLD_BOLT_23, 3),
            24: (RAC1ItemData.GOLD_BOLT_24, 3),
            25: (RAC1ItemData.GOLD_BOLT_25, 3),
            26: (RAC1ItemData.GOLD_BOLT_26, 3),
            27: (RAC1ItemData.GOLD_BOLT_27, 3),
            28: (RAC1ItemData.GOLD_BOLT_28, 3),
            29: (RAC1ItemData.GOLD_BOLT_29, 3),
            30: (RAC1ItemData.GOLD_BOLT_30, 2),
            31: (RAC1ItemData.GOLD_BOLT_31, 2),
            32: (RAC1ItemData.GOLD_BOLT_32, 2),
            33: (RAC1ItemData.GOLD_BOLT_33, 2),
            34: (RAC1ItemData.GOLD_BOLT_34, 2),
            35: (RAC1ItemData.GOLD_BOLT_35, 2),
            36: (RAC1ItemData.GOLD_BOLT_36, 2),
            37: (RAC1ItemData.GOLD_BOLT_37, 2),
            38: (RAC1ItemData.GOLD_BOLT_38, 2),
            39: (RAC1ItemData.GOLD_BOLT_39, 2),
            40: (RAC1ItemData.GOLD_BOLT_40, 1),
        }
        for _ in range(lookup[_options.pack_size_gold_bolts.value][1]):
            pool += [lookup[_options.pack_size_gold_bolts.value][0]]
        # [world.create_item(item.name) for item in  if
        #  item.name not in world.preplaced_items]
    return pool


def get_starting_planets(_options: RacOptions) -> list[ItemData]:
    planets: list[ItemData] = []
    for item in STARTING_PLANETS:
        planets += [item]
    if _options.shuffle_infobots.value >= ShuffleInfobots.option_unrestricted:
        planets += [RAC1ItemData.ARIDIA]
        if _options.shuffle_helmets.value >= ShuffleInfobots.option_unrestricted:
            planets += [RAC1ItemData.GASPAR]
        if _options.shuffle_gold_bolts.value:
            planets += [RAC1ItemData.HOVEN]
    return planets


def from_id(item_id: int) -> ItemData:
    matching = [item for item in ALL_ITEMS if item.item_id == item_id]
    if len(matching) == 0:
        raise ValueError(f"No item data for item id '{item_id}'")
    assert len(matching) < 2, f"{len(matching)} item data found with id '{item_id}'. Items are: {matching}"
    return matching[0]


def from_name(item_name: str) -> ItemData:
    matching = [item for item in ALL_ITEMS if item.name == item_name]
    if len(matching) == 0:
        raise ValueError(f"No item data for '{item_name}'")
    # if item_name != GOLD_BOLT :
    #     assert len(matching) < 2, f"Multiple item data with name '{item_name}'. Please report."
    return matching[0]


def get_item_groups() -> dict[str, set[str]]:
    groups: dict[str, set[str]] = {
        RAC1POOL.WEAPONS: {w.name for w in ALL_WEAPONS},
        RAC1POOL.GADGETS: {g.name for g in GADGETS},
        RAC1POOL.PACKS: {p.name for p in ALL_PACKS},
        RAC1POOL.HELMETS: {h.name for h in ALL_HELMETS},
        RAC1POOL.BOOTS: {b.name for b in ALL_BOOTS},
        RAC1POOL.EXTRA_ITEMS: {e.name for e in ALL_EXTRA_ITEMS},
        RAC1POOL.GOLD_BOLTS: {c.name for c in GOLD_BOLTS},
        RAC1POOL.INFOBOTS: {i.name for i in PLANETS},
        # RAC1POOL.SKILLPOINT: {s.name for s in SKILLPOINTS},
    }
    return groups


def check_progressive_item(_options: RacOptions, item: str) -> str:
    new_item = item
    match from_name(item).pool:
        case RAC1POOL.WEAPONS | RAC1POOL.GOLD_WEAPONS:
            if _options.progressive_weapons.value > GoldWeaponProgression.option_normal:
                match item:
                    case RAC1ITEM.SUCK_CANNON:
                        new_item = RAC1ITEM.PROGRESSIVE_SUCK
                    case RAC1ITEM.GOLD_SUCK_CANNON:
                        new_item = RAC1ITEM.PROGRESSIVE_SUCK
                    case RAC1ITEM.BOMB_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_BOMB
                    case RAC1ITEM.GOLD_BOMB_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_BOMB
                    case RAC1ITEM.DEVASTATOR:
                        new_item = RAC1ITEM.PROGRESSIVE_DEVASTATOR
                    case RAC1ITEM.GOLD_DEVASTATOR:
                        new_item = RAC1ITEM.PROGRESSIVE_DEVASTATOR
                    case RAC1ITEM.BLASTER:
                        new_item = RAC1ITEM.PROGRESSIVE_BLASTER
                    case RAC1ITEM.GOLD_BLASTER:
                        new_item = RAC1ITEM.PROGRESSIVE_BLASTER
                    case RAC1ITEM.PYROCITOR:
                        new_item = RAC1ITEM.PROGRESSIVE_PYROCITOR
                    case RAC1ITEM.GOLD_PYROCITOR:
                        new_item = RAC1ITEM.PROGRESSIVE_PYROCITOR
                    case RAC1ITEM.MINE_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_MINE
                    case RAC1ITEM.GOLD_MINE_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_MINE
                    case RAC1ITEM.TESLA_CLAW:
                        new_item = RAC1ITEM.PROGRESSIVE_TESLA
                    case RAC1ITEM.GOLD_TESLA_CLAW:
                        new_item = RAC1ITEM.PROGRESSIVE_TESLA
                    case RAC1ITEM.GLOVE_OF_DOOM:
                        new_item = RAC1ITEM.PROGRESSIVE_DOOM
                    case RAC1ITEM.GOLD_GLOVE_OF_DOOM:
                        new_item = RAC1ITEM.PROGRESSIVE_DOOM
                    case RAC1ITEM.MORPH_O_RAY:
                        new_item = RAC1ITEM.PROGRESSIVE_MORPH
                    case RAC1ITEM.GOLD_MORPH_O_RAY:
                        new_item = RAC1ITEM.PROGRESSIVE_MORPH
                    case RAC1ITEM.DECOY_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_DECOY
                    case RAC1ITEM.GOLD_DECOY_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_DECOY
        case RAC1POOL.PACKS:
            if _options.progressive_packs.value:
                new_item = RAC1ITEM.PROGRESSIVE_PACK
        case RAC1POOL.EXTRA_ITEMS:
            match item:
                case RAC1ITEM.PREMIUM_NANOTECH | RAC1ITEM.ULTRA_NANOTECH:
                    if _options.progressive_nanotech.value:
                        new_item = RAC1ITEM.PROGRESSIVE_NANOTECH
        case _:
            pass
    return new_item
