"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2416 import FELink
    from ._2417 import ElectricMachineStatorFELink
    from ._2418 import FELinkWithSelection
    from ._2419 import GearMeshFELink
    from ._2420 import GearWithDuplicatedMeshesFELink
    from ._2421 import MultiAngleConnectionFELink
    from ._2422 import MultiNodeConnectorFELink
    from ._2423 import MultiNodeFELink
    from ._2424 import PlanetaryConnectorMultiNodeFELink
    from ._2425 import PlanetBasedFELink
    from ._2426 import PlanetCarrierFELink
    from ._2427 import PointLoadFELink
    from ._2428 import RollingRingConnectionFELink
    from ._2429 import ShaftHubConnectionFELink
    from ._2430 import SingleNodeFELink
else:
    import_structure = {
        "_2416": ["FELink"],
        "_2417": ["ElectricMachineStatorFELink"],
        "_2418": ["FELinkWithSelection"],
        "_2419": ["GearMeshFELink"],
        "_2420": ["GearWithDuplicatedMeshesFELink"],
        "_2421": ["MultiAngleConnectionFELink"],
        "_2422": ["MultiNodeConnectorFELink"],
        "_2423": ["MultiNodeFELink"],
        "_2424": ["PlanetaryConnectorMultiNodeFELink"],
        "_2425": ["PlanetBasedFELink"],
        "_2426": ["PlanetCarrierFELink"],
        "_2427": ["PointLoadFELink"],
        "_2428": ["RollingRingConnectionFELink"],
        "_2429": ["ShaftHubConnectionFELink"],
        "_2430": ["SingleNodeFELink"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FELink",
    "ElectricMachineStatorFELink",
    "FELinkWithSelection",
    "GearMeshFELink",
    "GearWithDuplicatedMeshesFELink",
    "MultiAngleConnectionFELink",
    "MultiNodeConnectorFELink",
    "MultiNodeFELink",
    "PlanetaryConnectorMultiNodeFELink",
    "PlanetBasedFELink",
    "PlanetCarrierFELink",
    "PointLoadFELink",
    "RollingRingConnectionFELink",
    "ShaftHubConnectionFELink",
    "SingleNodeFELink",
)
