"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._581 import AGMACylindricalGearMaterial
    from ._582 import BevelGearAbstractMaterialDatabase
    from ._583 import BevelGearISOMaterial
    from ._584 import BevelGearISOMaterialDatabase
    from ._585 import BevelGearMaterial
    from ._586 import BevelGearMaterialDatabase
    from ._587 import CylindricalGearAGMAMaterialDatabase
    from ._588 import CylindricalGearISOMaterialDatabase
    from ._589 import CylindricalGearMaterial
    from ._590 import CylindricalGearMaterialDatabase
    from ._591 import CylindricalGearPlasticMaterialDatabase
    from ._592 import GearMaterial
    from ._593 import GearMaterialDatabase
    from ._594 import GearMaterialExpertSystemFactorSettings
    from ._595 import ISOCylindricalGearMaterial
    from ._596 import ISOTR1417912001CoefficientOfFrictionConstants
    from ._597 import ISOTR1417912001CoefficientOfFrictionConstantsDatabase
    from ._598 import KlingelnbergConicalGearMaterialDatabase
    from ._599 import KlingelnbergCycloPalloidConicalGearMaterial
    from ._600 import ManufactureRating
    from ._601 import PlasticCylindricalGearMaterial
    from ._602 import PlasticSNCurve
    from ._603 import RatingMethods
    from ._604 import RawMaterial
    from ._605 import RawMaterialDatabase
    from ._606 import SNCurveDefinition
else:
    import_structure = {
        "_581": ["AGMACylindricalGearMaterial"],
        "_582": ["BevelGearAbstractMaterialDatabase"],
        "_583": ["BevelGearISOMaterial"],
        "_584": ["BevelGearISOMaterialDatabase"],
        "_585": ["BevelGearMaterial"],
        "_586": ["BevelGearMaterialDatabase"],
        "_587": ["CylindricalGearAGMAMaterialDatabase"],
        "_588": ["CylindricalGearISOMaterialDatabase"],
        "_589": ["CylindricalGearMaterial"],
        "_590": ["CylindricalGearMaterialDatabase"],
        "_591": ["CylindricalGearPlasticMaterialDatabase"],
        "_592": ["GearMaterial"],
        "_593": ["GearMaterialDatabase"],
        "_594": ["GearMaterialExpertSystemFactorSettings"],
        "_595": ["ISOCylindricalGearMaterial"],
        "_596": ["ISOTR1417912001CoefficientOfFrictionConstants"],
        "_597": ["ISOTR1417912001CoefficientOfFrictionConstantsDatabase"],
        "_598": ["KlingelnbergConicalGearMaterialDatabase"],
        "_599": ["KlingelnbergCycloPalloidConicalGearMaterial"],
        "_600": ["ManufactureRating"],
        "_601": ["PlasticCylindricalGearMaterial"],
        "_602": ["PlasticSNCurve"],
        "_603": ["RatingMethods"],
        "_604": ["RawMaterial"],
        "_605": ["RawMaterialDatabase"],
        "_606": ["SNCurveDefinition"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMACylindricalGearMaterial",
    "BevelGearAbstractMaterialDatabase",
    "BevelGearISOMaterial",
    "BevelGearISOMaterialDatabase",
    "BevelGearMaterial",
    "BevelGearMaterialDatabase",
    "CylindricalGearAGMAMaterialDatabase",
    "CylindricalGearISOMaterialDatabase",
    "CylindricalGearMaterial",
    "CylindricalGearMaterialDatabase",
    "CylindricalGearPlasticMaterialDatabase",
    "GearMaterial",
    "GearMaterialDatabase",
    "GearMaterialExpertSystemFactorSettings",
    "ISOCylindricalGearMaterial",
    "ISOTR1417912001CoefficientOfFrictionConstants",
    "ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
    "KlingelnbergConicalGearMaterialDatabase",
    "KlingelnbergCycloPalloidConicalGearMaterial",
    "ManufactureRating",
    "PlasticCylindricalGearMaterial",
    "PlasticSNCurve",
    "RatingMethods",
    "RawMaterial",
    "RawMaterialDatabase",
    "SNCurveDefinition",
)
