import dataclasses
import logging

from typing_extensions import override

from BaseClasses import CollectionState
from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, Has, True_, HasAny, HasAll
from worlds.rac1.constants.items import RAC1ITEM
from worlds.rac1.constants.options import RAC1OPTION
from worlds.rac1.data.progressive_order import orders
from worlds.rac1.options import VendorOptions, GoldBoltPackSize, PackProgression, HelmetProgression, BootsProgression, \
    RaritaniumProgression, HoverboardProgression, GoldWeaponProgression

rac_logger = logging.getLogger(RAC1OPTION.GAME_TITLE_FULL)
rac_logger.setLevel(logging.DEBUG)

### start progressive filters ###
progressive_pack_vanilla = [OptionFilter(PackProgression, PackProgression.option_vanilla)]
progressive_pack_progressive = [OptionFilter(PackProgression, PackProgression.option_progressive)]
progressive_pack_reversed = [OptionFilter(PackProgression, PackProgression.option_progressive_reversed)]

progressive_helmet_vanilla = [OptionFilter(HelmetProgression, HelmetProgression.option_vanilla)]
progressive_helmet_progressive = [OptionFilter(HelmetProgression, HelmetProgression.option_progressive)]
progressive_helmet_reversed = [OptionFilter(HelmetProgression, HelmetProgression.option_progressive_reversed)]

progressive_boots_vanilla = [OptionFilter(BootsProgression, BootsProgression.option_vanilla)]
progressive_boots_progressive = [OptionFilter(BootsProgression, BootsProgression.option_progressive)]
progressive_boots_reversed = [OptionFilter(BootsProgression, BootsProgression.option_progressive_reversed)]

progressive_trade_vanilla = [OptionFilter(RaritaniumProgression, RaritaniumProgression.option_vanilla)]
progressive_trade_progressive = [OptionFilter(RaritaniumProgression, RaritaniumProgression.option_progressive)]
progressive_trade_reversed = [OptionFilter(RaritaniumProgression, RaritaniumProgression.option_progressive_reversed)]

progressive_hoverboard_vanilla = [OptionFilter(HoverboardProgression, HoverboardProgression.option_vanilla)]
progressive_hoverboard_progressive = [OptionFilter(HoverboardProgression, HoverboardProgression.option_progressive)]
progressive_hoverboard_reversed = [OptionFilter(HoverboardProgression, HoverboardProgression.option_progressive_reversed)]

progressive_weapons_vanilla = [OptionFilter(GoldWeaponProgression, GoldWeaponProgression.option_vanilla)]
progressive_weapons_normal = [OptionFilter(GoldWeaponProgression, GoldWeaponProgression.option_normal)]
progressive_weapons_progressive = [OptionFilter(GoldWeaponProgression, GoldWeaponProgression.option_progressive)]
progressive_weapons_reversed = [OptionFilter(GoldWeaponProgression, GoldWeaponProgression.option_progressive_reversed)]
### end progressive filters ###

### start progressive rules ###
has_progressive_helipack = (Has(RAC1ITEM.HELI_PACK, options=progressive_pack_vanilla)
                            | Has(RAC1ITEM.PROGRESSIVE_PACK, count=1, options=progressive_pack_progressive)
                            | Has(RAC1ITEM.PROGRESSIVE_PACK, count=3, options=progressive_pack_reversed))
has_progressive_thruster_pack = (Has(RAC1ITEM.THRUSTER_PACK, options=progressive_pack_vanilla)
                            | Has(RAC1ITEM.PROGRESSIVE_PACK, count=2, options=progressive_pack_progressive)
                            | Has(RAC1ITEM.PROGRESSIVE_PACK, count=2, options=progressive_pack_reversed))
has_progressive_hydro_pack = (Has(RAC1ITEM.THRUSTER_PACK, options=progressive_pack_vanilla)
                            | Has(RAC1ITEM.PROGRESSIVE_PACK, count=3, options=progressive_pack_progressive)
                            | Has(RAC1ITEM.PROGRESSIVE_PACK, count=1, options=progressive_pack_reversed))

