"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6801 import LoadCase
    from ._6802 import StaticLoadCase
    from ._6803 import TimeSeriesLoadCase
    from ._6804 import AbstractAssemblyLoadCase
    from ._6805 import AbstractShaftLoadCase
    from ._6806 import AbstractShaftOrHousingLoadCase
    from ._6807 import AbstractShaftToMountableComponentConnectionLoadCase
    from ._6808 import AdditionalAccelerationOptions
    from ._6809 import AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
    from ._6810 import AdvancedTimeSteppingAnalysisForModulationType
    from ._6811 import AGMAGleasonConicalGearLoadCase
    from ._6812 import AGMAGleasonConicalGearMeshLoadCase
    from ._6813 import AGMAGleasonConicalGearSetLoadCase
    from ._6814 import AllRingPinsManufacturingError
    from ._6815 import AnalysisType
    from ._6816 import AssemblyLoadCase
    from ._6817 import BearingLoadCase
    from ._6818 import BeltConnectionLoadCase
    from ._6819 import BeltDriveLoadCase
    from ._6820 import BevelDifferentialGearLoadCase
    from ._6821 import BevelDifferentialGearMeshLoadCase
    from ._6822 import BevelDifferentialGearSetLoadCase
    from ._6823 import BevelDifferentialPlanetGearLoadCase
    from ._6824 import BevelDifferentialSunGearLoadCase
    from ._6825 import BevelGearLoadCase
    from ._6826 import BevelGearMeshLoadCase
    from ._6827 import BevelGearSetLoadCase
    from ._6828 import BoltedJointLoadCase
    from ._6829 import BoltLoadCase
    from ._6830 import ClutchConnectionLoadCase
    from ._6831 import ClutchHalfLoadCase
    from ._6832 import ClutchLoadCase
    from ._6833 import CMSElementFaceGroupWithSelectionOption
    from ._6834 import CoaxialConnectionLoadCase
    from ._6835 import ComponentLoadCase
    from ._6836 import ConceptCouplingConnectionLoadCase
    from ._6837 import ConceptCouplingHalfLoadCase
    from ._6838 import ConceptCouplingLoadCase
    from ._6839 import ConceptGearLoadCase
    from ._6840 import ConceptGearMeshLoadCase
    from ._6841 import ConceptGearSetLoadCase
    from ._6842 import ConicalGearLoadCase
    from ._6843 import ConicalGearManufactureError
    from ._6844 import ConicalGearMeshLoadCase
    from ._6845 import ConicalGearSetHarmonicLoadData
    from ._6846 import ConicalGearSetLoadCase
    from ._6847 import ConnectionLoadCase
    from ._6848 import ConnectorLoadCase
    from ._6849 import CouplingConnectionLoadCase
    from ._6850 import CouplingHalfLoadCase
    from ._6851 import CouplingLoadCase
    from ._6852 import CVTBeltConnectionLoadCase
    from ._6853 import CVTLoadCase
    from ._6854 import CVTPulleyLoadCase
    from ._6855 import CycloidalAssemblyLoadCase
    from ._6856 import CycloidalDiscCentralBearingConnectionLoadCase
    from ._6857 import CycloidalDiscLoadCase
    from ._6858 import CycloidalDiscPlanetaryBearingConnectionLoadCase
    from ._6859 import CylindricalGearLoadCase
    from ._6860 import CylindricalGearManufactureError
    from ._6861 import CylindricalGearMeshLoadCase
    from ._6862 import CylindricalGearSetHarmonicLoadData
    from ._6863 import CylindricalGearSetLoadCase
    from ._6864 import CylindricalPlanetGearLoadCase
    from ._6865 import DataFromMotorPackagePerMeanTorque
    from ._6866 import DataFromMotorPackagePerSpeed
    from ._6867 import DatumLoadCase
    from ._6868 import ElectricMachineDataImportType
    from ._6869 import ElectricMachineHarmonicLoadData
    from ._6870 import ElectricMachineHarmonicLoadDataFromExcel
    from ._6871 import ElectricMachineHarmonicLoadDataFromFlux
    from ._6872 import ElectricMachineHarmonicLoadDataFromJMAG
    from ._6873 import ElectricMachineHarmonicLoadDataFromMASTA
    from ._6874 import ElectricMachineHarmonicLoadDataFromMotorCAD
    from ._6875 import ElectricMachineHarmonicLoadDataFromMotorPackages
    from ._6876 import ElectricMachineHarmonicLoadExcelImportOptions
    from ._6877 import ElectricMachineHarmonicLoadFluxImportOptions
    from ._6878 import ElectricMachineHarmonicLoadImportOptionsBase
    from ._6879 import ElectricMachineHarmonicLoadJMAGImportOptions
    from ._6880 import ElectricMachineHarmonicLoadMotorCADImportOptions
    from ._6881 import ExternalCADModelLoadCase
    from ._6882 import FaceGearLoadCase
    from ._6883 import FaceGearMeshLoadCase
    from ._6884 import FaceGearSetLoadCase
    from ._6885 import FEPartLoadCase
    from ._6886 import FlexiblePinAssemblyLoadCase
    from ._6887 import ForceAndTorqueScalingFactor
    from ._6888 import GearLoadCase
    from ._6889 import GearManufactureError
    from ._6890 import GearMeshLoadCase
    from ._6891 import GearMeshTEOrderType
    from ._6892 import GearSetHarmonicLoadData
    from ._6893 import GearSetLoadCase
    from ._6894 import GuideDxfModelLoadCase
    from ._6895 import HarmonicExcitationType
    from ._6896 import HarmonicLoadDataCSVImport
    from ._6897 import HarmonicLoadDataExcelImport
    from ._6898 import HarmonicLoadDataFluxImport
    from ._6899 import HarmonicLoadDataImportBase
    from ._6900 import HarmonicLoadDataImportFromMotorPackages
    from ._6901 import HarmonicLoadDataJMAGImport
    from ._6902 import HarmonicLoadDataMotorCADImport
    from ._6903 import HypoidGearLoadCase
    from ._6904 import HypoidGearMeshLoadCase
    from ._6905 import HypoidGearSetLoadCase
    from ._6906 import ImportType
    from ._6907 import InformationAtRingPinToDiscContactPointFromGeometry
    from ._6908 import InnerDiameterReference
    from ._6909 import InterMountableComponentConnectionLoadCase
    from ._6910 import KlingelnbergCycloPalloidConicalGearLoadCase
    from ._6911 import KlingelnbergCycloPalloidConicalGearMeshLoadCase
    from ._6912 import KlingelnbergCycloPalloidConicalGearSetLoadCase
    from ._6913 import KlingelnbergCycloPalloidHypoidGearLoadCase
    from ._6914 import KlingelnbergCycloPalloidHypoidGearMeshLoadCase
    from ._6915 import KlingelnbergCycloPalloidHypoidGearSetLoadCase
    from ._6916 import KlingelnbergCycloPalloidSpiralBevelGearLoadCase
    from ._6917 import KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
    from ._6918 import KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
    from ._6919 import MassDiscLoadCase
    from ._6920 import MeasurementComponentLoadCase
    from ._6921 import MeshStiffnessSource
    from ._6922 import MountableComponentLoadCase
    from ._6923 import NamedSpeed
    from ._6924 import OilSealLoadCase
    from ._6925 import ParametricStudyType
    from ._6926 import PartLoadCase
    from ._6927 import PartToPartShearCouplingConnectionLoadCase
    from ._6928 import PartToPartShearCouplingHalfLoadCase
    from ._6929 import PartToPartShearCouplingLoadCase
    from ._6930 import PlanetaryConnectionLoadCase
    from ._6931 import PlanetaryGearSetLoadCase
    from ._6932 import PlanetarySocketManufactureError
    from ._6933 import PlanetCarrierLoadCase
    from ._6934 import PlanetManufactureError
    from ._6935 import PointLoadHarmonicLoadData
    from ._6936 import PointLoadLoadCase
    from ._6937 import PowerLoadLoadCase
    from ._6938 import PulleyLoadCase
    from ._6939 import ResetMicroGeometryOptions
    from ._6940 import RingPinManufacturingError
    from ._6941 import RingPinsLoadCase
    from ._6942 import RingPinsToDiscConnectionLoadCase
    from ._6943 import RollingRingAssemblyLoadCase
    from ._6944 import RollingRingConnectionLoadCase
    from ._6945 import RollingRingLoadCase
    from ._6946 import RootAssemblyLoadCase
    from ._6947 import ShaftHubConnectionLoadCase
    from ._6948 import ShaftLoadCase
    from ._6949 import ShaftToMountableComponentConnectionLoadCase
    from ._6950 import SpecialisedAssemblyLoadCase
    from ._6951 import SpiralBevelGearLoadCase
    from ._6952 import SpiralBevelGearMeshLoadCase
    from ._6953 import SpiralBevelGearSetLoadCase
    from ._6954 import SpringDamperConnectionLoadCase
    from ._6955 import SpringDamperHalfLoadCase
    from ._6956 import SpringDamperLoadCase
    from ._6957 import StraightBevelDiffGearLoadCase
    from ._6958 import StraightBevelDiffGearMeshLoadCase
    from ._6959 import StraightBevelDiffGearSetLoadCase
    from ._6960 import StraightBevelGearLoadCase
    from ._6961 import StraightBevelGearMeshLoadCase
    from ._6962 import StraightBevelGearSetLoadCase
    from ._6963 import StraightBevelPlanetGearLoadCase
    from ._6964 import StraightBevelSunGearLoadCase
    from ._6965 import SynchroniserHalfLoadCase
    from ._6966 import SynchroniserLoadCase
    from ._6967 import SynchroniserPartLoadCase
    from ._6968 import SynchroniserSleeveLoadCase
    from ._6969 import TEExcitationType
    from ._6970 import TorqueConverterConnectionLoadCase
    from ._6971 import TorqueConverterLoadCase
    from ._6972 import TorqueConverterPumpLoadCase
    from ._6973 import TorqueConverterTurbineLoadCase
    from ._6974 import TorqueRippleInputType
    from ._6975 import TorqueSpecificationForSystemDeflection
    from ._6976 import TransmissionEfficiencySettings
    from ._6977 import UnbalancedMassHarmonicLoadData
    from ._6978 import UnbalancedMassLoadCase
    from ._6979 import VirtualComponentLoadCase
    from ._6980 import WormGearLoadCase
    from ._6981 import WormGearMeshLoadCase
    from ._6982 import WormGearSetLoadCase
    from ._6983 import ZerolBevelGearLoadCase
    from ._6984 import ZerolBevelGearMeshLoadCase
    from ._6985 import ZerolBevelGearSetLoadCase
