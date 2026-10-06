from dataclasses import dataclass
from typing import Any

from Options import Choice, PerGameCommonOptions, Range, TextChoice, Toggle
from worlds.rac1.constants.options import RAC1OPTION
from worlds.rac1.constants.pools import RAC1POOL
from worlds.rac1.constants.slotdata import RAC1SLOT


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


class StartingItem(Choice):
    """Randomize what weapon you start the game with.
        vanilla: Start with the Bomb Glove.
        random_same: Start with a random weapon.
        random_item: Start with any random equipable item, weapons or gadgets.
    """
    display_name = RAC1OPTION.STARTING_ITEM
    rich_text_doc = True
    value: int
    option_vanilla = 0
    option_random_same = 1
    option_random_item = 2
    default = 0
    alias_true = 2
    alias_false = 0
    pool = RAC1POOL.START_ITEM


class StartingLocation(Toggle):
    """Randomize what Planet you start on"""
    display_name = RAC1OPTION.SHUFFLE_STARTING_PLANET
    default = 1


class ShuffleWeapons(ItemOptions):
    """Randomize Weapon locations
        vanilla: Weapons are unshuffled.
        random_same: Weapons are shuffled to other Weapon locations.
        random_item: Weapons are shuffled anywhere, useful items are found at Weapon locations.
        unrestricted: Weapons are shuffled anywhere, anything can be found at Weapon locations.
    """
    display_name = RAC1OPTION.SHUFFLE_WEAPONS
    rich_text_doc = True
    default = 3
    pool = RAC1POOL.WEAPONS


class EarlyWeapon(TextChoice):
    """
        Force a weapon to be in your sphere 1.
        Set to off if 'Randomize Weapon locations' option is set to 'vanilla or random_same'.
    """
    display_name = RAC1OPTION.EARLY_WEAPON
    rich_text_doc = True


class ShuffleGadgets(ItemOptions):
    """Randomize Gadget locations
        vanilla: Gadgets are unshuffled.
        random_same: Gadgets are shuffled to other Gadget locations.
        random_item: Gadgets are shuffled anywhere, useful items are found at Gadget locations.
        unrestricted: Gadgets are shuffled anywhere, anything can be found at Gadget locations.
    """
    display_name = RAC1OPTION.SHUFFLE_GADGETS
    rich_text_doc = True
    default = 3
    pool = RAC1POOL.GADGETS


class ShufflePacks(ItemOptions):
    """Randomize Pack locations
        vanilla: Packs are unshuffled.
        random_same: Packs are shuffled to other Pack locations.
        random_item: Packs are shuffled anywhere, useful items are found at Pack locations.
        unrestricted: Packs are shuffled anywhere, anything can be found at Pack locations.
    """
    display_name = RAC1OPTION.SHUFFLE_PACKS
    rich_text_doc = True
    default = 3
    pool = RAC1POOL.PACKS


class ShuffleHelmets(ItemOptions):
    """Randomize Helmet locations
        vanilla: Helmets are unshuffled.
        random_same: Helmets are shuffled to other Helmet locations.
        random_item: Helmets are shuffled anywhere, useful items are found at Helmet locations.
        unrestricted: Helmets are shuffled anywhere, anything can be found at Helmet locations.
    """
    display_name = RAC1OPTION.SHUFFLE_HELMETS
    rich_text_doc = True
    default = 3
    pool = RAC1POOL.HELMETS


class ShuffleBoots(ItemOptions):
    """Randomize Boot locations
        vanilla: Boots are unshuffled.
        random_same: Boots are shuffled to other Boot locations.
        random_item: Boots are shuffled anywhere, useful items are found at Boot locations.
        unrestricted: Boots are shuffled anywhere, anything can be found at Boot locations.
    """
    display_name = RAC1OPTION.SHUFFLE_BOOTS
    rich_text_doc = True
    default = 3
    pool = RAC1POOL.BOOTS


class ShuffleExtraItems(ItemOptions):
    """Randomize Extra Item locations (Hoverboard, Persuader, etc...)
        vanilla: Extra Items are unshuffled.
        random_same: Extra Items are shuffled to other Extra Item locations.
        random_item: Extra Items are shuffled anywhere, useful items are found at Extra Item locations.
        unrestricted: Extra Items are shuffled anywhere, anything can be found at Extra Item locations.
    """
    display_name = RAC1OPTION.SHUFFLE_EXTRA_ITEMS
    rich_text_doc = True
    default = 3
    pool = RAC1POOL.EXTRA_ITEMS