has_o2_mask = (Has(RAC1ITEM.O2_MASK, options=progressive_helmet_vanilla)
            | Has(RAC1ITEM.PROGRESSIVE_HELMET, count=1, options=progressive_helmet_progressive)
            | Has(RAC1ITEM.PROGRESSIVE_HELMET, count=3, options=progressive_helmet_reversed))
has_sonic = (Has(RAC1ITEM.SONIC_SUMMONER, options=progressive_helmet_vanilla)
            | Has(RAC1ITEM.PROGRESSIVE_HELMET, count=2, options=progressive_helmet_progressive)
            | Has(RAC1ITEM.PROGRESSIVE_HELMET, count=2, options=progressive_helmet_reversed))
has_pilots_helmet = (Has(RAC1ITEM.PILOTS_HELMET, options=progressive_helmet_vanilla)
            | Has(RAC1ITEM.PROGRESSIVE_HELMET, count=3, options=progressive_helmet_progressive)
            | Has(RAC1ITEM.PROGRESSIVE_HELMET, count=1, options=progressive_helmet_reversed))

has_grindboots = (Has(RAC1ITEM.GRINDBOOTS, options=progressive_boots_vanilla)
            | Has(RAC1ITEM.PROGRESSIVE_BOOT, count=1, options=progressive_boots_progressive)
            | Has(RAC1ITEM.PROGRESSIVE_BOOT, count=2, options=progressive_boots_reversed))
has_magneboots = (Has(RAC1ITEM.MAGNEBOOTS, options=progressive_boots_vanilla)
            | Has(RAC1ITEM.PROGRESSIVE_BOOT, count=2, options=progressive_boots_progressive)
            | Has(RAC1ITEM.PROGRESSIVE_BOOT, count=1, options=progressive_boots_reversed))

has_raritanium = (Has(RAC1ITEM.RARITANIUM, options=progressive_trade_vanilla)
            | Has(RAC1ITEM.PROGRESSIVE_TRADE, count=1, options=progressive_trade_progressive)
            | Has(RAC1ITEM.PROGRESSIVE_TRADE, count=2, options=progressive_trade_reversed))
has_persuader = (Has(RAC1ITEM.PERSUADER, options=progressive_trade_vanilla)
            | Has(RAC1ITEM.PROGRESSIVE_TRADE, count=2, options=progressive_trade_progressive)
            | Has(RAC1ITEM.PROGRESSIVE_TRADE, count=1, options=progressive_trade_reversed))

has_hoverboard = (Has(RAC1ITEM.HOVERBOARD, options=progressive_hoverboard_vanilla)
            | Has(RAC1ITEM.PROGRESSIVE_HOVERBOARD, count=1, options=progressive_hoverboard_progressive)
            | Has(RAC1ITEM.PROGRESSIVE_HOVERBOARD, count=2, options=progressive_hoverboard_reversed))
has_zoomerator = (Has(RAC1ITEM.ZOOMERATOR, options=progressive_hoverboard_vanilla)
            | Has(RAC1ITEM.PROGRESSIVE_HOVERBOARD, count=2, options=progressive_hoverboard_progressive)
            | Has(RAC1ITEM.PROGRESSIVE_HOVERBOARD, count=1, options=progressive_hoverboard_reversed))


has_morph = (Has(RAC1ITEM.MORPH_O_RAY, options=progressive_weapons_vanilla)
            |HasAny(RAC1ITEM.MORPH_O_RAY, RAC1ITEM.GOLD_MORPH_O_RAY, options=progressive_weapons_normal)
            |Has(RAC1ITEM.PROGRESSIVE_MORPH, count=1, options=progressive_weapons_progressive)
            |Has(RAC1ITEM.PROGRESSIVE_MORPH, count=1, options=progressive_weapons_reversed))

