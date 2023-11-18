"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1610 import Acceleration
    from ._1611 import Angle
    from ._1612 import AnglePerUnitTemperature
    from ._1613 import AngleSmall
    from ._1614 import AngleVerySmall
    from ._1615 import AngularAcceleration
    from ._1616 import AngularCompliance
    from ._1617 import AngularJerk
    from ._1618 import AngularStiffness
    from ._1619 import AngularVelocity
    from ._1620 import Area
    from ._1621 import AreaSmall
    from ._1622 import CarbonEmissionFactor
    from ._1623 import CurrentDensity
    from ._1624 import CurrentPerLength
    from ._1625 import Cycles
    from ._1626 import Damage
    from ._1627 import DamageRate
    from ._1628 import DataSize
    from ._1629 import Decibel
    from ._1630 import Density
    from ._1631 import ElectricalResistance
    from ._1632 import ElectricalResistivity
    from ._1633 import ElectricCurrent
    from ._1634 import Energy
    from ._1635 import EnergyPerUnitArea
    from ._1636 import EnergyPerUnitAreaSmall
    from ._1637 import EnergySmall
    from ._1638 import Enum
    from ._1639 import FlowRate
    from ._1640 import Force
    from ._1641 import ForcePerUnitLength
    from ._1642 import ForcePerUnitPressure
    from ._1643 import ForcePerUnitTemperature
    from ._1644 import FractionMeasurementBase
    from ._1645 import FractionPerTemperature
    from ._1646 import Frequency
    from ._1647 import FuelConsumptionEngine
    from ._1648 import FuelEfficiencyVehicle
    from ._1649 import Gradient
    from ._1650 import HeatConductivity
    from ._1651 import HeatTransfer
    from ._1652 import HeatTransferCoefficientForPlasticGearTooth
    from ._1653 import HeatTransferResistance
    from ._1654 import Impulse
    from ._1655 import Index
    from ._1656 import Inductance
    from ._1657 import Integer
    from ._1658 import InverseShortLength
    from ._1659 import InverseShortTime
    from ._1660 import Jerk
    from ._1661 import KinematicViscosity
    from ._1662 import LengthLong
    from ._1663 import LengthMedium
    from ._1664 import LengthPerUnitTemperature
    from ._1665 import LengthShort
    from ._1666 import LengthToTheFourth
    from ._1667 import LengthVeryLong
    from ._1668 import LengthVeryShort
    from ._1669 import LengthVeryShortPerLengthShort
    from ._1670 import LinearAngularDamping
    from ._1671 import LinearAngularStiffnessCrossTerm
    from ._1672 import LinearDamping
    from ._1673 import LinearFlexibility
    from ._1674 import LinearStiffness
    from ._1675 import MagneticFieldStrength
    from ._1676 import MagneticFlux
    from ._1677 import MagneticFluxDensity
    from ._1678 import MagneticVectorPotential
    from ._1679 import MagnetomotiveForce
    from ._1680 import Mass
    from ._1681 import MassPerUnitLength
    from ._1682 import MassPerUnitTime
    from ._1683 import MomentOfInertia
    from ._1684 import MomentOfInertiaPerUnitLength
    from ._1685 import MomentPerUnitPressure
    from ._1686 import Number
    from ._1687 import Percentage
    from ._1688 import Power
    from ._1689 import PowerPerSmallArea
    from ._1690 import PowerPerUnitTime
    from ._1691 import PowerSmall
    from ._1692 import PowerSmallPerArea
    from ._1693 import PowerSmallPerMass
    from ._1694 import PowerSmallPerUnitAreaPerUnitTime
    from ._1695 import PowerSmallPerUnitTime
    from ._1696 import PowerSmallPerVolume
    from ._1697 import Pressure
    from ._1698 import PressurePerUnitTime
    from ._1699 import PressureVelocityProduct
    from ._1700 import PressureViscosityCoefficient
    from ._1701 import Price
    from ._1702 import PricePerUnitMass
    from ._1703 import QuadraticAngularDamping
    from ._1704 import QuadraticDrag
    from ._1705 import RescaledMeasurement
    from ._1706 import Rotatum
    from ._1707 import SafetyFactor
    from ._1708 import SpecificAcousticImpedance
    from ._1709 import SpecificHeat
    from ._1710 import SquareRootOfUnitForcePerUnitArea
    from ._1711 import StiffnessPerUnitFaceWidth
    from ._1712 import Stress
    from ._1713 import Temperature
    from ._1714 import TemperatureDifference
    from ._1715 import TemperaturePerUnitTime
    from ._1716 import Text
    from ._1717 import ThermalContactCoefficient
    from ._1718 import ThermalExpansionCoefficient
    from ._1719 import ThermoElasticFactor
    from ._1720 import Time
    from ._1721 import TimeShort
    from ._1722 import TimeVeryShort
    from ._1723 import Torque
    from ._1724 import TorqueConverterInverseK
    from ._1725 import TorqueConverterK
    from ._1726 import TorquePerCurrent
    from ._1727 import TorquePerSquareRootOfPower
    from ._1728 import TorquePerUnitTemperature
    from ._1729 import Velocity
    from ._1730 import VelocitySmall
    from ._1731 import Viscosity
    from ._1732 import Voltage
    from ._1733 import VoltagePerAngularVelocity
    from ._1734 import Volume
    from ._1735 import WearCoefficient
    from ._1736 import Yank
