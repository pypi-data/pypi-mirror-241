"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2574 import BeltDrive
    from ._2575 import BeltDriveType
    from ._2576 import Clutch
    from ._2577 import ClutchHalf
    from ._2578 import ClutchType
    from ._2579 import ConceptCoupling
    from ._2580 import ConceptCouplingHalf
    from ._2581 import Coupling
    from ._2582 import CouplingHalf
    from ._2583 import CrowningSpecification
    from ._2584 import CVT
    from ._2585 import CVTPulley
    from ._2586 import PartToPartShearCoupling
    from ._2587 import PartToPartShearCouplingHalf
    from ._2588 import Pulley
    from ._2589 import RigidConnectorStiffnessType
    from ._2590 import RigidConnectorTiltStiffnessTypes
    from ._2591 import RigidConnectorToothLocation
    from ._2592 import RigidConnectorToothSpacingType
    from ._2593 import RigidConnectorTypes
    from ._2594 import RollingRing
    from ._2595 import RollingRingAssembly
    from ._2596 import ShaftHubConnection
    from ._2597 import SplineLeadRelief
    from ._2598 import SpringDamper
    from ._2599 import SpringDamperHalf
    from ._2600 import Synchroniser
    from ._2601 import SynchroniserCone
    from ._2602 import SynchroniserHalf
    from ._2603 import SynchroniserPart
    from ._2604 import SynchroniserSleeve
    from ._2605 import TorqueConverter
    from ._2606 import TorqueConverterPump
    from ._2607 import TorqueConverterSpeedRatio
    from ._2608 import TorqueConverterTurbine
else:
    import_structure = {
        "_2574": ["BeltDrive"],
        "_2575": ["BeltDriveType"],
        "_2576": ["Clutch"],
        "_2577": ["ClutchHalf"],
        "_2578": ["ClutchType"],
        "_2579": ["ConceptCoupling"],
        "_2580": ["ConceptCouplingHalf"],
        "_2581": ["Coupling"],
        "_2582": ["CouplingHalf"],
        "_2583": ["CrowningSpecification"],
        "_2584": ["CVT"],
        "_2585": ["CVTPulley"],
        "_2586": ["PartToPartShearCoupling"],
        "_2587": ["PartToPartShearCouplingHalf"],
        "_2588": ["Pulley"],
        "_2589": ["RigidConnectorStiffnessType"],
        "_2590": ["RigidConnectorTiltStiffnessTypes"],
        "_2591": ["RigidConnectorToothLocation"],
        "_2592": ["RigidConnectorToothSpacingType"],
        "_2593": ["RigidConnectorTypes"],
        "_2594": ["RollingRing"],
        "_2595": ["RollingRingAssembly"],
        "_2596": ["ShaftHubConnection"],
        "_2597": ["SplineLeadRelief"],
        "_2598": ["SpringDamper"],
        "_2599": ["SpringDamperHalf"],
        "_2600": ["Synchroniser"],
        "_2601": ["SynchroniserCone"],
        "_2602": ["SynchroniserHalf"],
        "_2603": ["SynchroniserPart"],
        "_2604": ["SynchroniserSleeve"],
        "_2605": ["TorqueConverter"],
        "_2606": ["TorqueConverterPump"],
        "_2607": ["TorqueConverterSpeedRatio"],
        "_2608": ["TorqueConverterTurbine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltDrive",
    "BeltDriveType",
    "Clutch",
    "ClutchHalf",
    "ClutchType",
    "ConceptCoupling",
    "ConceptCouplingHalf",
    "Coupling",
    "CouplingHalf",
    "CrowningSpecification",
    "CVT",
    "CVTPulley",
    "PartToPartShearCoupling",
    "PartToPartShearCouplingHalf",
    "Pulley",
    "RigidConnectorStiffnessType",
    "RigidConnectorTiltStiffnessTypes",
    "RigidConnectorToothLocation",
    "RigidConnectorToothSpacingType",
    "RigidConnectorTypes",
    "RollingRing",
    "RollingRingAssembly",
    "ShaftHubConnection",
    "SplineLeadRelief",
    "SpringDamper",
    "SpringDamperHalf",
    "Synchroniser",
    "SynchroniserCone",
    "SynchroniserHalf",
    "SynchroniserPart",
    "SynchroniserSleeve",
    "TorqueConverter",
    "TorqueConverterPump",
    "TorqueConverterSpeedRatio",
    "TorqueConverterTurbine",
)
