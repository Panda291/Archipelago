import logging
from typing import Any, Mapping, Optional, Sequence

from BaseClasses import CollectionState, Item, ItemClassification, Location, Tutorial
from Fill import fill_restrictive, FillError, sweep_from_pool
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, SuffixIdentifier, Type
from . import ItemPool
from .data import Items, Locations, Planets
from .data.Items import CollectableData, ItemData
from .data.Locations import (ALL_POOLS, DEFAULT_LIST, LocationData, POOL_BOOT, POOL_EXTRA_ITEM, POOL_GADGET,
                             POOL_GOLD_BOLT, POOL_GOLDEN_WEAPON, POOL_HELMET, POOL_INFOBOT, POOL_PACK, POOL_SKILLPOINT,
                             POOL_WEAPON)
from .data.Planets import ALL_LOCATIONS, location_groups, PlanetData
from .Options import RacOptions, ShuffleInfobots, ShuffleWeapons, StartingItem, StartingLocation
from .Regions import create_regions

rac_logger = logging.getLogger("Ratchet & Clank")
rac_logger.setLevel(logging.DEBUG)


def run_client(_url: Optional[str] = None):
    # from .RacClient import launch
    # launch_subprocess(launch, name="RacClient")
    components.append(Component("Ratchet & Clank Client", func=run_client, component_type=Type.CLIENT,
                                file_identifier=SuffixIdentifier(".aprac")))


class RacWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Ratchet & Clank for Archipelago",
        "English",
        "setup.md",
        "setup/en",
        ["Panad"],
    )]


class RacItem(Item):
    game: str = "Ratchet & Clank"


