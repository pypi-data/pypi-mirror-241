"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2263 import AbstractShaftToMountableComponentConnection
    from ._2264 import BearingInnerSocket
    from ._2265 import BearingOuterSocket
    from ._2266 import BeltConnection
    from ._2267 import CoaxialConnection
    from ._2268 import ComponentConnection
    from ._2269 import ComponentMeasurer
    from ._2270 import Connection
    from ._2271 import CVTBeltConnection
    from ._2272 import CVTPulleySocket
    from ._2273 import CylindricalComponentConnection
    from ._2274 import CylindricalSocket
    from ._2275 import DatumMeasurement
    from ._2276 import ElectricMachineStatorSocket
    from ._2277 import InnerShaftSocket
    from ._2278 import InnerShaftSocketBase
    from ._2279 import InterMountableComponentConnection
    from ._2280 import MountableComponentInnerSocket
    from ._2281 import MountableComponentOuterSocket
    from ._2282 import MountableComponentSocket
    from ._2283 import OuterShaftSocket
    from ._2284 import OuterShaftSocketBase
    from ._2285 import PlanetaryConnection
    from ._2286 import PlanetarySocket
    from ._2287 import PlanetarySocketBase
    from ._2288 import PulleySocket
    from ._2289 import RealignmentResult
    from ._2290 import RollingRingConnection
    from ._2291 import RollingRingSocket
    from ._2292 import ShaftSocket
    from ._2293 import ShaftToMountableComponentConnection
    from ._2294 import Socket
    from ._2295 import SocketConnectionOptions
    from ._2296 import SocketConnectionSelection
else:
    import_structure = {
        "_2263": ["AbstractShaftToMountableComponentConnection"],
        "_2264": ["BearingInnerSocket"],
        "_2265": ["BearingOuterSocket"],
        "_2266": ["BeltConnection"],
        "_2267": ["CoaxialConnection"],
        "_2268": ["ComponentConnection"],
        "_2269": ["ComponentMeasurer"],
        "_2270": ["Connection"],
        "_2271": ["CVTBeltConnection"],
        "_2272": ["CVTPulleySocket"],
        "_2273": ["CylindricalComponentConnection"],
        "_2274": ["CylindricalSocket"],
        "_2275": ["DatumMeasurement"],
        "_2276": ["ElectricMachineStatorSocket"],
        "_2277": ["InnerShaftSocket"],
        "_2278": ["InnerShaftSocketBase"],
        "_2279": ["InterMountableComponentConnection"],
        "_2280": ["MountableComponentInnerSocket"],
        "_2281": ["MountableComponentOuterSocket"],
        "_2282": ["MountableComponentSocket"],
        "_2283": ["OuterShaftSocket"],
        "_2284": ["OuterShaftSocketBase"],
        "_2285": ["PlanetaryConnection"],
        "_2286": ["PlanetarySocket"],
        "_2287": ["PlanetarySocketBase"],
        "_2288": ["PulleySocket"],
        "_2289": ["RealignmentResult"],
        "_2290": ["RollingRingConnection"],
        "_2291": ["RollingRingSocket"],
        "_2292": ["ShaftSocket"],
        "_2293": ["ShaftToMountableComponentConnection"],
        "_2294": ["Socket"],
        "_2295": ["SocketConnectionOptions"],
        "_2296": ["SocketConnectionSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftToMountableComponentConnection",
    "BearingInnerSocket",
    "BearingOuterSocket",
    "BeltConnection",
    "CoaxialConnection",
    "ComponentConnection",
    "ComponentMeasurer",
    "Connection",
    "CVTBeltConnection",
    "CVTPulleySocket",
    "CylindricalComponentConnection",
    "CylindricalSocket",
    "DatumMeasurement",
    "ElectricMachineStatorSocket",
    "InnerShaftSocket",
    "InnerShaftSocketBase",
    "InterMountableComponentConnection",
    "MountableComponentInnerSocket",
    "MountableComponentOuterSocket",
    "MountableComponentSocket",
    "OuterShaftSocket",
    "OuterShaftSocketBase",
    "PlanetaryConnection",
    "PlanetarySocket",
    "PlanetarySocketBase",
    "PulleySocket",
    "RealignmentResult",
    "RollingRingConnection",
    "RollingRingSocket",
    "ShaftSocket",
    "ShaftToMountableComponentConnection",
    "Socket",
    "SocketConnectionOptions",
    "SocketConnectionSelection",
)
