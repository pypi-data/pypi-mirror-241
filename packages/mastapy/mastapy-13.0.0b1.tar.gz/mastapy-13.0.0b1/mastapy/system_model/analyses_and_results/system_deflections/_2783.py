"""PartSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PartSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.math_utility import _1515
    from mastapy.system_model.analyses_and_results.system_deflections import _2823
    from mastapy.system_model.analyses_and_results.power_flows import _4111
    from mastapy.system_model.drawing import _2258


__docformat__ = "restructuredtext en"
__all__ = ("PartSystemDeflection",)


Self = TypeVar("Self", bound="PartSystemDeflection")


class PartSystemDeflection(_7544.PartFEAnalysis):
    """PartSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartSystemDeflection")

    class _Cast_PartSystemDeflection:
        """Special nested class for casting PartSystemDeflection to subclasses."""

        def __init__(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
            parent: "PartSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_fe_analysis(self: "PartSystemDeflection._Cast_PartSystemDeflection"):
            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "PartSystemDeflection._Cast_PartSystemDeflection"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "PartSystemDeflection._Cast_PartSystemDeflection"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2683,
            )

            return self._parent._cast(_2683.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2684,
            )

            return self._parent._cast(_2684.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2685,
            )

            return self._parent._cast(_2685.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2690,
            )

            return self._parent._cast(_2690.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2696,
            )

            return self._parent._cast(_2696.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2698,
            )

            return self._parent._cast(_2698.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2703,
            )

            return self._parent._cast(_2703.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.ClutchSystemDeflection)

        @property
        def component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(
                _2742.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(
                _2745.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(_2755.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.GearSetSystemDeflection)

        @property
        def gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2760,
            )

            return self._parent._cast(_2760.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(
                _2768.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(
                _2771.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(
                _2774.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(_2777.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(_2778.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.OilSealSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(_2789.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(_2791.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(_2797.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(_2798.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.ZerolBevelGearSystemDeflection)

        @property
        def part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "PartSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartSystemDeflection._Cast_PartSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_axial_forces(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingAxialForces

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def two_d_drawing_showing_power_flow(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2466.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_from_node_model(self: Self) -> "_1515.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromNodeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection(self: Self) -> "_2823.SystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4111.PartPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PartPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2258.SystemDeflectionViewable":
        """mastapy.system_model.drawing.SystemDeflectionViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartSystemDeflection._Cast_PartSystemDeflection":
        return self._Cast_PartSystemDeflection(self)
