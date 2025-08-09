from dataclasses import dataclass
from typing import Any

from Options import (Choice, PerGameCommonOptions, TextChoice, Toggle)


class ItemOptions(Choice):
    """Template
        vanilla: Option selects the vanilla items for these locations.
        random_same: Option selects an item from the same item group as the vanilla item for these locations.
        random_item: Option selects any weapon, gadget, pack, helmet, boots, item, or infobot to be shuffled to these
            locations.
        unrestricted: Option selects anything to be shuffled to these locations (including Gold Bolts and Skillpoints).
    """
    value: int
    option_vanilla = 0
    option_random_same = 1
    option_random_item = 2
    option_unrestricted = 3
    alias_true = 3
    alias_false = 0


class StartingItem(ItemOptions):
    """Randomize what weapon you start the game with.
        vanilla: Start with the Bomb Glove.
        random_same: Start with a random weapon.
        random_item: Start with any random weapon, gadget, pack, helmet, boots, item, or infobot.
        unrestricted: Start with anything (including Gold Bolts and Skillpoints).
    """
    display_name = "Starting Weapon"
    default = 0
    pool = "StartItem"


class ShuffleWeapons(ItemOptions):
    """Randomize Weapon locations
        vanilla: Weapons are unshuffled.
        random_same: Weapons are shuffled to other Weapon locations.
        random_item: Weapons are shuffled anywhere, useful items are found at Weapon locations.
        unrestricted: Weapons are shuffled anywhere, anything can be found at Weapon locations.
    """
    display_name = "Shuffle Weapons"
    default = 3
    pool = "Weapons"


# TODO: Early Weapon option, off, shuffled amount (user states amount), list (user lists items)
class EarlyWeapon(TextChoice):
    """
        Force a weapon to be in your sphere 1.
        Set to off if 'Randomize Weapon locations' option is set to 'vanilla or random_same'.
    """
    display_name = "Early Weapon"


class ShuffleGadgets(ItemOptions):
    """Randomize Gadget locations
        vanilla: Gadgets are unshuffled.
        random_same: Gadgets are shuffled to other Gadget locations.
        random_item: Gadgets are shuffled anywhere, useful items are found at Gadget locations.
        unrestricted: Gadgets are shuffled anywhere, anything can be found at Gadget locations.
    """
    display_name = "Shuffle Gadgets"
    default = 3
    pool = "Gadgets"


class ShufflePacks(ItemOptions):
    """Randomize Pack locations
        vanilla: Packs are unshuffled.
        random_same: Packs are shuffled to other Pack locations.
        random_item: Packs are shuffled anywhere, useful items are found at Pack locations.
        unrestricted: Packs are shuffled anywhere, anything can be found at Pack locations.
    """
    display_name = "Shuffle Packs"
    default = 3
    pool = "Packs"


class ShuffleHelmets(ItemOptions):
    """Randomize Helmet locations
        vanilla: Helmets are unshuffled.
        random_same: Helmets are shuffled to other Helmet locations.
        random_item: Helmets are shuffled anywhere, useful items are found at Helmet locations.
        unrestricted: Helmets are shuffled anywhere, anything can be found at Helmet locations.
    """
    display_name = "Shuffle Helmets"
    default = 3
    pool = "Helmets"


class ShuffleBoots(ItemOptions):
    """Randomize Boot locations
        vanilla: Boots are unshuffled.
        random_same: Boots are shuffled to other Boot locations.
        random_item: Boots are shuffled anywhere, useful items are found at Boot locations.
        unrestricted: Boots are shuffled anywhere, anything can be found at Boot locations.
    """
    display_name = "Shuffle Boots"
    default = 3
    pool = "Boots"


class ShuffleExtraItems(ItemOptions):
    """Randomize Extra Item locations (Hoverboard, Persuader, etc...)
        vanilla: Extra Items are unshuffled.
        random_same: Extra Items are shuffled to other Extra Item locations.
        random_item: Extra Items are shuffled anywhere, useful items are found at Extra Item locations.
        unrestricted: Extra Items are shuffled anywhere, anything can be found at Extra Item locations.
    """
    display_name = "Shuffle Extra Items"
    default = 3
    pool = "ExtraItems"


class ShuffleGoldBolts(Toggle):
    """Randomize Gold Bolt locations"""
    display_name = "Shuffle Gold Bolts"
    default = 1


class ShuffleInfobots(ItemOptions):
    """Randomize Infobot locations
        vanilla: Infobots are unshuffled.
        random_same: Infobots are shuffled to other Infobot locations.
        random_item: Infobots are shuffled anywhere, useful items are found at Infobot locations.
        WARNING! Using random_same, or random_item with no other pool selected, is likely to fail on solo worlds.
        unrestricted: Infobots are shuffled anywhere, anything can be found at Infobot locations.
    """
    display_name = "Shuffle Infobots"
    default = 3
    pool = "Infobots"


class EnableBoltMultiplier(Toggle):
    """Enables the bolt multiplier feature without being in New Game+."""
    display_name = "Enable Bolt Multiplier"


class GoldenWeaponProgression(Toggle):
    """If enabled, make golden weapons and their standard variants progressive items.
        This means that there are two copies of the regular item in the pool, when you collect one for the first time
        then it is the standard version, but collecting the second one will give you the golden version."""
    display_name = "Golden Weapon Progression"


@dataclass
class RacOptions(PerGameCommonOptions):
    # death_link: DeathLink
    # starting_item: StartingItem
    shuffle_weapons: ShuffleWeapons
    shuffle_gadgets: ShuffleGadgets
    shuffle_packs: ShufflePacks
    shuffle_helmets: ShuffleHelmets
    shuffle_boots: ShuffleBoots
    shuffle_extra_items: ShuffleExtraItems
    shuffle_gold_bolts: ShuffleGoldBolts
    shuffle_infobots: ShuffleInfobots
    # enable_bolt_multiplier: EnableBoltMultiplier
    # extend_weapon_progression: GoldenWeaponProgression


def get_options_as_dict(options: RacOptions) -> dict[str, Any]:
    return {
        # "death_link",
        "start_inventory_from_pool": dict(),
        # "starting_item": options.starting_item.option_vanilla,
        "shuffle_weapons": options.shuffle_weapons.value,
        "shuffle_gadgets": options.shuffle_gadgets.value,
        "shuffle_packs": options.shuffle_packs.value,
        "shuffle_helmets": options.shuffle_helmets.value,
        "shuffle_boots": options.shuffle_boots.value,
        "shuffle_extra_items": options.shuffle_extra_items.value,
        "shuffle_gold_bolts": options.shuffle_gold_bolts.value,
        "shuffle_infobots": options.shuffle_infobots.value,
    }