else:
    import_structure = {
        "_1610": ["Acceleration"],
        "_1611": ["Angle"],
        "_1612": ["AnglePerUnitTemperature"],
        "_1613": ["AngleSmall"],
        "_1614": ["AngleVerySmall"],
        "_1615": ["AngularAcceleration"],
        "_1616": ["AngularCompliance"],
        "_1617": ["AngularJerk"],
        "_1618": ["AngularStiffness"],
        "_1619": ["AngularVelocity"],
        "_1620": ["Area"],
        "_1621": ["AreaSmall"],
        "_1622": ["CarbonEmissionFactor"],
        "_1623": ["CurrentDensity"],
        "_1624": ["CurrentPerLength"],
        "_1625": ["Cycles"],
        "_1626": ["Damage"],
        "_1627": ["DamageRate"],
        "_1628": ["DataSize"],
        "_1629": ["Decibel"],
        "_1630": ["Density"],
        "_1631": ["ElectricalResistance"],
        "_1632": ["ElectricalResistivity"],
        "_1633": ["ElectricCurrent"],
        "_1634": ["Energy"],
        "_1635": ["EnergyPerUnitArea"],
        "_1636": ["EnergyPerUnitAreaSmall"],
        "_1637": ["EnergySmall"],
        "_1638": ["Enum"],
        "_1639": ["FlowRate"],
        "_1640": ["Force"],
        "_1641": ["ForcePerUnitLength"],
        "_1642": ["ForcePerUnitPressure"],
        "_1643": ["ForcePerUnitTemperature"],
        "_1644": ["FractionMeasurementBase"],
        "_1645": ["FractionPerTemperature"],
        "_1646": ["Frequency"],
        "_1647": ["FuelConsumptionEngine"],
        "_1648": ["FuelEfficiencyVehicle"],
        "_1649": ["Gradient"],
        "_1650": ["HeatConductivity"],
        "_1651": ["HeatTransfer"],
        "_1652": ["HeatTransferCoefficientForPlasticGearTooth"],
        "_1653": ["HeatTransferResistance"],
        "_1654": ["Impulse"],
        "_1655": ["Index"],
        "_1656": ["Inductance"],
        "_1657": ["Integer"],
        "_1658": ["InverseShortLength"],
        "_1659": ["InverseShortTime"],
        "_1660": ["Jerk"],
        "_1661": ["KinematicViscosity"],
        "_1662": ["LengthLong"],
        "_1663": ["LengthMedium"],
        "_1664": ["LengthPerUnitTemperature"],
        "_1665": ["LengthShort"],
        "_1666": ["LengthToTheFourth"],
        "_1667": ["LengthVeryLong"],
        "_1668": ["LengthVeryShort"],
        "_1669": ["LengthVeryShortPerLengthShort"],
        "_1670": ["LinearAngularDamping"],
        "_1671": ["LinearAngularStiffnessCrossTerm"],
        "_1672": ["LinearDamping"],
        "_1673": ["LinearFlexibility"],
        "_1674": ["LinearStiffness"],
        "_1675": ["MagneticFieldStrength"],
        "_1676": ["MagneticFlux"],
        "_1677": ["MagneticFluxDensity"],
        "_1678": ["MagneticVectorPotential"],
        "_1679": ["MagnetomotiveForce"],
        "_1680": ["Mass"],
        "_1681": ["MassPerUnitLength"],
        "_1682": ["MassPerUnitTime"],
        "_1683": ["MomentOfInertia"],
        "_1684": ["MomentOfInertiaPerUnitLength"],
        "_1685": ["MomentPerUnitPressure"],
        "_1686": ["Number"],
        "_1687": ["Percentage"],
        "_1688": ["Power"],
        "_1689": ["PowerPerSmallArea"],
        "_1690": ["PowerPerUnitTime"],
        "_1691": ["PowerSmall"],
        "_1692": ["PowerSmallPerArea"],
        "_1693": ["PowerSmallPerMass"],
        "_1694": ["PowerSmallPerUnitAreaPerUnitTime"],
        "_1695": ["PowerSmallPerUnitTime"],
        "_1696": ["PowerSmallPerVolume"],
        "_1697": ["Pressure"],
        "_1698": ["PressurePerUnitTime"],
        "_1699": ["PressureVelocityProduct"],
        "_1700": ["PressureViscosityCoefficient"],
        "_1701": ["Price"],
        "_1702": ["PricePerUnitMass"],
        "_1703": ["QuadraticAngularDamping"],
        "_1704": ["QuadraticDrag"],
        "_1705": ["RescaledMeasurement"],
        "_1706": ["Rotatum"],
        "_1707": ["SafetyFactor"],
        "_1708": ["SpecificAcousticImpedance"],
        "_1709": ["SpecificHeat"],
        "_1710": ["SquareRootOfUnitForcePerUnitArea"],
        "_1711": ["StiffnessPerUnitFaceWidth"],
        "_1712": ["Stress"],
        "_1713": ["Temperature"],
        "_1714": ["TemperatureDifference"],
        "_1715": ["TemperaturePerUnitTime"],
        "_1716": ["Text"],
        "_1717": ["ThermalContactCoefficient"],
        "_1718": ["ThermalExpansionCoefficient"],
        "_1719": ["ThermoElasticFactor"],
        "_1720": ["Time"],
        "_1721": ["TimeShort"],
        "_1722": ["TimeVeryShort"],
        "_1723": ["Torque"],
        "_1724": ["TorqueConverterInverseK"],
        "_1725": ["TorqueConverterK"],
        "_1726": ["TorquePerCurrent"],
        "_1727": ["TorquePerSquareRootOfPower"],
        "_1728": ["TorquePerUnitTemperature"],
        "_1729": ["Velocity"],
        "_1730": ["VelocitySmall"],
        "_1731": ["Viscosity"],
        "_1732": ["Voltage"],
        "_1733": ["VoltagePerAngularVelocity"],
        "_1734": ["Volume"],
        "_1735": ["WearCoefficient"],
        "_1736": ["Yank"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Acceleration",
    "Angle",
    "AnglePerUnitTemperature",
    "AngleSmall",
    "AngleVerySmall",
    "AngularAcceleration",
    "AngularCompliance",
    "AngularJerk",
    "AngularStiffness",
    "AngularVelocity",
    "Area",
    "AreaSmall",
    "CarbonEmissionFactor",
    "CurrentDensity",
    "CurrentPerLength",
    "Cycles",
    "Damage",
    "DamageRate",
    "DataSize",
    "Decibel",
    "Density",
    "ElectricalResistance",
    "ElectricalResistivity",
    "ElectricCurrent",
    "Energy",
    "EnergyPerUnitArea",
    "EnergyPerUnitAreaSmall",
    "EnergySmall",
    "Enum",
    "FlowRate",
    "Force",
    "ForcePerUnitLength",
    "ForcePerUnitPressure",
    "ForcePerUnitTemperature",
    "FractionMeasurementBase",
    "FractionPerTemperature",
    "Frequency",
    "FuelConsumptionEngine",
    "FuelEfficiencyVehicle",
    "Gradient",
    "HeatConductivity",
    "HeatTransfer",
    "HeatTransferCoefficientForPlasticGearTooth",
    "HeatTransferResistance",
    "Impulse",
    "Index",
    "Inductance",
    "Integer",
    "InverseShortLength",
    "InverseShortTime",
    "Jerk",
    "KinematicViscosity",
    "LengthLong",
    "LengthMedium",
    "LengthPerUnitTemperature",
    "LengthShort",
    "LengthToTheFourth",
    "LengthVeryLong",
    "LengthVeryShort",
    "LengthVeryShortPerLengthShort",
    "LinearAngularDamping",
    "LinearAngularStiffnessCrossTerm",
    "LinearDamping",
    "LinearFlexibility",
    "LinearStiffness",
    "MagneticFieldStrength",
    "MagneticFlux",
    "MagneticFluxDensity",
    "MagneticVectorPotential",
    "MagnetomotiveForce",
    "Mass",
    "MassPerUnitLength",
    "MassPerUnitTime",
    "MomentOfInertia",
    "MomentOfInertiaPerUnitLength",
    "MomentPerUnitPressure",
    "Number",
    "Percentage",
    "Power",
    "PowerPerSmallArea",
    "PowerPerUnitTime",
    "PowerSmall",
    "PowerSmallPerArea",
    "PowerSmallPerMass",
    "PowerSmallPerUnitAreaPerUnitTime",
    "PowerSmallPerUnitTime",
    "PowerSmallPerVolume",
    "Pressure",
    "PressurePerUnitTime",
    "PressureVelocityProduct",
    "PressureViscosityCoefficient",
    "Price",
    "PricePerUnitMass",
    "QuadraticAngularDamping",
    "QuadraticDrag",
    "RescaledMeasurement",
    "Rotatum",
    "SafetyFactor",
    "SpecificAcousticImpedance",
    "SpecificHeat",
    "SquareRootOfUnitForcePerUnitArea",
    "StiffnessPerUnitFaceWidth",
    "Stress",
    "Temperature",
    "TemperatureDifference",
    "TemperaturePerUnitTime",
    "Text",
    "ThermalContactCoefficient",
    "ThermalExpansionCoefficient",
    "ThermoElasticFactor",
    "Time",
    "TimeShort",
    "TimeVeryShort",
    "Torque",
    "TorqueConverterInverseK",
    "TorqueConverterK",
    "TorquePerCurrent",
    "TorquePerSquareRootOfPower",
    "TorquePerUnitTemperature",
    "Velocity",
    "VelocitySmall",
    "Viscosity",
    "Voltage",
    "VoltagePerAngularVelocity",
    "Volume",
    "WearCoefficient",
    "Yank",
)