has_bomb_glove = (Has(RAC1ITEM.BOMB_GLOVE, options=progressive_weapons_vanilla)
            |HasAny(RAC1ITEM.BOMB_GLOVE, RAC1ITEM.GOLD_BOMB_GLOVE, options=progressive_weapons_normal)
            |Has(RAC1ITEM.PROGRESSIVE_BOMB, count=1, options=progressive_weapons_progressive)
            |Has(RAC1ITEM.PROGRESSIVE_BOMB, count=1, options=progressive_weapons_reversed))

has_mine_glove = (Has(RAC1ITEM.MINE_GLOVE, options=progressive_weapons_vanilla)
            |HasAny(RAC1ITEM.MINE_GLOVE, RAC1ITEM.GOLD_MINE_GLOVE, options=progressive_weapons_normal)
            |Has(RAC1ITEM.PROGRESSIVE_MINE, count=1, options=progressive_weapons_progressive)
            |Has(RAC1ITEM.PROGRESSIVE_MINE, count=1, options=progressive_weapons_reversed))

has_devastator = (Has(RAC1ITEM.DEVASTATOR, options=progressive_weapons_vanilla)
            |HasAny(RAC1ITEM.DEVASTATOR, RAC1ITEM.GOLD_DEVASTATOR, options=progressive_weapons_normal)
            |Has(RAC1ITEM.PROGRESSIVE_DEVASTATOR, count=1, options=progressive_weapons_progressive)
            |Has(RAC1ITEM.PROGRESSIVE_DEVASTATOR, count=1, options=progressive_weapons_reversed))

has_blaster = (Has(RAC1ITEM.BLASTER, options=progressive_weapons_vanilla)
            |HasAny(RAC1ITEM.BLASTER, RAC1ITEM.GOLD_BLASTER, options=progressive_weapons_normal)
            |Has(RAC1ITEM.PROGRESSIVE_BLASTER, count=1, options=progressive_weapons_progressive)
            |Has(RAC1ITEM.PROGRESSIVE_BLASTER, count=1, options=progressive_weapons_reversed))

has_pyro = (Has(RAC1ITEM.PYROCITOR, options=progressive_weapons_vanilla)
            |HasAny(RAC1ITEM.PYROCITOR, RAC1ITEM.GOLD_PYROCITOR, options=progressive_weapons_normal)
            |Has(RAC1ITEM.PROGRESSIVE_PYROCITOR, count=1, options=progressive_weapons_progressive)
            |Has(RAC1ITEM.PROGRESSIVE_PYROCITOR, count=1, options=progressive_weapons_reversed))

has_suck = (Has(RAC1ITEM.SUCK_CANNON, options=progressive_weapons_vanilla)
            |HasAny(RAC1ITEM.SUCK_CANNON, RAC1ITEM.GOLD_SUCK_CANNON, options=progressive_weapons_normal)
            |Has(RAC1ITEM.PROGRESSIVE_SUCK, count=1, options=progressive_weapons_progressive)
            |Has(RAC1ITEM.PROGRESSIVE_SUCK, count=1, options=progressive_weapons_reversed))

has_tesla = (Has(RAC1ITEM.TESLA_CLAW, options=progressive_weapons_vanilla)
            |HasAny(RAC1ITEM.TESLA_CLAW, RAC1ITEM.GOLD_TESLA_CLAW, options=progressive_weapons_normal)
            |Has(RAC1ITEM.PROGRESSIVE_TESLA, count=1, options=progressive_weapons_progressive)
            |Has(RAC1ITEM.PROGRESSIVE_TESLA, count=1, options=progressive_weapons_reversed))

### end progressive rules ###

can_improved_jump = has_progressive_helipack | has_progressive_thruster_pack
can_heli_high_jump = has_progressive_helipack
can_glide = has_progressive_helipack
can_ground_pound =has_progressive_thruster_pack
has_hydro_pack = has_progressive_hydro_pack
has_explosive_weapon = (HasAny(RAC1ITEM.VISIBOMB, RAC1ITEM.RYNO) |
                        has_bomb_glove |
                        has_mine_glove |
                        has_devastator)
