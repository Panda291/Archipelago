from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .data import Items
from .data.Items import ItemData

if TYPE_CHECKING:
    from . import RacWorld


def get_classification(item: ItemData) -> ItemClassification:
    if item in Items.PLANETS:
        return ItemClassification.progression
    if item in [
        Items.HELI_PACK,
        Items.THRUSTER_PACK,
        Items.HYDRO_PACK,
        Items.SWINGSHOT,
        Items.MAGNEBOOTS,
        Items.GRINDBOOTS,
        Items.HYDRODISPLACER,
        Items.TAUNTER,
        Items.O2_MASK,
        Items.PILOTS_HELMET,
        Items.TRESPASSER,
        Items.HOLOGUISE,
        Items.CODEBOT,
        Items.RARITANIUM,
        Items.HOVERBOARD,
        Items.ZOOMERATOR,
        Items.BOMB_GLOVE,
        Items.DEVASTATOR,
        Items.VISIBOMB,
        Items.METAL_DETECTOR,
    ]:
        return ItemClassification.progression
    if item in [
        Items.BOLT_GRABBER,
        Items.PERSUADER,
        Items.PREMIUM_NANOTECH,
        Items.ULTRA_NANOTECH,
    ]:
        return ItemClassification.useful
    if item in Items.WEAPONS:
        return ItemClassification.useful

    return ItemClassification.filler


def create_planets(world: "RacWorld") -> list["Item"]:
    starting_planet = Items.NOVALIS_INFOBOT
    world.multiworld.push_precollected(world.create_item(starting_planet.name))
    planets_to_add = [planet for planet in Items.PLANETS if planet not in [starting_planet]]
    # add randomization later, just hardcode to get it working
    return [world.create_item(planet.name) for planet in planets_to_add]


def create_equipment(world: "RacWorld") -> list["Item"]:
    equipment_to_add: list[ItemData] = list(Items.EQUIPMENT_AND_WEAPONS)

    # Starting Item
    # starting_item: list[ItemData] = list(Items.ALL)

    # starting_item: list[EquipmentData] = []
    # if world.options.starting_item == StartingItem.option_random_weapon:
    #     starting_item = list(Items.WEAPONS)
    # elif world.options.starting_item == StartingItem.option_random_item:
    #     starting_item = [item for item in Items.ALL if item.name is not "Gold Bolt" ]
    # elif world.options.starting_item == StartingItem.option_unrestricted:
    #     starting_item = list(Items.ALL)

    # if len(starting_item) > 0:
    #     world.random.shuffle(starting_item)
    # else:
    starting_item = [Items.BOMB_GLOVE]

    world.multiworld.push_precollected(world.create_item(starting_item[0].name))
    world.starting_item = [starting_item[0]]
    if Items.BOMB_GLOVE not in world.starting_item:
        equipment_to_add.append(Items.BOMB_GLOVE)

    # # Gadgetron Vendor
    # if world.options.randomize_gadgetron_vendor:
    #     equipment_to_add += [i for i in Items.GADGETRON_VENDOR_WEAPONS if i not in world.starting_item]

    # # Megacorp Vendor
    # if world.options.randomize_megacorp_vendor:
    #     equipment_to_add += [i for i in Items.MEGACORP_VENDOR_WEAPONS if i not in world.starting_item]

    # Misc Weapons
    # equipment_to_add += [Items.SHEEPINATOR]

    # Take out expensive items if they are excluded and in the pool.
    # if world.options.exclude_very_expensive_items:
    #     if Items.RYNO_II in equipment_to_add:
    #         location = world.multiworld.get_location(Locations.BARLOW_GADGETRON_5.name, world.player)
    #         location.place_locked_item(world.create_item(Items.RYNO_II.name))
    #         equipment_to_add.remove(Items.RYNO_II)
    #     if Items.ZODIAC in equipment_to_add:
    #         location = world.multiworld.get_location(Locations.ARANOS_VENDOR_WEAPON_2.name, world.player)
    #         location.place_locked_item(world.create_item(Items.ZODIAC.name))
    #         equipment_to_add.remove(Items.ZODIAC)

    # equipment_to_add = [equipment for equipment in equipment_to_add if equipment.item_id not in [starting_item[
    # 0].item_id]]
    precollected_ids: list[int] = [item.code for item in world.multiworld.precollected_items[world.player]]
    equipment_to_add = [equipment for equipment in equipment_to_add if equipment.item_id not in precollected_ids]

    return [world.create_item(equipment.name) for equipment in equipment_to_add]


def create_collectables(world: "RacWorld") -> list["Item"]:
    collectable_items: list["Item"] = []

    for _ in range(40):
        collectable_items.append(world.create_item(Items.GOLD_BOLT.name))

    return collectable_items