class ShuffleGoldBolts(Toggle):
    """Randomize Gold Bolt locations"""
    display_name = RAC1OPTION.SHUFFLE_GOLD_BOLTS
    default = 1


class GoldBoltPackSize(Range):
    """Gold Bolts received each time you collect a pack of Gold Bolts (Gold Bolts Shuffle Off forces this to 1)"""
    display_name = RAC1OPTION.GOLD_BOLT_PACK_SIZE
    default = 8
    range_start = 1
    range_end = 40


class BoltPackSize(Choice):
    """Bolts received each time you collect a pack of Bolts."""
    display_name = RAC1OPTION.BOLT_PACK_SIZE
    option_0 = 0
    option_1 = 1
    option_10 = 10
    option_100 = 100
    option_250 = 250
    option_500 = 500
    option_750 = 750
    option_1000 = 1000
    option_2000 = 2000
    option_3000 = 3000
    option_4000 = 4000
    option_5000 = 5000
    option_6000 = 6000
    option_7000 = 7000
    option_8000 = 8000
    option_9000 = 9000
    option_10000 = 10000
    option_12500 = 12500
    option_15000 = 15000
    option_17500 = 17500
    option_20000 = 20000
    option_25000 = 25000
    option_30000 = 30000
    option_40000 = 40000
    option_50000 = 50000
    option_75000 = 75000
    option_100000 = 100000
    default = option_15000


class ShuffleInfobots(ItemOptions):
    """Randomize Infobot locations
        vanilla: Infobots are unshuffled.
        random_same: Infobots are shuffled to other Infobot locations.
        random_item: Infobots are shuffled anywhere, useful items are found at Infobot locations.
        WARNING! Using random_same, or random_item with no other pool selected, is likely to fail on solo worlds.
        unrestricted: Infobots are shuffled anywhere, anything can be found at Infobot locations.
    """
    display_name = RAC1OPTION.SHUFFLE_INFOBOTS  #
    rich_text_doc = True
    default = 3
    pool = RAC1POOL.INFOBOTS


class ShuffleGoldWeapons(ItemOptions):
    """Randomize Gold Weapon locations
        vanilla: Gold Weapons are unshuffled.
        random_same: Gold Weapons are shuffled to other Gold Weapon locations.
        random_item: Gold Weapons are shuffled anywhere, useful items are found at Gold Weapon locations.
        unrestricted: Gold Weapons are shuffled anywhere, anything can be found at Gold Weapon locations.
    """
    display_name = RAC1OPTION.SHUFFLE_GOLD_WEAPONS
    rich_text_doc = True
    default = 3
    pool = RAC1POOL.GOLD_WEAPONS


class ShuffleSkillPoints(Toggle):
    """Randomize Skillpoint locations"""
    display_name = RAC1OPTION.SHUFFLE_SKILLPOINTS
    default = 1


class EnableBoltMultiplier(Range):
    """Enables the bolt multiplier feature without being in New Game+."""
    display_name = RAC1OPTION.BOLT_MULTIPLIER
    default = 5
    range_start = 1
    range_end = 20


class MDBoltMultiplier(Range):
    """Bolt Multiplier when using the metal detector"""
    display_name = RAC1OPTION.METAL_DETECTOR_MULTIPLIER
    default = 35
    range_start = 1
    range_end = 100


class VendorOptions(Choice):
    """Should expensive purchases require enough bolts in logic?
        no_bolt_logic: logic only considers reaching the location of expensive items, not the purchase cost
        all_bolts: logic requires enough bolt packs, planets unlocked and bolt multiplier level to purchase expensive
        items, or metal detector with dig spots available
        only_metal_detector: logic requires the metal detector, with access to dig spots, to purchase expensive items
    """
    display_name = RAC1OPTION.PURCHASING_LOGIC
    rich_text_doc = True
    value: int
    option_no_bolt_logic = 0
    option_all_bolts = 1
    option_only_metal_detector = 2
    alias_true = 0
    alias_false = 1
    default = 1


class ProgressiveOptions(Choice):
    """Template
        vanilla: These items are not progressive, each item is independent of other items.
        progressive: These items are progressive, collecting multiple of an item will upgrade it.
        progressive_reversed: These items are progressive, the order of upgrading is reversed.
        progressive_random: These items are progressive, the order of upgrading is random.
    """
    value: int
    option_vanilla = 0
    option_progressive = 1
    option_progressive_reversed = 2
    option_progressive_random = 3
    alias_true = 1
    alias_false = 0


