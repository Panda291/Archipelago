import typing

from BaseClasses import CollectionState, Location, Region
from rule_builder.rules import Has, Rule, True_
from .data import Planets
from .data.Locations import LocationData
from .data.Planets import PlanetData
from ..generic.Rules import set_rule

if typing.TYPE_CHECKING:
    from . import RacWorld


class RacLocation(Location):
    game: str = "Ratchet & Clank"


def create_regions(world: 'RacWorld'):
    # create all regions and populate with locations
    menu = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menu)

    for planet_data in Planets.LOGIC_PLANETS:
        if planet_data.locations:
            region = Region(planet_data.name, world.player, world.multiworld)
            world.multiworld.regions.append(region)
            menu.connect(region, None, Has(planet_data.name))

            for location_data in planet_data.locations:
                # Don't create the location if there is a "pool" it is in that is not enabled
                # if location_data.name in world.disabled_pools:
                #     continue

                region.add_locations({location_data.name: location_data.location_id}, RacLocation)
                location = world.multiworld.get_location(location_data.name, world.player)
                world.set_rule(location, location_data.access_rule)
                print(f"Setting location rule for {location_data.name}")

    # from Utils import visualize_regions
    # visualize_regions(world.multiworld.get_region("Menu", world.player), "my_world.puml")
