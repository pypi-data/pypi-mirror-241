"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._996 import AddendumModificationDistributionRule
    from ._997 import BacklashSpecification
    from ._998 import BasicRackProfiles
    from ._999 import CaseHardeningProperties
    from ._1000 import CreateNewSuitableCutterOption
    from ._1001 import CrossedAxisCylindricalGearPair
    from ._1002 import CrossedAxisCylindricalGearPairLineContact
    from ._1003 import CrossedAxisCylindricalGearPairPointContact
    from ._1004 import CylindricalGearAbstractRack
    from ._1005 import CylindricalGearAbstractRackFlank
    from ._1006 import CylindricalGearBasicRack
    from ._1007 import CylindricalGearBasicRackFlank
    from ._1008 import CylindricalGearCuttingOptions
    from ._1009 import CylindricalGearDefaults
    from ._1010 import CylindricalGearDesign
    from ._1011 import CylindricalGearDesignConstraint
    from ._1012 import CylindricalGearDesignConstraints
    from ._1013 import CylindricalGearDesignConstraintsDatabase
    from ._1014 import CylindricalGearDesignConstraintSettings
    from ._1015 import CylindricalGearFlankDesign
    from ._1016 import CylindricalGearMeshDesign
    from ._1017 import CylindricalGearMeshFlankDesign
    from ._1018 import CylindricalGearMicroGeometrySettings
    from ._1019 import CylindricalGearMicroGeometrySettingsDatabase
    from ._1020 import CylindricalGearMicroGeometrySettingsItem
    from ._1021 import CylindricalGearPinionTypeCutter
    from ._1022 import CylindricalGearPinionTypeCutterFlank
    from ._1023 import CylindricalGearProfileMeasurement
    from ._1024 import CylindricalGearProfileMeasurementType
    from ._1025 import CylindricalGearProfileModifications
    from ._1026 import CylindricalGearSetDesign
    from ._1027 import CylindricalGearSetFlankDesign
    from ._1028 import CylindricalGearSetMacroGeometryOptimiser
    from ._1029 import CylindricalGearSetManufacturingConfigurationSelection
    from ._1030 import CylindricalGearSetMicroGeometrySettings
    from ._1031 import CylindricalGearSetOptimisationWrapper
    from ._1032 import CylindricalGearTableMGItemDetail
    from ._1033 import CylindricalGearTableWithMGCharts
    from ._1034 import CylindricalGearToothThicknessSpecification
    from ._1035 import CylindricalMeshAngularBacklash
    from ._1036 import CylindricalMeshedGear
    from ._1037 import CylindricalMeshedGearFlank
    from ._1038 import CylindricalMeshLinearBacklashSpecification
    from ._1039 import CylindricalPlanetaryGearSetDesign
    from ._1040 import CylindricalPlanetGearDesign
    from ._1041 import DIN3967AllowanceSeries
    from ._1042 import DIN3967ToleranceSeries
    from ._1043 import DoubleAxisScaleAndRange
    from ._1044 import FinishToothThicknessDesignSpecification
    from ._1045 import GearFitSystems
    from ._1046 import GearManufacturingConfigSetupViewModel
    from ._1047 import GearSetManufacturingConfigurationSetup
    from ._1048 import GeometrySpecificationType
    from ._1049 import HardenedMaterialProperties
    from ._1050 import HardnessProfileCalculationMethod
    from ._1051 import HeatTreatmentType
    from ._1052 import ISO6336Geometry
    from ._1053 import ISO6336GeometryBase
    from ._1054 import ISO6336GeometryForShapedGears
    from ._1055 import ISO6336GeometryManufactured
    from ._1056 import LinearBacklashSpecification
    from ._1057 import LTCALoadCaseModifiableSettings
    from ._1058 import LTCASettings
    from ._1059 import MicroGeometryConvention
    from ._1060 import MicroGeometryProfileConvention
    from ._1061 import Micropitting
    from ._1062 import NamedPlanetAssemblyIndex
    from ._1063 import NamedPlanetSideBandAmplitudeFactor
    from ._1064 import ReadonlyToothThicknessSpecification
    from ._1065 import RelativeMeasurementViewModel
    from ._1066 import RelativeValuesSpecification
    from ._1067 import RootStressSurfaceChartOption
    from ._1068 import Scuffing
    from ._1069 import ScuffingCoefficientOfFrictionMethods
    from ._1070 import ScuffingTemperatureMethodsAGMA
    from ._1071 import ScuffingTemperatureMethodsISO
    from ._1072 import ShaperEdgeTypes
    from ._1073 import SpurGearLoadSharingCodes
    from ._1074 import StandardRack
    from ._1075 import StandardRackFlank
    from ._1076 import SurfaceRoughness
    from ._1077 import ThicknessType
    from ._1078 import TiffAnalysisSettings
    from ._1079 import TipAlterationCoefficientMethod
    from ._1080 import TolerancedMetalMeasurements
    from ._1081 import TolerancedValueSpecification
    from ._1082 import ToothFlankFractureAnalysisSettings
    from ._1083 import ToothThicknessSpecification
    from ._1084 import ToothThicknessSpecificationBase
    from ._1085 import TypeOfMechanismHousing
    from ._1086 import Usage
