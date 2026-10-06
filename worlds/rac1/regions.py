import typing

from BaseClasses import CollectionState, Location, Region
from worlds.generic.Rules import add_rule, forbid_item
from worlds.rac1.constants.items import RAC1ITEM
from worlds.rac1.constants.locations.planets import RAC1PLANET
from worlds.rac1.constants.options import RAC1OPTION
from worlds.rac1.constants.pools import RAC1POOL
from worlds.rac1.data.items import get_gold_bolts
from worlds.rac1.data.locations import LocationData
from worlds.rac1.data.planets import LOGIC_PLANETS, PLANET_NAME_TO_ITEM, PlanetData

if typing.TYPE_CHECKING:
    from . import RacWorld


class RacLocation(Location):
    game: str = RAC1OPTION.GAME_TITLE_FULL


def create_regions(world: 'RacWorld'):
    # create all regions and populate with locations
    menu = Region(RAC1PLANET.MENU, world.player, world.multiworld)
    world.multiworld.regions.append(menu)

    for planet_data in LOGIC_PLANETS:
        if planet_data.locations:
            def generate_planet_access_rule(planet: PlanetData) -> typing.Callable[[CollectionState], bool]:
                def planet_access_rule(state: CollectionState):
                    return state.has(PLANET_NAME_TO_ITEM[planet.name], world.player)

                return planet_access_rule

            def general_access(planet: PlanetData, index: int) -> typing.Callable[[CollectionState], bool]:
                def access(state: CollectionState) -> bool:
                    if state.prog_items[1].get(RAC1ITEM.HOVERBOARD):
                        pass
                    return planet.locations[index].access_rule(state, world)

                return access

            region = Region(planet_data.name, world.player, world.multiworld)
            world.multiworld.regions.append(region)
            if region.name is not RAC1PLANET.GENERAL:
                menu.connect(region, f'{RAC1PLANET.MENU} -> {region.name}', generate_planet_access_rule(planet_data))
            if planet_data.name is RAC1PLANET.RILGAR:
                region.connect(world.get_region(RAC1PLANET.GENERAL), "Rilgar Hoverboard Race",
                               general_access(planet_data, 1))
            if planet_data.name is RAC1PLANET.KALEBO:
                region.connect(world.get_region(RAC1PLANET.GENERAL), "Kalebo Hoverboard Race",
                               general_access(planet_data, 0))

            for location_data in planet_data.locations:
                def generate_access_rule(loc: LocationData) -> typing.Callable[[CollectionState], bool]:
                    def access_rule(state: CollectionState):
                        if loc.access_rule:
                            return loc.access_rule(state, world)
                        return True

                    return access_rule

                region.add_locations({location_data.name: location_data.location_id}, RacLocation)
                location = world.multiworld.get_location(location_data.name, world.player)
                add_rule(location, generate_access_rule(location_data))
                if RAC1POOL.GOLD_WEAPONS in location_data.pools:
                    forbid_item(location, get_gold_bolts(world.options), world.player)

    # from Utils import visualize_regions
    # visualize_regions(world.multiworld.get_region("Menu", world.player), "my_world.puml")