has_long_range_weapon = Has(RAC1ITEM.VISIBOMB) | has_devastator
has_medium_range_weapon = (HasAny(RAC1ITEM.VISIBOMB, RAC1ITEM.RYNO) |
                        has_devastator |
                        has_blaster)
has_short_range_weapon = (HasAny(RAC1ITEM.VISIBOMB, RAC1ITEM.RYNO) |
                        has_pyro |
                        has_blaster |
                        has_suck |
                        has_devastator |
                        has_tesla)

early_metal_spots = HasAny(RAC1ITEM.NOVALIS,
        RAC1ITEM.KERWAN,
        RAC1ITEM.ARIDIA,
        RAC1ITEM.EUDORA,
        RAC1ITEM.BATALIA,
        RAC1ITEM.POKITARU,
        RAC1ITEM.HOVEN,
        RAC1ITEM.QUARTU)
rilgar_metal_spots = can_improved_jump & Has(RAC1ITEM.RILGAR)
blarg_metal_spots = Has(RAC1ITEM.BLARG) & (Has(RAC1ITEM.SWINGSHOT) | has_o2_mask & Has(RAC1ITEM.TRESPASSER))
umbris_metal_spots = can_glide & Has(RAC1ITEM.SWINGSHOT) & Has(RAC1ITEM.UMBRIS)
gaspar_metal_spots = Has(RAC1ITEM.GASPAR) & (can_improved_jump | Has(RAC1ITEM.SWINGSHOT))
orxon_metal_spots = has_o2_mask & Has(RAC1ITEM.ORXON)
gemlik_metal_spots = has_magneboots & can_improved_jump & has_long_range_weapon & HasAll(RAC1ITEM.SWINGSHOT, RAC1ITEM.TRESPASSER) & Has(RAC1ITEM.GEMLIK)
oltanis_metal_spots = Has(RAC1ITEM.OLTANIS) & (has_magneboots | Has(RAC1ITEM.SWINGSHOT))
kalebo_metal_spots = (has_medium_range_weapon | has_bomb_glove | HasAny(RAC1ITEM.VISIBOMB, RAC1ITEM.RYNO)) & Has(RAC1ITEM.KALEBO) & (can_improved_jump | Has(RAC1ITEM.SWINGSHOT))
fleet_metal_spots = Has(RAC1ITEM.FLEET) & ((has_o2_mask & has_hydro_pack) | Has(RAC1ITEM.HOLOGUISE))
veldin_metal_spots = (has_magneboots & can_ground_pound & HasAll(RAC1ITEM.TRESPASSER, RAC1ITEM.HYDRODISPLACER)) & Has(RAC1ITEM.VELDIN) & Has(RAC1ITEM.SWINGSHOT)
can_farm_bolts = (Has(RAC1ITEM.METAL_DETECTOR) &
                     (early_metal_spots
                    | blarg_metal_spots
                    | rilgar_metal_spots
                    | umbris_metal_spots
                    | gaspar_metal_spots
                    | orxon_metal_spots
                    | gemlik_metal_spots
                    | oltanis_metal_spots
                    | kalebo_metal_spots
                    | fleet_metal_spots
                    | veldin_metal_spots)
                 )

can_buy = (True_(options=[OptionFilter(VendorOptions, VendorOptions.option_no_bolt_logic)])
         | Has(RAC1ITEM.METAL_DETECTOR, options=[OptionFilter(VendorOptions, VendorOptions.option_all_bolts)]) # | has_bolts
         | Has(RAC1ITEM.METAL_DETECTOR))

