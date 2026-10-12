import logging
from typing import Optional, Mapping, Any

from BaseClasses import Item, ItemClassification, LocationProgressType
from Fill import FillError
from rule_builder.rules import Has
from worlds.AutoWorld import World
from worlds.rac1.constants.items import RAC1ITEM
from worlds.rac1.constants.locations.general import RAC1LOCATION
from worlds.rac1.constants.locations.skillpoints import RAC1SKILLPOINT
from worlds.rac1.constants.options import RAC1OPTION
from worlds.rac1.constants.pools import RAC1POOL
from worlds.rac1.constants.slotdata import RAC1SLOT
from worlds.rac1.data.items import ALL_ITEMS, get_item_groups, check_progressive_item, from_name, get_pool, \
    get_bolt_pack, STARTING_WEAPONS, GADGETS, GOLD_WEAPONS, get_starting_planets
from worlds.rac1.data.locations import ALL_POOLS, DEFAULT_LIST
from worlds.rac1.data.planets import ALL_LOCATIONS, location_groups
from worlds.rac1.options import RacOptions, ItemOptions, StartingItem, ShuffleWeapons, ShuffleGadgets, \
    GoldWeaponProgression, ShuffleGoldWeapons, ShuffleInfobots, StartingLocation, get_options_as_dict
from worlds.rac1.regions import create_regions

rac_logger = logging.getLogger(RAC1OPTION.GAME_TITLE_FULL)
rac_logger.setLevel(logging.DEBUG)