class GoldWeaponProgression(ProgressiveOptions):
    """
    If enabled, make gold weapons and their standard variants progressive items.
        vanilla: Gold Weapons and Weapons are not progressive, Gold Weapons do nothing until their base item is
        found.
        normal: Gold Weapons and Weapons are not progressive, each item is independent of other items.
        progressive: Gold Weapons and Weapons are progressive, collecting multiple of an item will upgrade it.
        progressive_reversed: Gold Weapons and Weapons are progressive, the order of upgrading is reversed.
        progressive_random: Gold Weapons and Weapons are progressive, the order of upgrading is random."""
    display_name = RAC1OPTION.PROGRESSIVE_WEAPONS
    rich_text_doc = True
    value: int
    option_vanilla = 0
    option_normal = 1
    option_progressive = 2
    option_progressive_reversed = 3
    option_progressive_random = 4
    alias_true = 2
    alias_false = 0
    default = 1


class PackProgression(ProgressiveOptions):
    """
        vanilla: Packs are not progressive, each item is independent of other items.
        progressive: Packs are progressive, collecting multiple of an item will upgrade it.
        progressive_reversed: Packs are progressive, the order of upgrading is reversed.
        progressive_random: Packs are progressive, the order of upgrading is random.
    """
    display_name = RAC1OPTION.PROGRESSIVE_PACKS
    rich_text_doc = True
    value: int
    option_vanilla = 0
    option_progressive = 1
    option_progressive_reversed = 2
    option_progressive_random = 3
    alias_true = 1
    alias_false = 0


class HelmetProgression(ProgressiveOptions):
    """
        vanilla: Helmets are not progressive, each item is independent of other items.
        progressive: Helmets are progressive, collecting multiple of an item will upgrade it.
        progressive_reversed: Helmets are progressive, the order of upgrading is reversed.
        progressive_random: Helmets are progressive, the order of upgrading is random.
    """
    display_name = RAC1OPTION.PROGRESSIVE_HELMETS
    rich_text_doc = True
    value: int
    option_vanilla = 0
    option_progressive = 1
    option_progressive_reversed = 2
    option_progressive_random = 3
    alias_true = 1
    alias_false = 0


class BootsProgression(ProgressiveOptions):
    """
        vanilla: Grind and Magneboots are not progressive, each item is independent of other items.
        progressive: Grind and Magneboots are progressive, collecting multiple of an item will upgrade it.
        progressive_reversed: Grind and Magneboots are progressive, the order of upgrading is reversed.
        progressive_random: Grind and Magneboots are progressive, the order of upgrading is random.
    """
    display_name = RAC1OPTION.PROGRESSIVE_BOOTS
    rich_text_doc = True
    value: int
    option_vanilla = 0
    option_progressive = 1
    option_progressive_reversed = 2
    option_progressive_random = 3
    alias_true = 1
    alias_false = 0


class HoverboardProgression(ProgressiveOptions):
    """
        vanilla: Hoverboard and Zoomerator are not progressive, each item is independent of other items.
        progressive: Hoverboard and Zoomerator are progressive, collecting multiple of an item will upgrade it.
        progressive_reversed: Hoverboard and Zoomerator are progressive, the order of upgrading is reversed.
        progressive_random: Hoverboard and Zoomerator are progressive, the order of upgrading is random.
    """
    display_name = RAC1OPTION.PROGRESSIVE_HOVERBOARD
    rich_text_doc = True
    value: int
    option_vanilla = 0
    option_progressive = 1
    option_progressive_reversed = 2
    option_progressive_random = 3
    alias_true = 1
    alias_false = 0


class RaritaniumProgression(ProgressiveOptions):
    """
        vanilla: Raritanium and Persuader are not progressive, each item is independent of other items.
        progressive: Raritanium and Persuader are progressive, collecting multiple of an item will upgrade it.
        progressive_reversed: Raritanium and Persuader are progressive, the order of upgrading is reversed.
        progressive_random: Raritanium and Persuader are progressive, the order of upgrading is random.
    """
    display_name = RAC1OPTION.PROGRESSIVE_RARITANIUM
    rich_text_doc = True
    value: int
    option_vanilla = 0
    option_progressive = 1
    option_progressive_reversed = 2
    option_progressive_random = 3
    alias_true = 1
    alias_false = 0


