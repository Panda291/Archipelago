"""This module defines data for items in RAC1"""

from dataclasses import dataclass

from BaseClasses import ItemClassification
from worlds.rac1.constants.items import RAC1ITEM
from worlds.rac1.constants.pools import RAC1POOL


@dataclass
class ItemData:
    item_id: int
    name: str
    pool: str
    classification: ItemClassification
    quantity: int = 1
    max_capacity: int = 1

    def __init__(self,
                 item_id: int,
                 name: str,
                 pool: str = RAC1POOL.FILLER,
                 classification: ItemClassification = ItemClassification.filler,
                 quantity: int = 1,
                 max_capacity: int = 1):
        self.item_id = item_id
        self.name = name
        self.pool = pool
        self.classification = classification
        self.quantity = quantity
        self.max_capacity = max_capacity


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
    PROGRESSIVE_SUCK = ItemData(82, RAC1ITEM.PROGRESSIVE_SUCK, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_BOMB = ItemData(83, RAC1ITEM.PROGRESSIVE_BOMB, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_DEVASTATOR = ItemData(84, RAC1ITEM.PROGRESSIVE_DEVASTATOR, RAC1POOL.WEAPONS,
                                      ItemClassification.progression)
    PROGRESSIVE_BLASTER = ItemData(85, RAC1ITEM.PROGRESSIVE_BLASTER, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_PYROCITOR = ItemData(86, RAC1ITEM.PROGRESSIVE_PYROCITOR, RAC1POOL.WEAPONS,
                                     ItemClassification.progression)
    PROGRESSIVE_MINE = ItemData(87, RAC1ITEM.PROGRESSIVE_MINE, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_TESLA = ItemData(88, RAC1ITEM.PROGRESSIVE_TESLA, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_DOOM = ItemData(89, RAC1ITEM.PROGRESSIVE_DOOM, RAC1POOL.WEAPONS, ItemClassification.useful)
    PROGRESSIVE_MORPH = ItemData(90, RAC1ITEM.PROGRESSIVE_MORPH, RAC1POOL.WEAPONS, ItemClassification.progression)
    PROGRESSIVE_DECOY = ItemData(91, RAC1ITEM.PROGRESSIVE_DECOY, RAC1POOL.WEAPONS, ItemClassification.useful)
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

    BOLT_PACK = ItemData(302, RAC1ITEM.BOLT_PACK_GENERIC)
    BOLT_PACK_0 = ItemData(400, RAC1ITEM.BOLT_PACK_0, quantity=0)
    BOLT_PACK_1 = ItemData(401, RAC1ITEM.BOLT_PACK_1)
    BOLT_PACK_10 = ItemData(402, RAC1ITEM.BOLT_PACK_10, quantity=10)
    BOLT_PACK_100 = ItemData(403, RAC1ITEM.BOLT_PACK_100, quantity=100)
    BOLT_PACK_250 = ItemData(404, RAC1ITEM.BOLT_PACK_250, quantity=250)
    BOLT_PACK_500 = ItemData(405, RAC1ITEM.BOLT_PACK_500, quantity=500)
    BOLT_PACK_750 = ItemData(406, RAC1ITEM.BOLT_PACK_750, quantity=750)
    BOLT_PACK_1000 = ItemData(407, RAC1ITEM.BOLT_PACK_1000, quantity=1000)
    BOLT_PACK_2000 = ItemData(408, RAC1ITEM.BOLT_PACK_2000, quantity=2000)
    BOLT_PACK_3000 = ItemData(409, RAC1ITEM.BOLT_PACK_3000, quantity=3000)
    BOLT_PACK_4000 = ItemData(410, RAC1ITEM.BOLT_PACK_4000, quantity=4000)
    BOLT_PACK_5000 = ItemData(411, RAC1ITEM.BOLT_PACK_5000, quantity=5000)
    BOLT_PACK_6000 = ItemData(412, RAC1ITEM.BOLT_PACK_6000, quantity=6000)
    BOLT_PACK_7000 = ItemData(413, RAC1ITEM.BOLT_PACK_7000, quantity=7000)
    BOLT_PACK_8000 = ItemData(414, RAC1ITEM.BOLT_PACK_8000, quantity=8000)
    BOLT_PACK_9000 = ItemData(415, RAC1ITEM.BOLT_PACK_9000, quantity=9000)
    BOLT_PACK_10000 = ItemData(416, RAC1ITEM.BOLT_PACK_10000, quantity=10000)
    BOLT_PACK_12500 = ItemData(417, RAC1ITEM.BOLT_PACK_12500, quantity=12500)
    BOLT_PACK_15000 = ItemData(418, RAC1ITEM.BOLT_PACK_15000, quantity=15000)
    BOLT_PACK_17500 = ItemData(419, RAC1ITEM.BOLT_PACK_17500, quantity=17500)
    BOLT_PACK_20000 = ItemData(420, RAC1ITEM.BOLT_PACK_20000, quantity=20000)
    BOLT_PACK_25000 = ItemData(421, RAC1ITEM.BOLT_PACK_25000, quantity=25000)
    BOLT_PACK_30000 = ItemData(422, RAC1ITEM.BOLT_PACK_30000, quantity=30000)
    BOLT_PACK_40000 = ItemData(423, RAC1ITEM.BOLT_PACK_40000, quantity=40000)
    BOLT_PACK_50000 = ItemData(424, RAC1ITEM.BOLT_PACK_50000, quantity=50000)
    BOLT_PACK_75000 = ItemData(425, RAC1ITEM.BOLT_PACK_75000, quantity=75000)
    BOLT_PACK_100000 = ItemData(426, RAC1ITEM.BOLT_PACK_100000, quantity=100000)


WEAPONS: list[ItemData] = [
    RAC1ItemData.TAUNTER,
    RAC1ItemData.VISIBOMB,
    RAC1ItemData.WALLOPER,
    RAC1ItemData.RYNO,
    RAC1ItemData.DRONE_DEVICE,
]

NON_PROGRESSIVE_WEAPONS: list[ItemData] = [
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

PROGRESSIVE_WEAPONS: list[ItemData] = [
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

GOLD_WEAPONS: list[ItemData] = [
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

PROGRESSIVE_GOLD_WEAPONS: list[ItemData] = [
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

GADGETS: list[ItemData] = [
    RAC1ItemData.HYDRODISPLACER,
    RAC1ItemData.TRESPASSER,
    RAC1ItemData.METAL_DETECTOR,
    RAC1ItemData.HOLOGUISE,
    RAC1ItemData.PDA,
    RAC1ItemData.SWINGSHOT,
]

PACKS: list[ItemData] = [
    RAC1ItemData.HELI_PACK,
    RAC1ItemData.THRUSTER_PACK,
    RAC1ItemData.HYDRO_PACK,
]

PROGRESSIVE_PACKS: list[ItemData] = [
    RAC1ItemData.PROGRESSIVE_PACK,
]

HELMETS: list[ItemData] = [
    RAC1ItemData.SONIC_SUMMONER,
    RAC1ItemData.O2_MASK,
    RAC1ItemData.PILOTS_HELMET,
]

BOOTS: list[ItemData] = [
    RAC1ItemData.MAGNEBOOTS,
    RAC1ItemData.GRINDBOOTS,
]

EXTRA_ITEMS: list[ItemData] = [
    RAC1ItemData.MAP_O_MATIC,
    RAC1ItemData.BOLT_GRABBER,
    RAC1ItemData.CODEBOT,
]

HOVERBOARDS: list[ItemData] = [
    RAC1ItemData.HOVERBOARD,
    RAC1ItemData.ZOOMERATOR,
]

TRADES: list[ItemData] = [
    RAC1ItemData.PERSUADER,
    RAC1ItemData.RARITANIUM,
]

NON_PROGRESSIVE_NANOTECHS: list[ItemData] = [
    RAC1ItemData.PREMIUM_NANOTECH,
    RAC1ItemData.ULTRA_NANOTECH,
]

PROGRESSIVE_NANOTECHS: list[ItemData] = [
    RAC1ItemData.PROGRESSIVE_NANOTECH,
]

GOLD_BOLTS: list[ItemData] = [
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

GOLD_BOLT_SIZE_TO_PACK: dict[int, str] = {
    RAC1ItemData.GOLD_BOLT.quantity: RAC1ITEM.GOLD_BOLT,
    RAC1ItemData.GOLD_BOLT_1.quantity: RAC1ITEM.GOLD_BOLT_1,
    RAC1ItemData.GOLD_BOLT_2.quantity: RAC1ITEM.GOLD_BOLT_2,
    RAC1ItemData.GOLD_BOLT_3.quantity: RAC1ITEM.GOLD_BOLT_3,
    RAC1ItemData.GOLD_BOLT_4.quantity: RAC1ITEM.GOLD_BOLT_4,
    RAC1ItemData.GOLD_BOLT_5.quantity: RAC1ITEM.GOLD_BOLT_5,
    RAC1ItemData.GOLD_BOLT_6.quantity: RAC1ITEM.GOLD_BOLT_6,
    RAC1ItemData.GOLD_BOLT_7.quantity: RAC1ITEM.GOLD_BOLT_7,
    RAC1ItemData.GOLD_BOLT_8.quantity: RAC1ITEM.GOLD_BOLT_8,
    RAC1ItemData.GOLD_BOLT_9.quantity: RAC1ITEM.GOLD_BOLT_9,
    RAC1ItemData.GOLD_BOLT_10.quantity: RAC1ITEM.GOLD_BOLT_10,
    RAC1ItemData.GOLD_BOLT_11.quantity: RAC1ITEM.GOLD_BOLT_11,
    RAC1ItemData.GOLD_BOLT_12.quantity: RAC1ITEM.GOLD_BOLT_12,
    RAC1ItemData.GOLD_BOLT_13.quantity: RAC1ITEM.GOLD_BOLT_13,
    RAC1ItemData.GOLD_BOLT_14.quantity: RAC1ITEM.GOLD_BOLT_14,
    RAC1ItemData.GOLD_BOLT_15.quantity: RAC1ITEM.GOLD_BOLT_15,
    RAC1ItemData.GOLD_BOLT_16.quantity: RAC1ITEM.GOLD_BOLT_16,
    RAC1ItemData.GOLD_BOLT_17.quantity: RAC1ITEM.GOLD_BOLT_17,
    RAC1ItemData.GOLD_BOLT_18.quantity: RAC1ITEM.GOLD_BOLT_18,
    RAC1ItemData.GOLD_BOLT_19.quantity: RAC1ITEM.GOLD_BOLT_19,
    RAC1ItemData.GOLD_BOLT_20.quantity: RAC1ITEM.GOLD_BOLT_20,
    RAC1ItemData.GOLD_BOLT_21.quantity: RAC1ITEM.GOLD_BOLT_21,
    RAC1ItemData.GOLD_BOLT_22.quantity: RAC1ITEM.GOLD_BOLT_22,
    RAC1ItemData.GOLD_BOLT_23.quantity: RAC1ITEM.GOLD_BOLT_23,
    RAC1ItemData.GOLD_BOLT_24.quantity: RAC1ITEM.GOLD_BOLT_24,
    RAC1ItemData.GOLD_BOLT_25.quantity: RAC1ITEM.GOLD_BOLT_25,
    RAC1ItemData.GOLD_BOLT_26.quantity: RAC1ITEM.GOLD_BOLT_26,
    RAC1ItemData.GOLD_BOLT_27.quantity: RAC1ITEM.GOLD_BOLT_27,
    RAC1ItemData.GOLD_BOLT_28.quantity: RAC1ITEM.GOLD_BOLT_28,
    RAC1ItemData.GOLD_BOLT_29.quantity: RAC1ITEM.GOLD_BOLT_29,
    RAC1ItemData.GOLD_BOLT_30.quantity: RAC1ITEM.GOLD_BOLT_30,
    RAC1ItemData.GOLD_BOLT_31.quantity: RAC1ITEM.GOLD_BOLT_31,
    RAC1ItemData.GOLD_BOLT_32.quantity: RAC1ITEM.GOLD_BOLT_32,
    RAC1ItemData.GOLD_BOLT_33.quantity: RAC1ITEM.GOLD_BOLT_33,
    RAC1ItemData.GOLD_BOLT_34.quantity: RAC1ITEM.GOLD_BOLT_34,
    RAC1ItemData.GOLD_BOLT_35.quantity: RAC1ITEM.GOLD_BOLT_35,
    RAC1ItemData.GOLD_BOLT_36.quantity: RAC1ITEM.GOLD_BOLT_36,
    RAC1ItemData.GOLD_BOLT_37.quantity: RAC1ITEM.GOLD_BOLT_37,
    RAC1ItemData.GOLD_BOLT_38.quantity: RAC1ITEM.GOLD_BOLT_38,
    RAC1ItemData.GOLD_BOLT_39.quantity: RAC1ITEM.GOLD_BOLT_39,
    RAC1ItemData.GOLD_BOLT_40.quantity: RAC1ITEM.GOLD_BOLT_40,
}

BOLT_SIZE_TO_PACK: dict[int, str] = {
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

BOLT_PACKS: list[ItemData] = [
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

PLANETS: list[ItemData] = [
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

STARTING_PLANETS: list[ItemData] = [
    RAC1ItemData.NOVALIS,
    RAC1ItemData.KERWAN,
    RAC1ItemData.BLARG,
    RAC1ItemData.BATALIA,
    RAC1ItemData.ORXON,
]

# SKILLPOINTS: list[ItemData] = [
#     RAC1ItemData.TAKE_AIM,
#     RAC1ItemData.SWING_IT,
#     RAC1ItemData.TRANSPORTED,
#     RAC1ItemData.STRIKE_A_POSE,
#     RAC1ItemData.BLIMPY,
#     RAC1ItemData.QWARKTASTIC,
#     RAC1ItemData.ANY_TEN,
#     RAC1ItemData.TRICKY,
#     RAC1ItemData.CLUCK_CLUCK,
#     RAC1ItemData.SPEEDY,
#     RAC1ItemData.GIRL_TROUBLE,
#     RAC1ItemData.JUMPER,
#     RAC1ItemData.ACCURACY_COUNTS,
#     RAC1ItemData.EAT_LEAD,
#     RAC1ItemData.DESTROYED,
#     RAC1ItemData.GUNNER,
#     RAC1ItemData.SNIPER,
#     RAC1ItemData.HEY_OVER_HERE,
#     RAC1ItemData.ALIEN_INVASION,
#     RAC1ItemData.BURIED_TREASURE,
#     RAC1ItemData.PEST_CONTROL,
#     RAC1ItemData.WHIRLYBIRDS,
#     RAC1ItemData.SITTING_DUCKS,
#     RAC1ItemData.SHATTERED_GLASS,
#     RAC1ItemData.BLAST_EM,
#     RAC1ItemData.HEAVY_TRAFFIC,
#     RAC1ItemData.MAGICIAN,
#     RAC1ItemData.SNEAKY,
#     RAC1ItemData.CAREFUL_CRUISE,
#     RAC1ItemData.GOING_COMMANDO,
# ]

ALL_ITEMS: list[ItemData] = [*WEAPONS, *NON_PROGRESSIVE_WEAPONS, *PROGRESSIVE_WEAPONS, *GOLD_WEAPONS, *GADGETS,
                             *PACKS, *PROGRESSIVE_PACKS, *HELMETS, *BOOTS, *EXTRA_ITEMS, *HOVERBOARDS, *TRADES,
                             *NON_PROGRESSIVE_NANOTECHS, *PROGRESSIVE_NANOTECHS, *GOLD_BOLTS, *PLANETS, *BOLT_PACKS]

ITEM_POOL: list[ItemData] = [*PLANETS, *WEAPONS, *GADGETS, *EXTRA_ITEMS, *HELMETS, *BOOTS, *TRADES, *HOVERBOARDS]

STARTING_WEAPONS: list[ItemData] = [*WEAPONS, *NON_PROGRESSIVE_WEAPONS]
ALL_WEAPONS: list[ItemData] = [*WEAPONS, *NON_PROGRESSIVE_WEAPONS, *PROGRESSIVE_WEAPONS, *GOLD_WEAPONS]
ALL_PACKS: list[ItemData] = [*PACKS, *PROGRESSIVE_PACKS]
ALL_HELMETS: list[ItemData] = [*HELMETS]
ALL_BOOTS: list[ItemData] = [*BOOTS]
ALL_EXTRA_ITEMS: list[ItemData] = [*EXTRA_ITEMS, *HOVERBOARDS,
                                   *TRADES, *NON_PROGRESSIVE_NANOTECHS,
                                   *PROGRESSIVE_NANOTECHS]
ALL_HOVERBOARD: list[ItemData] = [*HOVERBOARDS]
ALL_TRADE: list[ItemData] = [*TRADES]
ALL_NANOTECH: list[ItemData] = [*NON_PROGRESSIVE_NANOTECHS, *PROGRESSIVE_NANOTECHS]
ALL_STARTING: list[ItemData] = [*STARTING_WEAPONS, *GADGETS]

SUCK_GROUP: list[ItemData] = [RAC1ItemData.SUCK_CANNON, RAC1ItemData.GOLD_SUCK_CANNON, RAC1ItemData.PROGRESSIVE_SUCK]
BOMB_GROUP: list[ItemData] = [RAC1ItemData.BOMB_GLOVE, RAC1ItemData.GOLD_BOMB_GLOVE, RAC1ItemData.PROGRESSIVE_BOMB]
DEVASTATOR_GROUP: list[ItemData] = [RAC1ItemData.DEVASTATOR, RAC1ItemData.GOLD_DEVASTATOR,
                                    RAC1ItemData.PROGRESSIVE_DEVASTATOR]
BLASTER_GROUP: list[ItemData] = [RAC1ItemData.BLASTER, RAC1ItemData.GOLD_BLASTER, RAC1ItemData.PROGRESSIVE_BLASTER]
PYROCITOR_GROUP: list[ItemData] = [RAC1ItemData.PYROCITOR, RAC1ItemData.GOLD_PYROCITOR,
                                   RAC1ItemData.PROGRESSIVE_PYROCITOR]
MINE_GROUP: list[ItemData] = [RAC1ItemData.MINE_GLOVE, RAC1ItemData.GOLD_MINE_GLOVE, RAC1ItemData.PROGRESSIVE_MINE]
TESLA_GROUP: list[ItemData] = [RAC1ItemData.TESLA_CLAW, RAC1ItemData.GOLD_TESLA_CLAW, RAC1ItemData.PROGRESSIVE_TESLA]
DOOM_GROUP: list[ItemData] = [RAC1ItemData.GLOVE_OF_DOOM, RAC1ItemData.GOLD_GLOVE_OF_DOOM,
                              RAC1ItemData.PROGRESSIVE_DOOM]
MORPH_GROUP: list[ItemData] = [RAC1ItemData.MORPH_O_RAY, RAC1ItemData.GOLD_MORPH_O_RAY, RAC1ItemData.PROGRESSIVE_MORPH]
DECOY_GROUP: list[ItemData] = [RAC1ItemData.DECOY_GLOVE, RAC1ItemData.GOLD_DECOY_GLOVE, RAC1ItemData.PROGRESSIVE_DECOY]
