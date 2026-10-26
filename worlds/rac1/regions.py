"""This module defines location regions in RAC1"""

import typing

from BaseClasses import Location, Region
from rule_builder.rules import Has
from worlds.generic.Rules import forbid_item
from worlds.rac1.constants.locations.planets import RAC1PLANET
from worlds.rac1.constants.options import RAC1OPTION
from worlds.rac1.constants.pools import RAC1POOL
from worlds.rac1.data.items import GOLD_BOLT_SIZE_TO_PACK
from worlds.rac1.data.planets import LOGIC_PLANETS, PLANET_NAME_TO_ITEM

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
            region = Region(planet_data.name, world.player, world.multiworld)
            world.multiworld.regions.append(region)
            if region.name is not RAC1PLANET.GENERAL:
                menu.connect(region, f'{RAC1PLANET.MENU} -> {region.name}', Has(PLANET_NAME_TO_ITEM[planet_data.name]))
            if planet_data.name is RAC1PLANET.RILGAR:
                region.connect(world.get_region(RAC1PLANET.GENERAL), "Rilgar Hoverboard Race",
                               planet_data.locations[1].access_rule)
            if planet_data.name is RAC1PLANET.KALEBO:
                region.connect(world.get_region(RAC1PLANET.GENERAL), "Kalebo Hoverboard Race",
                               planet_data.locations[0].access_rule)

            for location_data in planet_data.locations:
                if world.options.shuffle_skill_points == 0 and RAC1POOL.SKILLPOINT in location_data.pools:
                    continue
                region.add_locations({location_data.name: location_data.location_id}, RacLocation)
                location = world.multiworld.get_location(location_data.name, world.player)
                world.set_rule(location, location_data.access_rule)
                if RAC1POOL.GOLD_WEAPONS in location_data.pools:
                    forbid_item(location, GOLD_BOLT_SIZE_TO_PACK[world.options.pack_size_gold_bolts.value],
                                world.player)