else:
    import_structure = {
        "_996": ["AddendumModificationDistributionRule"],
        "_997": ["BacklashSpecification"],
        "_998": ["BasicRackProfiles"],
        "_999": ["CaseHardeningProperties"],
        "_1000": ["CreateNewSuitableCutterOption"],
        "_1001": ["CrossedAxisCylindricalGearPair"],
        "_1002": ["CrossedAxisCylindricalGearPairLineContact"],
        "_1003": ["CrossedAxisCylindricalGearPairPointContact"],
        "_1004": ["CylindricalGearAbstractRack"],
        "_1005": ["CylindricalGearAbstractRackFlank"],
        "_1006": ["CylindricalGearBasicRack"],
        "_1007": ["CylindricalGearBasicRackFlank"],
        "_1008": ["CylindricalGearCuttingOptions"],
        "_1009": ["CylindricalGearDefaults"],
        "_1010": ["CylindricalGearDesign"],
        "_1011": ["CylindricalGearDesignConstraint"],
        "_1012": ["CylindricalGearDesignConstraints"],
        "_1013": ["CylindricalGearDesignConstraintsDatabase"],
        "_1014": ["CylindricalGearDesignConstraintSettings"],
        "_1015": ["CylindricalGearFlankDesign"],
        "_1016": ["CylindricalGearMeshDesign"],
        "_1017": ["CylindricalGearMeshFlankDesign"],
        "_1018": ["CylindricalGearMicroGeometrySettings"],
        "_1019": ["CylindricalGearMicroGeometrySettingsDatabase"],
        "_1020": ["CylindricalGearMicroGeometrySettingsItem"],
        "_1021": ["CylindricalGearPinionTypeCutter"],
        "_1022": ["CylindricalGearPinionTypeCutterFlank"],
        "_1023": ["CylindricalGearProfileMeasurement"],
        "_1024": ["CylindricalGearProfileMeasurementType"],
        "_1025": ["CylindricalGearProfileModifications"],
        "_1026": ["CylindricalGearSetDesign"],
        "_1027": ["CylindricalGearSetFlankDesign"],
        "_1028": ["CylindricalGearSetMacroGeometryOptimiser"],
        "_1029": ["CylindricalGearSetManufacturingConfigurationSelection"],
        "_1030": ["CylindricalGearSetMicroGeometrySettings"],
        "_1031": ["CylindricalGearSetOptimisationWrapper"],
        "_1032": ["CylindricalGearTableMGItemDetail"],
        "_1033": ["CylindricalGearTableWithMGCharts"],
        "_1034": ["CylindricalGearToothThicknessSpecification"],
        "_1035": ["CylindricalMeshAngularBacklash"],
        "_1036": ["CylindricalMeshedGear"],
        "_1037": ["CylindricalMeshedGearFlank"],
        "_1038": ["CylindricalMeshLinearBacklashSpecification"],
        "_1039": ["CylindricalPlanetaryGearSetDesign"],
        "_1040": ["CylindricalPlanetGearDesign"],
        "_1041": ["DIN3967AllowanceSeries"],
        "_1042": ["DIN3967ToleranceSeries"],
        "_1043": ["DoubleAxisScaleAndRange"],
        "_1044": ["FinishToothThicknessDesignSpecification"],
        "_1045": ["GearFitSystems"],
        "_1046": ["GearManufacturingConfigSetupViewModel"],
        "_1047": ["GearSetManufacturingConfigurationSetup"],
        "_1048": ["GeometrySpecificationType"],
        "_1049": ["HardenedMaterialProperties"],
        "_1050": ["HardnessProfileCalculationMethod"],
        "_1051": ["HeatTreatmentType"],
        "_1052": ["ISO6336Geometry"],
        "_1053": ["ISO6336GeometryBase"],
        "_1054": ["ISO6336GeometryForShapedGears"],
        "_1055": ["ISO6336GeometryManufactured"],
        "_1056": ["LinearBacklashSpecification"],
        "_1057": ["LTCALoadCaseModifiableSettings"],
        "_1058": ["LTCASettings"],
        "_1059": ["MicroGeometryConvention"],
        "_1060": ["MicroGeometryProfileConvention"],
        "_1061": ["Micropitting"],
        "_1062": ["NamedPlanetAssemblyIndex"],
        "_1063": ["NamedPlanetSideBandAmplitudeFactor"],
        "_1064": ["ReadonlyToothThicknessSpecification"],
        "_1065": ["RelativeMeasurementViewModel"],
        "_1066": ["RelativeValuesSpecification"],
        "_1067": ["RootStressSurfaceChartOption"],
        "_1068": ["Scuffing"],
        "_1069": ["ScuffingCoefficientOfFrictionMethods"],
        "_1070": ["ScuffingTemperatureMethodsAGMA"],
        "_1071": ["ScuffingTemperatureMethodsISO"],
        "_1072": ["ShaperEdgeTypes"],
        "_1073": ["SpurGearLoadSharingCodes"],
        "_1074": ["StandardRack"],
        "_1075": ["StandardRackFlank"],
        "_1076": ["SurfaceRoughness"],
        "_1077": ["ThicknessType"],
        "_1078": ["TiffAnalysisSettings"],
        "_1079": ["TipAlterationCoefficientMethod"],
        "_1080": ["TolerancedMetalMeasurements"],
        "_1081": ["TolerancedValueSpecification"],
        "_1082": ["ToothFlankFractureAnalysisSettings"],
        "_1083": ["ToothThicknessSpecification"],
        "_1084": ["ToothThicknessSpecificationBase"],
        "_1085": ["TypeOfMechanismHousing"],
        "_1086": ["Usage"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AddendumModificationDistributionRule",
    "BacklashSpecification",
    "BasicRackProfiles",
    "CaseHardeningProperties",
    "CreateNewSuitableCutterOption",
    "CrossedAxisCylindricalGearPair",
    "CrossedAxisCylindricalGearPairLineContact",
    "CrossedAxisCylindricalGearPairPointContact",
    "CylindricalGearAbstractRack",
    "CylindricalGearAbstractRackFlank",
    "CylindricalGearBasicRack",
    "CylindricalGearBasicRackFlank",
    "CylindricalGearCuttingOptions",
    "CylindricalGearDefaults",
    "CylindricalGearDesign",
    "CylindricalGearDesignConstraint",
    "CylindricalGearDesignConstraints",
    "CylindricalGearDesignConstraintsDatabase",
    "CylindricalGearDesignConstraintSettings",
    "CylindricalGearFlankDesign",
    "CylindricalGearMeshDesign",
    "CylindricalGearMeshFlankDesign",
    "CylindricalGearMicroGeometrySettings",
    "CylindricalGearMicroGeometrySettingsDatabase",
    "CylindricalGearMicroGeometrySettingsItem",
    "CylindricalGearPinionTypeCutter",
    "CylindricalGearPinionTypeCutterFlank",
    "CylindricalGearProfileMeasurement",
    "CylindricalGearProfileMeasurementType",
    "CylindricalGearProfileModifications",
    "CylindricalGearSetDesign",
    "CylindricalGearSetFlankDesign",
    "CylindricalGearSetMacroGeometryOptimiser",
    "CylindricalGearSetManufacturingConfigurationSelection",
    "CylindricalGearSetMicroGeometrySettings",
    "CylindricalGearSetOptimisationWrapper",
    "CylindricalGearTableMGItemDetail",
    "CylindricalGearTableWithMGCharts",
    "CylindricalGearToothThicknessSpecification",
    "CylindricalMeshAngularBacklash",
    "CylindricalMeshedGear",
    "CylindricalMeshedGearFlank",
    "CylindricalMeshLinearBacklashSpecification",
    "CylindricalPlanetaryGearSetDesign",
    "CylindricalPlanetGearDesign",
    "DIN3967AllowanceSeries",
    "DIN3967ToleranceSeries",
    "DoubleAxisScaleAndRange",
    "FinishToothThicknessDesignSpecification",
    "GearFitSystems",
    "GearManufacturingConfigSetupViewModel",
    "GearSetManufacturingConfigurationSetup",
    "GeometrySpecificationType",
    "HardenedMaterialProperties",
    "HardnessProfileCalculationMethod",
    "HeatTreatmentType",
    "ISO6336Geometry",
    "ISO6336GeometryBase",
    "ISO6336GeometryForShapedGears",
    "ISO6336GeometryManufactured",
    "LinearBacklashSpecification",
    "LTCALoadCaseModifiableSettings",
    "LTCASettings",
    "MicroGeometryConvention",
    "MicroGeometryProfileConvention",
    "Micropitting",
    "NamedPlanetAssemblyIndex",
    "NamedPlanetSideBandAmplitudeFactor",
    "ReadonlyToothThicknessSpecification",
    "RelativeMeasurementViewModel",
    "RelativeValuesSpecification",
    "RootStressSurfaceChartOption",
    "Scuffing",
    "ScuffingCoefficientOfFrictionMethods",
    "ScuffingTemperatureMethodsAGMA",
    "ScuffingTemperatureMethodsISO",
    "ShaperEdgeTypes",
    "SpurGearLoadSharingCodes",
    "StandardRack",
    "StandardRackFlank",
    "SurfaceRoughness",
    "ThicknessType",
    "TiffAnalysisSettings",
    "TipAlterationCoefficientMethod",
    "TolerancedMetalMeasurements",
    "TolerancedValueSpecification",
    "ToothFlankFractureAnalysisSettings",
    "ToothThicknessSpecification",
    "ToothThicknessSpecificationBase",
    "TypeOfMechanismHousing",
    "Usage",
)
