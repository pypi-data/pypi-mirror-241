"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2340 import ClutchConnection
    from ._2341 import ClutchSocket
    from ._2342 import ConceptCouplingConnection
    from ._2343 import ConceptCouplingSocket
    from ._2344 import CouplingConnection
    from ._2345 import CouplingSocket
    from ._2346 import PartToPartShearCouplingConnection
    from ._2347 import PartToPartShearCouplingSocket
    from ._2348 import SpringDamperConnection
    from ._2349 import SpringDamperSocket
    from ._2350 import TorqueConverterConnection
    from ._2351 import TorqueConverterPumpSocket
    from ._2352 import TorqueConverterTurbineSocket
else:
    import_structure = {
        "_2340": ["ClutchConnection"],
        "_2341": ["ClutchSocket"],
        "_2342": ["ConceptCouplingConnection"],
        "_2343": ["ConceptCouplingSocket"],
        "_2344": ["CouplingConnection"],
        "_2345": ["CouplingSocket"],
        "_2346": ["PartToPartShearCouplingConnection"],
        "_2347": ["PartToPartShearCouplingSocket"],
        "_2348": ["SpringDamperConnection"],
        "_2349": ["SpringDamperSocket"],
        "_2350": ["TorqueConverterConnection"],
        "_2351": ["TorqueConverterPumpSocket"],
        "_2352": ["TorqueConverterTurbineSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ClutchConnection",
    "ClutchSocket",
    "ConceptCouplingConnection",
    "ConceptCouplingSocket",
    "CouplingConnection",
    "CouplingSocket",
    "PartToPartShearCouplingConnection",
    "PartToPartShearCouplingSocket",
    "SpringDamperConnection",
    "SpringDamperSocket",
    "TorqueConverterConnection",
    "TorqueConverterPumpSocket",
    "TorqueConverterTurbineSocket",
)