else:
    import_structure = {
        "_6801": ["LoadCase"],
        "_6802": ["StaticLoadCase"],
        "_6803": ["TimeSeriesLoadCase"],
        "_6804": ["AbstractAssemblyLoadCase"],
        "_6805": ["AbstractShaftLoadCase"],
        "_6806": ["AbstractShaftOrHousingLoadCase"],
        "_6807": ["AbstractShaftToMountableComponentConnectionLoadCase"],
        "_6808": ["AdditionalAccelerationOptions"],
        "_6809": ["AdvancedTimeSteppingAnalysisForModulationStaticLoadCase"],
        "_6810": ["AdvancedTimeSteppingAnalysisForModulationType"],
        "_6811": ["AGMAGleasonConicalGearLoadCase"],
        "_6812": ["AGMAGleasonConicalGearMeshLoadCase"],
        "_6813": ["AGMAGleasonConicalGearSetLoadCase"],
        "_6814": ["AllRingPinsManufacturingError"],
        "_6815": ["AnalysisType"],
        "_6816": ["AssemblyLoadCase"],
        "_6817": ["BearingLoadCase"],
        "_6818": ["BeltConnectionLoadCase"],
        "_6819": ["BeltDriveLoadCase"],
        "_6820": ["BevelDifferentialGearLoadCase"],
        "_6821": ["BevelDifferentialGearMeshLoadCase"],
        "_6822": ["BevelDifferentialGearSetLoadCase"],
        "_6823": ["BevelDifferentialPlanetGearLoadCase"],
        "_6824": ["BevelDifferentialSunGearLoadCase"],
        "_6825": ["BevelGearLoadCase"],
        "_6826": ["BevelGearMeshLoadCase"],
        "_6827": ["BevelGearSetLoadCase"],
        "_6828": ["BoltedJointLoadCase"],
        "_6829": ["BoltLoadCase"],
        "_6830": ["ClutchConnectionLoadCase"],
        "_6831": ["ClutchHalfLoadCase"],
        "_6832": ["ClutchLoadCase"],
        "_6833": ["CMSElementFaceGroupWithSelectionOption"],
        "_6834": ["CoaxialConnectionLoadCase"],
        "_6835": ["ComponentLoadCase"],
        "_6836": ["ConceptCouplingConnectionLoadCase"],
        "_6837": ["ConceptCouplingHalfLoadCase"],
        "_6838": ["ConceptCouplingLoadCase"],
        "_6839": ["ConceptGearLoadCase"],
        "_6840": ["ConceptGearMeshLoadCase"],
        "_6841": ["ConceptGearSetLoadCase"],
        "_6842": ["ConicalGearLoadCase"],
        "_6843": ["ConicalGearManufactureError"],
        "_6844": ["ConicalGearMeshLoadCase"],
        "_6845": ["ConicalGearSetHarmonicLoadData"],
        "_6846": ["ConicalGearSetLoadCase"],
        "_6847": ["ConnectionLoadCase"],
        "_6848": ["ConnectorLoadCase"],
        "_6849": ["CouplingConnectionLoadCase"],
        "_6850": ["CouplingHalfLoadCase"],
        "_6851": ["CouplingLoadCase"],
        "_6852": ["CVTBeltConnectionLoadCase"],
        "_6853": ["CVTLoadCase"],
        "_6854": ["CVTPulleyLoadCase"],
        "_6855": ["CycloidalAssemblyLoadCase"],
        "_6856": ["CycloidalDiscCentralBearingConnectionLoadCase"],
        "_6857": ["CycloidalDiscLoadCase"],
        "_6858": ["CycloidalDiscPlanetaryBearingConnectionLoadCase"],
        "_6859": ["CylindricalGearLoadCase"],
        "_6860": ["CylindricalGearManufactureError"],
        "_6861": ["CylindricalGearMeshLoadCase"],
        "_6862": ["CylindricalGearSetHarmonicLoadData"],
        "_6863": ["CylindricalGearSetLoadCase"],
        "_6864": ["CylindricalPlanetGearLoadCase"],
        "_6865": ["DataFromMotorPackagePerMeanTorque"],
        "_6866": ["DataFromMotorPackagePerSpeed"],
        "_6867": ["DatumLoadCase"],
        "_6868": ["ElectricMachineDataImportType"],
        "_6869": ["ElectricMachineHarmonicLoadData"],
        "_6870": ["ElectricMachineHarmonicLoadDataFromExcel"],
        "_6871": ["ElectricMachineHarmonicLoadDataFromFlux"],
        "_6872": ["ElectricMachineHarmonicLoadDataFromJMAG"],
        "_6873": ["ElectricMachineHarmonicLoadDataFromMASTA"],
        "_6874": ["ElectricMachineHarmonicLoadDataFromMotorCAD"],
        "_6875": ["ElectricMachineHarmonicLoadDataFromMotorPackages"],
        "_6876": ["ElectricMachineHarmonicLoadExcelImportOptions"],
        "_6877": ["ElectricMachineHarmonicLoadFluxImportOptions"],
        "_6878": ["ElectricMachineHarmonicLoadImportOptionsBase"],
        "_6879": ["ElectricMachineHarmonicLoadJMAGImportOptions"],
        "_6880": ["ElectricMachineHarmonicLoadMotorCADImportOptions"],
        "_6881": ["ExternalCADModelLoadCase"],
        "_6882": ["FaceGearLoadCase"],
        "_6883": ["FaceGearMeshLoadCase"],
        "_6884": ["FaceGearSetLoadCase"],
        "_6885": ["FEPartLoadCase"],
        "_6886": ["FlexiblePinAssemblyLoadCase"],
        "_6887": ["ForceAndTorqueScalingFactor"],
        "_6888": ["GearLoadCase"],
        "_6889": ["GearManufactureError"],
        "_6890": ["GearMeshLoadCase"],
        "_6891": ["GearMeshTEOrderType"],
        "_6892": ["GearSetHarmonicLoadData"],
        "_6893": ["GearSetLoadCase"],
        "_6894": ["GuideDxfModelLoadCase"],
        "_6895": ["HarmonicExcitationType"],
        "_6896": ["HarmonicLoadDataCSVImport"],
        "_6897": ["HarmonicLoadDataExcelImport"],
        "_6898": ["HarmonicLoadDataFluxImport"],
        "_6899": ["HarmonicLoadDataImportBase"],
        "_6900": ["HarmonicLoadDataImportFromMotorPackages"],
        "_6901": ["HarmonicLoadDataJMAGImport"],
        "_6902": ["HarmonicLoadDataMotorCADImport"],
        "_6903": ["HypoidGearLoadCase"],
        "_6904": ["HypoidGearMeshLoadCase"],
        "_6905": ["HypoidGearSetLoadCase"],
        "_6906": ["ImportType"],
        "_6907": ["InformationAtRingPinToDiscContactPointFromGeometry"],
        "_6908": ["InnerDiameterReference"],
        "_6909": ["InterMountableComponentConnectionLoadCase"],
        "_6910": ["KlingelnbergCycloPalloidConicalGearLoadCase"],
        "_6911": ["KlingelnbergCycloPalloidConicalGearMeshLoadCase"],
        "_6912": ["KlingelnbergCycloPalloidConicalGearSetLoadCase"],
        "_6913": ["KlingelnbergCycloPalloidHypoidGearLoadCase"],
        "_6914": ["KlingelnbergCycloPalloidHypoidGearMeshLoadCase"],
        "_6915": ["KlingelnbergCycloPalloidHypoidGearSetLoadCase"],
        "_6916": ["KlingelnbergCycloPalloidSpiralBevelGearLoadCase"],
        "_6917": ["KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase"],
        "_6918": ["KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase"],
        "_6919": ["MassDiscLoadCase"],
        "_6920": ["MeasurementComponentLoadCase"],
        "_6921": ["MeshStiffnessSource"],
        "_6922": ["MountableComponentLoadCase"],
        "_6923": ["NamedSpeed"],
        "_6924": ["OilSealLoadCase"],
        "_6925": ["ParametricStudyType"],
        "_6926": ["PartLoadCase"],
        "_6927": ["PartToPartShearCouplingConnectionLoadCase"],
        "_6928": ["PartToPartShearCouplingHalfLoadCase"],
        "_6929": ["PartToPartShearCouplingLoadCase"],
        "_6930": ["PlanetaryConnectionLoadCase"],
        "_6931": ["PlanetaryGearSetLoadCase"],
        "_6932": ["PlanetarySocketManufactureError"],
        "_6933": ["PlanetCarrierLoadCase"],
        "_6934": ["PlanetManufactureError"],
        "_6935": ["PointLoadHarmonicLoadData"],
        "_6936": ["PointLoadLoadCase"],
        "_6937": ["PowerLoadLoadCase"],
        "_6938": ["PulleyLoadCase"],
        "_6939": ["ResetMicroGeometryOptions"],
        "_6940": ["RingPinManufacturingError"],
        "_6941": ["RingPinsLoadCase"],
        "_6942": ["RingPinsToDiscConnectionLoadCase"],
        "_6943": ["RollingRingAssemblyLoadCase"],
        "_6944": ["RollingRingConnectionLoadCase"],
        "_6945": ["RollingRingLoadCase"],
        "_6946": ["RootAssemblyLoadCase"],
        "_6947": ["ShaftHubConnectionLoadCase"],
        "_6948": ["ShaftLoadCase"],
        "_6949": ["ShaftToMountableComponentConnectionLoadCase"],
        "_6950": ["SpecialisedAssemblyLoadCase"],
        "_6951": ["SpiralBevelGearLoadCase"],
        "_6952": ["SpiralBevelGearMeshLoadCase"],
        "_6953": ["SpiralBevelGearSetLoadCase"],
        "_6954": ["SpringDamperConnectionLoadCase"],
        "_6955": ["SpringDamperHalfLoadCase"],
        "_6956": ["SpringDamperLoadCase"],
        "_6957": ["StraightBevelDiffGearLoadCase"],
        "_6958": ["StraightBevelDiffGearMeshLoadCase"],
        "_6959": ["StraightBevelDiffGearSetLoadCase"],
        "_6960": ["StraightBevelGearLoadCase"],
        "_6961": ["StraightBevelGearMeshLoadCase"],
        "_6962": ["StraightBevelGearSetLoadCase"],
        "_6963": ["StraightBevelPlanetGearLoadCase"],
        "_6964": ["StraightBevelSunGearLoadCase"],
        "_6965": ["SynchroniserHalfLoadCase"],
        "_6966": ["SynchroniserLoadCase"],
        "_6967": ["SynchroniserPartLoadCase"],
        "_6968": ["SynchroniserSleeveLoadCase"],
        "_6969": ["TEExcitationType"],
        "_6970": ["TorqueConverterConnectionLoadCase"],
        "_6971": ["TorqueConverterLoadCase"],
        "_6972": ["TorqueConverterPumpLoadCase"],
        "_6973": ["TorqueConverterTurbineLoadCase"],
        "_6974": ["TorqueRippleInputType"],
        "_6975": ["TorqueSpecificationForSystemDeflection"],
        "_6976": ["TransmissionEfficiencySettings"],
        "_6977": ["UnbalancedMassHarmonicLoadData"],
        "_6978": ["UnbalancedMassLoadCase"],
        "_6979": ["VirtualComponentLoadCase"],
        "_6980": ["WormGearLoadCase"],
        "_6981": ["WormGearMeshLoadCase"],
        "_6982": ["WormGearSetLoadCase"],
        "_6983": ["ZerolBevelGearLoadCase"],
        "_6984": ["ZerolBevelGearMeshLoadCase"],
        "_6985": ["ZerolBevelGearSetLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LoadCase",
    "StaticLoadCase",
    "TimeSeriesLoadCase",
    "AbstractAssemblyLoadCase",
    "AbstractShaftLoadCase",
    "AbstractShaftOrHousingLoadCase",
    "AbstractShaftToMountableComponentConnectionLoadCase",
    "AdditionalAccelerationOptions",
    "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
    "AdvancedTimeSteppingAnalysisForModulationType",
    "AGMAGleasonConicalGearLoadCase",
    "AGMAGleasonConicalGearMeshLoadCase",
    "AGMAGleasonConicalGearSetLoadCase",
    "AllRingPinsManufacturingError",
    "AnalysisType",
    "AssemblyLoadCase",
    "BearingLoadCase",
    "BeltConnectionLoadCase",
    "BeltDriveLoadCase",
    "BevelDifferentialGearLoadCase",
    "BevelDifferentialGearMeshLoadCase",
    "BevelDifferentialGearSetLoadCase",
    "BevelDifferentialPlanetGearLoadCase",
    "BevelDifferentialSunGearLoadCase",
    "BevelGearLoadCase",
    "BevelGearMeshLoadCase",
    "BevelGearSetLoadCase",
    "BoltedJointLoadCase",
    "BoltLoadCase",
    "ClutchConnectionLoadCase",
    "ClutchHalfLoadCase",
    "ClutchLoadCase",
    "CMSElementFaceGroupWithSelectionOption",
    "CoaxialConnectionLoadCase",
    "ComponentLoadCase",
    "ConceptCouplingConnectionLoadCase",
    "ConceptCouplingHalfLoadCase",
    "ConceptCouplingLoadCase",
    "ConceptGearLoadCase",
    "ConceptGearMeshLoadCase",
    "ConceptGearSetLoadCase",
    "ConicalGearLoadCase",
    "ConicalGearManufactureError",
    "ConicalGearMeshLoadCase",
    "ConicalGearSetHarmonicLoadData",
    "ConicalGearSetLoadCase",
    "ConnectionLoadCase",
    "ConnectorLoadCase",
    "CouplingConnectionLoadCase",
    "CouplingHalfLoadCase",
    "CouplingLoadCase",
    "CVTBeltConnectionLoadCase",
    "CVTLoadCase",
    "CVTPulleyLoadCase",
    "CycloidalAssemblyLoadCase",
    "CycloidalDiscCentralBearingConnectionLoadCase",
    "CycloidalDiscLoadCase",
    "CycloidalDiscPlanetaryBearingConnectionLoadCase",
    "CylindricalGearLoadCase",
    "CylindricalGearManufactureError",
    "CylindricalGearMeshLoadCase",
    "CylindricalGearSetHarmonicLoadData",
    "CylindricalGearSetLoadCase",
    "CylindricalPlanetGearLoadCase",
    "DataFromMotorPackagePerMeanTorque",
    "DataFromMotorPackagePerSpeed",
    "DatumLoadCase",
    "ElectricMachineDataImportType",
    "ElectricMachineHarmonicLoadData",
    "ElectricMachineHarmonicLoadDataFromExcel",
    "ElectricMachineHarmonicLoadDataFromFlux",
    "ElectricMachineHarmonicLoadDataFromJMAG",
    "ElectricMachineHarmonicLoadDataFromMASTA",
    "ElectricMachineHarmonicLoadDataFromMotorCAD",
    "ElectricMachineHarmonicLoadDataFromMotorPackages",
    "ElectricMachineHarmonicLoadExcelImportOptions",
    "ElectricMachineHarmonicLoadFluxImportOptions",
    "ElectricMachineHarmonicLoadImportOptionsBase",
    "ElectricMachineHarmonicLoadJMAGImportOptions",
    "ElectricMachineHarmonicLoadMotorCADImportOptions",
    "ExternalCADModelLoadCase",
    "FaceGearLoadCase",
    "FaceGearMeshLoadCase",
    "FaceGearSetLoadCase",
    "FEPartLoadCase",
    "FlexiblePinAssemblyLoadCase",
    "ForceAndTorqueScalingFactor",
    "GearLoadCase",
    "GearManufactureError",
    "GearMeshLoadCase",
    "GearMeshTEOrderType",
    "GearSetHarmonicLoadData",
    "GearSetLoadCase",
    "GuideDxfModelLoadCase",
    "HarmonicExcitationType",
    "HarmonicLoadDataCSVImport",
    "HarmonicLoadDataExcelImport",
    "HarmonicLoadDataFluxImport",
    "HarmonicLoadDataImportBase",
    "HarmonicLoadDataImportFromMotorPackages",
    "HarmonicLoadDataJMAGImport",
    "HarmonicLoadDataMotorCADImport",
    "HypoidGearLoadCase",
    "HypoidGearMeshLoadCase",
    "HypoidGearSetLoadCase",
    "ImportType",
    "InformationAtRingPinToDiscContactPointFromGeometry",
    "InnerDiameterReference",
    "InterMountableComponentConnectionLoadCase",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
    "KlingelnbergCycloPalloidConicalGearMeshLoadCase",
    "KlingelnbergCycloPalloidConicalGearSetLoadCase",
    "KlingelnbergCycloPalloidHypoidGearLoadCase",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
    "MassDiscLoadCase",
    "MeasurementComponentLoadCase",
    "MeshStiffnessSource",
    "MountableComponentLoadCase",
    "NamedSpeed",
    "OilSealLoadCase",
    "ParametricStudyType",
    "PartLoadCase",
    "PartToPartShearCouplingConnectionLoadCase",
    "PartToPartShearCouplingHalfLoadCase",
    "PartToPartShearCouplingLoadCase",
    "PlanetaryConnectionLoadCase",
    "PlanetaryGearSetLoadCase",
    "PlanetarySocketManufactureError",
    "PlanetCarrierLoadCase",
    "PlanetManufactureError",
    "PointLoadHarmonicLoadData",
    "PointLoadLoadCase",
    "PowerLoadLoadCase",
    "PulleyLoadCase",
    "ResetMicroGeometryOptions",
    "RingPinManufacturingError",
    "RingPinsLoadCase",
    "RingPinsToDiscConnectionLoadCase",
    "RollingRingAssemblyLoadCase",
    "RollingRingConnectionLoadCase",
    "RollingRingLoadCase",
    "RootAssemblyLoadCase",
    "ShaftHubConnectionLoadCase",
    "ShaftLoadCase",
    "ShaftToMountableComponentConnectionLoadCase",
    "SpecialisedAssemblyLoadCase",
    "SpiralBevelGearLoadCase",
    "SpiralBevelGearMeshLoadCase",
    "SpiralBevelGearSetLoadCase",
    "SpringDamperConnectionLoadCase",
    "SpringDamperHalfLoadCase",
    "SpringDamperLoadCase",
    "StraightBevelDiffGearLoadCase",
    "StraightBevelDiffGearMeshLoadCase",
    "StraightBevelDiffGearSetLoadCase",
    "StraightBevelGearLoadCase",
    "StraightBevelGearMeshLoadCase",
    "StraightBevelGearSetLoadCase",
    "StraightBevelPlanetGearLoadCase",
    "StraightBevelSunGearLoadCase",
    "SynchroniserHalfLoadCase",
    "SynchroniserLoadCase",
    "SynchroniserPartLoadCase",
    "SynchroniserSleeveLoadCase",
    "TEExcitationType",
    "TorqueConverterConnectionLoadCase",
    "TorqueConverterLoadCase",
    "TorqueConverterPumpLoadCase",
    "TorqueConverterTurbineLoadCase",
    "TorqueRippleInputType",
    "TorqueSpecificationForSystemDeflection",
    "TransmissionEfficiencySettings",
    "UnbalancedMassHarmonicLoadData",
    "UnbalancedMassLoadCase",
    "VirtualComponentLoadCase",
    "WormGearLoadCase",
    "WormGearMeshLoadCase",
    "WormGearSetLoadCase",
    "ZerolBevelGearLoadCase",
    "ZerolBevelGearMeshLoadCase",
    "ZerolBevelGearSetLoadCase",
)
