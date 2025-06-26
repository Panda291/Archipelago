import logging
from typing import Any, Dict, Mapping, Optional

from BaseClasses import CollectionState, Item, ItemClassification, Tutorial
from Fill import fill_restrictive
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, SuffixIdentifier, Type
from . import ItemPool
from .data import Items, Locations, Planets
from .data.Items import CollectableData, ItemData
from .data.Locations import DEFAULT_LIST, LocationData, POOL_GOLD_BOLT
from .data.Planets import ALL_LOCATIONS, location_groups, PlanetData
from .RacOptions import RacOptions
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
    starting_planet: Optional[PlanetData] = None
    starting_item: list[ItemData] = []
    disabled_pools: list[str] = []
    enabled_pools: list[str] = []

    # def get_filler_item_name(self) -> str:
    #     return Items.BOLT_PACK.name

    def generate_early(self) -> None:
        rac_logger.warning(
            "INCOMPLETE WORLD! Slot '%s' is using an unfinished alpha world that is not stable yet!",
            self.player_name)
        rac_logger.warning("INCOMPLETE WORLD! Slot '%s' may require send_location/send_item for completion!",
                           self.player_name)

        self.enabled_pools += DEFAULT_LIST

        if self.options.shuffle_gold_bolts.value:
            self.enabled_pools += [POOL_GOLD_BOLT]
        else:
            self.disabled_pools += [POOL_GOLD_BOLT]

        rac_logger.debug(f"Enabled Pools: {self.enabled_pools}")

        # self.disabled_location_data = set(loc for loc in ALL_LOCATIONS if not loc.pools.issubset(enabled_pools))

        # for location in ALL_LOCATIONS:
        #     if not location.pools.issubset(enabled_pools):
        #         logging.debug(f"disable: {location.name}")
        #         self.disabled_location_data.append(location)
        # output: list[str] = list(loc.name for loc in self.disabled_location_data)
        # logging.debug(f"disabled location data: {output}")

    def create_regions(self) -> None:
        create_regions(self)

    def create_item(self, name: str, override: Optional[ItemClassification] = None) -> "Item":
        if override:
            return RacItem(name, override, self.item_name_to_id[name], self.player)
        item_data = Items.from_name(name)
        return RacItem(name, ItemPool.get_classification(item_data), self.item_name_to_id[name], self.player)

    def create_event(self, name: str) -> "Item":
        return RacItem(name, ItemClassification.progression, None, self.player)

    # def get_pre_fill_items(self) -> List["Item"]:
    #     return list(self.create_item(location.vanilla_item) for location in ALL_LOCATIONS)

    def pre_fill(self) -> None:
        rac_logger.debug(f"Disabled Pools: {self.disabled_pools}")
        if self.disabled_pools:
            multiworld = self.multiworld
            base_state = CollectionState(multiworld)
            for item in multiworld.itempool:
                base_state.collect(item)
            base_state.sweep_for_advancements(multiworld.get_locations(self.player))
            locations: list = []
            items: list = []
            for pool in self.disabled_pools:
                rac_logger.debug(f"Pool: {pool}")
                for loc in ALL_LOCATIONS:
                    if pool in loc.pools and loc.vanilla_item is not None:
                        rac_logger.debug(f"vanilla: {loc.name}, item: {loc.vanilla_item}")
                        locations += [self.get_location(loc.name)]
                        items += [self.create_item(loc.vanilla_item)]

            fill_restrictive(multiworld, base_state, locations, items, single_player_placement=True, lock=True,
                             allow_excluded=True, name="RAC1 Vanilla Item Fill")

    def create_items(self) -> None:
        items_to_add: list["Item"] = []
        items_to_add += ItemPool.create_planets(self)
        items_to_add += ItemPool.create_equipment(self)

        if POOL_GOLD_BOLT in self.enabled_pools:
            rac_logger.debug(f"Gold Bolts added to pool")
            items_to_add += ItemPool.create_collectables(self)
        else:
            rac_logger.debug(f"Gold Bolts removed from pool")

        # add gold bolts in whatever slots we have left
        # unfilled = [i for i in self.multiworld.get_unfilled_locations(self.player) if not i.is_event]
        # print(self.multiworld.get_filled_locations(self.player))
        # print(f"{len(items_to_add)} {len(unfilled)}")
        # remain = len(unfilled) - len(items_to_add)
        # assert remain >= 0, "There are more items than locations. This is not supported."
        # print(f"Not enough items to fill all locations. Adding {remain} filler items to the item pool")
        # for _ in range(remain):
        #     items_to_add.append(self.create_item(Items.GOLD_BOLT.name, ItemClassification.filler))

        self.multiworld.itempool += items_to_add

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

    def get_options_as_dict(self) -> Dict[str, Any]:
        return self.options.as_dict(
            # "death_link",
            # "starting_item",
            "shuffle_gold_bolts",
        )

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.get_options_as_dict()

    # def post_fill(self) -> None:
    #    from Utils import visualize_regions
    #    visualize_regions(self.multiworld.get_region("Menu", self.player), f"{self.player_name}_world.puml",
    #                      regions_to_highlight=self.multiworld.get_all_state(False).reachable_regions[
    #                          self.player])
