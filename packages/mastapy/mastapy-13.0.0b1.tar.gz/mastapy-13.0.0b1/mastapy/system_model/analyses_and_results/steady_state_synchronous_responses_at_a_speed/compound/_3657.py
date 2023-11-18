"""ComponentCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3711,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3527,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ComponentCompoundSteadyStateSynchronousResponseAtASpeed")


class ComponentCompoundSteadyStateSynchronousResponseAtASpeed(
    _3711.PartCompoundSteadyStateSynchronousResponseAtASpeed
):
    """ComponentCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ComponentCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3711.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3633,
            )

            return self._parent._cast(
                _3633.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3634,
            )

            return self._parent._cast(
                _3634.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3636,
            )

            return self._parent._cast(
                _3636.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3640,
            )

            return self._parent._cast(
                _3640.BearingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3643,
            )

            return self._parent._cast(
                _3643.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3646,
            )

            return self._parent._cast(
                _3646.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3647,
            )

            return self._parent._cast(
                _3647.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3648,
            )

            return self._parent._cast(
                _3648.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3651,
            )

            return self._parent._cast(
                _3651.BoltCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3655,
            )

            return self._parent._cast(
                _3655.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3660,
            )

            return self._parent._cast(
                _3660.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3661,
            )

            return self._parent._cast(
                _3661.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3664,
            )

            return self._parent._cast(
                _3664.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3668,
            )

            return self._parent._cast(
                _3668.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3671,
            )

            return self._parent._cast(
                _3671.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3674,
            )

            return self._parent._cast(
                _3674.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3677,
            )

            return self._parent._cast(
                _3677.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3679,
            )

            return self._parent._cast(
                _3679.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3682,
            )

            return self._parent._cast(
                _3682.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3683,
            )

            return self._parent._cast(
                _3683.DatumCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3684,
            )

            return self._parent._cast(
                _3684.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3685,
            )

            return self._parent._cast(
                _3685.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3688,
            )

            return self._parent._cast(
                _3688.FEPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3690,
            )

            return self._parent._cast(
                _3690.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3693,
            )

            return self._parent._cast(
                _3693.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3694,
            )

            return self._parent._cast(
                _3694.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3698,
            )

            return self._parent._cast(
                _3698.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3701,
            )

            return self._parent._cast(
                _3701.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3704,
            )

            return self._parent._cast(
                _3704.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3707,
            )

            return self._parent._cast(
                _3707.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3708,
            )

            return self._parent._cast(
                _3708.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3709,
            )

            return self._parent._cast(
                _3709.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3710,
            )

            return self._parent._cast(
                _3710.OilSealCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3714,
            )

            return self._parent._cast(
                _3714.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3717,
            )

            return self._parent._cast(
                _3717.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3718,
            )

            return self._parent._cast(
                _3718.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3719,
            )

            return self._parent._cast(
                _3719.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3720,
            )

            return self._parent._cast(
                _3720.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3724,
            )

            return self._parent._cast(
                _3724.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3727,
            )

            return self._parent._cast(
                _3727.ShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3728,
            )

            return self._parent._cast(
                _3728.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3731,
            )

            return self._parent._cast(
                _3731.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3737,
            )

            return self._parent._cast(
                _3737.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3740,
            )

            return self._parent._cast(
                _3740.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3743,
            )

            return self._parent._cast(
                _3743.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3744,
            )

            return self._parent._cast(
                _3744.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3746,
            )

            return self._parent._cast(
                _3746.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3747,
            )

            return self._parent._cast(
                _3747.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3748,
            )

            return self._parent._cast(
                _3748.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3751,
            )

            return self._parent._cast(
                _3751.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3752,
            )

            return self._parent._cast(
                _3752.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3753,
            )

            return self._parent._cast(
                _3753.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3754,
            )

            return self._parent._cast(
                _3754.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3755,
            )

            return self._parent._cast(
                _3755.WormGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3758,
            )

            return self._parent._cast(
                _3758.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ComponentCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3527.ComponentSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ComponentSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3527.ComponentSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ComponentSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ComponentCompoundSteadyStateSynchronousResponseAtASpeed(self)
