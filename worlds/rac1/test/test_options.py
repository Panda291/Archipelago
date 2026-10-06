from worlds.rac1 import RAC1SLOT
from worlds.rac1.options import (GoldBoltPackSize, ShuffleBoots, ShuffleExtraItems, ShuffleGadgets, ShuffleGoldBolts,
                                 ShuffleGoldWeapons, ShuffleHelmets, ShuffleInfobots, ShufflePacks, ShuffleSkillPoints,
                                 ShuffleWeapons)
from worlds.rac1.test import RACTestBase


class TestVanillaWeapons(RACTestBase):
    """Test Weapons unshuffled to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_WEAPONS: ShuffleWeapons.option_vanilla}


class TestRandomWeapons(RACTestBase):
    """Test Weapons local shuffle to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_WEAPONS: ShuffleWeapons.option_random_same}


class TestVanillaGadgets(RACTestBase):
    """Test Gadgets unshuffled to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_GADGETS: ShuffleGadgets.option_vanilla}


class TestRandomGadgets(RACTestBase):
    """Test Gadgets local shuffle to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_GADGETS: ShuffleGadgets.option_random_same}


class TestVanillaPacks(RACTestBase):
    """Test Packs unshuffled to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_PACKS: ShufflePacks.option_vanilla}


class TestRandomPacks(RACTestBase):
    """Test Packs local shuffle to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_PACKS: ShufflePacks.option_random_same}


class TestVanillaHelmets(RACTestBase):
    """Test Helmets unshuffled to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_HELMETS: ShuffleHelmets.option_vanilla}


class TestRandomHelmets(RACTestBase):
    """Test Helmets local shuffle to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_HELMETS: ShuffleHelmets.option_random_same}


class TestVanillaBoots(RACTestBase):
    """Test Boots unshuffled to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_BOOTS: ShuffleBoots.option_vanilla}


class TestRandomBoots(RACTestBase):
    """Test Boots local shuffle to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_BOOTS: ShuffleBoots.option_random_same}


class TestVanillaExtraItems(RACTestBase):
    """Test ExtraItems unshuffled to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_EXTRA_ITEMS: ShuffleExtraItems.option_vanilla}


class TestRandomExtraItems(RACTestBase):
    """Test ExtraItems local shuffle to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_EXTRA_ITEMS: ShuffleExtraItems.option_random_same}


class TestVanillaGoldBolts(RACTestBase):
    """Test Gold Bolts off to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_GOLD_BOLTS: ShuffleGoldBolts.option_false}


class TestRandomGoldBolts(RACTestBase):
    """Test Gold Bolts with a random pack size"""
    options = {RAC1SLOT.GOLD_BOLT_PACK_SIZE: GoldBoltPackSize.weighted_range("random-low")}


class TestVanillaSkillpoints(RACTestBase):
    """Test Skillpoints off to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_SKILLPOINTS: ShuffleSkillPoints.option_false}


class TestRandomSkillpoints(RACTestBase):
    """Test Skillpoints on to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_SKILLPOINTS: ShuffleSkillPoints.option_true}


class TestVanillaInfobots(RACTestBase):
    """Test Infobots unshuffled to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_INFOBOTS: ShuffleInfobots.option_vanilla}


class TestRandomInfobots(RACTestBase):
    """Test Infobots local shuffle to verify beatable"""
    options = {RAC1SLOT.SHUFFLE_INFOBOTS: ShuffleInfobots.option_random_same}


class TestUseful(RACTestBase):
    """Test Useful items local shuffle to verify beatable"""
    options = {
        RAC1SLOT.SHUFFLE_WEAPONS: ShuffleWeapons.option_random_item,
        RAC1SLOT.SHUFFLE_GOLD_WEAPONS: ShuffleGoldWeapons.option_random_item,
        RAC1SLOT.SHUFFLE_GADGETS: ShuffleGadgets.option_random_item,
        RAC1SLOT.SHUFFLE_PACKS: ShufflePacks.option_random_item,
        RAC1SLOT.SHUFFLE_HELMETS: ShuffleHelmets.option_random_item,
        RAC1SLOT.SHUFFLE_BOOTS: ShuffleBoots.option_random_item,
        RAC1SLOT.SHUFFLE_EXTRA_ITEMS: ShuffleExtraItems.option_random_item,
        RAC1SLOT.SHUFFLE_INFOBOTS: ShuffleInfobots.option_random_item,
    }
