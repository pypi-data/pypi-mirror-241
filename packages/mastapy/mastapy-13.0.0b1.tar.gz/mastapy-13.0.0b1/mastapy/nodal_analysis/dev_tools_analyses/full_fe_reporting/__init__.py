"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._202 import ContactPairReporting
    from ._203 import CoordinateSystemReporting
    from ._204 import DegreeOfFreedomType
    from ._205 import ElasticModulusOrthotropicComponents
    from ._206 import ElementDetailsForFEModel
    from ._207 import ElementPropertiesBase
    from ._208 import ElementPropertiesBeam
    from ._209 import ElementPropertiesInterface
    from ._210 import ElementPropertiesMass
    from ._211 import ElementPropertiesRigid
    from ._212 import ElementPropertiesShell
    from ._213 import ElementPropertiesSolid
    from ._214 import ElementPropertiesSpringDashpot
    from ._215 import ElementPropertiesWithMaterial
    from ._216 import MaterialPropertiesReporting
    from ._217 import NodeDetailsForFEModel
    from ._218 import PoissonRatioOrthotropicComponents
    from ._219 import RigidElementNodeDegreesOfFreedom
    from ._220 import ShearModulusOrthotropicComponents
    from ._221 import ThermalExpansionOrthotropicComponents
else:
    import_structure = {
        "_202": ["ContactPairReporting"],
        "_203": ["CoordinateSystemReporting"],
        "_204": ["DegreeOfFreedomType"],
        "_205": ["ElasticModulusOrthotropicComponents"],
        "_206": ["ElementDetailsForFEModel"],
        "_207": ["ElementPropertiesBase"],
        "_208": ["ElementPropertiesBeam"],
        "_209": ["ElementPropertiesInterface"],
        "_210": ["ElementPropertiesMass"],
        "_211": ["ElementPropertiesRigid"],
        "_212": ["ElementPropertiesShell"],
        "_213": ["ElementPropertiesSolid"],
        "_214": ["ElementPropertiesSpringDashpot"],
        "_215": ["ElementPropertiesWithMaterial"],
        "_216": ["MaterialPropertiesReporting"],
        "_217": ["NodeDetailsForFEModel"],
        "_218": ["PoissonRatioOrthotropicComponents"],
        "_219": ["RigidElementNodeDegreesOfFreedom"],
        "_220": ["ShearModulusOrthotropicComponents"],
        "_221": ["ThermalExpansionOrthotropicComponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactPairReporting",
    "CoordinateSystemReporting",
    "DegreeOfFreedomType",
    "ElasticModulusOrthotropicComponents",
    "ElementDetailsForFEModel",
    "ElementPropertiesBase",
    "ElementPropertiesBeam",
    "ElementPropertiesInterface",
    "ElementPropertiesMass",
    "ElementPropertiesRigid",
    "ElementPropertiesShell",
    "ElementPropertiesSolid",
    "ElementPropertiesSpringDashpot",
    "ElementPropertiesWithMaterial",
    "MaterialPropertiesReporting",
    "NodeDetailsForFEModel",
    "PoissonRatioOrthotropicComponents",
    "RigidElementNodeDegreesOfFreedom",
    "ShearModulusOrthotropicComponents",
    "ThermalExpansionOrthotropicComponents",
)
