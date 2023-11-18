"""MountableComponentSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3527,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "MountableComponentSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="MountableComponentSteadyStateSynchronousResponseAtASpeed")


class MountableComponentSteadyStateSynchronousResponseAtASpeed(
    _3527.ComponentSteadyStateSynchronousResponseAtASpeed
):
    """MountableComponentSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting MountableComponentSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
            parent: "MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3527.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(_3581.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3508,
            )

            return self._parent._cast(
                _3508.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3510,
            )

            return self._parent._cast(
                _3510.BearingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3515,
            )

            return self._parent._cast(
                _3515.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3516,
            )

            return self._parent._cast(
                _3516.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3517,
            )

            return self._parent._cast(
                _3517.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3520,
            )

            return self._parent._cast(
                _3520.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3524,
            )

            return self._parent._cast(
                _3524.ClutchHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3533,
            )

            return self._parent._cast(
                _3533.ConceptGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3536,
            )

            return self._parent._cast(
                _3536.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3538,
            )

            return self._parent._cast(
                _3538.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3543,
            )

            return self._parent._cast(
                _3543.CVTPulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3551,
            )

            return self._parent._cast(
                _3551.CylindricalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3557,
            )

            return self._parent._cast(
                _3557.FaceGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(_3562.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(
                _3566.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3570,
            )

            return self._parent._cast(
                _3570.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3573,
            )

            return self._parent._cast(
                _3573.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3576,
            )

            return self._parent._cast(
                _3576.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3577,
            )

            return self._parent._cast(
                _3577.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(
                _3580.OilSealSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(
                _3587.PlanetCarrierSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3588,
            )

            return self._parent._cast(
                _3588.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3590,
            )

            return self._parent._cast(
                _3590.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(
                _3591.RingPinsSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3595,
            )

            return self._parent._cast(
                _3595.RollingRingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3597,
            )

            return self._parent._cast(
                _3597.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3603,
            )

            return self._parent._cast(
                _3603.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3605,
            )

            return self._parent._cast(
                _3605.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3610,
            )

            return self._parent._cast(
                _3610.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3613,
            )

            return self._parent._cast(
                _3613.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3614,
            )

            return self._parent._cast(
                _3614.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3615,
            )

            return self._parent._cast(
                _3615.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3617,
            )

            return self._parent._cast(
                _3617.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3618,
            )

            return self._parent._cast(
                _3618.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3621,
            )

            return self._parent._cast(
                _3621.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3623,
            )

            return self._parent._cast(
                _3623.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3624,
            )

            return self._parent._cast(
                _3624.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3625,
            )

            return self._parent._cast(
                _3625.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3628,
            )

            return self._parent._cast(
                _3628.WormGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3631,
            )

            return self._parent._cast(
                _3631.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "MountableComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "MountableComponentSteadyStateSynchronousResponseAtASpeed.TYPE",
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
    ) -> "MountableComponentSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_MountableComponentSteadyStateSynchronousResponseAtASpeed(self)
