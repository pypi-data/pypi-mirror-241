"""MountableComponentSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3268,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "MountableComponentSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="MountableComponentSteadyStateSynchronousResponseOnAShaft")


class MountableComponentSteadyStateSynchronousResponseOnAShaft(
    _3268.ComponentSteadyStateSynchronousResponseOnAShaft
):
    """MountableComponentSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting MountableComponentSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
            parent: "MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3268.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(_3322.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3249,
            )

            return self._parent._cast(
                _3249.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3251,
            )

            return self._parent._cast(
                _3251.BearingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3256,
            )

            return self._parent._cast(
                _3256.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3257,
            )

            return self._parent._cast(
                _3257.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3258,
            )

            return self._parent._cast(
                _3258.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3261,
            )

            return self._parent._cast(
                _3261.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3265,
            )

            return self._parent._cast(
                _3265.ClutchHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3274,
            )

            return self._parent._cast(
                _3274.ConceptGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3277,
            )

            return self._parent._cast(
                _3277.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3279,
            )

            return self._parent._cast(
                _3279.ConnectorSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3281,
            )

            return self._parent._cast(
                _3281.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3284,
            )

            return self._parent._cast(
                _3284.CVTPulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3292,
            )

            return self._parent._cast(
                _3292.CylindricalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3293,
            )

            return self._parent._cast(
                _3293.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3298,
            )

            return self._parent._cast(
                _3298.FaceGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3303,
            )

            return self._parent._cast(_3303.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(
                _3307.HypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3311,
            )

            return self._parent._cast(
                _3311.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3314,
            )

            return self._parent._cast(
                _3314.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3317,
            )

            return self._parent._cast(
                _3317.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.MassDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3319,
            )

            return self._parent._cast(
                _3319.MeasurementComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(
                _3321.OilSealSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3328,
            )

            return self._parent._cast(
                _3328.PlanetCarrierSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3329,
            )

            return self._parent._cast(
                _3329.PointLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3330,
            )

            return self._parent._cast(
                _3330.PowerLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3331,
            )

            return self._parent._cast(
                _3331.PulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(
                _3332.RingPinsSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3336,
            )

            return self._parent._cast(
                _3336.RollingRingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3338,
            )

            return self._parent._cast(
                _3338.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3344,
            )

            return self._parent._cast(
                _3344.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3346,
            )

            return self._parent._cast(
                _3346.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3351,
            )

            return self._parent._cast(
                _3351.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3354,
            )

            return self._parent._cast(
                _3354.StraightBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3355,
            )

            return self._parent._cast(
                _3355.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3356,
            )

            return self._parent._cast(
                _3356.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3357,
            )

            return self._parent._cast(
                _3357.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3358,
            )

            return self._parent._cast(
                _3358.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3359,
            )

            return self._parent._cast(
                _3359.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3362,
            )

            return self._parent._cast(
                _3362.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3364,
            )

            return self._parent._cast(
                _3364.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3365,
            )

            return self._parent._cast(
                _3365.UnbalancedMassSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3366,
            )

            return self._parent._cast(
                _3366.VirtualComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3369,
            )

            return self._parent._cast(
                _3369.WormGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3372,
            )

            return self._parent._cast(
                _3372.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "MountableComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "MountableComponentSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_MountableComponentSteadyStateSynchronousResponseOnAShaft(self)
