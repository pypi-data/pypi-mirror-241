"""PartFEAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_FE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "PartFEAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("PartFEAnalysis",)


Self = TypeVar("Self", bound="PartFEAnalysis")


class PartFEAnalysis(_7545.PartStaticLoadAnalysisCase):
    """PartFEAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_FE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartFEAnalysis")

    class _Cast_PartFEAnalysis:
        """Special nested class for casting PartFEAnalysis to subclasses."""

        def __init__(
            self: "PartFEAnalysis._Cast_PartFEAnalysis", parent: "PartFEAnalysis"
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2683,
            )

            return self._parent._cast(_2683.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2684,
            )

            return self._parent._cast(_2684.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2685,
            )

            return self._parent._cast(_2685.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2690,
            )

            return self._parent._cast(_2690.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2696,
            )

            return self._parent._cast(_2696.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2698,
            )

            return self._parent._cast(_2698.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2703,
            )

            return self._parent._cast(_2703.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.ClutchSystemDeflection)

        @property
        def component_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(
                _2742.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(
                _2745.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(_2755.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.GearSetSystemDeflection)

        @property
        def gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2760,
            )

            return self._parent._cast(_2760.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(
                _2768.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(
                _2771.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(
                _2774.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(_2777.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(_2778.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.OilSealSystemDeflection)

        @property
        def part_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(_2789.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(_2791.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(_2797.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(_2798.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.ZerolBevelGearSystemDeflection)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6274

            return self._parent._cast(_6274.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6275

            return self._parent._cast(_6275.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276

            return self._parent._cast(_6276.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278

            return self._parent._cast(_6278.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280

            return self._parent._cast(_6280.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281

            return self._parent._cast(_6281.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(_6282.BearingDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284

            return self._parent._cast(_6284.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(_6288.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294

            return self._parent._cast(_6294.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297

            return self._parent._cast(_6297.ClutchHalfDynamicAnalysis)

        @property
        def component_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ComponentDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306

            return self._parent._cast(_6306.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConicalGearSetDynamicAnalysis)

        @property
        def connector_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ConnectorDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.CouplingHalfDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329

            return self._parent._cast(_6329.FaceGearDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(_6331.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.GearDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(_6340.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(
                _6342.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(
                _6344.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(
                _6345.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(
                _6347.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(
                _6348.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(
                _6350.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(_6351.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.OilSealDynamicAnalysis)

        @property
        def part_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(_6361.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(_6367.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(_6370.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372

            return self._parent._cast(_6372.ShaftHubConnectionDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(_6375.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.WormGearDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402

            return self._parent._cast(_6402.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.ZerolBevelGearSetDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "PartFEAnalysis":
            return self._parent

        def __getattr__(self: "PartFEAnalysis._Cast_PartFEAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartFEAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PartFEAnalysis._Cast_PartFEAnalysis":
        return self._Cast_PartFEAnalysis(self)
