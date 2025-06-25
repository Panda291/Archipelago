from dataclasses import dataclass

from Options import (Choice, PerGameCommonOptions, StartInventoryPool, Toggle)


class StartingItem(Choice):
    """Randomize what weapon you start the game with.
    Vanilla: Start with the Bomb Glove.
    Random_Weapon: Start with a random weapon.
    Random_Item: Start with any random weapon, gadget, pack, helmet, boots, item, or infobot.
    Unrestricted: Start with anything (including Gold Bolts).
    """
    display_name = "Starting Weapon"
    option_vanilla = 0
    option_random_weapon = 1
    option_random_item = 2
    option_unrestricted = 3
    default = 0


class EnableBoltMultiplier(Toggle):
    """Enables the bolt multiplier feature without being in New Game+."""
    display_name = "Enable Bolt Multiplier"


class ExtendWeaponProgression(Toggle):
    """If enabled, make all weapon tiers obtainable through weapon experience. This means LV2 (orange) weapons can
    upgrade into LV3 (yellow) weapons, which can then upgrade into LV4 (blue) weapons.
    This effectively makes all weapons that are usually restricted to NG+ available with enough grinding."""
    display_name = "Extended Weapon Progression"


@dataclass
class RacOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    # death_link: DeathLink
    # starting_item: StartingItem
    # enable_bolt_multiplier: EnableBoltMultiplier
    # extend_weapon_progression: ExtendWeaponProgression