has_7500_bolts = can_farm_bolts # | has_bolts...
has_10k_bolts = can_farm_bolts # | has_bolts...
has_15k_bolts = can_farm_bolts # | has_bolts...
has_20k_bolts = can_farm_bolts # | has_bolts...
has_30k_bolts = can_farm_bolts # | has_bolts...
has_40k_bolts = can_farm_bolts # | has_bolts...
has_60k_bolts = can_farm_bolts # | has_bolts...
has_150k_bolts = can_farm_bolts # | has_bolts...

# def has_bolts(state: CollectionState, world: 'RacWorld', count: int) -> bool:
#     # 500,
#     # 1000 * 3,
#     # 2000 * 5,
#     # 2500 * 3,
#     # 4000 * 2,
#     # 7500 * 5,
#     # 10000 * 5,
#     # 15000,
#     # 20000 * 3
#     # 30000 * 2,
#     # 40000,
#     # 60000 * 2,
#     # 150000
#     lookup: dict[int, int] = {
#         500: 500,
#         1000: 1500,
#         2000: 5500,
#         2500: 16000,
#         4000: 25000,
#         7500: 36500,
#         10000: 75000,
#         15000: 130000,
#         20000: 150000,
#         30000: 220000,
#         40000: 290000,
#         60000: 350000,
#         150000: 560000,
#     }
#
#     total = 0
#     for item in [
#         RAC1ItemData.BOLT_PACK_1,
#         RAC1ItemData.BOLT_PACK_10,
#         RAC1ItemData.BOLT_PACK_100,
#         RAC1ItemData.BOLT_PACK_250,
#         RAC1ItemData.BOLT_PACK_500,
#         RAC1ItemData.BOLT_PACK_750,
#         RAC1ItemData.BOLT_PACK_1000,
#         RAC1ItemData.BOLT_PACK_2000,
#         RAC1ItemData.BOLT_PACK_3000,
#         RAC1ItemData.BOLT_PACK_4000,
#         RAC1ItemData.BOLT_PACK_5000,
#         RAC1ItemData.BOLT_PACK_6000,
#         RAC1ItemData.BOLT_PACK_7000,
#         RAC1ItemData.BOLT_PACK_8000,
#         RAC1ItemData.BOLT_PACK_9000,
#         RAC1ItemData.BOLT_PACK_10000,
#         RAC1ItemData.BOLT_PACK_12500,
#         RAC1ItemData.BOLT_PACK_15000,
#         RAC1ItemData.BOLT_PACK_17500,
#         RAC1ItemData.BOLT_PACK_20000,
#         RAC1ItemData.BOLT_PACK_25000,
#         RAC1ItemData.BOLT_PACK_30000,
#         RAC1ItemData.BOLT_PACK_40000,
#         RAC1ItemData.BOLT_PACK_50000,
#         RAC1ItemData.BOLT_PACK_75000,
#         RAC1ItemData.BOLT_PACK_100000
#     ]:
#         if state.prog_items[world.player].get(item.item_id) is not None:
#             total += (state.prog_items[world.player].get(item.item_id)
#                       * item.quantity * world.options.pack_size_bolts.value)
#         for planet, bolts in {
#             RAC1ITEM.NOVALIS: 4800,
#             RAC1ITEM.KERWAN: 2250,
#             RAC1ITEM.EUDORA: 4500,
#             RAC1ITEM.BLARG: 2250,
#             RAC1ITEM.RILGAR: 325,
#             RAC1ITEM.BATALIA: 3000,
#             RAC1ITEM.GASPAR: 7850,
#             RAC1ITEM.ORXON: 4750,
#             RAC1ITEM.POKITARU: 2430,
#             RAC1ITEM.HOVEN: 2600,
#             RAC1ITEM.OLTANIS: 4150,
#         }.items():
#             total += state.has(planet, world.player) * bolts * world.options.pack_size_bolts.value
#     return total >= lookup[count]

