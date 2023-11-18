"""ConnectionCompoundAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7540
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "ConnectionCompoundAnalysis",
)


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundAnalysis",)


Self = TypeVar("Self", bound="ConnectionCompoundAnalysis")


class ConnectionCompoundAnalysis(_7540.DesignEntityCompoundAnalysis):
    """ConnectionCompoundAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCompoundAnalysis")

    class _Cast_ConnectionCompoundAnalysis:
        """Special nested class for casting ConnectionCompoundAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
            parent: "ConnectionCompoundAnalysis",
        ):
            self._parent = parent

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2852,
            )

            return self._parent._cast(
                _2852.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2854,
            )

            return self._parent._cast(
                _2854.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def belt_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2858,
            )

            return self._parent._cast(_2858.BeltConnectionCompoundSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2861,
            )

            return self._parent._cast(
                _2861.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2866,
            )

            return self._parent._cast(_2866.BevelGearMeshCompoundSystemDeflection)

        @property
        def clutch_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2871,
            )

            return self._parent._cast(_2871.ClutchConnectionCompoundSystemDeflection)

        @property
        def coaxial_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.CoaxialConnectionCompoundSystemDeflection)

        @property
        def concept_coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(
                _2876.ConceptCouplingConnectionCompoundSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(_2879.ConceptGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ConicalGearMeshCompoundSystemDeflection)

        @property
        def connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ConnectionCompoundSystemDeflection)

        @property
        def coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(_2887.CouplingConnectionCompoundSystemDeflection)

        @property
        def cvt_belt_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.CVTBeltConnectionCompoundSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(
                _2893.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(
                _2895.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.CylindricalGearMeshCompoundSystemDeflection)

        @property
        def face_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.FaceGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.GearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.HypoidGearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(
                _2915.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(
                _2917.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(
                _2920.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(
                _2923.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(
                _2931.PartToPartShearCouplingConnectionCompoundSystemDeflection
            )

        @property
        def planetary_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.PlanetaryConnectionCompoundSystemDeflection)

        @property
        def ring_pins_to_disc_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(
                _2940.RingPinsToDiscConnectionCompoundSystemDeflection
            )

        @property
        def rolling_ring_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(
                _2943.RollingRingConnectionCompoundSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(
                _2948.ShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def spring_damper_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(
                _2954.SpringDamperConnectionCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(
                _2957.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(
                _2960.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def torque_converter_connection_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(
                _2969.TorqueConverterConnectionCompoundSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.WormGearMeshCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3117,
            )

            return self._parent._cast(
                _3117.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3119,
            )

            return self._parent._cast(
                _3119.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3123,
            )

            return self._parent._cast(
                _3123.BeltConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3126,
            )

            return self._parent._cast(
                _3126.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3131,
            )

            return self._parent._cast(
                _3131.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3136,
            )

            return self._parent._cast(
                _3136.ClutchConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.CoaxialConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3144,
            )

            return self._parent._cast(
                _3144.ConceptGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3147,
            )

            return self._parent._cast(
                _3147.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.CouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3154,
            )

            return self._parent._cast(
                _3154.CVTBeltConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3158,
            )

            return self._parent._cast(
                _3158.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3160,
            )

            return self._parent._cast(
                _3160.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.CylindricalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3168,
            )

            return self._parent._cast(
                _3168.FaceGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3177,
            )

            return self._parent._cast(
                _3177.HypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3179,
            )

            return self._parent._cast(
                _3179.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3181,
            )

            return self._parent._cast(
                _3181.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3184,
            )

            return self._parent._cast(
                _3184.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3187,
            )

            return self._parent._cast(
                _3187.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(
                _3195.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(
                _3197.PlanetaryConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3207,
            )

            return self._parent._cast(
                _3207.RollingRingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(
                _3211.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3217,
            )

            return self._parent._cast(
                _3217.SpringDamperConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3223,
            )

            return self._parent._cast(
                _3223.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3232,
            )

            return self._parent._cast(
                _3232.TorqueConverterConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3238,
            )

            return self._parent._cast(
                _3238.WormGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3241,
            )

            return self._parent._cast(
                _3241.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3376,
            )

            return self._parent._cast(
                _3376.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3378,
            )

            return self._parent._cast(
                _3378.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3382,
            )

            return self._parent._cast(
                _3382.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3385,
            )

            return self._parent._cast(
                _3385.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3390,
            )

            return self._parent._cast(
                _3390.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3395,
            )

            return self._parent._cast(
                _3395.ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3397,
            )

            return self._parent._cast(
                _3397.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3400,
            )

            return self._parent._cast(
                _3400.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3403,
            )

            return self._parent._cast(
                _3403.ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3406,
            )

            return self._parent._cast(
                _3406.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3411,
            )

            return self._parent._cast(
                _3411.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3413,
            )

            return self._parent._cast(
                _3413.CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3417,
            )

            return self._parent._cast(
                _3417.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3419,
            )

            return self._parent._cast(
                _3419.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3421,
            )

            return self._parent._cast(
                _3421.CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3427,
            )

            return self._parent._cast(
                _3427.FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3432,
            )

            return self._parent._cast(
                _3432.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3436,
            )

            return self._parent._cast(
                _3436.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3438,
            )

            return self._parent._cast(
                _3438.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3440,
            )

            return self._parent._cast(
                _3440.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3443,
            )

            return self._parent._cast(
                _3443.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3446,
            )

            return self._parent._cast(
                _3446.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3454,
            )

            return self._parent._cast(
                _3454.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3463,
            )

            return self._parent._cast(
                _3463.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3466,
            )

            return self._parent._cast(
                _3466.RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3470,
            )

            return self._parent._cast(
                _3470.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3473,
            )

            return self._parent._cast(
                _3473.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3476,
            )

            return self._parent._cast(
                _3476.SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3479,
            )

            return self._parent._cast(
                _3479.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3491,
            )

            return self._parent._cast(
                _3491.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3497,
            )

            return self._parent._cast(
                _3497.WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3500,
            )

            return self._parent._cast(
                _3500.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3635,
            )

            return self._parent._cast(
                _3635.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3637,
            )

            return self._parent._cast(
                _3637.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3641,
            )

            return self._parent._cast(
                _3641.BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3644,
            )

            return self._parent._cast(
                _3644.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3649,
            )

            return self._parent._cast(
                _3649.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3654,
            )

            return self._parent._cast(
                _3654.ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3656,
            )

            return self._parent._cast(
                _3656.CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3659,
            )

            return self._parent._cast(
                _3659.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3662,
            )

            return self._parent._cast(
                _3662.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3665,
            )

            return self._parent._cast(
                _3665.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3670,
            )

            return self._parent._cast(
                _3670.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3672,
            )

            return self._parent._cast(
                _3672.CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3676,
            )

            return self._parent._cast(
                _3676.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3678,
            )

            return self._parent._cast(
                _3678.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3680,
            )

            return self._parent._cast(
                _3680.CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3686,
            )

            return self._parent._cast(
                _3686.FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3691,
            )

            return self._parent._cast(
                _3691.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3695,
            )

            return self._parent._cast(
                _3695.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3697,
            )

            return self._parent._cast(
                _3697.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3699,
            )

            return self._parent._cast(
                _3699.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3702,
            )

            return self._parent._cast(
                _3702.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3705,
            )

            return self._parent._cast(
                _3705.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3715,
            )

            return self._parent._cast(
                _3715.PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3722,
            )

            return self._parent._cast(
                _3722.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3725,
            )

            return self._parent._cast(
                _3725.RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3729,
            )

            return self._parent._cast(
                _3729.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3732,
            )

            return self._parent._cast(
                _3732.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3735,
            )

            return self._parent._cast(
                _3735.SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3738,
            )

            return self._parent._cast(
                _3738.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3741,
            )

            return self._parent._cast(
                _3741.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3750,
            )

            return self._parent._cast(
                _3750.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3756,
            )

            return self._parent._cast(
                _3756.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3759,
            )

            return self._parent._cast(
                _3759.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3898,
            )

            return self._parent._cast(
                _3898.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3900,
            )

            return self._parent._cast(
                _3900.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def belt_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3904,
            )

            return self._parent._cast(_3904.BeltConnectionCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(
                _3907.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(_3912.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def clutch_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3917,
            )

            return self._parent._cast(_3917.ClutchConnectionCompoundStabilityAnalysis)

        @property
        def coaxial_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(
                _3922.ConceptCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def concept_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(_3925.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConnectionCompoundStabilityAnalysis)

        @property
        def coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(_3933.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def cvt_belt_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(_3935.CVTBeltConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(
                _3939.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(
                _3941.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(
                _3943.CylindricalGearMeshCompoundStabilityAnalysis
            )

        @property
        def face_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(_3949.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.GearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(
                _3960.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(
                _3965.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3968,
            )

            return self._parent._cast(
                _3968.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(
                _3976.PartToPartShearCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def planetary_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(
                _3978.PlanetaryConnectionCompoundStabilityAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.RingPinsToDiscConnectionCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(
                _3988.RollingRingConnectionCompoundStabilityAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(
                _3992.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(
                _3995.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def spring_damper_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3998,
            )

            return self._parent._cast(
                _3998.SpringDamperConnectionCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(
                _4001.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(
                _4004.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def torque_converter_connection_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(
                _4013.TorqueConverterConnectionCompoundStabilityAnalysis
            )

        @property
        def worm_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4167,
            )

            return self._parent._cast(
                _4167.AbstractShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4169,
            )

            return self._parent._cast(_4169.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def belt_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.BeltConnectionCompoundPowerFlow)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.BevelGearMeshCompoundPowerFlow)

        @property
        def clutch_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4186,
            )

            return self._parent._cast(_4186.ClutchConnectionCompoundPowerFlow)

        @property
        def coaxial_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.CoaxialConnectionCompoundPowerFlow)

        @property
        def concept_coupling_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.ConceptCouplingConnectionCompoundPowerFlow)

        @property
        def concept_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ConceptGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.ConicalGearMeshCompoundPowerFlow)

        @property
        def connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.ConnectionCompoundPowerFlow)

        @property
        def coupling_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.CouplingConnectionCompoundPowerFlow)

        @property
        def cvt_belt_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.CVTBeltConnectionCompoundPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(
                _4208.CycloidalDiscCentralBearingConnectionCompoundPowerFlow
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(
                _4210.CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
            )

        @property
        def cylindrical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CylindricalGearMeshCompoundPowerFlow)

        @property
        def face_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.FaceGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.GearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.HypoidGearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(
                _4229.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(
                _4231.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(
                _4237.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
            )

        @property
        def part_to_part_shear_coupling_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(
                _4245.PartToPartShearCouplingConnectionCompoundPowerFlow
            )

        @property
        def planetary_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(_4247.PlanetaryConnectionCompoundPowerFlow)

        @property
        def ring_pins_to_disc_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.RingPinsToDiscConnectionCompoundPowerFlow)

        @property
        def rolling_ring_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(_4257.RollingRingConnectionCompoundPowerFlow)

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(
                _4261.ShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def spring_damper_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.SpringDamperConnectionCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def torque_converter_connection_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.TorqueConverterConnectionCompoundPowerFlow)

        @property
        def worm_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.WormGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(
                _4443.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4445,
            )

            return self._parent._cast(
                _4445.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def belt_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4449,
            )

            return self._parent._cast(_4449.BeltConnectionCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4452,
            )

            return self._parent._cast(
                _4452.BevelDifferentialGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(_4457.BevelGearMeshCompoundParametricStudyTool)

        @property
        def clutch_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4462,
            )

            return self._parent._cast(_4462.ClutchConnectionCompoundParametricStudyTool)

        @property
        def coaxial_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(
                _4464.CoaxialConnectionCompoundParametricStudyTool
            )

        @property
        def concept_coupling_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(
                _4467.ConceptCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def concept_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(_4470.ConceptGearMeshCompoundParametricStudyTool)

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(_4473.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConnectionCompoundParametricStudyTool)

        @property
        def coupling_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(
                _4478.CouplingConnectionCompoundParametricStudyTool
            )

        @property
        def cvt_belt_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(
                _4480.CVTBeltConnectionCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(
                _4484.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(
                _4486.CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(
                _4488.CylindricalGearMeshCompoundParametricStudyTool
            )

        @property
        def face_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(_4494.FaceGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.GearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(
                _4505.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(
                _4507.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4510,
            )

            return self._parent._cast(
                _4510.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(
                _4513.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(
                _4521.PartToPartShearCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def planetary_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(
                _4523.PlanetaryConnectionCompoundParametricStudyTool
            )

        @property
        def ring_pins_to_disc_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(
                _4530.RingPinsToDiscConnectionCompoundParametricStudyTool
            )

        @property
        def rolling_ring_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4533,
            )

            return self._parent._cast(
                _4533.RollingRingConnectionCompoundParametricStudyTool
            )

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(
                _4537.ShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4540,
            )

            return self._parent._cast(
                _4540.SpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def spring_damper_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.SpringDamperConnectionCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(
                _4546.StraightBevelDiffGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.StraightBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def torque_converter_connection_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(
                _4558.TorqueConverterConnectionCompoundParametricStudyTool
            )

        @property
        def worm_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(_4564.WormGearMeshCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(
                _4567.ZerolBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4728,
            )

            return self._parent._cast(
                _4728.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4730,
            )

            return self._parent._cast(
                _4730.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def belt_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4734,
            )

            return self._parent._cast(_4734.BeltConnectionCompoundModalAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4737,
            )

            return self._parent._cast(
                _4737.BevelDifferentialGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(_4742.BevelGearMeshCompoundModalAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4747,
            )

            return self._parent._cast(_4747.ClutchConnectionCompoundModalAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.CoaxialConnectionCompoundModalAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(
                _4752.ConceptCouplingConnectionCompoundModalAnalysis
            )

        @property
        def concept_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(_4755.ConceptGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4758,
            )

            return self._parent._cast(_4758.ConicalGearMeshCompoundModalAnalysis)

        @property
        def connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.ConnectionCompoundModalAnalysis)

        @property
        def coupling_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(_4763.CouplingConnectionCompoundModalAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4765,
            )

            return self._parent._cast(_4765.CVTBeltConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(
                _4769.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(
                _4771.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4773,
            )

            return self._parent._cast(_4773.CylindricalGearMeshCompoundModalAnalysis)

        @property
        def face_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.FaceGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.GearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.HypoidGearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4790,
            )

            return self._parent._cast(
                _4790.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(
                _4792.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4795,
            )

            return self._parent._cast(
                _4795.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(
                _4798.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(
                _4806.PartToPartShearCouplingConnectionCompoundModalAnalysis
            )

        @property
        def planetary_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(_4808.PlanetaryConnectionCompoundModalAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(
                _4815.RingPinsToDiscConnectionCompoundModalAnalysis
            )

        @property
        def rolling_ring_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4818,
            )

            return self._parent._cast(_4818.RollingRingConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(
                _4822.ShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4825,
            )

            return self._parent._cast(_4825.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.SpringDamperConnectionCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(
                _4831.StraightBevelDiffGearMeshCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(
                _4843.TorqueConverterConnectionCompoundModalAnalysis
            )

        @property
        def worm_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.WormGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4988,
            )

            return self._parent._cast(
                _4988.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4990,
            )

            return self._parent._cast(
                _4990.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4994,
            )

            return self._parent._cast(
                _4994.BeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4997,
            )

            return self._parent._cast(
                _4997.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5002,
            )

            return self._parent._cast(
                _5002.BevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5007,
            )

            return self._parent._cast(
                _5007.ClutchConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5009,
            )

            return self._parent._cast(
                _5009.CoaxialConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(
                _5012.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(
                _5015.ConceptGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5018,
            )

            return self._parent._cast(
                _5018.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5020,
            )

            return self._parent._cast(_5020.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(
                _5023.CouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(
                _5025.CVTBeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5029,
            )

            return self._parent._cast(
                _5029.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(
                _5031.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5033,
            )

            return self._parent._cast(
                _5033.CylindricalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5039,
            )

            return self._parent._cast(
                _5039.FaceGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(_5044.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5048,
            )

            return self._parent._cast(
                _5048.HypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5050,
            )

            return self._parent._cast(
                _5050.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(
                _5052.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(
                _5055.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(
                _5058.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(
                _5066.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5068,
            )

            return self._parent._cast(
                _5068.PlanetaryConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(
                _5075.RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5078,
            )

            return self._parent._cast(
                _5078.RollingRingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5082,
            )

            return self._parent._cast(
                _5082.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(
                _5085.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.SpringDamperConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5091,
            )

            return self._parent._cast(
                _5091.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5103,
            )

            return self._parent._cast(
                _5103.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.WormGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5247,
            )

            return self._parent._cast(
                _5247.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5253,
            )

            return self._parent._cast(_5253.BeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(
                _5256.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5261,
            )

            return self._parent._cast(_5261.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def clutch_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5266,
            )

            return self._parent._cast(
                _5266.ClutchConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(
                _5268.CoaxialConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(
                _5271.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(
                _5274.ConceptGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(
                _5277.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5279,
            )

            return self._parent._cast(_5279.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(
                _5282.CouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(
                _5284.CVTBeltConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(
                _5288.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(
                _5290.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(
                _5292.CylindricalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(_5298.FaceGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(
                _5309.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(
                _5311.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(
                _5325.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.PlanetaryConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(
                _5334.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5337,
            )

            return self._parent._cast(
                _5337.RollingRingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(
                _5341.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(
                _5344.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpringDamperConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(
                _5362.TorqueConverterConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(_5368.WormGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5531,
            )

            return self._parent._cast(
                _5531.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5535,
            )

            return self._parent._cast(
                _5535.BeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5538,
            )

            return self._parent._cast(
                _5538.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5543,
            )

            return self._parent._cast(
                _5543.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5548,
            )

            return self._parent._cast(
                _5548.ClutchConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(
                _5550.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(
                _5553.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(
                _5556.ConceptGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(_5561.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5564,
            )

            return self._parent._cast(
                _5564.CouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(
                _5566.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(
                _5570.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(
                _5572.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(
                _5574.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(
                _5580.FaceGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(_5585.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(
                _5589.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(
                _5591.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(
                _5593.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(
                _5596.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(
                _5607.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(
                _5609.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(
                _5616.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(
                _5619.RollingRingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5626,
            )

            return self._parent._cast(
                _5626.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(
                _5644.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.WormGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5879,
            )

            return self._parent._cast(
                _5879.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5881,
            )

            return self._parent._cast(
                _5881.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def belt_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5885,
            )

            return self._parent._cast(_5885.BeltConnectionCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5888,
            )

            return self._parent._cast(
                _5888.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5893,
            )

            return self._parent._cast(_5893.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def clutch_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5898,
            )

            return self._parent._cast(_5898.ClutchConnectionCompoundHarmonicAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5900,
            )

            return self._parent._cast(_5900.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def concept_coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(
                _5903.ConceptCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(_5906.ConceptGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(_5909.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(_5911.ConnectionCompoundHarmonicAnalysis)

        @property
        def coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5914,
            )

            return self._parent._cast(_5914.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5916,
            )

            return self._parent._cast(_5916.CVTBeltConnectionCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5920,
            )

            return self._parent._cast(
                _5920.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5922,
            )

            return self._parent._cast(
                _5922.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5924,
            )

            return self._parent._cast(_5924.CylindricalGearMeshCompoundHarmonicAnalysis)

        @property
        def face_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.FaceGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5935,
            )

            return self._parent._cast(_5935.GearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(
                _5941.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5943,
            )

            return self._parent._cast(
                _5943.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(
                _5946.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(
                _5949.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(
                _5957.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def planetary_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5959,
            )

            return self._parent._cast(_5959.PlanetaryConnectionCompoundHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(
                _5966.RingPinsToDiscConnectionCompoundHarmonicAnalysis
            )

        @property
        def rolling_ring_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5969,
            )

            return self._parent._cast(
                _5969.RollingRingConnectionCompoundHarmonicAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5973,
            )

            return self._parent._cast(
                _5973.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(_5976.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def spring_damper_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(
                _5979.SpringDamperConnectionCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(
                _5982.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(
                _5985.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def torque_converter_connection_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5994,
            )

            return self._parent._cast(
                _5994.TorqueConverterConnectionCompoundHarmonicAnalysis
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.WormGearMeshCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6139,
            )

            return self._parent._cast(
                _6139.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6141,
            )

            return self._parent._cast(
                _6141.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6145,
            )

            return self._parent._cast(
                _6145.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6148,
            )

            return self._parent._cast(
                _6148.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6153,
            )

            return self._parent._cast(
                _6153.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6158,
            )

            return self._parent._cast(
                _6158.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coaxial_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6160,
            )

            return self._parent._cast(
                _6160.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6169,
            )

            return self._parent._cast(
                _6169.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6171,
            )

            return self._parent._cast(
                _6171.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6174,
            )

            return self._parent._cast(
                _6174.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6176,
            )

            return self._parent._cast(
                _6176.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6180,
            )

            return self._parent._cast(
                _6180.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6184,
            )

            return self._parent._cast(
                _6184.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6195,
            )

            return self._parent._cast(
                _6195.GearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6201,
            )

            return self._parent._cast(
                _6201.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6203,
            )

            return self._parent._cast(
                _6203.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6206,
            )

            return self._parent._cast(
                _6206.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6229,
            )

            return self._parent._cast(
                _6229.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6233,
            )

            return self._parent._cast(
                _6233.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6245,
            )

            return self._parent._cast(
                _6245.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6254,
            )

            return self._parent._cast(
                _6254.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6260,
            )

            return self._parent._cast(
                _6260.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(
                _6408.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6410,
            )

            return self._parent._cast(
                _6410.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def belt_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(_6414.BeltConnectionCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6417,
            )

            return self._parent._cast(
                _6417.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6422,
            )

            return self._parent._cast(_6422.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def clutch_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6427,
            )

            return self._parent._cast(_6427.ClutchConnectionCompoundDynamicAnalysis)

        @property
        def coaxial_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def concept_coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(
                _6432.ConceptCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def concept_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(_6435.ConceptGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6438,
            )

            return self._parent._cast(_6438.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(_6440.ConnectionCompoundDynamicAnalysis)

        @property
        def coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(_6443.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(_6445.CVTBeltConnectionCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6449,
            )

            return self._parent._cast(
                _6449.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(
                _6451.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CylindricalGearMeshCompoundDynamicAnalysis)

        @property
        def face_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.FaceGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.GearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6470,
            )

            return self._parent._cast(
                _6470.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(
                _6472.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6475,
            )

            return self._parent._cast(
                _6475.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(
                _6486.PartToPartShearCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def planetary_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(_6488.PlanetaryConnectionCompoundDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(
                _6495.RingPinsToDiscConnectionCompoundDynamicAnalysis
            )

        @property
        def rolling_ring_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6498,
            )

            return self._parent._cast(
                _6498.RollingRingConnectionCompoundDynamicAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6502,
            )

            return self._parent._cast(
                _6502.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6505,
            )

            return self._parent._cast(_6505.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def spring_damper_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(
                _6508.SpringDamperConnectionCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(
                _6511.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(
                _6514.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def torque_converter_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6523,
            )

            return self._parent._cast(
                _6523.TorqueConverterConnectionCompoundDynamicAnalysis
            )

        @property
        def worm_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.WormGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(
                _6675.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6677,
            )

            return self._parent._cast(
                _6677.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def belt_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6681,
            )

            return self._parent._cast(_6681.BeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6684,
            )

            return self._parent._cast(
                _6684.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6689,
            )

            return self._parent._cast(_6689.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def clutch_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6694,
            )

            return self._parent._cast(
                _6694.ClutchConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def coaxial_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(
                _6696.CoaxialConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(
                _6699.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(
                _6702.ConceptGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(
                _6705.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(_6707.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(
                _6710.CouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cvt_belt_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6712,
            )

            return self._parent._cast(
                _6712.CVTBeltConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(
                _6716.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(
                _6718.CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6720,
            )

            return self._parent._cast(
                _6720.CylindricalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(_6726.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6737,
            )

            return self._parent._cast(
                _6737.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6739,
            )

            return self._parent._cast(
                _6739.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6742,
            )

            return self._parent._cast(
                _6742.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6745,
            )

            return self._parent._cast(
                _6745.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(
                _6753.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6755,
            )

            return self._parent._cast(
                _6755.PlanetaryConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(
                _6762.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6765,
            )

            return self._parent._cast(
                _6765.RollingRingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(
                _6769.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6772,
            )

            return self._parent._cast(
                _6772.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(
                _6775.SpringDamperConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6781,
            )

            return self._parent._cast(
                _6781.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_connection_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6790,
            )

            return self._parent._cast(
                _6790.TorqueConverterConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6796,
            )

            return self._parent._cast(_6796.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7141,
            )

            return self._parent._cast(
                _7141.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7143,
            )

            return self._parent._cast(
                _7143.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7147,
            )

            return self._parent._cast(
                _7147.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7150,
            )

            return self._parent._cast(
                _7150.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7155,
            )

            return self._parent._cast(
                _7155.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7160,
            )

            return self._parent._cast(
                _7160.ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7162,
            )

            return self._parent._cast(
                _7162.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7168,
            )

            return self._parent._cast(
                _7168.ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7171,
            )

            return self._parent._cast(
                _7171.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7173,
            )

            return self._parent._cast(
                _7173.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7176,
            )

            return self._parent._cast(
                _7176.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7178,
            )

            return self._parent._cast(
                _7178.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7182,
            )

            return self._parent._cast(
                _7182.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7184,
            )

            return self._parent._cast(
                _7184.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7186,
            )

            return self._parent._cast(
                _7186.CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7197,
            )

            return self._parent._cast(
                _7197.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7201,
            )

            return self._parent._cast(
                _7201.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7203,
            )

            return self._parent._cast(
                _7203.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7205,
            )

            return self._parent._cast(
                _7205.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7208,
            )

            return self._parent._cast(
                _7208.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7211,
            )

            return self._parent._cast(
                _7211.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7219,
            )

            return self._parent._cast(
                _7219.PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7221,
            )

            return self._parent._cast(
                _7221.PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7231,
            )

            return self._parent._cast(
                _7231.RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7235,
            )

            return self._parent._cast(
                _7235.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7238,
            )

            return self._parent._cast(
                _7238.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7241,
            )

            return self._parent._cast(
                _7241.SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7244,
            )

            return self._parent._cast(
                _7244.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7247,
            )

            return self._parent._cast(
                _7247.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7256,
            )

            return self._parent._cast(
                _7256.TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7262,
            )

            return self._parent._cast(
                _7262.WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7265,
            )

            return self._parent._cast(
                _7265.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7408,
            )

            return self._parent._cast(
                _7408.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def belt_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7412,
            )

            return self._parent._cast(
                _7412.BeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7415,
            )

            return self._parent._cast(
                _7415.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7420,
            )

            return self._parent._cast(
                _7420.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def clutch_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7425,
            )

            return self._parent._cast(
                _7425.ClutchConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def coaxial_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(
                _7427.CoaxialConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7430,
            )

            return self._parent._cast(
                _7430.ConceptCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(
                _7433.ConceptGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(_7438.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(
                _7441.CouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_belt_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(
                _7443.CVTBeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7447,
            )

            return self._parent._cast(
                _7447.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(
                _7449.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(
                _7451.CylindricalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(
                _7457.FaceGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7462,
            )

            return self._parent._cast(_7462.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(
                _7466.HypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7468,
            )

            return self._parent._cast(
                _7468.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(
                _7470.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(
                _7473.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(
                _7476.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(
                _7484.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7486,
            )

            return self._parent._cast(
                _7486.PlanetaryConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(
                _7493.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(
                _7496.RollingRingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7500,
            )

            return self._parent._cast(
                _7500.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(
                _7503.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpringDamperConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.TorqueConverterConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(
                _7527.WormGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
        ) -> "ConnectionCompoundAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionCompoundAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionCompoundAnalysis._Cast_ConnectionCompoundAnalysis":
        return self._Cast_ConnectionCompoundAnalysis(self)
