from dataclasses import dataclass
from typing import Sequence

from BaseClasses import Item, ItemClassification
from worlds.rac1.constants.items import RAC1ITEM
from worlds.rac1.constants.pools import RAC1POOL
from worlds.rac1.constants.progressive_orders import RAC1ORDER
from worlds.rac1.options import (BootsProgression, GoldWeaponProgression, HelmetProgression, HoverboardProgression,
                                 NanotechProgression, PackProgression, RacOptions, RaritaniumProgression,
                                 ShuffleExtraItems, ShuffleHelmets, ShuffleInfobots)


@dataclass
class ItemData(Item):
    item_id: int
    name: str
    pool: str
    classification: ItemClassification
    quantity: int = 1


@dataclass
class CollectableData(ItemData):
    max_capacity: int = 0x7F


class RAC1ItemData:
    HELI_PACK = ItemData(2, RAC1ITEM.HELI_PACK, RAC1POOL.PACKS, ItemClassification.progression)
    THRUSTER_PACK = ItemData(3, RAC1ITEM.THRUSTER_PACK, RAC1POOL.PACKS, ItemClassification.progression)
    HYDRO_PACK = ItemData(4, RAC1ITEM.HYDRO_PACK, RAC1POOL.PACKS, ItemClassification.progression)
    SONIC_SUMMONER = ItemData(5, RAC1ITEM.SONIC_SUMMONER, RAC1POOL.HELMETS, ItemClassification.progression)
    O2_MASK = ItemData(6, RAC1ITEM.O2_MASK, RAC1POOL.HELMETS, ItemClassification.progression)
    PILOTS_HELMET = ItemData(7, RAC1ITEM.PILOTS_HELMET, RAC1POOL.HELMETS, ItemClassification.progression)
    # WRENCH = ItemData(8, RAC1ITEM.WRENCH, "?")
    SUCK_CANNON = ItemData(9, RAC1ITEM.SUCK_CANNON, RAC1POOL.WEAPONS, ItemClassification.progression)
    BOMB_GLOVE = ItemData(10, RAC1ITEM.BOMB_GLOVE, RAC1POOL.WEAPONS, ItemClassification.progression)
    DEVASTATOR = ItemData(11, RAC1ITEM.DEVASTATOR, RAC1POOL.WEAPONS, ItemClassification.progression)
    SWINGSHOT = ItemData(12, RAC1ITEM.SWINGSHOT, RAC1POOL.GADGETS, ItemClassification.progression)
    VISIBOMB = ItemData(13, RAC1ITEM.VISIBOMB, RAC1POOL.WEAPONS, ItemClassification.progression)
    TAUNTER = ItemData(14, RAC1ITEM.TAUNTER, RAC1POOL.WEAPONS, ItemClassification.progression)
    BLASTER = ItemData(15, RAC1ITEM.BLASTER, RAC1POOL.WEAPONS, ItemClassification.progression)
    PYROCITOR = ItemData(16, RAC1ITEM.PYROCITOR, RAC1POOL.WEAPONS, ItemClassification.progression)
    MINE_GLOVE = ItemData(17, RAC1ITEM.MINE_GLOVE, RAC1POOL.WEAPONS, ItemClassification.progression)
    WALLOPER = ItemData(18, RAC1ITEM.WALLOPER, RAC1POOL.WEAPONS, ItemClassification.useful)
    TESLA_CLAW = ItemData(19, RAC1ITEM.TESLA_CLAW, RAC1POOL.WEAPONS, ItemClassification.progression)
    GLOVE_OF_DOOM = ItemData(20, RAC1ITEM.GLOVE_OF_DOOM, RAC1POOL.WEAPONS, ItemClassification.useful)
    MORPH_O_RAY = ItemData(21, RAC1ITEM.MORPH_O_RAY, RAC1POOL.WEAPONS, ItemClassification.progression)
    HYDRODISPLACER = ItemData(22, RAC1ITEM.HYDRODISPLACER, RAC1POOL.GADGETS, ItemClassification.progression)
    RYNO = ItemData(23, RAC1ITEM.RYNO, RAC1POOL.WEAPONS, ItemClassification.progression)
    DRONE_DEVICE = ItemData(24, RAC1ITEM.DRONE_DEVICE, RAC1POOL.WEAPONS, ItemClassification.useful)
    DECOY_GLOVE = ItemData(25, RAC1ITEM.DECOY_GLOVE, RAC1POOL.WEAPONS, ItemClassification.useful)
    TRESPASSER = ItemData(26, RAC1ITEM.TRESPASSER, RAC1POOL.GADGETS, ItemClassification.progression)
    METAL_DETECTOR = ItemData(27, RAC1ITEM.METAL_DETECTOR, RAC1POOL.GADGETS, ItemClassification.progression)
    MAGNEBOOTS = ItemData(28, RAC1ITEM.MAGNEBOOTS, RAC1POOL.BOOTS, ItemClassification.progression)
    GRINDBOOTS = ItemData(29, RAC1ITEM.GRINDBOOTS, RAC1POOL.BOOTS, ItemClassification.progression)
    HOVERBOARD = ItemData(30, RAC1ITEM.HOVERBOARD, RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
    HOLOGUISE = ItemData(31, RAC1ITEM.HOLOGUISE, RAC1POOL.GADGETS, ItemClassification.progression)
    PDA = ItemData(32, RAC1ITEM.PDA, RAC1POOL.GADGETS, ItemClassification.useful)
    MAP_O_MATIC = ItemData(33, RAC1ITEM.MAP_O_MATIC, RAC1POOL.EXTRA_ITEMS, ItemClassification.useful)
    BOLT_GRABBER = ItemData(34, RAC1ITEM.BOLT_GRABBER, RAC1POOL.EXTRA_ITEMS, ItemClassification.useful)
    PERSUADER = ItemData(35, RAC1ITEM.PERSUADER, RAC1POOL.EXTRA_ITEMS, ItemClassification.useful)

    ZOOMERATOR = ItemData(48, RAC1ITEM.ZOOMERATOR, RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
    RARITANIUM = ItemData(49, RAC1ITEM.RARITANIUM, RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
    CODEBOT = ItemData(50, RAC1ITEM.CODEBOT, RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
    PREMIUM_NANOTECH = ItemData(52, RAC1ITEM.PREMIUM_NANOTECH, RAC1POOL.EXTRA_ITEMS, ItemClassification.useful)
    ULTRA_NANOTECH = ItemData(53, RAC1ITEM.ULTRA_NANOTECH, RAC1POOL.EXTRA_ITEMS, ItemClassification.useful)

    GOLD_SUCK_CANNON = ItemData(309, RAC1ITEM.GOLD_SUCK_CANNON, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
    GOLD_BOMB_GLOVE = ItemData(310, RAC1ITEM.GOLD_BOMB_GLOVE, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
    GOLD_DEVASTATOR = ItemData(311, RAC1ITEM.GOLD_DEVASTATOR, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
    GOLD_BLASTER = ItemData(315, RAC1ITEM.GOLD_BLASTER, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
    GOLD_PYROCITOR = ItemData(316, RAC1ITEM.GOLD_PYROCITOR, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
    GOLD_MINE_GLOVE = ItemData(317, RAC1ITEM.GOLD_MINE_GLOVE, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
    GOLD_TESLA_CLAW = ItemData(319, RAC1ITEM.GOLD_TESLA_CLAW, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
    GOLD_GLOVE_OF_DOOM = ItemData(320, RAC1ITEM.GOLD_GLOVE_OF_DOOM, RAC1POOL.GOLD_WEAPONS, ItemClassification.useful)
    GOLD_MORPH_O_RAY = ItemData(321, RAC1ITEM.GOLD_MORPH_O_RAY, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
    GOLD_DECOY_GLOVE = ItemData(325, RAC1ITEM.GOLD_DECOY_GLOVE, RAC1POOL.GOLD_WEAPONS, ItemClassification.useful)

    PROGRESSIVE_PACK = ItemData(80, RAC1ITEM.PROGRESSIVE_PACK, RAC1POOL.PACKS, ItemClassification.progression)
    PROGRESSIVE_HELMET = ItemData(81, RAC1ITEM.PROGRESSIVE_HELMET, RAC1POOL.HELMETS, ItemClassification.progression)
    PROGRESSIVE_SUCK = ItemData(82, RAC1ITEM.PROGRESSIVE_SUCK, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_BOMB = ItemData(83, RAC1ITEM.PROGRESSIVE_BOMB, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_DEVASTATOR = ItemData(84, RAC1ITEM.PROGRESSIVE_DEVASTATOR,
                                      RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_BLASTER = ItemData(85, RAC1ITEM.PROGRESSIVE_BLASTER, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_PYROCITOR = ItemData(86, RAC1ITEM.PROGRESSIVE_PYROCITOR,
                                     RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_MINE = ItemData(87, RAC1ITEM.PROGRESSIVE_MINE, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_TESLA = ItemData(88, RAC1ITEM.PROGRESSIVE_TESLA, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_DOOM = ItemData(89, RAC1ITEM.PROGRESSIVE_DOOM, RAC1POOL.WEAPONS, ItemClassification.useful)
    PROGRESSIVE_MORPH = ItemData(90, RAC1ITEM.PROGRESSIVE_MORPH, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_DECOY = ItemData(91, RAC1ITEM.PROGRESSIVE_DECOY, RAC1POOL.WEAPONS, ItemClassification.useful)
    PROGRESSIVE_BOOT = ItemData(92, RAC1ITEM.PROGRESSIVE_BOOT, RAC1POOL.BOOTS, ItemClassification.progression)
    PROGRESSIVE_HOVERBOARD = ItemData(93, RAC1ITEM.PROGRESSIVE_HOVERBOARD,
                                      RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
    PROGRESSIVE_TRADE = ItemData(94, RAC1ITEM.PROGRESSIVE_TRADE, RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
    PROGRESSIVE_NANOTECH = ItemData(95, RAC1ITEM.PROGRESSIVE_NANOTECH, RAC1POOL.EXTRA_ITEMS, ItemClassification.useful)

    NOVALIS = ItemData(101, RAC1ITEM.NOVALIS, RAC1POOL.INFOBOTS, ItemClassification.progression)
    ARIDIA = ItemData(102, RAC1ITEM.ARIDIA, RAC1POOL.INFOBOTS, ItemClassification.progression)
    KERWAN = ItemData(103, RAC1ITEM.KERWAN, RAC1POOL.INFOBOTS, ItemClassification.progression)
    EUDORA = ItemData(104, RAC1ITEM.EUDORA, RAC1POOL.INFOBOTS, ItemClassification.progression)
    RILGAR = ItemData(105, RAC1ITEM.RILGAR, RAC1POOL.INFOBOTS, ItemClassification.progression)
    BLARG = ItemData(106, RAC1ITEM.BLARG, RAC1POOL.INFOBOTS, ItemClassification.progression)
    UMBRIS = ItemData(107, RAC1ITEM.UMBRIS, RAC1POOL.INFOBOTS, ItemClassification.progression)
    BATALIA = ItemData(108, RAC1ITEM.BATALIA, RAC1POOL.INFOBOTS, ItemClassification.progression)
    GASPAR = ItemData(109, RAC1ITEM.GASPAR, RAC1POOL.INFOBOTS, ItemClassification.progression)
    ORXON = ItemData(110, RAC1ITEM.ORXON, RAC1POOL.INFOBOTS, ItemClassification.progression)
    POKITARU = ItemData(111, RAC1ITEM.POKITARU, RAC1POOL.INFOBOTS, ItemClassification.progression)
    HOVEN = ItemData(112, RAC1ITEM.HOVEN, RAC1POOL.INFOBOTS, ItemClassification.progression)
    GEMLIK = ItemData(113, RAC1ITEM.GEMLIK, RAC1POOL.INFOBOTS, ItemClassification.progression)
    OLTANIS = ItemData(114, RAC1ITEM.OLTANIS, RAC1POOL.INFOBOTS, ItemClassification.progression)
    QUARTU = ItemData(115, RAC1ITEM.QUARTU, RAC1POOL.INFOBOTS, ItemClassification.progression)
    KALEBO = ItemData(116, RAC1ITEM.KALEBO, RAC1POOL.INFOBOTS, ItemClassification.progression)
    FLEET = ItemData(117, RAC1ITEM.FLEET, RAC1POOL.INFOBOTS, ItemClassification.progression)
    VELDIN = ItemData(118, RAC1ITEM.VELDIN, RAC1POOL.INFOBOTS, ItemClassification.progression)

    TAKE_AIM = ItemData(200, RAC1ITEM.TAKE_AIM, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    SWING_IT = ItemData(201, RAC1ITEM.SWING_IT, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    TRANSPORTED = ItemData(202, RAC1ITEM.TRANSPORTED, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    STRIKE_A_POSE = ItemData(203, RAC1ITEM.STRIKE_A_POSE, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    BLIMPY = ItemData(204, RAC1ITEM.BLIMPY, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    QWARKTASTIC = ItemData(205, RAC1ITEM.QWARKTASTIC, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    ANY_TEN = ItemData(206, RAC1ITEM.ANY_TEN, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    TRICKY = ItemData(207, RAC1ITEM.TRICKY, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    CLUCK_CLUCK = ItemData(208, RAC1ITEM.CLUCK_CLUCK, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    SPEEDY = ItemData(209, RAC1ITEM.SPEEDY, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    GIRL_TROUBLE = ItemData(210, RAC1ITEM.GIRL_TROUBLE, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    JUMPER = ItemData(211, RAC1ITEM.JUMPER, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    ACCURACY_COUNTS = ItemData(212, RAC1ITEM.ACCURACY_COUNTS, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    EAT_LEAD = ItemData(213, RAC1ITEM.EAT_LEAD, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    DESTROYED = ItemData(214, RAC1ITEM.DESTROYED, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    GUNNER = ItemData(215, RAC1ITEM.GUNNER, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    SNIPER = ItemData(216, RAC1ITEM.SNIPER, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    HEY_OVER_HERE = ItemData(217, RAC1ITEM.HEY_OVER_HERE, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    ALIEN_INVASION = ItemData(218, RAC1ITEM.ALIEN_INVASION, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    BURIED_TREASURE = ItemData(219, RAC1ITEM.BURIED_TREASURE, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    PEST_CONTROL = ItemData(220, RAC1ITEM.PEST_CONTROL, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    WHIRLYBIRDS = ItemData(221, RAC1ITEM.WHIRLYBIRDS, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    SITTING_DUCKS = ItemData(222, RAC1ITEM.SITTING_DUCKS, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    SHATTERED_GLASS = ItemData(223, RAC1ITEM.SHATTERED_GLASS, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    BLAST_EM = ItemData(224, RAC1ITEM.BLAST_EM, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    HEAVY_TRAFFIC = ItemData(225, RAC1ITEM.HEAVY_TRAFFIC, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    MAGICIAN = ItemData(226, RAC1ITEM.MAGICIAN, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    SNEAKY = ItemData(227, RAC1ITEM.SNEAKY, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    CAREFUL_CRUISE = ItemData(228, RAC1ITEM.CAREFUL_CRUISE, RAC1POOL.SKILLPOINT, ItemClassification.useful)
    GOING_COMMANDO = ItemData(229, RAC1ITEM.GOING_COMMANDO, RAC1POOL.SKILLPOINT, ItemClassification.useful)

    # Collectables
    GOLD_BOLT = ItemData(261, RAC1ITEM.GOLD_BOLT, RAC1POOL.GOLD_BOLTS,
                         ItemClassification.progression_deprioritized_skip_balancing)
    GOLD_BOLT_1 = ItemData(262, RAC1ITEM.GOLD_BOLT_1, RAC1POOL.GOLD_BOLTS,
                           ItemClassification.progression_deprioritized_skip_balancing)
    GOLD_BOLT_2 = ItemData(263, RAC1ITEM.GOLD_BOLT_2, RAC1POOL.GOLD_BOLTS,
                           ItemClassification.progression_deprioritized_skip_balancing, 2)
    GOLD_BOLT_3 = ItemData(264, RAC1ITEM.GOLD_BOLT_3, RAC1POOL.GOLD_BOLTS,
                           ItemClassification.progression_deprioritized_skip_balancing, 3)
    GOLD_BOLT_4 = ItemData(265, RAC1ITEM.GOLD_BOLT_4, RAC1POOL.GOLD_BOLTS,
                           ItemClassification.progression_deprioritized_skip_balancing, 4)
    GOLD_BOLT_5 = ItemData(266, RAC1ITEM.GOLD_BOLT_5, RAC1POOL.GOLD_BOLTS,
                           ItemClassification.progression_deprioritized_skip_balancing, 5)
    GOLD_BOLT_6 = ItemData(267, RAC1ITEM.GOLD_BOLT_6, RAC1POOL.GOLD_BOLTS,
                           ItemClassification.progression_deprioritized_skip_balancing, 6)
    GOLD_BOLT_7 = ItemData(268, RAC1ITEM.GOLD_BOLT_7, RAC1POOL.GOLD_BOLTS,
                           ItemClassification.progression_deprioritized_skip_balancing, 7)
    GOLD_BOLT_8 = ItemData(269, RAC1ITEM.GOLD_BOLT_8, RAC1POOL.GOLD_BOLTS,
                           ItemClassification.progression_deprioritized_skip_balancing, 8)
    GOLD_BOLT_9 = ItemData(270, RAC1ITEM.GOLD_BOLT_9, RAC1POOL.GOLD_BOLTS,
                           ItemClassification.progression_deprioritized_skip_balancing, 9)
    GOLD_BOLT_10 = ItemData(271, RAC1ITEM.GOLD_BOLT_10, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 10)
    GOLD_BOLT_11 = ItemData(272, RAC1ITEM.GOLD_BOLT_11, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 11)
    GOLD_BOLT_12 = ItemData(273, RAC1ITEM.GOLD_BOLT_12, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 12)
    GOLD_BOLT_13 = ItemData(274, RAC1ITEM.GOLD_BOLT_13, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 13)
    GOLD_BOLT_14 = ItemData(275, RAC1ITEM.GOLD_BOLT_14, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 14)
    GOLD_BOLT_15 = ItemData(276, RAC1ITEM.GOLD_BOLT_15, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 15)
    GOLD_BOLT_16 = ItemData(277, RAC1ITEM.GOLD_BOLT_16, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 16)
    GOLD_BOLT_17 = ItemData(278, RAC1ITEM.GOLD_BOLT_17, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 17)
    GOLD_BOLT_18 = ItemData(279, RAC1ITEM.GOLD_BOLT_18, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 18)
    GOLD_BOLT_19 = ItemData(280, RAC1ITEM.GOLD_BOLT_19, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 19)
    GOLD_BOLT_20 = ItemData(281, RAC1ITEM.GOLD_BOLT_20, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 20)
    GOLD_BOLT_21 = ItemData(282, RAC1ITEM.GOLD_BOLT_21, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 21)
    GOLD_BOLT_22 = ItemData(283, RAC1ITEM.GOLD_BOLT_22, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 22)
    GOLD_BOLT_23 = ItemData(284, RAC1ITEM.GOLD_BOLT_23, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 23)
    GOLD_BOLT_24 = ItemData(285, RAC1ITEM.GOLD_BOLT_24, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 24)
    GOLD_BOLT_25 = ItemData(286, RAC1ITEM.GOLD_BOLT_25, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 25)
    GOLD_BOLT_26 = ItemData(287, RAC1ITEM.GOLD_BOLT_26, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 26)
    GOLD_BOLT_27 = ItemData(288, RAC1ITEM.GOLD_BOLT_27, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 27)
    GOLD_BOLT_28 = ItemData(289, RAC1ITEM.GOLD_BOLT_28, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 28)
    GOLD_BOLT_29 = ItemData(290, RAC1ITEM.GOLD_BOLT_29, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 29)
    GOLD_BOLT_30 = ItemData(291, RAC1ITEM.GOLD_BOLT_30, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 30)
    GOLD_BOLT_31 = ItemData(292, RAC1ITEM.GOLD_BOLT_31, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 31)
    GOLD_BOLT_32 = ItemData(293, RAC1ITEM.GOLD_BOLT_32, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 32)
    GOLD_BOLT_33 = ItemData(294, RAC1ITEM.GOLD_BOLT_33, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 33)
    GOLD_BOLT_34 = ItemData(295, RAC1ITEM.GOLD_BOLT_34, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 34)
    GOLD_BOLT_35 = ItemData(296, RAC1ITEM.GOLD_BOLT_35, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 35)
    GOLD_BOLT_36 = ItemData(297, RAC1ITEM.GOLD_BOLT_36, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 36)
    GOLD_BOLT_37 = ItemData(298, RAC1ITEM.GOLD_BOLT_37, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 37)
    GOLD_BOLT_38 = ItemData(299, RAC1ITEM.GOLD_BOLT_38, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 38)
    GOLD_BOLT_39 = ItemData(300, RAC1ITEM.GOLD_BOLT_39, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 39)
    GOLD_BOLT_40 = ItemData(301, RAC1ITEM.GOLD_BOLT_40, RAC1POOL.GOLD_BOLTS,
                            ItemClassification.progression_deprioritized_skip_balancing, 40)

    BOLT_PACK = ItemData(302, RAC1ITEM.BOLT_PACK_GENERIC, RAC1POOL.FILLER,
                         ItemClassification.progression_deprioritized_skip_balancing)
    BOLT_PACK_0 = ItemData(400, RAC1ITEM.BOLT_PACK_0, RAC1POOL.FILLER,
                           ItemClassification.progression_deprioritized_skip_balancing, 0)
    BOLT_PACK_1 = ItemData(401, RAC1ITEM.BOLT_PACK_1, RAC1POOL.FILLER,
                           ItemClassification.progression_deprioritized_skip_balancing)
    BOLT_PACK_10 = ItemData(402, RAC1ITEM.BOLT_PACK_10, RAC1POOL.FILLER,
                            ItemClassification.progression_deprioritized_skip_balancing, 10)
    BOLT_PACK_100 = ItemData(403, RAC1ITEM.BOLT_PACK_100, RAC1POOL.FILLER,
                             ItemClassification.progression_deprioritized_skip_balancing, 100)
    BOLT_PACK_250 = ItemData(404, RAC1ITEM.BOLT_PACK_250, RAC1POOL.FILLER,
                             ItemClassification.progression_deprioritized_skip_balancing, 250)
    BOLT_PACK_500 = ItemData(405, RAC1ITEM.BOLT_PACK_500, RAC1POOL.FILLER,
                             ItemClassification.progression_deprioritized_skip_balancing, 500)
    BOLT_PACK_750 = ItemData(406, RAC1ITEM.BOLT_PACK_750, RAC1POOL.FILLER,
                             ItemClassification.progression_deprioritized_skip_balancing, 750)
    BOLT_PACK_1000 = ItemData(407, RAC1ITEM.BOLT_PACK_1000, RAC1POOL.FILLER,
                              ItemClassification.progression_deprioritized_skip_balancing, 1000)
    BOLT_PACK_2000 = ItemData(408, RAC1ITEM.BOLT_PACK_2000, RAC1POOL.FILLER,
                              ItemClassification.progression_deprioritized_skip_balancing, 2000)
    BOLT_PACK_3000 = ItemData(409, RAC1ITEM.BOLT_PACK_3000, RAC1POOL.FILLER,
                              ItemClassification.progression_deprioritized_skip_balancing, 3000)
    BOLT_PACK_4000 = ItemData(410, RAC1ITEM.BOLT_PACK_4000, RAC1POOL.FILLER,
                              ItemClassification.progression_deprioritized_skip_balancing, 4000)
    BOLT_PACK_5000 = ItemData(411, RAC1ITEM.BOLT_PACK_5000, RAC1POOL.FILLER,
                              ItemClassification.progression_deprioritized_skip_balancing, 5000)
    BOLT_PACK_6000 = ItemData(412, RAC1ITEM.BOLT_PACK_6000, RAC1POOL.FILLER,
                              ItemClassification.progression_deprioritized_skip_balancing, 6000)
    BOLT_PACK_7000 = ItemData(413, RAC1ITEM.BOLT_PACK_7000, RAC1POOL.FILLER,
                              ItemClassification.progression_deprioritized_skip_balancing, 7000)
    BOLT_PACK_8000 = ItemData(414, RAC1ITEM.BOLT_PACK_8000, RAC1POOL.FILLER,
                              ItemClassification.progression_deprioritized_skip_balancing, 8000)
    BOLT_PACK_9000 = ItemData(415, RAC1ITEM.BOLT_PACK_9000, RAC1POOL.FILLER,
                              ItemClassification.progression_deprioritized_skip_balancing, 9000)
    BOLT_PACK_10000 = ItemData(416, RAC1ITEM.BOLT_PACK_10000, RAC1POOL.FILLER,
                               ItemClassification.progression_deprioritized_skip_balancing, 10000)
    BOLT_PACK_12500 = ItemData(417, RAC1ITEM.BOLT_PACK_12500, RAC1POOL.FILLER,
                               ItemClassification.progression_deprioritized_skip_balancing, 12500)
    BOLT_PACK_15000 = ItemData(418, RAC1ITEM.BOLT_PACK_15000, RAC1POOL.FILLER,
                               ItemClassification.progression_deprioritized_skip_balancing, 15000)
    BOLT_PACK_17500 = ItemData(419, RAC1ITEM.BOLT_PACK_17500, RAC1POOL.FILLER,
                               ItemClassification.progression_deprioritized_skip_balancing, 17500)
    BOLT_PACK_20000 = ItemData(420, RAC1ITEM.BOLT_PACK_20000, RAC1POOL.FILLER,
                               ItemClassification.progression_deprioritized_skip_balancing, 20000)
    BOLT_PACK_25000 = ItemData(421, RAC1ITEM.BOLT_PACK_25000, RAC1POOL.FILLER,
                               ItemClassification.progression_deprioritized_skip_balancing, 25000)
    BOLT_PACK_30000 = ItemData(422, RAC1ITEM.BOLT_PACK_30000, RAC1POOL.FILLER,
                               ItemClassification.progression_deprioritized_skip_balancing, 30000)
    BOLT_PACK_40000 = ItemData(423, RAC1ITEM.BOLT_PACK_40000, RAC1POOL.FILLER,
                               ItemClassification.progression_deprioritized_skip_balancing, 40000)
    BOLT_PACK_50000 = ItemData(424, RAC1ITEM.BOLT_PACK_50000, RAC1POOL.FILLER,
                               ItemClassification.progression_deprioritized_skip_balancing, 50000)
    BOLT_PACK_75000 = ItemData(425, RAC1ITEM.BOLT_PACK_75000, RAC1POOL.FILLER,
                               ItemClassification.progression_deprioritized_skip_balancing, 75000)
    BOLT_PACK_100000 = ItemData(426, RAC1ITEM.BOLT_PACK_100000, RAC1POOL.FILLER,
                                ItemClassification.progression_deprioritized_skip_balancing, 100000)


WEAPONS: Sequence[ItemData] = [
    RAC1ItemData.TAUNTER,
    RAC1ItemData.VISIBOMB,
    RAC1ItemData.WALLOPER,
    RAC1ItemData.RYNO,
    RAC1ItemData.DRONE_DEVICE,
]

NON_PROGRESSIVE_WEAPONS: Sequence[ItemData] = [
    RAC1ItemData.SUCK_CANNON,
    RAC1ItemData.BOMB_GLOVE,
    RAC1ItemData.DEVASTATOR,
    RAC1ItemData.BLASTER,
    RAC1ItemData.PYROCITOR,
    RAC1ItemData.MINE_GLOVE,
    RAC1ItemData.TESLA_CLAW,
    RAC1ItemData.GLOVE_OF_DOOM,
    RAC1ItemData.MORPH_O_RAY,
    RAC1ItemData.DECOY_GLOVE,
]

PROGRESSIVE_WEAPONS: Sequence[ItemData] = [
    RAC1ItemData.PROGRESSIVE_SUCK,
    RAC1ItemData.PROGRESSIVE_BOMB,
    RAC1ItemData.PROGRESSIVE_DEVASTATOR,
    RAC1ItemData.PROGRESSIVE_BLASTER,
    RAC1ItemData.PROGRESSIVE_PYROCITOR,
    RAC1ItemData.PROGRESSIVE_MINE,
    RAC1ItemData.PROGRESSIVE_TESLA,
    RAC1ItemData.PROGRESSIVE_DOOM,
    RAC1ItemData.PROGRESSIVE_MORPH,
    RAC1ItemData.PROGRESSIVE_DECOY,
]

GOLD_WEAPONS: Sequence[ItemData] = [
    RAC1ItemData.GOLD_SUCK_CANNON,
    RAC1ItemData.GOLD_BOMB_GLOVE,
    RAC1ItemData.GOLD_DEVASTATOR,
    RAC1ItemData.GOLD_BLASTER,
    RAC1ItemData.GOLD_PYROCITOR,
    RAC1ItemData.GOLD_MINE_GLOVE,
    RAC1ItemData.GOLD_TESLA_CLAW,
    RAC1ItemData.GOLD_GLOVE_OF_DOOM,
    RAC1ItemData.GOLD_MORPH_O_RAY,
    RAC1ItemData.GOLD_DECOY_GLOVE,
]

PROGRESSIVE_GOLD_WEAPONS: Sequence[ItemData] = [
    RAC1ItemData.GOLD_SUCK_CANNON,
    RAC1ItemData.GOLD_BOMB_GLOVE,
    RAC1ItemData.GOLD_DEVASTATOR,
    RAC1ItemData.GOLD_BLASTER,
    RAC1ItemData.GOLD_PYROCITOR,
    RAC1ItemData.GOLD_MINE_GLOVE,
    RAC1ItemData.GOLD_TESLA_CLAW,
    RAC1ItemData.GOLD_GLOVE_OF_DOOM,
    RAC1ItemData.GOLD_MORPH_O_RAY,
    RAC1ItemData.GOLD_DECOY_GLOVE,
]

GADGETS: Sequence[ItemData] = [
    RAC1ItemData.HYDRODISPLACER,
    RAC1ItemData.TRESPASSER,
    RAC1ItemData.METAL_DETECTOR,
    RAC1ItemData.HOLOGUISE,
    RAC1ItemData.PDA,
    RAC1ItemData.SWINGSHOT,
]

PACKS: Sequence[ItemData] = [
    RAC1ItemData.HELI_PACK,
    RAC1ItemData.THRUSTER_PACK,
    RAC1ItemData.HYDRO_PACK,
]

PROGRESSIVE_PACKS: Sequence[ItemData] = [
    *[RAC1ItemData.PROGRESSIVE_PACK] * 3,
]

HELMETS: Sequence[ItemData] = [
    RAC1ItemData.SONIC_SUMMONER,
    RAC1ItemData.O2_MASK,
    RAC1ItemData.PILOTS_HELMET,
]

PROGRESSIVE_HELMETS: Sequence[ItemData] = [
    *[RAC1ItemData.PROGRESSIVE_HELMET] * 3,
]

BOOTS: Sequence[ItemData] = [
    RAC1ItemData.MAGNEBOOTS,
    RAC1ItemData.GRINDBOOTS,
]

PROGRESSIVE_BOOTS: Sequence[ItemData] = [
    *[RAC1ItemData.PROGRESSIVE_BOOT] * 2,
]

EXTRA_ITEMS: Sequence[ItemData] = [
    RAC1ItemData.MAP_O_MATIC,
    RAC1ItemData.BOLT_GRABBER,
    RAC1ItemData.CODEBOT,
]

NON_PROGRESSIVE_HOVERBOARDS: Sequence[ItemData] = [
    RAC1ItemData.HOVERBOARD,
    RAC1ItemData.ZOOMERATOR,
]

PROGRESSIVE_HOVERBOARDS: Sequence[ItemData] = [
    *[RAC1ItemData.PROGRESSIVE_HOVERBOARD] * 2,
]

NON_PROGRESSIVE_TRADES: Sequence[ItemData] = [
    RAC1ItemData.PERSUADER,
    RAC1ItemData.RARITANIUM,
]

PROGRESSIVE_TRADES: Sequence[ItemData] = [
    *[RAC1ItemData.PROGRESSIVE_TRADE] * 2,
]

NON_PROGRESSIVE_NANOTECHS: Sequence[ItemData] = [
    RAC1ItemData.PREMIUM_NANOTECH,
    RAC1ItemData.ULTRA_NANOTECH,
]

PROGRESSIVE_NANOTECHS: Sequence[ItemData] = [
    *[RAC1ItemData.PROGRESSIVE_NANOTECH] * 2,
]

GOLD_BOLTS: Sequence[ItemData] = [
    RAC1ItemData.GOLD_BOLT,
    RAC1ItemData.GOLD_BOLT_1,
    RAC1ItemData.GOLD_BOLT_2,
    RAC1ItemData.GOLD_BOLT_3,
    RAC1ItemData.GOLD_BOLT_4,
    RAC1ItemData.GOLD_BOLT_5,
    RAC1ItemData.GOLD_BOLT_6,
    RAC1ItemData.GOLD_BOLT_7,
    RAC1ItemData.GOLD_BOLT_8,
    RAC1ItemData.GOLD_BOLT_9,
    RAC1ItemData.GOLD_BOLT_10,
    RAC1ItemData.GOLD_BOLT_11,
    RAC1ItemData.GOLD_BOLT_12,
    RAC1ItemData.GOLD_BOLT_13,
    RAC1ItemData.GOLD_BOLT_14,
    RAC1ItemData.GOLD_BOLT_15,
    RAC1ItemData.GOLD_BOLT_16,
    RAC1ItemData.GOLD_BOLT_17,
    RAC1ItemData.GOLD_BOLT_18,
    RAC1ItemData.GOLD_BOLT_19,
    RAC1ItemData.GOLD_BOLT_20,
    RAC1ItemData.GOLD_BOLT_21,
    RAC1ItemData.GOLD_BOLT_22,
    RAC1ItemData.GOLD_BOLT_23,
    RAC1ItemData.GOLD_BOLT_24,
    RAC1ItemData.GOLD_BOLT_25,
    RAC1ItemData.GOLD_BOLT_26,
    RAC1ItemData.GOLD_BOLT_27,
    RAC1ItemData.GOLD_BOLT_28,
    RAC1ItemData.GOLD_BOLT_29,
    RAC1ItemData.GOLD_BOLT_30,
    RAC1ItemData.GOLD_BOLT_31,
    RAC1ItemData.GOLD_BOLT_32,
    RAC1ItemData.GOLD_BOLT_33,
    RAC1ItemData.GOLD_BOLT_34,
    RAC1ItemData.GOLD_BOLT_35,
    RAC1ItemData.GOLD_BOLT_36,
    RAC1ItemData.GOLD_BOLT_37,
    RAC1ItemData.GOLD_BOLT_38,
    RAC1ItemData.GOLD_BOLT_39,
    RAC1ItemData.GOLD_BOLT_40,
]

BOLT_PACKS: Sequence[ItemData] = [
    RAC1ItemData.BOLT_PACK,
    RAC1ItemData.BOLT_PACK_0,
    RAC1ItemData.BOLT_PACK_1,
    RAC1ItemData.BOLT_PACK_10,
    RAC1ItemData.BOLT_PACK_100,
    RAC1ItemData.BOLT_PACK_250,
    RAC1ItemData.BOLT_PACK_500,
    RAC1ItemData.BOLT_PACK_750,
    RAC1ItemData.BOLT_PACK_1000,
    RAC1ItemData.BOLT_PACK_2000,
    RAC1ItemData.BOLT_PACK_3000,
    RAC1ItemData.BOLT_PACK_4000,
    RAC1ItemData.BOLT_PACK_5000,
    RAC1ItemData.BOLT_PACK_6000,
    RAC1ItemData.BOLT_PACK_7000,
    RAC1ItemData.BOLT_PACK_8000,
    RAC1ItemData.BOLT_PACK_9000,
    RAC1ItemData.BOLT_PACK_10000,
    RAC1ItemData.BOLT_PACK_12500,
    RAC1ItemData.BOLT_PACK_15000,
    RAC1ItemData.BOLT_PACK_17500,
    RAC1ItemData.BOLT_PACK_20000,
    RAC1ItemData.BOLT_PACK_25000,
    RAC1ItemData.BOLT_PACK_30000,
    RAC1ItemData.BOLT_PACK_40000,
    RAC1ItemData.BOLT_PACK_50000,
    RAC1ItemData.BOLT_PACK_75000,
    RAC1ItemData.BOLT_PACK_100000,
]

PLANETS: Sequence[ItemData] = [
    RAC1ItemData.NOVALIS,
    RAC1ItemData.ARIDIA,
    RAC1ItemData.KERWAN,
    RAC1ItemData.EUDORA,
    RAC1ItemData.RILGAR,
    RAC1ItemData.BLARG,
    RAC1ItemData.UMBRIS,
    RAC1ItemData.BATALIA,
    RAC1ItemData.GASPAR,
    RAC1ItemData.ORXON,
    RAC1ItemData.POKITARU,
    RAC1ItemData.HOVEN,
    RAC1ItemData.GEMLIK,
    RAC1ItemData.OLTANIS,
    RAC1ItemData.QUARTU,
    RAC1ItemData.KALEBO,
    RAC1ItemData.FLEET,
    RAC1ItemData.VELDIN,
]

STARTING_PLANETS: Sequence[ItemData] = [
    RAC1ItemData.NOVALIS,
    RAC1ItemData.KERWAN,
    RAC1ItemData.BLARG,
    RAC1ItemData.BATALIA,
    RAC1ItemData.ORXON,
]

SKILLPOINTS: Sequence[ItemData] = [
    RAC1ItemData.TAKE_AIM,
    RAC1ItemData.SWING_IT,
    RAC1ItemData.TRANSPORTED,
    RAC1ItemData.STRIKE_A_POSE,
    RAC1ItemData.BLIMPY,
    RAC1ItemData.QWARKTASTIC,
    RAC1ItemData.ANY_TEN,
    RAC1ItemData.TRICKY,
    RAC1ItemData.CLUCK_CLUCK,
    RAC1ItemData.SPEEDY,
    RAC1ItemData.GIRL_TROUBLE,
    RAC1ItemData.JUMPER,
    RAC1ItemData.ACCURACY_COUNTS,
    RAC1ItemData.EAT_LEAD,
    RAC1ItemData.DESTROYED,
    RAC1ItemData.GUNNER,
    RAC1ItemData.SNIPER,
    RAC1ItemData.HEY_OVER_HERE,
    RAC1ItemData.ALIEN_INVASION,
    RAC1ItemData.BURIED_TREASURE,
    RAC1ItemData.PEST_CONTROL,
    RAC1ItemData.WHIRLYBIRDS,
    RAC1ItemData.SITTING_DUCKS,
    RAC1ItemData.SHATTERED_GLASS,
    RAC1ItemData.BLAST_EM,
    RAC1ItemData.HEAVY_TRAFFIC,
    RAC1ItemData.MAGICIAN,
    RAC1ItemData.SNEAKY,
    RAC1ItemData.CAREFUL_CRUISE,
    RAC1ItemData.GOING_COMMANDO,
]

ALL_ITEMS: Sequence[ItemData] = [*WEAPONS, *NON_PROGRESSIVE_WEAPONS, *PROGRESSIVE_WEAPONS, *GOLD_WEAPONS, *GADGETS,
                                 *PACKS, *PROGRESSIVE_PACKS, *HELMETS, *PROGRESSIVE_HELMETS, *BOOTS, *PROGRESSIVE_BOOTS,
                                 *EXTRA_ITEMS, *NON_PROGRESSIVE_HOVERBOARDS, *PROGRESSIVE_HOVERBOARDS,
                                 *NON_PROGRESSIVE_TRADES, *PROGRESSIVE_TRADES, *NON_PROGRESSIVE_NANOTECHS,
                                 *PROGRESSIVE_NANOTECHS, *GOLD_BOLTS, *PLANETS, *SKILLPOINTS, *BOLT_PACKS]

ITEM_POOL: Sequence[ItemData] = [*PLANETS, *WEAPONS, *GADGETS, *EXTRA_ITEMS, *SKILLPOINTS]

STARTING_WEAPONS: Sequence[ItemData] = [*WEAPONS, *NON_PROGRESSIVE_WEAPONS]
ALL_WEAPONS: Sequence[ItemData] = [*WEAPONS, *NON_PROGRESSIVE_WEAPONS, *PROGRESSIVE_WEAPONS, *GOLD_WEAPONS]
ALL_PACKS: Sequence[ItemData] = [*PACKS, *PROGRESSIVE_PACKS]
ALL_HELMETS: Sequence[ItemData] = [*HELMETS, *PROGRESSIVE_HELMETS]
ALL_BOOTS: Sequence[ItemData] = [*BOOTS, *PROGRESSIVE_BOOTS]
ALL_EXTRA_ITEMS: Sequence[ItemData] = [*EXTRA_ITEMS, *NON_PROGRESSIVE_HOVERBOARDS, *PROGRESSIVE_HOVERBOARDS,
                                       *NON_PROGRESSIVE_TRADES, *PROGRESSIVE_TRADES, *NON_PROGRESSIVE_NANOTECHS,
                                       *PROGRESSIVE_NANOTECHS]
ALL_HOVERBOARD: Sequence[ItemData] = [*NON_PROGRESSIVE_HOVERBOARDS, *PROGRESSIVE_HOVERBOARDS]
ALL_TRADE: Sequence[ItemData] = [*NON_PROGRESSIVE_TRADES, *PROGRESSIVE_TRADES]
ALL_NANOTECH: Sequence[ItemData] = [*NON_PROGRESSIVE_NANOTECHS, *PROGRESSIVE_NANOTECHS]
ALL_STARTING: Sequence[ItemData] = [*STARTING_WEAPONS, *GADGETS]

SUCK_GROUP: Sequence[ItemData] = [RAC1ItemData.SUCK_CANNON,
                                  RAC1ItemData.GOLD_SUCK_CANNON, RAC1ItemData.PROGRESSIVE_SUCK]
BOMB_GROUP: Sequence[ItemData] = [RAC1ItemData.BOMB_GLOVE, RAC1ItemData.GOLD_BOMB_GLOVE, RAC1ItemData.PROGRESSIVE_BOMB]
DEVASTATOR_GROUP: Sequence[ItemData] = [RAC1ItemData.DEVASTATOR,
                                        RAC1ItemData.GOLD_DEVASTATOR, RAC1ItemData.PROGRESSIVE_DEVASTATOR]
BLASTER_GROUP: Sequence[ItemData] = [RAC1ItemData.BLASTER, RAC1ItemData.GOLD_BLASTER, RAC1ItemData.PROGRESSIVE_BLASTER]
PYROCITOR_GROUP: Sequence[ItemData] = [RAC1ItemData.PYROCITOR,
                                       RAC1ItemData.GOLD_PYROCITOR, RAC1ItemData.PROGRESSIVE_PYROCITOR]
MINE_GROUP: Sequence[ItemData] = [RAC1ItemData.MINE_GLOVE, RAC1ItemData.GOLD_MINE_GLOVE, RAC1ItemData.PROGRESSIVE_MINE]
TESLA_GROUP: Sequence[ItemData] = [RAC1ItemData.TESLA_CLAW,
                                   RAC1ItemData.GOLD_TESLA_CLAW, RAC1ItemData.PROGRESSIVE_TESLA]
DOOM_GROUP: Sequence[ItemData] = [RAC1ItemData.GLOVE_OF_DOOM,
                                  RAC1ItemData.GOLD_GLOVE_OF_DOOM, RAC1ItemData.PROGRESSIVE_DOOM]
MORPH_GROUP: Sequence[ItemData] = [RAC1ItemData.MORPH_O_RAY,
                                   RAC1ItemData.GOLD_MORPH_O_RAY, RAC1ItemData.PROGRESSIVE_MORPH]
DECOY_GROUP: Sequence[ItemData] = [RAC1ItemData.DECOY_GLOVE,
                                   RAC1ItemData.GOLD_DECOY_GLOVE, RAC1ItemData.PROGRESSIVE_DECOY]


def get_bolt_pack(_options) -> str:
    lookup: dict[int, str] = {
        RAC1ItemData.BOLT_PACK_0.quantity: RAC1ITEM.BOLT_PACK_0,
        RAC1ItemData.BOLT_PACK_1.quantity: RAC1ITEM.BOLT_PACK_1,
        RAC1ItemData.BOLT_PACK_10.quantity: RAC1ITEM.BOLT_PACK_10,
        RAC1ItemData.BOLT_PACK_100.quantity: RAC1ITEM.BOLT_PACK_100,
        RAC1ItemData.BOLT_PACK_250.quantity: RAC1ITEM.BOLT_PACK_250,
        RAC1ItemData.BOLT_PACK_500.quantity: RAC1ITEM.BOLT_PACK_500,
        RAC1ItemData.BOLT_PACK_750.quantity: RAC1ITEM.BOLT_PACK_750,
        RAC1ItemData.BOLT_PACK_1000.quantity: RAC1ITEM.BOLT_PACK_1000,
        RAC1ItemData.BOLT_PACK_2000.quantity: RAC1ITEM.BOLT_PACK_2000,
        RAC1ItemData.BOLT_PACK_3000.quantity: RAC1ITEM.BOLT_PACK_3000,
        RAC1ItemData.BOLT_PACK_4000.quantity: RAC1ITEM.BOLT_PACK_4000,
        RAC1ItemData.BOLT_PACK_5000.quantity: RAC1ITEM.BOLT_PACK_5000,
        RAC1ItemData.BOLT_PACK_6000.quantity: RAC1ITEM.BOLT_PACK_6000,
        RAC1ItemData.BOLT_PACK_7000.quantity: RAC1ITEM.BOLT_PACK_7000,
        RAC1ItemData.BOLT_PACK_8000.quantity: RAC1ITEM.BOLT_PACK_8000,
        RAC1ItemData.BOLT_PACK_9000.quantity: RAC1ITEM.BOLT_PACK_9000,
        RAC1ItemData.BOLT_PACK_10000.quantity: RAC1ITEM.BOLT_PACK_10000,
        RAC1ItemData.BOLT_PACK_12500.quantity: RAC1ITEM.BOLT_PACK_12500,
        RAC1ItemData.BOLT_PACK_15000.quantity: RAC1ITEM.BOLT_PACK_15000,
        RAC1ItemData.BOLT_PACK_17500.quantity: RAC1ITEM.BOLT_PACK_17500,
        RAC1ItemData.BOLT_PACK_20000.quantity: RAC1ITEM.BOLT_PACK_20000,
        RAC1ItemData.BOLT_PACK_25000.quantity: RAC1ITEM.BOLT_PACK_25000,
        RAC1ItemData.BOLT_PACK_30000.quantity: RAC1ITEM.BOLT_PACK_30000,
        RAC1ItemData.BOLT_PACK_40000.quantity: RAC1ITEM.BOLT_PACK_40000,
        RAC1ItemData.BOLT_PACK_50000.quantity: RAC1ITEM.BOLT_PACK_50000,
        RAC1ItemData.BOLT_PACK_75000.quantity: RAC1ITEM.BOLT_PACK_75000,
        RAC1ItemData.BOLT_PACK_100000.quantity: RAC1ITEM.BOLT_PACK_100000,
    }
    return lookup[_options.pack_size_bolts.value]


def get_gold_bolts(_options) -> str:
    lookup: dict[int, str] = {}
    for gold_bolt in GOLD_BOLTS:
        if gold_bolt == RAC1ITEM.GOLD_BOLT:
            continue
        lookup.update({gold_bolt.quantity: gold_bolt.name})
    return lookup[_options.pack_size_gold_bolts.value]


def progression_rules(world):
    world.orders = {
        RAC1ORDER.SUCK_CANNON: [RAC1ItemData.SUCK_CANNON.item_id, RAC1ItemData.GOLD_SUCK_CANNON.item_id],
        RAC1ORDER.BOMB_GLOVE: [RAC1ItemData.BOMB_GLOVE.item_id, RAC1ItemData.GOLD_BOMB_GLOVE.item_id],
        RAC1ORDER.DEVASTATOR: [RAC1ItemData.DEVASTATOR.item_id, RAC1ItemData.GOLD_DEVASTATOR.item_id],
        RAC1ORDER.BLASTER: [RAC1ItemData.BLASTER.item_id, RAC1ItemData.GOLD_BLASTER.item_id],
        RAC1ORDER.PYROCITOR: [RAC1ItemData.PYROCITOR.item_id, RAC1ItemData.GOLD_PYROCITOR.item_id],
        RAC1ORDER.MINE_GLOVE: [RAC1ItemData.MINE_GLOVE.item_id, RAC1ItemData.GOLD_MINE_GLOVE.item_id],
        RAC1ORDER.TESLA_CLAW: [RAC1ItemData.TESLA_CLAW.item_id, RAC1ItemData.GOLD_TESLA_CLAW.item_id],
        RAC1ORDER.GLOVE_OF_DOOM: [RAC1ItemData.GLOVE_OF_DOOM.item_id, RAC1ItemData.GOLD_GLOVE_OF_DOOM.item_id],
        RAC1ORDER.MORPH_O_RAY: [RAC1ItemData.MORPH_O_RAY.item_id, RAC1ItemData.GOLD_MORPH_O_RAY.item_id],
        RAC1ORDER.DECOY_GLOVE: [RAC1ItemData.DECOY_GLOVE.item_id, RAC1ItemData.GOLD_DECOY_GLOVE.item_id],
        RAC1ORDER.PACKS: [RAC1ItemData.HELI_PACK.item_id,
                          RAC1ItemData.THRUSTER_PACK.item_id, RAC1ItemData.HYDRO_PACK.item_id],
        RAC1ORDER.HELMETS: [RAC1ItemData.O2_MASK.item_id,
                            RAC1ItemData.SONIC_SUMMONER.item_id, RAC1ItemData.PILOTS_HELMET.item_id],
        RAC1ORDER.BOOTS: [RAC1ItemData.GRINDBOOTS.item_id, RAC1ItemData.MAGNEBOOTS.item_id],
        RAC1ORDER.HOVERBOARD: [RAC1ItemData.HOVERBOARD.item_id, RAC1ItemData.ZOOMERATOR.item_id],
        RAC1ORDER.TRADE: [RAC1ItemData.RARITANIUM.item_id, RAC1ItemData.PERSUADER.item_id],
        RAC1ORDER.NANOTECH: [RAC1ItemData.PREMIUM_NANOTECH.item_id, RAC1ItemData.ULTRA_NANOTECH.item_id],
    }
    world.progressive_convert = {
        RAC1ITEM.HELI_PACK: {RAC1ITEM.HELI_PACK: 1},
        RAC1ITEM.THRUSTER_PACK: {RAC1ITEM.THRUSTER_PACK: 1},
        RAC1ITEM.HYDRO_PACK: {RAC1ITEM.HYDRO_PACK: 1},
        RAC1ITEM.SONIC_SUMMONER: {RAC1ITEM.SONIC_SUMMONER: 1, RAC1ITEM.PROGRESSIVE_HELMET: 2},
        RAC1ITEM.O2_MASK: {RAC1ITEM.O2_MASK: 1, RAC1ITEM.PROGRESSIVE_HELMET: 1},
        RAC1ITEM.PILOTS_HELMET: {RAC1ITEM.PILOTS_HELMET: 1, RAC1ITEM.PROGRESSIVE_HELMET: 3},
        RAC1ITEM.SUCK_CANNON: {RAC1ITEM.SUCK_CANNON: 1},
        RAC1ITEM.GOLD_SUCK_CANNON: {RAC1ITEM.SUCK_CANNON: 1, RAC1ITEM.GOLD_SUCK_CANNON: 1},
        RAC1ITEM.BOMB_GLOVE: {RAC1ITEM.BOMB_GLOVE: 1},
        RAC1ITEM.GOLD_BOMB_GLOVE: {RAC1ITEM.BOMB_GLOVE: 1, RAC1ITEM.GOLD_BOMB_GLOVE: 1},
        RAC1ITEM.DEVASTATOR: {RAC1ITEM.DEVASTATOR: 1},
        RAC1ITEM.GOLD_DEVASTATOR: {RAC1ITEM.DEVASTATOR: 1, RAC1ITEM.GOLD_DEVASTATOR: 1},
        RAC1ITEM.BLASTER: {RAC1ITEM.BLASTER: 1},
        RAC1ITEM.GOLD_BLASTER: {RAC1ITEM.BLASTER: 1, RAC1ITEM.GOLD_BLASTER: 1},
        RAC1ITEM.PYROCITOR: {RAC1ITEM.PYROCITOR: 1},
        RAC1ITEM.GOLD_PYROCITOR: {RAC1ITEM.PYROCITOR: 1, RAC1ITEM.GOLD_PYROCITOR: 1},
        RAC1ITEM.MINE_GLOVE: {RAC1ITEM.MINE_GLOVE: 1},
        RAC1ITEM.GOLD_MINE_GLOVE: {RAC1ITEM.MINE_GLOVE: 1, RAC1ITEM.GOLD_MINE_GLOVE: 1},
        RAC1ITEM.TESLA_CLAW: {RAC1ITEM.TESLA_CLAW: 1},
        RAC1ITEM.GOLD_TESLA_CLAW: {RAC1ITEM.TESLA_CLAW: 1, RAC1ITEM.GOLD_TESLA_CLAW: 1},
        RAC1ITEM.GLOVE_OF_DOOM: {RAC1ITEM.GLOVE_OF_DOOM: 1},
        RAC1ITEM.GOLD_GLOVE_OF_DOOM: {RAC1ITEM.GLOVE_OF_DOOM: 1, RAC1ITEM.GOLD_GLOVE_OF_DOOM: 1},
        RAC1ITEM.MORPH_O_RAY: {RAC1ITEM.MORPH_O_RAY: 1},
        RAC1ITEM.GOLD_MORPH_O_RAY: {RAC1ITEM.MORPH_O_RAY: 1, RAC1ITEM.GOLD_MORPH_O_RAY: 1},
        RAC1ITEM.DECOY_GLOVE: {RAC1ITEM.DECOY_GLOVE: 1},
        RAC1ITEM.GOLD_DECOY_GLOVE: {RAC1ITEM.DECOY_GLOVE: 1, RAC1ITEM.GOLD_DECOY_GLOVE: 1},
        RAC1ITEM.MAGNEBOOTS: {RAC1ITEM.MAGNEBOOTS: 1, RAC1ITEM.PROGRESSIVE_BOOT: 2},
        RAC1ITEM.GRINDBOOTS: {RAC1ITEM.GRINDBOOTS: 1, RAC1ITEM.PROGRESSIVE_BOOT: 1},
        RAC1ITEM.HOVERBOARD: {RAC1ITEM.HOVERBOARD: 1, RAC1ITEM.PROGRESSIVE_HOVERBOARD: 1},
        RAC1ITEM.ZOOMERATOR: {RAC1ITEM.ZOOMERATOR: 1, RAC1ITEM.PROGRESSIVE_HOVERBOARD: 2},
        RAC1ITEM.PERSUADER: {RAC1ITEM.PERSUADER: 1, RAC1ITEM.PROGRESSIVE_TRADE: 1},
        RAC1ITEM.RARITANIUM: {RAC1ITEM.RARITANIUM: 1, RAC1ITEM.PROGRESSIVE_TRADE: 2},
        RAC1ITEM.PREMIUM_NANOTECH: {RAC1ITEM.PREMIUM_NANOTECH: 1, RAC1ITEM.PROGRESSIVE_NANOTECH: 1},
        RAC1ITEM.ULTRA_NANOTECH: {RAC1ITEM.ULTRA_NANOTECH: 1, RAC1ITEM.PROGRESSIVE_NANOTECH: 2},
    }
    match world.options.progressive_weapons.value:
        case GoldWeaponProgression.option_normal:
            world.progressive_convert[RAC1ITEM.SUCK_CANNON] = {RAC1ITEM.SUCK_CANNON: 1,
                                                               RAC1ITEM.GOLD_SUCK_CANNON: 1}
            world.progressive_convert[RAC1ITEM.GOLD_SUCK_CANNON] = {RAC1ITEM.GOLD_SUCK_CANNON: 1}
            world.progressive_convert[RAC1ITEM.BOMB_GLOVE] = {RAC1ITEM.BOMB_GLOVE: 1,
                                                              RAC1ITEM.GOLD_BOMB_GLOVE: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BOMB_GLOVE] = {RAC1ITEM.GOLD_BOMB_GLOVE: 1}
            world.progressive_convert[RAC1ITEM.DEVASTATOR] = {RAC1ITEM.DEVASTATOR: 1,
                                                              RAC1ITEM.GOLD_DEVASTATOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DEVASTATOR] = {RAC1ITEM.GOLD_DEVASTATOR: 1}
            world.progressive_convert[RAC1ITEM.BLASTER] = {RAC1ITEM.BLASTER: 1,
                                                           RAC1ITEM.GOLD_BLASTER: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BLASTER] = {RAC1ITEM.GOLD_BLASTER: 1}
            world.progressive_convert[RAC1ITEM.PYROCITOR] = {RAC1ITEM.PYROCITOR: 1,
                                                             RAC1ITEM.GOLD_PYROCITOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_PYROCITOR] = {RAC1ITEM.GOLD_PYROCITOR: 1}
            world.progressive_convert[RAC1ITEM.MINE_GLOVE] = {RAC1ITEM.MINE_GLOVE: 1,
                                                              RAC1ITEM.GOLD_MINE_GLOVE: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MINE_GLOVE] = {RAC1ITEM.GOLD_MINE_GLOVE: 1}
            world.progressive_convert[RAC1ITEM.TESLA_CLAW] = {RAC1ITEM.TESLA_CLAW: 1,
                                                              RAC1ITEM.GOLD_TESLA_CLAW: 1}
            world.progressive_convert[RAC1ITEM.GOLD_TESLA_CLAW] = {RAC1ITEM.GOLD_TESLA_CLAW: 1}
            world.progressive_convert[RAC1ITEM.GLOVE_OF_DOOM] = {RAC1ITEM.GLOVE_OF_DOOM: 1,
                                                                 RAC1ITEM.GOLD_GLOVE_OF_DOOM: 1}
            world.progressive_convert[RAC1ITEM.GOLD_GLOVE_OF_DOOM] = {RAC1ITEM.GOLD_GLOVE_OF_DOOM: 1}
            world.progressive_convert[RAC1ITEM.MORPH_O_RAY] = {RAC1ITEM.MORPH_O_RAY: 1,
                                                               RAC1ITEM.GOLD_MORPH_O_RAY: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MORPH_O_RAY] = {RAC1ITEM.GOLD_MORPH_O_RAY: 1}
            world.progressive_convert[RAC1ITEM.DECOY_GLOVE] = {RAC1ITEM.DECOY_GLOVE: 1,
                                                               RAC1ITEM.GOLD_DECOY_GLOVE: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DECOY_GLOVE] = {RAC1ITEM.GOLD_DECOY_GLOVE: 1}
        case GoldWeaponProgression.option_progressive:
            world.progressive_convert[RAC1ITEM.SUCK_CANNON] = {RAC1ITEM.PROGRESSIVE_SUCK: 1}
            world.progressive_convert[RAC1ITEM.GOLD_SUCK_CANNON] = {RAC1ITEM.PROGRESSIVE_SUCK: 2}
            world.progressive_convert[RAC1ITEM.BOMB_GLOVE] = {RAC1ITEM.PROGRESSIVE_BOMB: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BOMB_GLOVE] = {RAC1ITEM.PROGRESSIVE_BOMB: 2}
            world.progressive_convert[RAC1ITEM.DEVASTATOR] = {RAC1ITEM.PROGRESSIVE_DEVASTATOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DEVASTATOR] = {RAC1ITEM.PROGRESSIVE_DEVASTATOR: 2}
            world.progressive_convert[RAC1ITEM.BLASTER] = {RAC1ITEM.PROGRESSIVE_BLASTER: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BLASTER] = {RAC1ITEM.PROGRESSIVE_BLASTER: 2}
            world.progressive_convert[RAC1ITEM.PYROCITOR] = {RAC1ITEM.PROGRESSIVE_PYROCITOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_PYROCITOR] = {RAC1ITEM.PROGRESSIVE_PYROCITOR: 2}
            world.progressive_convert[RAC1ITEM.MINE_GLOVE] = {RAC1ITEM.PROGRESSIVE_MINE: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MINE_GLOVE] = {RAC1ITEM.PROGRESSIVE_MINE: 2}
            world.progressive_convert[RAC1ITEM.TESLA_CLAW] = {RAC1ITEM.PROGRESSIVE_TESLA: 1}
            world.progressive_convert[RAC1ITEM.GOLD_TESLA_CLAW] = {RAC1ITEM.PROGRESSIVE_TESLA: 2}
            world.progressive_convert[RAC1ITEM.GLOVE_OF_DOOM] = {RAC1ITEM.PROGRESSIVE_DOOM: 1}
            world.progressive_convert[RAC1ITEM.GOLD_GLOVE_OF_DOOM] = {RAC1ITEM.PROGRESSIVE_DOOM: 2}
            world.progressive_convert[RAC1ITEM.MORPH_O_RAY] = {RAC1ITEM.PROGRESSIVE_MORPH: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MORPH_O_RAY] = {RAC1ITEM.PROGRESSIVE_MORPH: 2}
            world.progressive_convert[RAC1ITEM.DECOY_GLOVE] = {RAC1ITEM.PROGRESSIVE_DECOY: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DECOY_GLOVE] = {RAC1ITEM.PROGRESSIVE_DECOY: 2}
        case GoldWeaponProgression.option_progressive_reversed:
            world.orders[RAC1ORDER.SUCK_CANNON].reverse()
            world.progressive_convert[RAC1ITEM.SUCK_CANNON] = {RAC1ITEM.PROGRESSIVE_SUCK: 1}
            world.progressive_convert[RAC1ITEM.GOLD_SUCK_CANNON] = {RAC1ITEM.PROGRESSIVE_SUCK: 1}
            world.orders[RAC1ORDER.BOMB_GLOVE].reverse()
            world.progressive_convert[RAC1ITEM.BOMB_GLOVE] = {RAC1ITEM.PROGRESSIVE_BOMB: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BOMB_GLOVE] = {RAC1ITEM.PROGRESSIVE_BOMB: 1}
            world.orders[RAC1ORDER.DEVASTATOR].reverse()
            world.progressive_convert[RAC1ITEM.DEVASTATOR] = {RAC1ITEM.PROGRESSIVE_DEVASTATOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DEVASTATOR] = {RAC1ITEM.PROGRESSIVE_DEVASTATOR: 1}
            world.orders[RAC1ORDER.BLASTER].reverse()
            world.progressive_convert[RAC1ITEM.BLASTER] = {RAC1ITEM.PROGRESSIVE_BLASTER: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BLASTER] = {RAC1ITEM.PROGRESSIVE_BLASTER: 1}
            world.orders[RAC1ORDER.PYROCITOR].reverse()
            world.progressive_convert[RAC1ITEM.PYROCITOR] = {RAC1ITEM.PROGRESSIVE_PYROCITOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_PYROCITOR] = {RAC1ITEM.PROGRESSIVE_PYROCITOR: 1}
            world.orders[RAC1ORDER.MINE_GLOVE].reverse()
            world.progressive_convert[RAC1ITEM.MINE_GLOVE] = {RAC1ITEM.PROGRESSIVE_MINE: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MINE_GLOVE] = {RAC1ITEM.PROGRESSIVE_MINE: 1}
            world.orders[RAC1ORDER.TESLA_CLAW].reverse()
            world.progressive_convert[RAC1ITEM.TESLA_CLAW] = {RAC1ITEM.PROGRESSIVE_TESLA: 1}
            world.progressive_convert[RAC1ITEM.GOLD_TESLA_CLAW] = {RAC1ITEM.PROGRESSIVE_TESLA: 1}
            world.orders[RAC1ORDER.GLOVE_OF_DOOM].reverse()
            world.progressive_convert[RAC1ITEM.GLOVE_OF_DOOM] = {RAC1ITEM.PROGRESSIVE_DOOM: 1}
            world.progressive_convert[RAC1ITEM.GOLD_GLOVE_OF_DOOM] = {RAC1ITEM.PROGRESSIVE_DOOM: 1}
            world.orders[RAC1ORDER.MORPH_O_RAY].reverse()
            world.progressive_convert[RAC1ITEM.MORPH_O_RAY] = {RAC1ITEM.PROGRESSIVE_MORPH: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MORPH_O_RAY] = {RAC1ITEM.PROGRESSIVE_MORPH: 1}
            world.orders[RAC1ORDER.DECOY_GLOVE].reverse()
            world.progressive_convert[RAC1ITEM.DECOY_GLOVE] = {RAC1ITEM.PROGRESSIVE_DECOY: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DECOY_GLOVE] = {RAC1ITEM.PROGRESSIVE_DECOY: 1}
        case GoldWeaponProgression.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.SUCK_CANNON])
            world.progressive_convert[RAC1ITEM.SUCK_CANNON] = {RAC1ITEM.PROGRESSIVE_SUCK: 1}
            world.progressive_convert[RAC1ITEM.GOLD_SUCK_CANNON] = {
                RAC1ITEM.PROGRESSIVE_SUCK:
                    1 + world.orders[RAC1ORDER.SUCK_CANNON].index(RAC1ItemData.GOLD_SUCK_CANNON.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.BOMB_GLOVE])
            world.progressive_convert[RAC1ITEM.BOMB_GLOVE] = {RAC1ITEM.PROGRESSIVE_BOMB: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BOMB_GLOVE] = {
                RAC1ITEM.PROGRESSIVE_BOMB:
                    1 + world.orders[RAC1ORDER.BOMB_GLOVE].index(RAC1ItemData.GOLD_BOMB_GLOVE.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.DEVASTATOR])
            world.progressive_convert[RAC1ITEM.DEVASTATOR] = {RAC1ITEM.PROGRESSIVE_DEVASTATOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DEVASTATOR] = {
                RAC1ITEM.PROGRESSIVE_DEVASTATOR:
                    1 + world.orders[RAC1ORDER.DEVASTATOR].index(RAC1ItemData.GOLD_DEVASTATOR.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.BLASTER])
            world.progressive_convert[RAC1ITEM.BLASTER] = {RAC1ITEM.PROGRESSIVE_BLASTER: 1}
            world.progressive_convert[RAC1ITEM.GOLD_BLASTER] = {
                RAC1ITEM.PROGRESSIVE_BLASTER:
                    1 + world.orders[RAC1ORDER.BLASTER].index(RAC1ItemData.GOLD_BLASTER.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.PYROCITOR])
            world.progressive_convert[RAC1ITEM.PYROCITOR] = {RAC1ITEM.PROGRESSIVE_PYROCITOR: 1}
            world.progressive_convert[RAC1ITEM.GOLD_PYROCITOR] = {
                RAC1ITEM.PROGRESSIVE_PYROCITOR:
                    1 + world.orders[RAC1ORDER.PYROCITOR].index(RAC1ItemData.GOLD_PYROCITOR.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.MINE_GLOVE])
            world.progressive_convert[RAC1ITEM.MINE_GLOVE] = {RAC1ITEM.PROGRESSIVE_MINE: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MINE_GLOVE] = {
                RAC1ITEM.PROGRESSIVE_MINE:
                    1 + world.orders[RAC1ORDER.MINE_GLOVE].index(RAC1ItemData.GOLD_MINE_GLOVE.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.TESLA_CLAW])
            world.progressive_convert[RAC1ITEM.TESLA_CLAW] = {RAC1ITEM.PROGRESSIVE_TESLA: 1}
            world.progressive_convert[RAC1ITEM.GOLD_TESLA_CLAW] = {
                RAC1ITEM.PROGRESSIVE_TESLA:
                    1 + world.orders[RAC1ORDER.TESLA_CLAW].index(RAC1ItemData.TESLA_CLAW.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.GLOVE_OF_DOOM])
            world.progressive_convert[RAC1ITEM.GLOVE_OF_DOOM] = {RAC1ITEM.PROGRESSIVE_DOOM: 1}
            world.progressive_convert[RAC1ITEM.GOLD_GLOVE_OF_DOOM] = {
                RAC1ITEM.PROGRESSIVE_DOOM:
                    1 + world.orders[RAC1ORDER.GLOVE_OF_DOOM].index(RAC1ItemData.GOLD_GLOVE_OF_DOOM.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.MORPH_O_RAY])
            world.progressive_convert[RAC1ITEM.MORPH_O_RAY] = {RAC1ITEM.PROGRESSIVE_MORPH: 1}
            world.progressive_convert[RAC1ITEM.GOLD_MORPH_O_RAY] = {
                RAC1ITEM.PROGRESSIVE_MORPH:
                    1 + world.orders[RAC1ORDER.MORPH_O_RAY].index(RAC1ItemData.GOLD_MORPH_O_RAY.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.DECOY_GLOVE])
            world.progressive_convert[RAC1ITEM.DECOY_GLOVE] = {RAC1ITEM.PROGRESSIVE_DECOY: 1}
            world.progressive_convert[RAC1ITEM.GOLD_DECOY_GLOVE] = {
                RAC1ITEM.PROGRESSIVE_DECOY:
                    1 + world.orders[RAC1ORDER.DECOY_GLOVE].index(RAC1ItemData.GOLD_DECOY_GLOVE.item_id)}
        case _:
            pass

    match world.options.progressive_packs.value:
        case PackProgression.option_progressive:
            world.progressive_convert[RAC1ITEM.HELI_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 1}
            world.progressive_convert[RAC1ITEM.THRUSTER_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 2}
            world.progressive_convert[RAC1ITEM.HYDRO_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 3}
        case PackProgression.option_progressive_reversed:
            world.orders[RAC1ORDER.PACKS].reverse()
            world.progressive_convert[RAC1ITEM.HELI_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 3}
            world.progressive_convert[RAC1ITEM.THRUSTER_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 2}
            world.progressive_convert[RAC1ITEM.HYDRO_PACK] = {RAC1ITEM.PROGRESSIVE_PACK: 1}
        case PackProgression.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.PACKS])
            world.progressive_convert[RAC1ITEM.HELI_PACK] = {
                RAC1ITEM.PROGRESSIVE_PACK: 1 + world.orders[RAC1ORDER.PACKS].index(RAC1ItemData.HELI_PACK.item_id)}
            world.progressive_convert[RAC1ITEM.THRUSTER_PACK] = {
                RAC1ITEM.PROGRESSIVE_PACK: 1 + world.orders[RAC1ORDER.PACKS].index(RAC1ItemData.THRUSTER_PACK.item_id)}
            world.progressive_convert[RAC1ITEM.HYDRO_PACK] = {
                RAC1ITEM.PROGRESSIVE_PACK: 1 + world.orders[RAC1ORDER.PACKS].index(RAC1ItemData.HYDRO_PACK.item_id)}
        case _:
            pass

    match world.options.progressive_helmets.value:
        case HelmetProgression.option_progressive:
            world.progressive_convert[RAC1ITEM.O2_MASK] = {RAC1ITEM.PROGRESSIVE_HELMET: 1}
            if world.options.shuffle_helmets.value <= ShuffleHelmets.option_random_same:
                world.progressive_convert[RAC1ITEM.SONIC_SUMMONER] = {RAC1ITEM.PROGRESSIVE_HELMET: 3}
                world.progressive_convert[RAC1ITEM.PILOTS_HELMET] = {RAC1ITEM.PROGRESSIVE_HELMET: 2}
                world.orders[RAC1ORDER.HELMETS] = [RAC1ItemData.O2_MASK.item_id, RAC1ItemData.PILOTS_HELMET.item_id,
                                                   RAC1ItemData.SONIC_SUMMONER.item_id]
            else:
                world.progressive_convert[RAC1ITEM.SONIC_SUMMONER] = {RAC1ITEM.PROGRESSIVE_HELMET: 2}
                world.progressive_convert[RAC1ITEM.PILOTS_HELMET] = {RAC1ITEM.PROGRESSIVE_HELMET: 3}
        case HelmetProgression.option_progressive_reversed:
            world.orders[RAC1ORDER.HELMETS].reverse()
            world.progressive_convert[RAC1ITEM.O2_MASK] = {RAC1ITEM.PROGRESSIVE_HELMET: 3}
            world.progressive_convert[RAC1ITEM.SONIC_SUMMONER] = {RAC1ITEM.PROGRESSIVE_HELMET: 2}
            world.progressive_convert[RAC1ITEM.PILOTS_HELMET] = {RAC1ITEM.PROGRESSIVE_HELMET: 1}
        case HelmetProgression.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.HELMETS])
            world.progressive_convert[RAC1ITEM.O2_MASK] = {
                RAC1ITEM.PROGRESSIVE_HELMET:
                    1 + world.orders[RAC1ORDER.HELMETS].index(RAC1ItemData.O2_MASK.item_id)}
            world.progressive_convert[RAC1ITEM.SONIC_SUMMONER] = {
                RAC1ITEM.PROGRESSIVE_HELMET:
                    1 + world.orders[RAC1ORDER.HELMETS].index(RAC1ItemData.SONIC_SUMMONER.item_id)}
            world.progressive_convert[RAC1ITEM.PILOTS_HELMET] = {
                RAC1ITEM.PROGRESSIVE_HELMET:
                    1 + world.orders[RAC1ORDER.HELMETS].index(RAC1ItemData.PILOTS_HELMET.item_id)}
            if (world.options.shuffle_helmets.value <= ShuffleHelmets.option_random_same
                    and world.progressive_convert[RAC1ITEM.PILOTS_HELMET].values() == 3):
                temp = world.progressive_convert[RAC1ITEM.PILOTS_HELMET]
                world.progressive_convert[RAC1ITEM.PILOTS_HELMET] = world.progressive_convert[RAC1ITEM.SONIC_SUMMONER]
                world.progressive_convert[RAC1ITEM.SONIC_SUMMONER] = temp
                if world.orders[RAC1ORDER.HELMETS].index(RAC1ItemData.O2_MASK.item_id) == 0:
                    world.orders[RAC1ORDER.HELMETS] = [RAC1ItemData.O2_MASK.item_id, RAC1ItemData.PILOTS_HELMET.item_id,
                                                       RAC1ItemData.SONIC_SUMMONER.item_id]
                else:
                    world.orders[RAC1ORDER.HELMETS] = [RAC1ItemData.PILOTS_HELMET.item_id, RAC1ItemData.O2_MASK.item_id,
                                                       RAC1ItemData.SONIC_SUMMONER.item_id]

        case _:
            pass

    match world.options.progressive_boots.value:
        case BootsProgression.option_progressive:
            world.progressive_convert[RAC1ITEM.GRINDBOOTS] = {RAC1ITEM.PROGRESSIVE_BOOT: 1}
            world.progressive_convert[RAC1ITEM.MAGNEBOOTS] = {RAC1ITEM.PROGRESSIVE_BOOT: 2}
        case BootsProgression.option_progressive_reversed:
            world.orders[RAC1ORDER.BOOTS].reverse()
            world.progressive_convert[RAC1ITEM.GRINDBOOTS] = {RAC1ITEM.PROGRESSIVE_BOOT: 2}
            world.progressive_convert[RAC1ITEM.MAGNEBOOTS] = {RAC1ITEM.PROGRESSIVE_BOOT: 1}
        case BootsProgression.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.BOOTS])
            world.progressive_convert[RAC1ITEM.GRINDBOOTS] = {
                RAC1ITEM.PROGRESSIVE_BOOT:
                    1 + world.orders[RAC1ORDER.BOOTS].index(RAC1ItemData.GRINDBOOTS.item_id)}
            world.progressive_convert[RAC1ITEM.MAGNEBOOTS] = {
                RAC1ITEM.PROGRESSIVE_BOOT:
                    1 + world.orders[RAC1ORDER.BOOTS].index(RAC1ItemData.MAGNEBOOTS.item_id)}
        case _:
            pass

    if world.options.shuffle_extra_items.value == ShuffleExtraItems.option_vanilla:
        world.progressive_convert[RAC1ITEM.HOVERBOARD] = {RAC1ITEM.HOVERBOARD: 1, RAC1ITEM.PROGRESSIVE_HOVERBOARD: 1}
        world.progressive_convert[RAC1ITEM.ZOOMERATOR] = {RAC1ITEM.ZOOMERATOR: 1, RAC1ITEM.PROGRESSIVE_HOVERBOARD: 2}
    else:
        match world.options.progressive_hoverboard.value:
            case HoverboardProgression.option_progressive:
                world.progressive_convert[RAC1ITEM.HOVERBOARD] = {RAC1ITEM.PROGRESSIVE_HOVERBOARD: 1}
                world.progressive_convert[RAC1ITEM.ZOOMERATOR] = {RAC1ITEM.PROGRESSIVE_HOVERBOARD: 2}
            case HoverboardProgression.option_progressive_reversed:
                world.orders[RAC1ORDER.HOVERBOARD].reverse()
                world.progressive_convert[RAC1ITEM.HOVERBOARD] = {RAC1ITEM.PROGRESSIVE_HOVERBOARD: 2}
                world.progressive_convert[RAC1ITEM.ZOOMERATOR] = {RAC1ITEM.PROGRESSIVE_HOVERBOARD: 1}
            case HoverboardProgression.option_progressive_random:
                world.random.shuffle(world.orders[RAC1ORDER.HOVERBOARD])
                world.progressive_convert[RAC1ITEM.HOVERBOARD] = {
                    RAC1ITEM.PROGRESSIVE_HOVERBOARD:
                        1 + world.orders[RAC1ORDER.HOVERBOARD].index(RAC1ItemData.HOVERBOARD.item_id)}
                world.progressive_convert[RAC1ITEM.ZOOMERATOR] = {
                    RAC1ITEM.PROGRESSIVE_HOVERBOARD:
                        1 + world.orders[RAC1ORDER.HOVERBOARD].index(RAC1ItemData.ZOOMERATOR.item_id)}
            case _:
                pass
    if world.options.shuffle_extra_items.value == ShuffleExtraItems.option_vanilla:
        world.progressive_convert[RAC1ITEM.RARITANIUM] = {RAC1ITEM.RARITANIUM: 1, RAC1ITEM.PROGRESSIVE_TRADE: 1}
        world.progressive_convert[RAC1ITEM.PERSUADER] = {RAC1ITEM.PERSUADER: 1, RAC1ITEM.PROGRESSIVE_TRADE: 2}
    else:
        match world.options.progressive_raritanium.value:
            case RaritaniumProgression.option_progressive:
                world.progressive_convert[RAC1ITEM.RARITANIUM] = {RAC1ITEM.PROGRESSIVE_TRADE: 1}
                world.progressive_convert[RAC1ITEM.PERSUADER] = {RAC1ITEM.PROGRESSIVE_TRADE: 2}
            case RaritaniumProgression.option_progressive_reversed:
                world.orders[RAC1ORDER.TRADE].reverse()
                world.progressive_convert[RAC1ITEM.RARITANIUM] = {RAC1ITEM.PROGRESSIVE_TRADE: 2}
                world.progressive_convert[RAC1ITEM.PERSUADER] = {RAC1ITEM.PROGRESSIVE_TRADE: 1}
            case RaritaniumProgression.option_progressive_random:
                world.random.shuffle(world.orders[RAC1ORDER.TRADE])
                world.progressive_convert[RAC1ITEM.RARITANIUM] = {
                    RAC1ITEM.PROGRESSIVE_TRADE:
                        1 + world.orders[RAC1ORDER.TRADE].index(RAC1ItemData.RARITANIUM.item_id)}
                world.progressive_convert[RAC1ITEM.PERSUADER] = {
                    RAC1ITEM.PROGRESSIVE_TRADE:
                        1 + world.orders[RAC1ORDER.TRADE].index(RAC1ItemData.PERSUADER.item_id)}
            case _:
                pass

    match world.options.progressive_nanotech.value:
        case NanotechProgression.option_progressive:
            world.progressive_convert[RAC1ITEM.PREMIUM_NANOTECH] = {RAC1ITEM.PROGRESSIVE_NANOTECH: 1}
            world.progressive_convert[RAC1ITEM.ULTRA_NANOTECH] = {RAC1ITEM.PROGRESSIVE_NANOTECH: 2}
        case NanotechProgression.option_progressive_reversed:
            world.orders[RAC1ORDER.NANOTECH].reverse()
            world.progressive_convert[RAC1ITEM.PREMIUM_NANOTECH] = {RAC1ITEM.PROGRESSIVE_NANOTECH: 2}
            world.progressive_convert[RAC1ITEM.ULTRA_NANOTECH] = {RAC1ITEM.PROGRESSIVE_NANOTECH: 1}
        case NanotechProgression.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.NANOTECH])
            world.progressive_convert[RAC1ITEM.PREMIUM_NANOTECH] = {
                RAC1ITEM.PROGRESSIVE_NANOTECH:
                    1 + world.orders[RAC1ORDER.NANOTECH].index(RAC1ItemData.PREMIUM_NANOTECH.item_id)}
            world.progressive_convert[RAC1ITEM.ULTRA_NANOTECH] = {
                RAC1ITEM.PROGRESSIVE_NANOTECH:
                    1 + world.orders[RAC1ORDER.NANOTECH].index(RAC1ItemData.ULTRA_NANOTECH.item_id)}
        case _:
            pass
    return


def get_pool(_options) -> Sequence[ItemData]:
    pool = []
    for item in ITEM_POOL:
        pool += [item]
    if _options.progressive_weapons.value > GoldWeaponProgression.option_normal:
        for item in PROGRESSIVE_WEAPONS:
            pool += [item, item]
    else:
        for item in NON_PROGRESSIVE_WEAPONS:
            pool += [item]
        for item in GOLD_WEAPONS:
            pool += [item]
    if _options.progressive_packs.value > PackProgression.option_vanilla:
        for item in PROGRESSIVE_PACKS:
            pool += [item]
    else:
        for item in PACKS:
            pool += [item]
    if _options.progressive_helmets.value > HelmetProgression.option_vanilla:
        for item in PROGRESSIVE_HELMETS:
            pool += [item]
    else:
        for item in HELMETS:
            pool += [item]
    if _options.progressive_boots.value > BootsProgression.option_vanilla:
        for item in PROGRESSIVE_BOOTS:
            pool += [item]
    else:
        for item in BOOTS:
            pool += [item]
    if _options.progressive_hoverboard.value > HoverboardProgression.option_vanilla:
        for item in PROGRESSIVE_HOVERBOARDS:
            pool += [item]
    else:
        for item in NON_PROGRESSIVE_HOVERBOARDS:
            pool += [item]
    if _options.progressive_raritanium.value > RaritaniumProgression.option_vanilla:
        for item in PROGRESSIVE_TRADES:
            pool += [item]
    else:
        for item in NON_PROGRESSIVE_TRADES:
            pool += [item]
    if _options.progressive_nanotech.value > NanotechProgression.option_vanilla:
        for item in PROGRESSIVE_NANOTECHS:
            pool += [item]
    else:
        for item in NON_PROGRESSIVE_NANOTECHS:
            pool += [item]
    lookup: dict[int, tuple[ItemData, int]] = {
        1: (RAC1ItemData.GOLD_BOLT_1, 40),
        2: (RAC1ItemData.GOLD_BOLT_2, 30),
        3: (RAC1ItemData.GOLD_BOLT_3, 20),
        4: (RAC1ItemData.GOLD_BOLT_4, 15),
        5: (RAC1ItemData.GOLD_BOLT_5, 12),
        6: (RAC1ItemData.GOLD_BOLT_6, 10),
        7: (RAC1ItemData.GOLD_BOLT_7, 9),
        8: (RAC1ItemData.GOLD_BOLT_8, 8),
        9: (RAC1ItemData.GOLD_BOLT_9, 7),
        10: (RAC1ItemData.GOLD_BOLT_10, 6),
        11: (RAC1ItemData.GOLD_BOLT_11, 5),
        12: (RAC1ItemData.GOLD_BOLT_12, 5),
        13: (RAC1ItemData.GOLD_BOLT_13, 5),
        14: (RAC1ItemData.GOLD_BOLT_14, 4),
        15: (RAC1ItemData.GOLD_BOLT_15, 4),
        16: (RAC1ItemData.GOLD_BOLT_16, 4),
        17: (RAC1ItemData.GOLD_BOLT_17, 4),
        18: (RAC1ItemData.GOLD_BOLT_18, 4),
        19: (RAC1ItemData.GOLD_BOLT_19, 4),
        20: (RAC1ItemData.GOLD_BOLT_20, 3),
        21: (RAC1ItemData.GOLD_BOLT_21, 3),
        22: (RAC1ItemData.GOLD_BOLT_22, 3),
        23: (RAC1ItemData.GOLD_BOLT_23, 3),
        24: (RAC1ItemData.GOLD_BOLT_24, 3),
        25: (RAC1ItemData.GOLD_BOLT_25, 3),
        26: (RAC1ItemData.GOLD_BOLT_26, 3),
        27: (RAC1ItemData.GOLD_BOLT_27, 3),
        28: (RAC1ItemData.GOLD_BOLT_28, 3),
        29: (RAC1ItemData.GOLD_BOLT_29, 3),
        30: (RAC1ItemData.GOLD_BOLT_30, 2),
        31: (RAC1ItemData.GOLD_BOLT_31, 2),
        32: (RAC1ItemData.GOLD_BOLT_32, 2),
        33: (RAC1ItemData.GOLD_BOLT_33, 2),
        34: (RAC1ItemData.GOLD_BOLT_34, 2),
        35: (RAC1ItemData.GOLD_BOLT_35, 2),
        36: (RAC1ItemData.GOLD_BOLT_36, 2),
        37: (RAC1ItemData.GOLD_BOLT_37, 2),
        38: (RAC1ItemData.GOLD_BOLT_38, 2),
        39: (RAC1ItemData.GOLD_BOLT_39, 2),
        40: (RAC1ItemData.GOLD_BOLT_40, 1),
    }
    for _ in range(lookup[_options.pack_size_gold_bolts.value][1]):
        pool += [lookup[_options.pack_size_gold_bolts.value][0]]
    return pool


def get_starting_planets(_options) -> Sequence[ItemData]:
    planets: Sequence[ItemData] = []
    for item in STARTING_PLANETS:
        planets += [item]
    if _options.shuffle_infobots.value >= ShuffleInfobots.option_unrestricted:
        planets += [RAC1ItemData.ARIDIA]
        if _options.shuffle_helmets.value >= ShuffleInfobots.option_unrestricted:
            planets += [RAC1ItemData.GASPAR]
        if _options.shuffle_gold_bolts.value:
            planets += [RAC1ItemData.HOVEN]
    return planets


def from_id(item_id: int) -> ItemData:
    matching = [item for item in ALL_ITEMS if item.item_id == item_id]
    if len(matching) == 0:
        raise ValueError(f"No item data for item id '{item_id}'")
    assert len(matching) < 2, f"{len(matching)} item data found with id '{item_id}'. Items are: {matching}"
    return matching[0]


def from_name(item_name: str) -> ItemData:
    matching = [item for item in ALL_ITEMS if item.name == item_name]
    if len(matching) == 0:
        raise ValueError(f"No item data for '{item_name}'")
    # if item_name != GOLD_BOLT :
    #     assert len(matching) < 2, f"Multiple item data with name '{item_name}'. Please report."
    return matching[0]


def get_item_groups() -> dict[str, set[str]]:
    groups: dict[str, set[str]] = {
        RAC1POOL.WEAPONS: {w.name for w in ALL_WEAPONS},
        RAC1POOL.GADGETS: {g.name for g in GADGETS},
        RAC1POOL.PACKS: {p.name for p in ALL_PACKS},
        RAC1POOL.HELMETS: {h.name for h in ALL_HELMETS},
        RAC1POOL.BOOTS: {b.name for b in ALL_BOOTS},
        RAC1POOL.EXTRA_ITEMS: {e.name for e in ALL_EXTRA_ITEMS},
        RAC1POOL.GOLD_BOLTS: {c.name for c in GOLD_BOLTS},
        RAC1POOL.INFOBOTS: {i.name for i in PLANETS},
        RAC1POOL.SKILLPOINT: {s.name for s in SKILLPOINTS},
    }
    return groups


def check_progressive_item(_options: 'RacOptions', item: str) -> str:
    new_item = item
    match from_name(item).pool:
        case RAC1POOL.WEAPONS | RAC1POOL.GOLD_WEAPONS:
            if _options.progressive_weapons.value > GoldWeaponProgression.option_normal:
                match item:
                    case RAC1ITEM.SUCK_CANNON:
                        new_item = RAC1ITEM.PROGRESSIVE_SUCK
                    case RAC1ITEM.GOLD_SUCK_CANNON:
                        new_item = RAC1ITEM.PROGRESSIVE_SUCK
                    case RAC1ITEM.BOMB_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_BOMB
                    case RAC1ITEM.GOLD_BOMB_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_BOMB
                    case RAC1ITEM.DEVASTATOR:
                        new_item = RAC1ITEM.PROGRESSIVE_DEVASTATOR
                    case RAC1ITEM.GOLD_DEVASTATOR:
                        new_item = RAC1ITEM.PROGRESSIVE_DEVASTATOR
                    case RAC1ITEM.BLASTER:
                        new_item = RAC1ITEM.PROGRESSIVE_BLASTER
                    case RAC1ITEM.GOLD_BLASTER:
                        new_item = RAC1ITEM.PROGRESSIVE_BLASTER
                    case RAC1ITEM.PYROCITOR:
                        new_item = RAC1ITEM.PROGRESSIVE_PYROCITOR
                    case RAC1ITEM.GOLD_PYROCITOR:
                        new_item = RAC1ITEM.PROGRESSIVE_PYROCITOR
                    case RAC1ITEM.MINE_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_MINE
                    case RAC1ITEM.GOLD_MINE_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_MINE
                    case RAC1ITEM.TESLA_CLAW:
                        new_item = RAC1ITEM.PROGRESSIVE_TESLA
                    case RAC1ITEM.GOLD_TESLA_CLAW:
                        new_item = RAC1ITEM.PROGRESSIVE_TESLA
                    case RAC1ITEM.GLOVE_OF_DOOM:
                        new_item = RAC1ITEM.PROGRESSIVE_DOOM
                    case RAC1ITEM.GOLD_GLOVE_OF_DOOM:
                        new_item = RAC1ITEM.PROGRESSIVE_DOOM
                    case RAC1ITEM.MORPH_O_RAY:
                        new_item = RAC1ITEM.PROGRESSIVE_MORPH
                    case RAC1ITEM.GOLD_MORPH_O_RAY:
                        new_item = RAC1ITEM.PROGRESSIVE_MORPH
                    case RAC1ITEM.DECOY_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_DECOY
                    case RAC1ITEM.GOLD_DECOY_GLOVE:
                        new_item = RAC1ITEM.PROGRESSIVE_DECOY
        case RAC1POOL.PACKS:
            if _options.progressive_packs.value:
                new_item = RAC1ITEM.PROGRESSIVE_PACK
        case RAC1POOL.HELMETS:
            if _options.progressive_helmets.value:
                new_item = RAC1ITEM.PROGRESSIVE_HELMET
        case RAC1POOL.BOOTS:
            if _options.progressive_boots.value:
                new_item = RAC1ITEM.PROGRESSIVE_BOOT
        case RAC1POOL.EXTRA_ITEMS:
            match item:
                case RAC1ITEM.HOVERBOARD | RAC1ITEM.ZOOMERATOR:
                    if _options.progressive_hoverboard.value:
                        new_item = RAC1ITEM.PROGRESSIVE_HOVERBOARD
                case RAC1ITEM.RARITANIUM | RAC1ITEM.PERSUADER:
                    if _options.progressive_raritanium.value:
                        new_item = RAC1ITEM.PROGRESSIVE_TRADE
                case RAC1ITEM.PREMIUM_NANOTECH | RAC1ITEM.ULTRA_NANOTECH:
                    if _options.progressive_nanotech.value:
                        new_item = RAC1ITEM.PROGRESSIVE_NANOTECH
        case _:
            pass
    return new_item