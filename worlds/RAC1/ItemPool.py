from BaseClasses import ItemClassification
from .data import Items
from .data.Items import ItemData


def get_classification(item: ItemData) -> ItemClassification:
    if item in Items.PLANETS:
        return ItemClassification.progression
    if item in [
        Items.HELI_PACK,
        Items.THRUSTER_PACK,
        Items.HYDRO_PACK,
        Items.SWINGSHOT,
        Items.MAGNEBOOTS,
        Items.GRINDBOOTS,
        Items.HYDRODISPLACER,
        Items.TAUNTER,
        Items.O2_MASK,
        Items.PILOTS_HELMET,
        Items.TRESPASSER,
        Items.HOLOGUISE,
        Items.CODEBOT,
        Items.RARITANIUM,
        Items.HOVERBOARD,
        Items.ZOOMERATOR,
        Items.BOMB_GLOVE,
        Items.DEVASTATOR,
        Items.VISIBOMB,
        Items.METAL_DETECTOR,
    ]:
        return ItemClassification.progression
    if item in [
        Items.BOLT_GRABBER,
        Items.PERSUADER,
        Items.PREMIUM_NANOTECH,
        Items.ULTRA_NANOTECH,
    ]:
        return ItemClassification.useful
    if item in Items.WEAPONS:
        return ItemClassification.useful
    if item in Items.GOLDEN_WEAPONS:
        return ItemClassification.useful

    return ItemClassification.filler
