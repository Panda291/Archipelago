"""This module defines the world class for the Ratchet and Clank 1 APWorld"""
import logging
from enum import Enum
from typing import Any, Counter, Mapping, Optional

from BaseClasses import Item, ItemClassification
from Fill import FillError
from Options import OptionError
from rule_builder.rules import Has
from worlds.AutoWorld import World
from worlds.rac1.constants.items import RAC1ITEM
from worlds.rac1.constants.options import RAC1OPTION
from worlds.rac1.constants.pools import RAC1POOL
from worlds.rac1.constants.slotdata import RAC1SLOT
from worlds.rac1.data.items import ALL_ITEMS, BOLT_SIZE_TO_PACK, GADGETS, GOLD_WEAPONS, STARTING_WEAPONS
from worlds.rac1.data.locations import ALL_POOLS, DEFAULT_LIST
from worlds.rac1.data.planets import ALL_LOCATIONS, location_groups
from worlds.rac1.items import (check_progressive_item, create_item, from_name, get_item_groups, get_pool,
                               get_starting_planets, progression_rules)
from worlds.rac1.options import (get_options_as_dict, GoldWeaponProgression, ItemOptions, RacOptions, ShuffleGadgets,
                                 ShuffleGoldBolts, ShuffleGoldWeapons, ShuffleInfobots, ShuffleSkillPoints,
                                 ShuffleWeapons, StartingItem, StartingLocation)
from worlds.rac1.regions import create_regions
from worlds.rac1.universal_tracker import setup_options_from_slot_data

rac_logger = logging.getLogger(RAC1OPTION.GAME_TITLE_FULL)
rac_logger.setLevel(logging.DEBUG)