class RacItem(Item):
    game: str = RAC1OPTION.GAME_TITLE_FULL

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

    disabled_pools = []
    restricted_pools  = []
    useful_pools   = []
    enabled_pools = []

    preplaced_items = []

    starting_item = RAC1ITEM.BOMB_GLOVE
    starting_planet = RAC1ITEM.NOVALIS

    def generate_early(self) -> None:
        rac_logger.debug(f"--generate_early--")
        rac_logger.debug(f"--start decide item pools--")
        match self.options.shuffle_gold_bolts.value :
            case 1:
                self.enabled_pools += [RAC1POOL.GOLD_BOLTS]
            case 0:
                self.disabled_pools += [RAC1POOL.GOLD_BOLTS]
        match self.options.shuffle_skill_points.value:
            case 1:
                self.enabled_pools += [RAC1POOL.SKILLPOINT]
            case 0:
                self.disabled_pools += [RAC1POOL.SKILLPOINT]

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
                    self.restricted_pools += [pool.pool]
                case ItemOptions.option_random_item:
                    self.useful_pools += [pool.pool]
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

    def fill_pool(self, pools, scope) -> list:
        # this step should fill in items that have restricted locations, then also return them so they are removed from the pool
        add_items: list[Item] = []
        match scope:
            case 0: # disabled
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
                            self.get_location(loc.name).place_locked_item(vanilla_item)
                            add_items += [vanilla_item.name]
                            rac_logger.debug(f"vanilla: {loc.name}, item: {vanilla_item.name}")
            case 1: # restricted
                return []
            case 2: # useful
                return []
        return add_items

    def create_item(self, item: str, override: Optional[ItemClassification] = None) -> RacItem:
        new_name = check_progressive_item(self.options, item)
        if new_name is not item:
            rac_logger.warning(f"Item {item} was not initially set to its progressive item: {new_name}")
        if item == RAC1ITEM.GOLD_BOLT or item == RAC1ITEM.BOLT_PACK_GENERIC:
            rac_logger.warning(f"{item} should not be in the item pool!!! Please report")
        if override:
            return RacItem(new_name, override, self.item_name_to_id[new_name], self.player)
        item_data = from_name(new_name)
        return RacItem(new_name, item_data.classification, self.item_name_to_id[new_name], self.player)

    def create_event(self, event: str) -> RacItem:
        return RacItem(event, ItemClassification.progression, None, self.player)

    def pre_fill(self) -> None:
        disabled_pools = self.disabled_pools
        restricted_pools = self.restricted_pools
        useful_pools = self.useful_pools
        rac_logger.debug(f"Disabled Shuffled Pools___")
        self.preplaced_items += self.fill_pool(disabled_pools, 0)
        rac_logger.debug(f"___Internal Shuffled Pools___")
        self.preplaced_items += self.fill_pool(restricted_pools, 1)
        rac_logger.debug(f"___Group Shuffled Pools___")
        self.preplaced_items += self.fill_pool(useful_pools, 2)

        if (self.options.shuffle_weapons == ShuffleWeapons.option_vanilla
            or self.options.starting_item == StartingItem.option_vanilla):
            starting_item = RAC1ITEM.BOMB_GLOVE
        else:
            starting_item = []
            item_list = [item.name for item in STARTING_WEAPONS]
            if (self.options.starting_item == StartingItem.option_random_item
                    and self.options.shuffle_gadgets > ShuffleGadgets.option_random_same):
                item_list += [item.name for item in GADGETS]
            if (self.options.progressive_weapons.value is GoldWeaponProgression.option_normal and
                    self.options.shuffle_gold_weapons.value is not ShuffleGoldWeapons.option_vanilla):
                item_list += [item.name for item in GOLD_WEAPONS]

            self.random.shuffle(starting_item)
            self.starting_item = starting_item[0].name

        if (self.options.shuffle_infobots == ShuffleInfobots.option_vanilla
                or self.options.starting_location == StartingLocation.option_false):
            starting_planet = RAC1ITEM.NOVALIS
        else:
            starting_planet = [planet for planet in get_starting_planets(self.options)]
            self.random.shuffle(starting_planet)
            self.starting_planet = starting_planet[0].name

        self.preplaced_items += [self.starting_item, self.starting_planet]
        self.multiworld.push_precollected(self.create_item(self.starting_planet))
        self.multiworld.push_precollected(self.create_item(self.starting_item))

        for name, count in self.options.start_inventory.items():
            item = from_name(name)
            if item.classification != ItemClassification.filler:
                self.preplaced_items += item.name

            for _ in range(count):
                self.multiworld.push_precollected(item)

        return

    def create_items(self) -> None:
        # After this step all locations and items need to be added/removed
        rac_logger.debug(f"_________START ITEM CREATION__________")
        items_to_create_for_world: list[Item] = []

        items_to_create_for_world.extend([self.create_item(item.name) for item in get_pool(self.options)])

        unfilled = [loc for loc in self.multiworld.get_unfilled_locations(self.player) if not loc.is_event]
        rac_logger.debug(f"Items:{len(items_to_create_for_world)}, Locations:{len(unfilled)}")
        remain = len(unfilled) - len(items_to_create_for_world)
        if remain < 0:
            rac_logger.debug(f"Items unplaced: {items_to_create_for_world}")
            rac_logger.debug(f"Locations unfilled: {unfilled}")
            raise FillError(f"Item Count: {len(items_to_create_for_world)} exceeds Location count: {len(unfilled)}")
        elif remain == 0:
            pass
        else:
            rac_logger.debug(f"Not enough items to fill all locations. Adding {remain} filler items to the item pool")
            for _ in range(remain):
                items_to_create_for_world.append(self.create_item(get_bolt_pack(self.options)))
        rac_logger.debug(f"Add item pool to multiworld: {items_to_create_for_world}")
        self.multiworld.itempool.extend(items_to_create_for_world)
        rac_logger.debug(f"_________END ITEM CREATION__________")

    def create_regions(self) -> None:
        create_regions(self)

    def set_rules(self) -> None:
        boss_location = self.multiworld.get_location(RAC1LOCATION.VELDIN_DREK, self.player)
        boss_location.place_locked_item(self.create_event("Victory"))
        self.set_completion_rule(Has("Victory"))

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data: dict[str, Any] = {}
        slot_data |= get_options_as_dict(self.options)
        slot_data[RAC1SLOT.STARTING_PLANET] = self.item_name_to_id[self.starting_planet]
        return slot_data