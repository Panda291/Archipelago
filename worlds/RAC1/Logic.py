from BaseClasses import CollectionState
from rule_builder.rules import Has, HasAny, HasAll
from .data import Items

can_swingshot = Has(Items.SWINGSHOT.name)
can_improved_jump = HasAny(Items.HELI_PACK.name, Items.THRUSTER_PACK.name)
can_heli_high_jump = Has(Items.HELI_PACK.name)
can_glide = Has(Items.HELI_PACK.name)
can_ground_pound = Has(Items.THRUSTER_PACK.name)
can_grind = Has(Items.GRINDBOOTS.name)
can_taunt = Has(Items.TAUNTER.name)
has_explosive_weapon = HasAny(Items.BOMB_GLOVE.name,
                              Items.DEVASTATOR.name,
                              Items.MINE_GLOVE.name,
                              Items.VISIBOMB.name,
                              Items.RYNO.name)
has_long_range_weapon = HasAny(Items.BLASTER.name,
                             Items.DEVASTATOR.name,
                             Items.VISIBOMB.name,
                             Items.RYNO.name)
can_farm_money = Has(Items.METAL_DETECTOR.name)

has_40_gold_bolts = Has(Items.GOLD_BOLT.name, count=40)


# Novalis
novalis_underwater_caves_rule = Has(Items.HYDRO_PACK.name)
novalis_gold_weapon_rule = has_40_gold_bolts & can_farm_money
novalis_skillpoint_rule = has_long_range_weapon


# Eudora
eudora_suck_cannon_rule = can_improved_jump & can_glide
eudora_henchman_rule = can_swingshot & Has(Items.TRESPASSER.name) & can_improved_jump

# Rilgar
rilgar_hoverboard_rule = can_improved_jump & Has(Items.HOVERBOARD.name)
rilgar_bouncer_rule = can_swingshot & can_improved_jump & Has(Items.HYDRODISPLACER.name)
rilgar_underwater_bolt_rule = rilgar_bouncer_rule & Has(Items.O2_MASK.name)
rilgar_ryno_rule = can_improved_jump & can_farm_money

# Blarg
blarg_outside_gold_bolt_rule = HasAll(Items.O2_MASK.name, Items.TRESPASSER.name)

# Umbris
umbris_snagglebeast_rule = can_swingshot & can_glide & Has(Items.HYDRODISPLACER.name)
umbris_pressure_bolt_rule = can_swingshot & can_glide
umbris_jump_bolt_rule = can_swingshot & can_glide & Has(Items.HYDRODISPLACER.name)

# Orxon
orxon_nanotech_rule = can_glide & Has(Items.O2_MASK.name)
orxon_ultra_nanotech_rule = orxon_nanotech_rule & can_farm_money
orxon_visibomb_rule = can_farm_money & Has(Items.O2_MASK.name)
orxon_visibomb_bolt_rule = (HasAll(Items.O2_MASK.name, Items.VISIBOMB.name, Items.MAGNEBOOTS.name) &
                            can_swingshot &
                            can_glide)
orxon_ratchet_infobot_rule = can_glide & can_swingshot & HasAll(Items.O2_MASK.name, Items.MAGNEBOOTS.name)

# Pokitaru
pokitaru_ship_rule = can_ground_pound & Has(Items.PILOTS_HELMET.name)
pokitaru_persuader_rule = HasAll(Items.RARITANIUM.name, Items.TRESPASSER.name, Items.HYDRODISPLACER.name)
pokitaru_gold_bolt_rule = can_swingshot & can_ground_pound

# Hoven
hoven_infobot_rule = can_improved_jump & has_long_range_weapon
hoven_raritanium_rule = can_swingshot & can_improved_jump

# Gemlik
gemlik_quark_rule = (can_improved_jump & has_long_range_weapon & can_swingshot &
                     HasAll(Items.TRESPASSER.name, Items.MAGNEBOOTS.name))
gemlik_bolt_rule = can_improved_jump & HasAll(Items.VISIBOMB.name, Items.TRESPASSER.name)
gemlik_gold_weapon_rule = (can_improved_jump &
                           has_long_range_weapon  &
                           can_swingshot &
                           has_40_gold_bolts &
                           can_farm_money &
                           HasAll(Items.TRESPASSER.name, Items.MAGNEBOOTS.name))


# Oltanis
oltanis_main_bolt_rule = can_grind & can_swingshot
oltanis_final_bolt_rule = can_grind & can_swingshot & Has(Items.MAGNEBOOTS.name)

# Quartu
quartu_infiltrate_rule = can_swingshot & can_ground_pound & Has(Items.HOLOGUISE.name)
quartu_codebot_rule = can_swingshot & Has(Items.CODEBOT.name)
quartu_bolt_grabber_rule = HasAll(Items.HYDRO_PACK.name, Items.O2_MASK.name)

# Kalebo III
kalebo_hologuise_rule = can_swingshot & can_grind & Has(Items.HOVERBOARD.name)

# Drek's Fleet
fleet_infobot_rule = can_swingshot & HasAll(Items.MAGNEBOOTS.name, Items.PILOTS_HELMET.name, Items.HOLOGUISE.name)
fleet_water_rule = HasAll(Items.HYDRO_PACK.name, Items.O2_MASK.name)
fleet_second_bolt_rule = can_swingshot & HasAll(Items.MAGNEBOOTS.name, Items.PILOTS_HELMET.name, Items.HOLOGUISE.name)

# Veldin
veldin_global_rule = can_ground_pound & HasAll(Items.TRESPASSER.name, Items.MAGNEBOOTS.name, Items.HYDRODISPLACER.name)
veldin_grind_bolt_rule = veldin_global_rule & can_grind & can_swingshot
veldin_halfway_bolt_rule = veldin_global_rule
veldin_taunter_bolt_rule = veldin_global_rule & Has(Items.TAUNTER.name)
veldin_defeat_drek_rule = veldin_global_rule & can_swingshot