class RacWorld(World):
    """
    Ratchet and Clank is a third-person shooter platform video game developed by Insomniac Games
    and published by Sony Computer Entertainment for the PlayStation 2 in 2002. It is the first
    game in the Ratchet and Clank series and the first game developed by Insomniac to not be owned by Universal
    Interactive.
    """
    game = RAC1OPTION.GAME_TITLE_FULL
    options_dataclass = RacOptions
    options: RacOptions
    topology_present = False

    item_name_to_id = {item.name: item.item_id for item in ALL_ITEMS}
    location_name_to_id = {location.name: location.location_id for location in ALL_LOCATIONS if
                           location.location_id}
    item_name_groups = get_item_groups()
    location_name_groups = location_groups

    starting_item = RAC1ITEM.BOMB_GLOVE
    starting_planet = RAC1ITEM.NOVALIS
    disabled_pools: list[str] = []
    restricted_pools: list[str] = []
    useful_pools: list[str] = []
    enabled_pools: list[str] = []
    preplaced_items: list[str] = []

    progressive_convert: dict[str, dict[str, int]] = {}

    class Scope(Enum):
        Disabled = 0
        Restricted = 1
        Useful = 2
        Enabled = 3

    def generate_early(self) -> None:
        rac_logger.debug(f"--generate_early--")
        rac_logger.debug(f"--start decide item pools--")

        self.disabled_pools = []
        self.restricted_pools = []
        self.useful_pools = []
        self.enabled_pools = []

        self.preplaced_items = []

        self.process_options()

        # implement .yaml-less Universal Tracker support
        setup_options_from_slot_data(self)

        progression_rules(self)
        self.generate_starting_items()

        shuffle_pools: list = [
            self.options.shuffle_infobots,
            self.options.shuffle_packs,
            self.options.shuffle_gadgets,
            self.options.shuffle_helmets,
            self.options.shuffle_boots,
            self.options.shuffle_weapons,
            self.options.shuffle_extra_items,
            self.options.shuffle_gold_weapons,
        ]

        for pool in shuffle_pools:
            rac_logger.debug(f"Option: {pool}")
            match pool.value:
                case ItemOptions.option_vanilla:
                    self.disabled_pools += [pool.pool]
                case ItemOptions.option_random_same:
                    # self.restricted_pools += [pool.pool]
                    self.enabled_pools += [pool.pool]  # temporary force full random
                case ItemOptions.option_random_item:
                    # self.useful_pools += [pool.pool]
                    self.enabled_pools += [pool.pool]  # temporary force full random
                case ItemOptions.option_unrestricted:
                    self.enabled_pools += [pool.pool]

        if not self.enabled_pools:
            rac_logger.debug(f"No pools enabled, setting to defaults")
            self.disabled_pools = [pool for pool in ALL_POOLS if pool not in DEFAULT_LIST]
            self.restricted_pools = []
            self.useful_pools = []
            self.enabled_pools = DEFAULT_LIST

        rac_logger.debug(f"Disabled Pools: {self.disabled_pools}")
        rac_logger.debug(f"Restricted Pools: {self.restricted_pools}")
        rac_logger.debug(f"Useful Pools: {self.useful_pools}")
        rac_logger.debug(f"Enabled Pools: {self.enabled_pools}")

        rac_logger.debug(f"--end decide item pools--")
        rac_logger.debug(f"--end generate_early--")

    def process_options(self):
        match self.options.shuffle_gold_bolts.value:
            case ShuffleGoldBolts.option_true:
                self.enabled_pools += [RAC1POOL.GOLD_BOLTS]
            case ShuffleGoldBolts.option_false:
                self.disabled_pools += [RAC1POOL.GOLD_BOLTS]
                self.options.pack_size_gold_bolts.value = 1
        match self.options.shuffle_skill_points.value:
            case ShuffleSkillPoints.option_true:
                self.enabled_pools += [RAC1POOL.SKILLPOINT]
            case ShuffleSkillPoints.option_false:
                self.disabled_pools += [RAC1POOL.SKILLPOINT]

        if self.options.shuffle_infobots.value == ShuffleInfobots.option_vanilla:
            self.options.starting_location.value = StartingLocation.option_false
            # if all planets in vanilla locations, we can never start anywhere other than novalis

        rac_logger.debug(f"options: {self.options}")

    def generate_starting_items(self):
        """Process player options to generate a list of early placed items, ensuring successful seed generation"""
        if (self.options.shuffle_weapons == ShuffleWeapons.option_vanilla
                or self.options.starting_item == StartingItem.option_vanilla):
            starting_item = [RAC1ITEM.BOMB_GLOVE]
        else:
            starting_item = [item.name for item in STARTING_WEAPONS]
            if (self.options.starting_item == StartingItem.option_random_item
                    and self.options.shuffle_gadgets > ShuffleGadgets.option_random_same):
                starting_item += [item.name for item in GADGETS]
            if (self.options.progressive_weapons.value is GoldWeaponProgression.option_normal and
                    self.options.shuffle_gold_weapons.value is not ShuffleGoldWeapons.option_vanilla):
                starting_item += [item.name for item in GOLD_WEAPONS]
            starting_item = [item for item in starting_item if
                             item not in [RAC1ITEM.DRONE_DEVICE]]  # only items that can be held in hand

        self.random.shuffle(starting_item)
        self.starting_item = starting_item[0]
        if self.starting_item in self.progressive_convert.keys():
            if self.progressive_convert[self.starting_item] is not {}:
                self.starting_item = list(self.progressive_convert[self.starting_item].keys())[0]

        if (self.options.shuffle_infobots == ShuffleInfobots.option_vanilla
                or self.options.starting_location == StartingLocation.option_false):
            starting_planet = [RAC1ITEM.NOVALIS]
        else:
            starting_planet = [planet.name for planet in get_starting_planets(self.options)]
        self.random.shuffle(starting_planet)
        self.starting_planet = starting_planet[0]

        # maybe also handle disabled pools here?

    def create_regions(self):
        create_regions(self)
        self.place_starting_items()

    def place_starting_items(self):
        """Take the list of starting planets and starting weapons and place them on locations or as precollected"""
        self.multiworld.push_precollected(self.create_item(self.starting_item))
        self.preplaced_items.append(self.starting_item)
        rac_logger.debug(f"Starting planet: {self.starting_planet}")
        self.multiworld.push_precollected(self.create_item(self.starting_planet))
        self.preplaced_items.append(self.starting_planet)

        # for name, count in self.options.start_inventory.items():
        #     item = from_name(name)
        #     if item.classification != ItemClassification.filler:
        #         self.preplaced_items += item.name
        #
        #     for _ in range(count):
        #         self.multiworld.push_precollected(self.create_item(item.name))

        disabled_pools = self.disabled_pools
        restricted_pools = self.restricted_pools
        useful_pools = self.useful_pools
        rac_logger.debug(f"Disabled Shuffled Pools___")
        self.preplaced_items += self.fill_pool(disabled_pools, self.Scope.Disabled)
        rac_logger.debug(f"___Internal Shuffled Pools___")
        self.preplaced_items += self.fill_pool(restricted_pools, self.Scope.Restricted)
        rac_logger.debug(f"___Group Shuffled Pools___")
        self.preplaced_items += self.fill_pool(useful_pools, self.Scope.Useful)

    def fill_pool(self, pools: list[str], scope: Scope) -> list[str]:
        # this step should fill in items that have restricted locations, then also return them so they are removed
        # from the pool
        add_items: list[str] = []
        match scope:
            case self.Scope.Disabled:
                for pool in pools:
                    rac_logger.debug(f"Disable Pool: {pool}")
                    # if pool == RAC1POOL.SKILLPOINT:
                    #     rac_logger.debug(f"Disabling Pool {pool}. no prefill needed")
                    #     continue
                    for loc in ALL_LOCATIONS:
                        if pool in loc.pools and loc.vanilla_item is not None:
                            vanilla_item = from_name(check_progressive_item(self.options, loc.vanilla_item))
                            if self.get_location(loc.name).item is not None:
                                raise FillError(f"Slot {self.player_name} selected vanilla {pool}, but Location:"
                                                f" {loc.name} was already filled")
                            self.get_location(loc.name).place_locked_item(self.create_item(vanilla_item.name))
                            add_items += [vanilla_item.name]
                            rac_logger.debug(f"vanilla: {loc.name}, item: {vanilla_item.name}")
            case self.Scope.Restricted:
                rac_logger.debug(f"Restricted Pools: {pools}")
                if pools:
                    raise OptionError(f"Options for 'random_same' are currently disabled")
            case self.Scope.Useful:
                rac_logger.debug(f"Useful Pools: {pools}")
                if pools:
                    raise OptionError(f"Options for 'random_item' are currently disabled")
        return add_items

    def set_rules(self):
        self.set_completion_rule(Has("Victory"))

    def create_item(self, name: str, override: Optional[ItemClassification] = None) -> Item:
        return create_item(self, name)

    def pre_fill(self) -> None:
        return

    def create_items(self) -> None:
        # After this step all locations and items need to be added/removed
        rac_logger.debug(f"_________START ITEM CREATION__________")
        exclusion_filler = [self.create_filler() for _ in range(self.get_excluded_count())]
        self.multiworld.itempool.extend(exclusion_filler)
        own_location_count = len(self.multiworld.get_unfilled_locations(self.player))
        itempool = get_pool(self)
        item_count = len(itempool + exclusion_filler)
        filler_count = own_location_count - item_count

        if filler_count < 0:
            self.handle_not_enough_locations(-filler_count)
            self.random.shuffle(itempool)
            # rac_logger.info(f"Placing {-filler_count} starting items")
            for item in range(-filler_count):
                # rac_logger.info(f"Starting with: {itempool[0].name}")
                self.push_precollected(itempool.pop(0))
        else:
            filler = [self.create_filler() for _ in range(filler_count)]
            self.multiworld.itempool.extend(filler)

        self.multiworld.itempool.extend(itempool)
        player_items = Counter(item.player for item in self.multiworld.itempool)
        player_locs = Counter(loc.player for loc in self.multiworld.get_locations() if not loc.item)
        assert player_items[self.player] == player_locs[self.player], (f"Player item count {player_items[self.player]} "
                                                                       f"and location count {player_locs[self.player]} "
                                                                       f"do not match")

    def get_filler_item_name(self) -> str:
        return BOLT_SIZE_TO_PACK[self.options.pack_size_bolts.value]

    def get_excluded_count(self) -> int:
        """Get the number of unique excluded locations for this player"""
        excluded_options = self.options.exclude_locations.value
        excluded_locations = set()
        for option in excluded_options:
            if option in location_groups:
                excluded_locations.update(location_groups[option])
            else:
                excluded_locations.add(option)
        return len(excluded_locations)

    def handle_not_enough_locations(self, count):
        """Check the available location and items counts, raise OptionErrors to warn the player of too few locations"""
        # excluded_count = self.get_excluded_count()
        option_list: list[str] = []
        if self.options.shuffle_skill_points.value == 0:
            option_list.append(RAC1OPTION.SHUFFLE_SKILLPOINTS)
        if self.options.shuffle_gold_bolts.value == 0:
            option_list.append(RAC1OPTION.SHUFFLE_GOLD_BOLTS)
        if self.options.shuffle_weapons.value == 0:
            option_list.append(RAC1OPTION.SHUFFLE_WEAPONS)
        if self.options.shuffle_boots.value == 0:
            option_list.append(RAC1OPTION.SHUFFLE_BOOTS)
        if self.options.shuffle_packs.value == 0:
            option_list.append(RAC1OPTION.SHUFFLE_PACKS)
        if self.options.shuffle_helmets.value == 0:
            option_list.append(RAC1OPTION.SHUFFLE_HELMETS)
        if self.options.shuffle_extra_items.value == 0:
            option_list.append(RAC1OPTION.SHUFFLE_EXTRA_ITEMS)
        if self.options.shuffle_infobots.value == 0:
            option_list.append(RAC1OPTION.SHUFFLE_INFOBOTS)
        if self.options.shuffle_gadgets.value == 0:
            option_list.append(RAC1OPTION.SHUFFLE_GADGETS)

        # if excluded_count > 30:
        #     option_list.append(RAC1OPTION.EXCLUDE)
        if not option_list:
            option_list: str = "dunno"  # ¯\_(''/)_/¯
        message = f"Not enough location options enabled! {count} items have nowhere to be placed."
        # if count >= 50:
        #     message += ("\nThis large of a difference requires Progressive Weapons to be disabled, Additional Sewer "
        #                 "Crystal Trade locations, Additional Nanotech level locations or Additional Weapon Level "
        #                 "locations.")
        if count <= 10 and sum(self.options.start_inventory_from_pool.value.values()) <= 10:
            message += "\nConsider adding some items to your starting_items_from_pool or "
        else:
            message += "\nConsider "
        message += f"adjusting some of the following options: {option_list}"
        raise OptionError(message)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data: dict[str, Any] = {}
        slot_data |= get_options_as_dict(self.options)
        slot_data |= self.orders
        slot_data[RAC1SLOT.STARTING_PLANET] = self.item_name_to_id[self.starting_planet]
        return slot_data

    # For Universal Tracker integration
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        """Trigger a regen in UT"""
        return slot_data
