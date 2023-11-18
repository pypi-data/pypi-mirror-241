"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2198 import Design
    from ._2199 import ComponentDampingOption
    from ._2200 import ConceptCouplingSpeedRatioSpecificationMethod
    from ._2201 import DesignEntity
    from ._2202 import DesignEntityId
    from ._2203 import DesignSettings
    from ._2204 import DutyCycleImporter
    from ._2205 import DutyCycleImporterDesignEntityMatch
    from ._2206 import ElectricMachineGroup
    from ._2207 import ExternalFullFELoader
    from ._2208 import HypoidWindUpRemovalMethod
    from ._2209 import IncludeDutyCycleOption
    from ._2210 import MASTASettings
    from ._2211 import MemorySummary
    from ._2212 import MeshStiffnessModel
    from ._2213 import PlanetPinManufacturingErrorsCoordinateSystem
    from ._2214 import PowerLoadDragTorqueSpecificationMethod
    from ._2215 import PowerLoadInputTorqueSpecificationMethod
    from ._2216 import PowerLoadPIDControlSpeedInputType
    from ._2217 import PowerLoadType
    from ._2218 import RelativeComponentAlignment
    from ._2219 import RelativeOffsetOption
    from ._2220 import SystemReporting
    from ._2221 import ThermalExpansionOptionForGroundedNodes
    from ._2222 import TransmissionTemperatureSet
else:
    import_structure = {
        "_2198": ["Design"],
        "_2199": ["ComponentDampingOption"],
        "_2200": ["ConceptCouplingSpeedRatioSpecificationMethod"],
        "_2201": ["DesignEntity"],
        "_2202": ["DesignEntityId"],
        "_2203": ["DesignSettings"],
        "_2204": ["DutyCycleImporter"],
        "_2205": ["DutyCycleImporterDesignEntityMatch"],
        "_2206": ["ElectricMachineGroup"],
        "_2207": ["ExternalFullFELoader"],
        "_2208": ["HypoidWindUpRemovalMethod"],
        "_2209": ["IncludeDutyCycleOption"],
        "_2210": ["MASTASettings"],
        "_2211": ["MemorySummary"],
        "_2212": ["MeshStiffnessModel"],
        "_2213": ["PlanetPinManufacturingErrorsCoordinateSystem"],
        "_2214": ["PowerLoadDragTorqueSpecificationMethod"],
        "_2215": ["PowerLoadInputTorqueSpecificationMethod"],
        "_2216": ["PowerLoadPIDControlSpeedInputType"],
        "_2217": ["PowerLoadType"],
        "_2218": ["RelativeComponentAlignment"],
        "_2219": ["RelativeOffsetOption"],
        "_2220": ["SystemReporting"],
        "_2221": ["ThermalExpansionOptionForGroundedNodes"],
        "_2222": ["TransmissionTemperatureSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Design",
    "ComponentDampingOption",
    "ConceptCouplingSpeedRatioSpecificationMethod",
    "DesignEntity",
    "DesignEntityId",
    "DesignSettings",
    "DutyCycleImporter",
    "DutyCycleImporterDesignEntityMatch",
    "ElectricMachineGroup",
    "ExternalFullFELoader",
    "HypoidWindUpRemovalMethod",
    "IncludeDutyCycleOption",
    "MASTASettings",
    "MemorySummary",
    "MeshStiffnessModel",
    "PlanetPinManufacturingErrorsCoordinateSystem",
    "PowerLoadDragTorqueSpecificationMethod",
    "PowerLoadInputTorqueSpecificationMethod",
    "PowerLoadPIDControlSpeedInputType",
    "PowerLoadType",
    "RelativeComponentAlignment",
    "RelativeOffsetOption",
    "SystemReporting",
    "ThermalExpansionOptionForGroundedNodes",
    "TransmissionTemperatureSet",
)
