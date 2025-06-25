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


class GoldenWeaponProgression(Toggle):
    """If enabled, make golden weapons and their standard variants progressive items.
    This means that there are two copies of the regular item in the pool, when you collect one for the first time
    then it is the standard version, but collecting the second one will give you the golden version."""
    display_name = "Golden Weapon Progression"


@dataclass
class RacOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    # death_link: DeathLink
    # starting_item: StartingItem
    # enable_bolt_multiplier: EnableBoltMultiplier
    # extend_weapon_progression: GoldenWeaponProgression
