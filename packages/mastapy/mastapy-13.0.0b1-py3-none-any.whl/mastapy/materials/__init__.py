"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._234 import AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial
    from ._235 import AcousticRadiationEfficiency
    from ._236 import AcousticRadiationEfficiencyInputType
    from ._237 import AGMALubricantType
    from ._238 import AGMAMaterialApplications
    from ._239 import AGMAMaterialClasses
    from ._240 import AGMAMaterialGrade
    from ._241 import AirProperties
    from ._242 import BearingLubricationCondition
    from ._243 import BearingMaterial
    from ._244 import BearingMaterialDatabase
    from ._245 import BHCurveExtrapolationMethod
    from ._246 import BHCurveSpecification
    from ._247 import ComponentMaterialDatabase
    from ._248 import CompositeFatigueSafetyFactorItem
    from ._249 import CylindricalGearRatingMethods
    from ._250 import DensitySpecificationMethod
    from ._251 import FatigueSafetyFactorItem
    from ._252 import FatigueSafetyFactorItemBase
    from ._253 import GearingTypes
    from ._254 import GeneralTransmissionProperties
    from ._255 import GreaseContaminationOptions
    from ._256 import HardnessType
    from ._257 import ISO76StaticSafetyFactorLimits
    from ._258 import ISOLubricantType
    from ._259 import LubricantDefinition
    from ._260 import LubricantDelivery
    from ._261 import LubricantViscosityClassAGMA
    from ._262 import LubricantViscosityClassification
    from ._263 import LubricantViscosityClassISO
    from ._264 import LubricantViscosityClassSAE
    from ._265 import LubricationDetail
    from ._266 import LubricationDetailDatabase
    from ._267 import Material
    from ._268 import MaterialDatabase
    from ._269 import MaterialsSettings
    from ._270 import MaterialsSettingsDatabase
    from ._271 import MaterialsSettingsItem
    from ._272 import MaterialStandards
    from ._273 import MetalPlasticType
    from ._274 import OilFiltrationOptions
    from ._275 import PressureViscosityCoefficientMethod
    from ._276 import QualityGrade
    from ._277 import SafetyFactorGroup
    from ._278 import SafetyFactorItem
    from ._279 import SNCurve
    from ._280 import SNCurvePoint
    from ._281 import SoundPressureEnclosure
    from ._282 import SoundPressureEnclosureType
    from ._283 import StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial
    from ._284 import StressCyclesDataForTheContactSNCurveOfAPlasticMaterial
    from ._285 import TransmissionApplications
    from ._286 import VDI2736LubricantType
    from ._287 import VehicleDynamicsProperties
    from ._288 import WindTurbineStandards
    from ._289 import WorkingCharacteristics
else:
    import_structure = {
        "_234": ["AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial"],
        "_235": ["AcousticRadiationEfficiency"],
        "_236": ["AcousticRadiationEfficiencyInputType"],
        "_237": ["AGMALubricantType"],
        "_238": ["AGMAMaterialApplications"],
        "_239": ["AGMAMaterialClasses"],
        "_240": ["AGMAMaterialGrade"],
        "_241": ["AirProperties"],
        "_242": ["BearingLubricationCondition"],
        "_243": ["BearingMaterial"],
        "_244": ["BearingMaterialDatabase"],
        "_245": ["BHCurveExtrapolationMethod"],
        "_246": ["BHCurveSpecification"],
        "_247": ["ComponentMaterialDatabase"],
        "_248": ["CompositeFatigueSafetyFactorItem"],
        "_249": ["CylindricalGearRatingMethods"],
        "_250": ["DensitySpecificationMethod"],
        "_251": ["FatigueSafetyFactorItem"],
        "_252": ["FatigueSafetyFactorItemBase"],
        "_253": ["GearingTypes"],
        "_254": ["GeneralTransmissionProperties"],
        "_255": ["GreaseContaminationOptions"],
        "_256": ["HardnessType"],
        "_257": ["ISO76StaticSafetyFactorLimits"],
        "_258": ["ISOLubricantType"],
        "_259": ["LubricantDefinition"],
        "_260": ["LubricantDelivery"],
        "_261": ["LubricantViscosityClassAGMA"],
        "_262": ["LubricantViscosityClassification"],
        "_263": ["LubricantViscosityClassISO"],
        "_264": ["LubricantViscosityClassSAE"],
        "_265": ["LubricationDetail"],
        "_266": ["LubricationDetailDatabase"],
        "_267": ["Material"],
        "_268": ["MaterialDatabase"],
        "_269": ["MaterialsSettings"],
        "_270": ["MaterialsSettingsDatabase"],
        "_271": ["MaterialsSettingsItem"],
        "_272": ["MaterialStandards"],
        "_273": ["MetalPlasticType"],
        "_274": ["OilFiltrationOptions"],
        "_275": ["PressureViscosityCoefficientMethod"],
        "_276": ["QualityGrade"],
        "_277": ["SafetyFactorGroup"],
        "_278": ["SafetyFactorItem"],
        "_279": ["SNCurve"],
        "_280": ["SNCurvePoint"],
        "_281": ["SoundPressureEnclosure"],
        "_282": ["SoundPressureEnclosureType"],
        "_283": ["StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial"],
        "_284": ["StressCyclesDataForTheContactSNCurveOfAPlasticMaterial"],
        "_285": ["TransmissionApplications"],
        "_286": ["VDI2736LubricantType"],
        "_287": ["VehicleDynamicsProperties"],
        "_288": ["WindTurbineStandards"],
        "_289": ["WorkingCharacteristics"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
    "AcousticRadiationEfficiency",
    "AcousticRadiationEfficiencyInputType",
    "AGMALubricantType",
    "AGMAMaterialApplications",
    "AGMAMaterialClasses",
    "AGMAMaterialGrade",
    "AirProperties",
    "BearingLubricationCondition",
    "BearingMaterial",
    "BearingMaterialDatabase",
    "BHCurveExtrapolationMethod",
    "BHCurveSpecification",
    "ComponentMaterialDatabase",
    "CompositeFatigueSafetyFactorItem",
    "CylindricalGearRatingMethods",
    "DensitySpecificationMethod",
    "FatigueSafetyFactorItem",
    "FatigueSafetyFactorItemBase",
    "GearingTypes",
    "GeneralTransmissionProperties",
    "GreaseContaminationOptions",
    "HardnessType",
    "ISO76StaticSafetyFactorLimits",
    "ISOLubricantType",
    "LubricantDefinition",
    "LubricantDelivery",
    "LubricantViscosityClassAGMA",
    "LubricantViscosityClassification",
    "LubricantViscosityClassISO",
    "LubricantViscosityClassSAE",
    "LubricationDetail",
    "LubricationDetailDatabase",
    "Material",
    "MaterialDatabase",
    "MaterialsSettings",
    "MaterialsSettingsDatabase",
    "MaterialsSettingsItem",
    "MaterialStandards",
    "MetalPlasticType",
    "OilFiltrationOptions",
    "PressureViscosityCoefficientMethod",
    "QualityGrade",
    "SafetyFactorGroup",
    "SafetyFactorItem",
    "SNCurve",
    "SNCurvePoint",
    "SoundPressureEnclosure",
    "SoundPressureEnclosureType",
    "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial",
    "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial",
    "TransmissionApplications",
    "VDI2736LubricantType",
    "VehicleDynamicsProperties",
    "WindTurbineStandards",
    "WorkingCharacteristics",
)