has_40_gold_bolts = (Has(RAC1ITEM.GOLD_BOLT_1, count=40, options=[OptionFilter(GoldBoltPackSize, 1)]) |
                     Has(RAC1ITEM.GOLD_BOLT_2, count=20, options=[OptionFilter(GoldBoltPackSize, 2)]) |
                     Has(RAC1ITEM.GOLD_BOLT_3, count=14, options=[OptionFilter(GoldBoltPackSize, 3)]) |
                     Has(RAC1ITEM.GOLD_BOLT_4, count=10, options=[OptionFilter(GoldBoltPackSize, 4)]) |
                     Has(RAC1ITEM.GOLD_BOLT_5, count=8, options=[OptionFilter(GoldBoltPackSize, 5)]) |
                     Has(RAC1ITEM.GOLD_BOLT_6, count=7, options=[OptionFilter(GoldBoltPackSize, 6)]) |
                     Has(RAC1ITEM.GOLD_BOLT_7, count=6, options=[OptionFilter(GoldBoltPackSize, 7)]) |
                     Has(RAC1ITEM.GOLD_BOLT_8, count=5, options=[OptionFilter(GoldBoltPackSize, 8)]) |
                     Has(RAC1ITEM.GOLD_BOLT_9, count=5, options=[OptionFilter(GoldBoltPackSize, 9)]) |
                     Has(RAC1ITEM.GOLD_BOLT_10, count=4, options=[OptionFilter(GoldBoltPackSize, 10)]) |
                     Has(RAC1ITEM.GOLD_BOLT_11, count=4, options=[OptionFilter(GoldBoltPackSize, 11)]) |
                     Has(RAC1ITEM.GOLD_BOLT_12, count=4, options=[OptionFilter(GoldBoltPackSize, 12)]) |
                     Has(RAC1ITEM.GOLD_BOLT_13, count=4, options=[OptionFilter(GoldBoltPackSize, 13)]) |
                     Has(RAC1ITEM.GOLD_BOLT_14, count=3, options=[OptionFilter(GoldBoltPackSize, 14)]) |
                     Has(RAC1ITEM.GOLD_BOLT_15, count=3, options=[OptionFilter(GoldBoltPackSize, 15)]) |
                     Has(RAC1ITEM.GOLD_BOLT_16, count=3, options=[OptionFilter(GoldBoltPackSize, 16)]) |
                     Has(RAC1ITEM.GOLD_BOLT_17, count=3, options=[OptionFilter(GoldBoltPackSize, 17)]) |
                     Has(RAC1ITEM.GOLD_BOLT_18, count=3, options=[OptionFilter(GoldBoltPackSize, 18)]) |
                     Has(RAC1ITEM.GOLD_BOLT_19, count=3, options=[OptionFilter(GoldBoltPackSize, 19)]) |
                     Has(RAC1ITEM.GOLD_BOLT_20, count=2, options=[OptionFilter(GoldBoltPackSize, 20)]) |
                     Has(RAC1ITEM.GOLD_BOLT_21, count=2, options=[OptionFilter(GoldBoltPackSize, 21)]) |
                     Has(RAC1ITEM.GOLD_BOLT_22, count=2, options=[OptionFilter(GoldBoltPackSize, 22)]) |
                     Has(RAC1ITEM.GOLD_BOLT_23, count=2, options=[OptionFilter(GoldBoltPackSize, 23)]) |
                     Has(RAC1ITEM.GOLD_BOLT_24, count=2, options=[OptionFilter(GoldBoltPackSize, 24)]) |
                     Has(RAC1ITEM.GOLD_BOLT_25, count=2, options=[OptionFilter(GoldBoltPackSize, 25)]) |
                     Has(RAC1ITEM.GOLD_BOLT_26, count=2, options=[OptionFilter(GoldBoltPackSize, 26)]) |
                     Has(RAC1ITEM.GOLD_BOLT_27, count=2, options=[OptionFilter(GoldBoltPackSize, 27)]) |
                     Has(RAC1ITEM.GOLD_BOLT_28, count=2, options=[OptionFilter(GoldBoltPackSize, 28)]) |
                     Has(RAC1ITEM.GOLD_BOLT_29, count=2, options=[OptionFilter(GoldBoltPackSize, 29)]) |
                     Has(RAC1ITEM.GOLD_BOLT_30, count=2, options=[OptionFilter(GoldBoltPackSize, 30)]) |
                     Has(RAC1ITEM.GOLD_BOLT_31, count=2, options=[OptionFilter(GoldBoltPackSize, 31)]) |
                     Has(RAC1ITEM.GOLD_BOLT_32, count=2, options=[OptionFilter(GoldBoltPackSize, 32)]) |
                     Has(RAC1ITEM.GOLD_BOLT_33, count=2, options=[OptionFilter(GoldBoltPackSize, 33)]) |
                     Has(RAC1ITEM.GOLD_BOLT_34, count=2, options=[OptionFilter(GoldBoltPackSize, 34)]) |
                     Has(RAC1ITEM.GOLD_BOLT_35, count=2, options=[OptionFilter(GoldBoltPackSize, 35)]) |
                     Has(RAC1ITEM.GOLD_BOLT_36, count=2, options=[OptionFilter(GoldBoltPackSize, 36)]) |
                     Has(RAC1ITEM.GOLD_BOLT_37, count=2, options=[OptionFilter(GoldBoltPackSize, 37)]) |
                     Has(RAC1ITEM.GOLD_BOLT_38, count=2, options=[OptionFilter(GoldBoltPackSize, 38)]) |
                     Has(RAC1ITEM.GOLD_BOLT_39, count=2, options=[OptionFilter(GoldBoltPackSize, 39)]) |
                     Has(RAC1ITEM.GOLD_BOLT_40, count=1, options=[OptionFilter(GoldBoltPackSize, 40)])
                     )