class NanotechProgression(ProgressiveOptions):
    """
        vanilla: Nanotech is not progressive, each item is independent of other items.
        progressive: Nanotech are progressive, collecting multiple of an item will upgrade it.
        progressive_reversed: Nanotech are progressive, the order of upgrading is reversed.
        progressive_random: Nanotech are progressive, the order of upgrading is random.
    """
    display_name = RAC1OPTION.PROGRESSIVE_NANOTECH
    rich_text_doc = True
    value: int
    option_vanilla = 0
    option_progressive = 1
    option_progressive_reversed = 2
    option_progressive_random = 3
    alias_true = 1
    alias_false = 0


@dataclass
class RacOptions(PerGameCommonOptions):
    # death_link: DeathLink
    starting_item: StartingItem
    starting_location: StartingLocation
    shuffle_weapons: ShuffleWeapons
    shuffle_gadgets: ShuffleGadgets
    shuffle_packs: ShufflePacks
    shuffle_helmets: ShuffleHelmets
    shuffle_boots: ShuffleBoots
    shuffle_extra_items: ShuffleExtraItems
    shuffle_gold_bolts: ShuffleGoldBolts
    shuffle_infobots: ShuffleInfobots
    shuffle_gold_weapons: ShuffleGoldWeapons
    shuffle_skill_points: ShuffleSkillPoints
    pack_size_gold_bolts: GoldBoltPackSize
    pack_size_bolts: BoltPackSize
    metal_bolt_multiplier: MDBoltMultiplier
    enable_bolt_multiplier: EnableBoltMultiplier
    vendor_logic: VendorOptions
    progressive_weapons: GoldWeaponProgression
    progressive_packs: PackProgression
    progressive_helmets: HelmetProgression
    progressive_boots: BootsProgression
    progressive_hoverboard: HoverboardProgression
    progressive_raritanium: RaritaniumProgression
    progressive_nanotech: NanotechProgression


def get_options_as_dict(options: RacOptions) -> dict[str, Any]:
    return {
        # RAC1SLOT.DEATHLINK,
        RAC1SLOT.STARTING_ITEM: options.starting_item.value,
        RAC1SLOT.STARTING_LOCATION: options.starting_location.value,
        RAC1SLOT.SHUFFLE_WEAPONS: options.shuffle_weapons.value,
        RAC1SLOT.SHUFFLE_GADGETS: options.shuffle_gadgets.value,
        RAC1SLOT.SHUFFLE_PACKS: options.shuffle_packs.value,
        RAC1SLOT.SHUFFLE_HELMETS: options.shuffle_helmets.value,
        RAC1SLOT.SHUFFLE_BOOTS: options.shuffle_boots.value,
        RAC1SLOT.SHUFFLE_EXTRA_ITEMS: options.shuffle_extra_items.value,
        RAC1SLOT.SHUFFLE_GOLD_BOLTS: options.shuffle_gold_bolts.value,
        RAC1SLOT.SHUFFLE_INFOBOTS: options.shuffle_infobots.value,
        RAC1SLOT.SHUFFLE_GOLD_WEAPONS: options.shuffle_gold_weapons.value,
        RAC1SLOT.SHUFFLE_SKILLPOINTS: options.shuffle_skill_points.value,
        RAC1SLOT.GOLD_BOLT_PACK_SIZE: options.pack_size_gold_bolts.value,
        RAC1SLOT.BOLT_PACK_SIZE: options.pack_size_bolts.value,
        RAC1SLOT.METAL_BOLT_MULTIPLIER: options.metal_bolt_multiplier.value,
        RAC1SLOT.BOLT_MULTIPLIER: options.enable_bolt_multiplier.value,
        RAC1SLOT.VENDOR_LOGIC: options.vendor_logic.value,
        RAC1SLOT.PROGRESSIVE_WEAPONS: options.progressive_weapons.value,
        RAC1SLOT.PROGRESSIVE_PACKS: options.progressive_packs.value,
        RAC1SLOT.PROGRESSIVE_HELMETS: options.progressive_helmets.value,
        RAC1SLOT.PROGRESSIVE_BOOTS: options.progressive_boots.value,
        RAC1SLOT.PROGRESSIVE_HOVERBOARD: options.progressive_hoverboard.value,
        RAC1SLOT.PROGRESSIVE_TRADE: options.progressive_raritanium.value,
        RAC1SLOT.PROGRESSIVE_NANOTECH: options.progressive_nanotech.value,
    }