"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2491 import AbstractShaftFromCAD
    from ._2492 import ClutchFromCAD
    from ._2493 import ComponentFromCAD
    from ._2494 import ConceptBearingFromCAD
    from ._2495 import ConnectorFromCAD
    from ._2496 import CylindricalGearFromCAD
    from ._2497 import CylindricalGearInPlanetarySetFromCAD
    from ._2498 import CylindricalPlanetGearFromCAD
    from ._2499 import CylindricalRingGearFromCAD
    from ._2500 import CylindricalSunGearFromCAD
    from ._2501 import HousedOrMounted
    from ._2502 import MountableComponentFromCAD
    from ._2503 import PlanetShaftFromCAD
    from ._2504 import PulleyFromCAD
    from ._2505 import RigidConnectorFromCAD
    from ._2506 import RollingBearingFromCAD
    from ._2507 import ShaftFromCAD
else:
    import_structure = {
        "_2491": ["AbstractShaftFromCAD"],
        "_2492": ["ClutchFromCAD"],
        "_2493": ["ComponentFromCAD"],
        "_2494": ["ConceptBearingFromCAD"],
        "_2495": ["ConnectorFromCAD"],
        "_2496": ["CylindricalGearFromCAD"],
        "_2497": ["CylindricalGearInPlanetarySetFromCAD"],
        "_2498": ["CylindricalPlanetGearFromCAD"],
        "_2499": ["CylindricalRingGearFromCAD"],
        "_2500": ["CylindricalSunGearFromCAD"],
        "_2501": ["HousedOrMounted"],
        "_2502": ["MountableComponentFromCAD"],
        "_2503": ["PlanetShaftFromCAD"],
        "_2504": ["PulleyFromCAD"],
        "_2505": ["RigidConnectorFromCAD"],
        "_2506": ["RollingBearingFromCAD"],
        "_2507": ["ShaftFromCAD"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftFromCAD",
    "ClutchFromCAD",
    "ComponentFromCAD",
    "ConceptBearingFromCAD",
    "ConnectorFromCAD",
    "CylindricalGearFromCAD",
    "CylindricalGearInPlanetarySetFromCAD",
    "CylindricalPlanetGearFromCAD",
    "CylindricalRingGearFromCAD",
    "CylindricalSunGearFromCAD",
    "HousedOrMounted",
    "MountableComponentFromCAD",
    "PlanetShaftFromCAD",
    "PulleyFromCAD",
    "RigidConnectorFromCAD",
    "RollingBearingFromCAD",
    "ShaftFromCAD",
)