# TODO: Trick/Glitch logic

# Novalis
novalis_cave_gb_rule = has_explosive_weapon
novalis_underwater_caves_rule = has_hydro_pack
novalis_gold_weapon_10k = has_40_gold_bolts & has_10k_bolts
novalis_gold_weapon_20k = has_40_gold_bolts & has_20k_bolts
novalis_gold_weapon_30k = has_40_gold_bolts & has_30k_bolts
novalis_gold_weapon_60k = has_40_gold_bolts & has_60k_bolts

# Aridia
aridia_trespasser_rule = Has(RAC1ITEM.SWINGSHOT)
aridia_laser_rule = has_magneboots
aridia_cave_rule = has_explosive_weapon

# Kerwan
kerwan_train_rule = can_improved_jump
kerwan_course_gb_rule = can_glide

# Eudora
eudora_suck_cannon_rule = can_glide
eudora_henchman_rule = can_improved_jump & HasAll(RAC1ITEM.SWINGSHOT, RAC1ITEM.TRESPASSER)
eudora_skillpoint_rule = has_short_range_weapon

# Rilgar
rilgar_hoverboard_rule = has_hoverboard & can_improved_jump
rilgar_bouncer_rule = can_improved_jump & HasAll(RAC1ITEM.SWINGSHOT, RAC1ITEM.HYDRODISPLACER)
rilgar_underwater_bolt_rule = rilgar_bouncer_rule & has_o2_mask
rilgar_ryno_rule = can_improved_jump & has_150k_bolts

# Blarg
blarg_outside_gold_bolt_rule = has_o2_mask & Has(RAC1ITEM.TRESPASSER)

# Umbris
umbris_snagglebeast_rule = can_glide & HasAll(RAC1ITEM.SWINGSHOT, RAC1ITEM.HYDRODISPLACER)
umbris_pressure_bolt_rule = can_glide & Has(RAC1ITEM.SWINGSHOT)
umbris_jump_bolt_rule = can_glide & HasAll(RAC1ITEM.SWINGSHOT, RAC1ITEM.HYDRODISPLACER)