class RacWorld(World):
    """
    Ratchet & Clank is a third-person shooter platform video game developed by Insomniac Games
    and published by Sony Computer Entertainment for the PlayStation 2 in 2002. It is the first
    game in the Ratchet & Clank series and the first game developed by Insomniac to not be owned by Universal
    Interactive.
    """
    game = "Ratchet & Clank"
    web = RacWeb()
    options_dataclass = RacOptions
    options: RacOptions
    topology_present = False
    item_name_to_id = {item.name: item.item_id for item in Items.ALL}
    location_name_to_id = {location.name: location.location_id for location in Planets.ALL_LOCATIONS if
                           location.location_id}
    item_name_groups = Items.get_item_groups()
    location_name_groups = location_groups
    starting_planet = Items.NOVALIS_INFOBOT.name
    starting_items: list[Item] = []
    preplaced_locations: list[Location] = []

    # def get_filler_item_name(self) -> str:
    #     return Items.BOLT_PACK.name

    def generate_early(self) -> None:
        rac_logger.debug(f"_________START EARLY GENERATION____________")
        rac_logger.warning(
            "INCOMPLETE WORLD! Slot '%s' is using an unfinished alpha world that is not stable yet!",
            self.player_name)
        rac_logger.warning("INCOMPLETE WORLD! Slot '%s' may require send_location/send_item for completion!",
                           self.player_name)
        self.starting_items = []
        self.preplaced_locations = []
        rac_logger.debug(f"Pre-placed Item List: {[loc.item for loc in self.preplaced_locations]}")

        # TODO: Item Pools

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
        disabled_pools = []
        restricted_pools = []
        useful_pools = []
        enabled_pools = []

        if self.options.shuffle_gold_bolts.value:
            enabled_pools += [POOL_GOLD_BOLT]
        else:
            disabled_pools += [POOL_GOLD_BOLT]
        rac_logger.debug(f"Iterating through Options:")
        for pool_option in shuffle_pools:
            rac_logger.debug(f"Option: {pool_option}")
            match pool_option.value:  # TODO: starting item and planet
                case Options.ItemOptions.option_vanilla:
                    disabled_pools += [pool_option.pool]
                case Options.ItemOptions.option_random_same:
                    restricted_pools += [pool_option.pool]
                case Options.ItemOptions.option_random_item:
                    useful_pools += [pool_option.pool]
                case Options.ItemOptions.option_unrestricted:
                    enabled_pools += [pool_option.pool]

        if not enabled_pools:
            rac_logger.debug(f"No pools enabled, setting to defaults")
            disabled_pools = [pool for pool in ALL_POOLS if pool not in DEFAULT_LIST]
            restricted_pools = []
            useful_pools = []
            enabled_pools = DEFAULT_LIST

        rac_logger.debug(f"Disabled Pools: {disabled_pools}")
        rac_logger.debug(f"Restricted Pools: {restricted_pools}")
        rac_logger.debug(f"Useful Pools: {useful_pools}")
        rac_logger.debug(f"Enabled Pools: {enabled_pools}")

        rac_logger.debug(f"Creating Regions")
        create_regions(self)

        # TODO: Item Pools: get_pre_fill_items()
        # if (self.options.shuffle_weapons == ShuffleWeapons.option_vanilla or
        #         self.options.starting_item == StartingItem.option_vanilla):
        starting_item = self.create_item(Items.BOMB_GLOVE.name)
        # else:
        #     starting_item = []
        #     match self.options.starting_item:
        #         case StartingItem.option_random_same:
        #             starting_item = list(Items.WEAPONS)
        #         case StartingItem.option_random_item:
        #             starting_item = [item for item in Items.ALL if item.name != "Gold Bolt"]
        #         case StartingItem.option_unrestricted:
        #             starting_item = list(Items.ALL)
        #     self.random.shuffle(starting_item)
        #     self.multiworld.push_precollected(self.create_item(starting_item[0].name))
        #     starting_item = self.create_item(starting_item[0].name)

        if (self.options.shuffle_infobots == ShuffleInfobots.option_vanilla or
                self.options.starting_location == StartingLocation.option_false):
            starting_planet = self.create_item(Items.NOVALIS_INFOBOT.name)
        else:
            starting_planet = list(Planets.STARTING_PLANETS)
            self.random.shuffle(starting_planet)
            self.starting_planet = starting_planet[0].name
            starting_planet = self.create_item(starting_planet[0].name)

        self.starting_items = [starting_item, starting_planet]
        self.multiworld.push_precollected(starting_item)
        self.multiworld.push_precollected(starting_planet)
        rac_logger.debug(f"Starting items: {self.starting_items}")

        rac_logger.debug(f"___Vanilla Locations___")
        self.preplaced_locations += self.fill_pool(disabled_pools, 0)
        rac_logger.debug(f"___Internal Shuffled Pools___")
        self.preplaced_locations += self.fill_pool(restricted_pools, 1)
        rac_logger.debug(f"___Group Shuffled Pools___")
        self.preplaced_locations += self.fill_pool(useful_pools, 2)
        rac_logger.debug(f"Pre-placed Items placed: {[loc.item for loc in self.preplaced_locations]}")
        rac_logger.debug(f"Pre-filled Locations removed: {self.preplaced_locations}")
        rac_logger.debug(f"_________END EARLY GENERATION____________")

        # self.disabled_location_data = set(loc for loc in ALL_LOCATIONS if not loc.pools.issubset(enabled_pools))

        # for location in ALL_LOCATIONS:
        #     if not location.pools.issubset(enabled_pools):
        #         logging.debug(f"disable: {location.name}")
        #         self.disabled_location_data.append(location)
        # output: list[str] = list(loc.name for loc in self.disabled_location_data)
        # logging.debug(f"disabled location data: {output}")

    def fill_pool(self, pools, scope) -> (list, list):
        multiworld = self.multiworld
        placed_items = [loc.item.name for loc in self.preplaced_locations]
        starting_item_list = [item.name for item in self.starting_items]
        placed_items += starting_item_list
        placed_items += [*[Items.GOLD_BOLT.name] * 40]
        unplaced_items: list[ItemData] = [item for item in Items.ALL if item.name not in placed_items]
        placed_locations: list[Location] = []
        match scope:
            case 0:
                for pool in pools:
                    rac_logger.debug(f"Disable Pool: {pool}")
                    for loc in ALL_LOCATIONS:
                        if pool in loc.pools and loc.vanilla_item is not None:
                            if self.get_location(loc.name).item is not None:
                                raise FillError(f"Slot {self.player_name} selected vanilla {pool}, but Location:"
                                                f" {loc.name} was already filled")
                            item = self.create_item(loc.vanilla_item)
                            placed_locations += [self.get_location(loc.name)]
                            rac_logger.debug(f"vanilla: {loc.name}, item: {item}")
                            placed_locations[len(placed_locations) - 1].place_locked_item(item)
            case 1:
                for pool in pools:
                    if pool == POOL_GOLDEN_WEAPON and POOL_WEAPON in pools:
                        continue
                    base_state = CollectionState(multiworld)
                    item_sweep: Sequence[Item] = []
                    unplaced_items = [item for item in Items.ALL if item.name not in placed_items]
                    for item in starting_item_list:
                        item_sweep += [self.create_item(item)]
                    for item in unplaced_items:
                        if item.pool != pool:
                            if pool == POOL_WEAPON and POOL_GOLDEN_WEAPON in pools and item.pool == POOL_GOLDEN_WEAPON:
                                continue
                            item_sweep += [self.create_item(item.name)]
                    rac_logger.debug(f"Assumed collected: {item_sweep}")
                    base_state = sweep_from_pool(base_state, item_sweep)
                    rac_logger.debug(f"Restricted Pool: {pool}")
                    loc_temp = []
                    item_temp = []
                    for loc in ALL_LOCATIONS:
                        if pool in loc.pools and loc.vanilla_item is not None:
                            loc_temp += [self.get_location(loc.name)]
                            item_temp += [self.create_item(loc.vanilla_item)]
                            placed_items += [loc.vanilla_item]
                        if pool == POOL_WEAPON and POOL_GOLDEN_WEAPON in pools:
                            if POOL_GOLDEN_WEAPON in loc.pools and loc.vanilla_item is not None:
                                loc_temp += [self.get_location(loc.name)]
                                item_temp += [self.create_item(loc.vanilla_item)]
                                placed_items += [loc.vanilla_item]
                    rac_logger.debug(f"Randomize Locations: {loc_temp}")
                    placed_locations += loc_temp
                    self.random.shuffle(item_temp)
                    rac_logger.debug(f"Shuffled items: {item_temp}")
                    rac_logger.debug(f"Reachability before Shuffle: {base_state.reachable_regions}")
                    rac_logger.debug(f"Locations already checked: {base_state.locations_checked}")
                    reachable = [loc for loc in multiworld.get_reachable_locations(base_state, self.player)
                                 if loc in loc_temp]
                    rac_logger.debug(f"Reachable Locations: {reachable}")
                    fill_restrictive(multiworld, base_state, loc_temp, item_temp, single_player_placement=True,
                                     swap=True, name=f"RAC1 Restricted Item Fill: {pool}")
                    for loc in loc_temp:
                        placed_locations.remove(loc)
                    # if item_temp:
                    #     for loc in placed_locations:
                    #         rac_logger.debug(f"same group: {loc.name}, item: {loc.item}")
                    #     raise FillError(f"Slot {self.player_name} selected shuffle {pool} only among themselves, "
                    #                     f"but Items: {item_temp} could not get placed at Locations: {loc_temp}")
            case 2:
                loc_temp = []
                item_temp = []
                item_sweep = []
                base_state = CollectionState(multiworld)
                for pool in pools:
                    rac_logger.debug(f"add Pool: {pool}")
                    for loc in ALL_LOCATIONS:
                        if pool in loc.pools and loc.vanilla_item is not None:
                            loc_temp += [self.get_location(loc.name)]
                if loc_temp:
                    for item in starting_item_list:
                        item_sweep += [self.create_item(item)]
                    for item in unplaced_items:
                        if item.name != Items.GOLD_BOLT.name:
                            item_temp += [self.create_item(item.name)]
                    base_state = sweep_from_pool(base_state, item_sweep)
                    rac_logger.debug(f"Randomizing Useful Locations: {loc_temp}")
                    placed_locations += loc_temp
                    self.random.shuffle(item_temp)
                    rac_logger.debug(f"Shuffled items: {item_temp}")
                    rac_logger.debug(f"Reachability before Shuffle: {base_state.reachable_regions}")
                    reachable = [loc for loc in multiworld.get_reachable_locations(base_state, self.player)
                                 if loc in loc_temp]
                    rac_logger.debug(f"Reachable Locations: {reachable}")
                    # TODO: Try using remaining_fill() to prevent deadend seeds
                    fill_restrictive(multiworld, base_state, loc_temp, item_temp, single_player_placement=True,
                                     swap=True, allow_partial=True, allow_excluded=True,
                                     name="RAC1 Useful Item Fill")
                    for loc in loc_temp:
                        placed_locations.remove(loc)
                    # if loc_temp:
                    #     for loc in placed_locations:
                    #         rac_logger.debug(f"any item: {loc.name}, item: {loc.item}")
                    #     if item_temp:
                    #         raise FillError(f"Slot {self.player_name} has locations requiring useful items that are "
                    #                     f"unfilled, Items: {item_temp} could not get placed at Locations: {loc_temp}")
                    #     else:
                    #         raise FillError(f"Slot {self.player_name} has locations requiring useful items that are "
                    #                     f"unfilled, No items left to get placed at Locations: {loc_temp}")
        return placed_locations

    def create_item(self, name: str, override: Optional[ItemClassification] = None) -> "Item":
        new_name = Items.check_progressive_item(self.options, name)
        if Items.from_name(name).pool == POOL_WEAPON or Items.from_name(name).pool == POOL_GOLDEN_WEAPON:
            rac_logger.debug(f"Checking progressive weapon: {name}")
            rac_logger.debug(f"Weapon is: {new_name}")
        if override:
            return RacItem(new_name, override, self.item_name_to_id[new_name], self.player)
        item_data = Items.from_name(new_name)
        return RacItem(new_name, ItemPool.get_classification(item_data), self.item_name_to_id[new_name], self.player)

    def create_event(self, name: str) -> "Item":
        return RacItem(name, ItemClassification.progression, None, self.player)

    def get_pre_fill_items(self) -> list["Item"]:
        rac_logger.debug(f"fetching preplaced_items")
        return [loc.item for loc in self.preplaced_locations]

    def create_items(self) -> None:
        rac_logger.debug(f"_________START ITEM CREATION__________")
        items_to_add: list[Item] = [self.create_item(item.name) for item in Items.ALL]

        # add gold bolts in whatever slots we have left
        # unfilled = [i for i in self.multiworld.get_unfilled_locations(self.player) if not i.is_event]
        # rac_logger.debug(self.multiworld.get_filled_locations(self.player))
        # rac_logger.debug(f"{len(items_to_add)} {len(unfilled)}")
        # remain = len(unfilled) - len(items_to_add)
        # assert remain >= 0, "There are more items than locations. This is not supported."
        # rac_logger.debug(f"Not enough items to fill all locations. Adding {remain} filler items to the item pool")
        # for _ in range(remain):
        #     items_to_add.append(self.create_item(Items.GOLD_BOLT.name, ItemClassification.filler))

        items_to_remove: list[Item] = [loc.item for loc in self.preplaced_locations]
        items_to_remove += self.starting_items
        rac_logger.debug(f"Preplaced item list before removal: {items_to_remove}")
        for item in items_to_remove:
            items_to_add.remove(item)
            rac_logger.debug(f"{item} removed")
        if len(items_to_add) == len(self.multiworld.get_unfilled_locations(self.player)) - 1:
            rac_logger.debug(f"Add item pool to multiworld: {items_to_add}")
            self.multiworld.itempool.extend(items_to_add)
            rac_logger.debug(f"_________END ITEM CREATION__________")
        else:
            rac_logger.debug(f"Items unplaced: {items_to_add}")
            rac_logger.debug(f"Locations unfilled: {self.multiworld.get_unfilled_locations(self.player)}")
            raise FillError(f"Item Count: {len(items_to_add)} does not match Location count: "
                            f"{len(self.multiworld.get_unfilled_locations(self.player))}")

    def set_rules(self) -> None:
        boss_location = self.multiworld.get_location(Locations.VELDIN_DREK.name, self.player)
        boss_location.place_locked_item(self.create_event("Victory"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        # def generate_output(self, output_directory: str) -> None:
        #     aprac2 = Rac2ProcedurePatch(player=self.player, player_name=self.multiworld.get_player_name(self.player))
        #     generate_patch(self, aprac2)
        #     rom_path = os.path.join(output_directory,
        #                             f"{self.multiworld.get_out_file_name_base(self.player)}{
        #                             aprac2.patch_file_ending}")
        # aprac2.write(rom_path)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data: dict[str, Any] = {}
        slot_data |= Options.get_options_as_dict(self.options)
        slot_data["starting_planet"] = self.item_name_to_id[self.starting_planet]
        return slot_data

    # def post_fill(self) -> None:
    #    from Utils import visualize_regions
    #    visualize_regions(self.multiworld.get_region("Menu", self.player), f"{self.player_name}_world.puml",
    #                      regions_to_highlight=self.multiworld.get_all_state(False).reachable_regions[
    #                          self.player])
