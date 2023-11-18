"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._607 import CutterFlankSections
    from ._608 import CylindricalCutterDatabase
    from ._609 import CylindricalGearBlank
    from ._610 import CylindricalGearManufacturingConfig
    from ._611 import CylindricalGearSpecifiedMicroGeometry
    from ._612 import CylindricalGearSpecifiedProfile
    from ._613 import CylindricalHobDatabase
    from ._614 import CylindricalManufacturedGearDutyCycle
    from ._615 import CylindricalManufacturedGearLoadCase
    from ._616 import CylindricalManufacturedGearMeshDutyCycle
    from ._617 import CylindricalManufacturedGearMeshLoadCase
    from ._618 import CylindricalManufacturedGearSetDutyCycle
    from ._619 import CylindricalManufacturedGearSetLoadCase
    from ._620 import CylindricalMeshManufacturingConfig
    from ._621 import CylindricalMftFinishingMethods
    from ._622 import CylindricalMftRoughingMethods
    from ._623 import CylindricalSetManufacturingConfig
    from ._624 import CylindricalShaperDatabase
    from ._625 import Flank
    from ._626 import GearManufacturingConfigurationViewModel
    from ._627 import GearManufacturingConfigurationViewModelPlaceholder
    from ._628 import GearSetConfigViewModel
    from ._629 import HobEdgeTypes
    from ._630 import LeadModificationSegment
    from ._631 import MicroGeometryInputs
    from ._632 import MicroGeometryInputsLead
    from ._633 import MicroGeometryInputsProfile
    from ._634 import ModificationSegment
    from ._635 import ProfileModificationSegment
    from ._636 import SuitableCutterSetup
else:
    import_structure = {
        "_607": ["CutterFlankSections"],
        "_608": ["CylindricalCutterDatabase"],
        "_609": ["CylindricalGearBlank"],
        "_610": ["CylindricalGearManufacturingConfig"],
        "_611": ["CylindricalGearSpecifiedMicroGeometry"],
        "_612": ["CylindricalGearSpecifiedProfile"],
        "_613": ["CylindricalHobDatabase"],
        "_614": ["CylindricalManufacturedGearDutyCycle"],
        "_615": ["CylindricalManufacturedGearLoadCase"],
        "_616": ["CylindricalManufacturedGearMeshDutyCycle"],
        "_617": ["CylindricalManufacturedGearMeshLoadCase"],
        "_618": ["CylindricalManufacturedGearSetDutyCycle"],
        "_619": ["CylindricalManufacturedGearSetLoadCase"],
        "_620": ["CylindricalMeshManufacturingConfig"],
        "_621": ["CylindricalMftFinishingMethods"],
        "_622": ["CylindricalMftRoughingMethods"],
        "_623": ["CylindricalSetManufacturingConfig"],
        "_624": ["CylindricalShaperDatabase"],
        "_625": ["Flank"],
        "_626": ["GearManufacturingConfigurationViewModel"],
        "_627": ["GearManufacturingConfigurationViewModelPlaceholder"],
        "_628": ["GearSetConfigViewModel"],
        "_629": ["HobEdgeTypes"],
        "_630": ["LeadModificationSegment"],
        "_631": ["MicroGeometryInputs"],
        "_632": ["MicroGeometryInputsLead"],
        "_633": ["MicroGeometryInputsProfile"],
        "_634": ["ModificationSegment"],
        "_635": ["ProfileModificationSegment"],
        "_636": ["SuitableCutterSetup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterFlankSections",
    "CylindricalCutterDatabase",
    "CylindricalGearBlank",
    "CylindricalGearManufacturingConfig",
    "CylindricalGearSpecifiedMicroGeometry",
    "CylindricalGearSpecifiedProfile",
    "CylindricalHobDatabase",
    "CylindricalManufacturedGearDutyCycle",
    "CylindricalManufacturedGearLoadCase",
    "CylindricalManufacturedGearMeshDutyCycle",
    "CylindricalManufacturedGearMeshLoadCase",
    "CylindricalManufacturedGearSetDutyCycle",
    "CylindricalManufacturedGearSetLoadCase",
    "CylindricalMeshManufacturingConfig",
    "CylindricalMftFinishingMethods",
    "CylindricalMftRoughingMethods",
    "CylindricalSetManufacturingConfig",
    "CylindricalShaperDatabase",
    "Flank",
    "GearManufacturingConfigurationViewModel",
    "GearManufacturingConfigurationViewModelPlaceholder",
    "GearSetConfigViewModel",
    "HobEdgeTypes",
    "LeadModificationSegment",
    "MicroGeometryInputs",
    "MicroGeometryInputsLead",
    "MicroGeometryInputsProfile",
    "ModificationSegment",
    "ProfileModificationSegment",
    "SuitableCutterSetup",
)
