"""This module contains functionality for universal tracker"""

from typing import TYPE_CHECKING

from worlds.rac1.constants.slotdata import RAC1SLOT

if TYPE_CHECKING:
    from worlds.rac1.world import RacWorld


def setup_options_from_slot_data(world: "RacWorld") -> None:
    """Set the option values to the values already generated"""
    if hasattr(world.multiworld, "re_gen_passthrough"):
        if world.game in world.multiworld.re_gen_passthrough:
            world.using_ut = True
            world.passthrough = world.multiworld.re_gen_passthrough[world.game]
            world.options.start_inventory_from_pool.value = world.passthrough[RAC1SLOT.START_INVENTORY_FROM_POOL]
            world.options.starting_item.value = world.passthrough[RAC1SLOT.STARTING_ITEM]
            world.options.starting_location.value = world.passthrough[RAC1SLOT.STARTING_LOCATION]
            world.options.shuffle_weapons.value = world.passthrough[RAC1SLOT.SHUFFLE_WEAPONS]
            world.options.shuffle_gadgets.value = world.passthrough[RAC1SLOT.SHUFFLE_GADGETS]
            world.options.shuffle_packs.value = world.passthrough[RAC1SLOT.SHUFFLE_PACKS]
            world.options.shuffle_helmets.value = world.passthrough[RAC1SLOT.SHUFFLE_HELMETS]
            world.options.shuffle_boots.value = world.passthrough[RAC1SLOT.SHUFFLE_BOOTS]
            world.options.shuffle_extra_items.value = world.passthrough[RAC1SLOT.SHUFFLE_EXTRA_ITEMS]
            world.options.shuffle_gold_bolts.value = world.passthrough[RAC1SLOT.SHUFFLE_GOLD_BOLTS]
            world.options.shuffle_infobots.value = world.passthrough[RAC1SLOT.SHUFFLE_INFOBOTS]
            world.options.shuffle_gold_weapons.value = world.passthrough[RAC1SLOT.SHUFFLE_GOLD_WEAPONS]
            world.options.shuffle_skill_points.value = world.passthrough[RAC1SLOT.SHUFFLE_SKILLPOINTS]
            world.options.pack_size_gold_bolts.value = world.passthrough[RAC1SLOT.GOLD_BOLT_PACK_SIZE]
            world.options.pack_size_bolts.value = world.passthrough[RAC1SLOT.BOLT_PACK_SIZE]
            world.options.metal_bolt_multiplier.value = world.passthrough[RAC1SLOT.METAL_BOLT_MULTIPLIER]
            world.options.enable_bolt_multiplier.value = world.passthrough[RAC1SLOT.BOLT_MULTIPLIER]
            world.options.vendor_logic.value = world.passthrough[RAC1SLOT.VENDOR_LOGIC]
            world.options.progressive_weapons.value = world.passthrough[RAC1SLOT.PROGRESSIVE_WEAPONS]
            world.options.progressive_packs.value = world.passthrough[RAC1SLOT.PROGRESSIVE_PACKS]
            world.options.progressive_nanotech.value = world.passthrough[RAC1SLOT.PROGRESSIVE_NANOTECH]
        else:
            world.using_ut = False
    else:
        world.using_ut = False
