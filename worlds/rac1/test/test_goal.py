from worlds.rac1.constants.items import RAC1ITEM
from worlds.rac1.constants.locations.goldbolts import RAC1BOLT
from worlds.rac1.constants.locations.planets import RAC1PLANET

from worlds.rac1.test import RACTestBase


class TestDrek(RACTestBase):
    options = {}

    def test_goal(self) -> None:
        """Test various states to verify goal is beatable with correct items"""
        self.collect_by_name(RAC1ITEM.VELDIN)
        self.assertEqual(self.can_reach_region(RAC1PLANET.VELDIN), True,
                         msg="Veldin region not reached with the infobot")
        self.collect_by_name([RAC1ITEM.TRESPASSER, RAC1ITEM.HYDRODISPLACER,
                              RAC1ITEM.MAGNEBOOTS, RAC1ITEM.THRUSTER_PACK])
        self.assertAccessDependency([RAC1BOLT.VELDIN_HALFWAY],
                                    [[RAC1ITEM.TRESPASSER, RAC1ITEM.HYDRODISPLACER, RAC1ITEM.MAGNEBOOTS,
                                      RAC1ITEM.THRUSTER_PACK, RAC1ITEM.VELDIN]],
                                    True)
        self.assertBeatable(False)
        self.remove_by_name(RAC1ITEM.VELDIN)
        self.assertBeatable(False)
        self.collect_by_name(RAC1ITEM.SWINGSHOT)
        self.assertBeatable(False)
        self.collect_all_but([RAC1ITEM.VELDIN, RAC1ITEM.VICTORY])
        self.assertBeatable(False)
        self.collect_by_name(RAC1ITEM.VELDIN)
        self.assertBeatable(True)