# Gaspar
gaspar_skillpoint_rule = Has(RAC1ITEM.VISIBOMB) | (has_medium_range_weapon & Has(RAC1ITEM.SWINGSHOT))

# Orxon
orxon_nanotech_rule = has_o2_mask & can_glide
orxon_ultra_nanotech_rule = orxon_nanotech_rule & has_30k_bolts
orxon_visibomb_rule = has_o2_mask & has_15k_bolts
orxon_ratchet_infobot_rule = has_o2_mask & can_glide & has_magneboots & Has(RAC1ITEM.SWINGSHOT)
orxon_visibomb_bolt_rule = orxon_ratchet_infobot_rule & Has(RAC1ITEM.VISIBOMB)
orxon_sniper_rule = has_o2_mask & can_glide & has_medium_range_weapon
orxon_hey_over_here_rule = has_o2_mask & can_glide & has_magneboots & Has(RAC1ITEM.TAUNTER)

# Pokitaru
pokitaru_ship_rule = has_pilots_helmet & can_ground_pound
pokitaru_persuader_rule = has_raritanium & HasAll(RAC1ITEM.TRESPASSER, RAC1ITEM.HYDRODISPLACER)
pokitaru_gold_bolt_rule = can_ground_pound & Has(RAC1ITEM.SWINGSHOT)

# Hoven
hoven_infobot_rule = has_short_range_weapon & can_improved_jump
hoven_raritanium_rule = can_improved_jump & Has(RAC1ITEM.SWINGSHOT)

# Gemlik
gemlik_quark_rule = has_magneboots & can_improved_jump & has_long_range_weapon & HasAll(RAC1ITEM.SWINGSHOT, RAC1ITEM.TRESPASSER)
gemlik_bolt_rule = can_improved_jump & HasAll(RAC1ITEM.VISIBOMB, RAC1ITEM.TRESPASSER)
#gemlik_gold_weapon_rule = gemlik_quark_rule & has_40_gold_bolts & has_bolts

# Oltanis
oltanis_main_bolt_rule = has_grindboots & Has(RAC1ITEM.SWINGSHOT)
oltanis_final_bolt_rule = has_grindboots & has_magneboots & Has(RAC1ITEM.SWINGSHOT)

# Quartu
quartu_infiltrate_rule = can_ground_pound & HasAll(RAC1ITEM.HOLOGUISE, RAC1ITEM.SWINGSHOT)
quartu_codebot_rule = HasAll(RAC1ITEM.CODEBOT, RAC1ITEM.SWINGSHOT)
quartu_bolt_grabber_rule = has_o2_mask & has_hydro_pack

# Kalebo III
kalebo_switch_rule = has_medium_range_weapon | has_bomb_glove | HasAny(RAC1ITEM.VISIBOMB, RAC1ITEM.RYNO)
kalebo_hologuise_rule = has_hoverboard & has_grindboots & kalebo_switch_rule & Has(RAC1ITEM.SWINGSHOT)

# Drek's Fleet
fleet_infobot_rule = has_magneboots & has_pilots_helmet & HasAll(RAC1ITEM.HOLOGUISE, RAC1ITEM.SWINGSHOT)
fleet_water_rule = has_o2_mask & has_hydro_pack
fleet_second_bolt_rule = has_magneboots & has_pilots_helmet & HasAll(RAC1ITEM.HOLOGUISE, RAC1ITEM.SWINGSHOT)

# Veldin
veldin_global_rule = has_magneboots & can_ground_pound & HasAll(RAC1ITEM.TRESPASSER, RAC1ITEM.HYDRODISPLACER)
veldin_grind_bolt_rule = veldin_global_rule & has_grindboots & Has(RAC1ITEM.SWINGSHOT)
veldin_halfway_bolt_rule = veldin_global_rule
veldin_taunter_bolt_rule = veldin_global_rule & Has(RAC1ITEM.TAUNTER)
veldin_defeat_drek_rule = veldin_global_rule & Has(RAC1ITEM.SWINGSHOT)
