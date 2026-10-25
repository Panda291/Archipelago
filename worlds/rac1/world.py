import logging
from typing import Optional, Mapping, Any

from BaseClasses import Item, ItemClassification, LocationProgressType, Location
from Fill import FillError
from Options import OptionError
from rule_builder.rules import Has
from worlds.AutoWorld import World
from worlds.rac1.constants.items import RAC1ITEM
from worlds.rac1.constants.locations.general import RAC1LOCATION
from worlds.rac1.constants.locations.planets import RAC1PLANET
from worlds.rac1.constants.locations.skillpoints import RAC1SKILLPOINT
from worlds.rac1.constants.options import RAC1OPTION
from worlds.rac1.constants.pools import RAC1POOL
from worlds.rac1.constants.slotdata import RAC1SLOT
from worlds.rac1.data.items import ALL_ITEMS, get_item_groups, check_progressive_item, from_name, get_pool, \
    get_bolt_pack, STARTING_WEAPONS, GADGETS, GOLD_WEAPONS, get_starting_planets, progression_rules
from worlds.rac1.data.locations import ALL_POOLS, DEFAULT_LIST, RAC1LocationData
from worlds.rac1.data.planets import ALL_LOCATIONS, location_groups
from worlds.rac1.logic import veldin_defeat_drek_rule
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

    starting_item = RAC1ITEM.BOMB_GLOVE
    starting_planet = RAC1ITEM.NOVALIS

    def generate_early(self) -> None:
        rac_logger.debug(f"--generate_early--")
        rac_logger.debug(f"--start decide item pools--")

        self.disabled_pools = []
        self.restricted_pools = []
        self.useful_pools = []
        self.enabled_pools = []

        self.preplaced_items = []

        self.process_options()

        progression_rules(self)
        create_regions(self)

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

        starting_items, starting_planets = self.generate_starting_items()
        self.place_starting_items(starting_planets, starting_items)

        rac_logger.debug(f"--end decide item pools--")
        rac_logger.debug(f"--end generate_early--")

    def process_options(self):
        match self.options.shuffle_gold_bolts.value :
            case 1:
                self.enabled_pools += [RAC1POOL.GOLD_BOLTS]
            case 0:
                self.disabled_pools += [RAC1POOL.GOLD_BOLTS]
                self.options.pack_size_gold_bolts.value = 1
        match self.options.shuffle_skill_points.value:
            case 1:
                self.enabled_pools += [RAC1POOL.SKILLPOINT]
            case 0:
                self.disabled_pools += [RAC1POOL.SKILLPOINT]

        if self.options.shuffle_infobots.value == 0:
            self.options.starting_location.value = 0 # if all planets in vanilla locations, we can never start anywhere other than novalis

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
            starting_item = [item for item in starting_item if item not in [RAC1ITEM.DRONE_DEVICE]] # only items that can be held in hand

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

        return [self.starting_item], [self.starting_planet]

    def place_starting_items(self, starting_planet_list: list[str], starting_item_list: list[str]):
        """Take the list of starting planets and starting weapons and place them on locations or as precollected"""
        for item in starting_item_list:
            self.multiworld.push_precollected(self.create_item(item))
            self.preplaced_items.append(item)
        for planet in starting_planet_list:
            rac_logger.debug(f"startingplanet: {planet}")
            self.multiworld.push_precollected(self.create_item(planet))
            self.preplaced_items.append(planet)

        for name, count in self.options.start_inventory.items():
            item = from_name(name)
            if item.classification != ItemClassification.filler:
                self.preplaced_items += item.name

            for _ in range(count):
                self.multiworld.push_precollected(self.create_item(item.name))

        disabled_pools = self.disabled_pools
        restricted_pools = self.restricted_pools
        useful_pools = self.useful_pools
        rac_logger.debug(f"Disabled Shuffled Pools___")
        self.preplaced_items += self.fill_pool(disabled_pools, 0)
        rac_logger.debug(f"___Internal Shuffled Pools___")
        self.preplaced_items += self.fill_pool(restricted_pools, 1)
        rac_logger.debug(f"___Group Shuffled Pools___")
        self.preplaced_items += self.fill_pool(useful_pools, 2)

        boss_location = self.multiworld.get_location(RAC1LOCATION.VELDIN_DREK, self.player)
        boss_location.place_locked_item(self.create_event("Victory"))
        self.set_completion_rule(Has("Victory"))


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
                            self.get_location(loc.name).place_locked_item(self.create_item(vanilla_item.name))
                            add_items += [vanilla_item.name]
                            rac_logger.debug(f"vanilla: {loc.name}, item: {vanilla_item.name}")
            case 1: # restricted
                rac_logger.debug(f"Restricted Pools: {pools}")
                if pools:
                    raise OptionError(f"Options for 'random_same' are currently disabled")
            case 2: # useful
                rac_logger.debug(f"Useful Pools: {pools}")
                if pools:
                    raise OptionError(f"Options for 'random_item' are currently disabled")
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
        return

    def create_items(self) -> None:
        # After this step all locations and items need to be added/removed
        rac_logger.debug(f"_________START ITEM CREATION__________")
        itempool: list[Item] = [self.create_item(item.name) for item in get_pool(self.options) if item.name not in self.preplaced_items]
        own_location_count = len(self.multiworld.get_unfilled_locations(self.player))
        total_location_count = len(self.multiworld.get_unfilled_locations())
        existing_item_count = len(self.multiworld.itempool)
        placement_location_count = total_location_count - existing_item_count if self.multiworld.players > 1 else own_location_count
        excluded_count = self.get_excluded_count()
        already_placed = len(self.preplaced_items)
        item_count = len(itempool)
        filler_count = own_location_count - item_count

        rac_logger.debug(f"own_location_count: {own_location_count}\n"
                         f"total_location_count:{total_location_count}\n"
                         f"existing_item_count:{existing_item_count}\n"
                         f"item_count:{item_count}\n"
                         f"placement_location_count:{placement_location_count}\n"
                         f"excluded_count:{excluded_count}\n"
                         f"filler_count:{filler_count}\n"
                         f"already_placed:{already_placed}\n"
                         f"already_placed:{self.preplaced_items}\n"
                         f"self.multiworld.itempool: {self.multiworld.itempool}"
                         f"")

        if item_count > placement_location_count:
            self.handle_not_enough_locations(item_count - placement_location_count)

        self.multiworld.itempool.extend(itempool)

        if excluded_count > filler_count and self.multiworld.players == 1:
            self.handle_not_enough_locations(excluded_count - filler_count)

        if filler_count >= 0:
            filler = [self.create_item(get_bolt_pack(self.options)) for _ in range(filler_count)]
            self.multiworld.itempool.extend(filler)
        elif self.multiworld.players == 1:
            self.handle_not_enough_locations(-filler_count)

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
