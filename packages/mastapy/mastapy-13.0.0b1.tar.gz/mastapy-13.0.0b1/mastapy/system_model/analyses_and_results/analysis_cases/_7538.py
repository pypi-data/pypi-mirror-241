"""ConnectionStaticLoadAnalysisCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STATIC_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "ConnectionStaticLoadAnalysisCase",
)


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionStaticLoadAnalysisCase",)


Self = TypeVar("Self", bound="ConnectionStaticLoadAnalysisCase")


class ConnectionStaticLoadAnalysisCase(_7535.ConnectionAnalysisCase):
    """ConnectionStaticLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _CONNECTION_STATIC_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionStaticLoadAnalysisCase")

    class _Cast_ConnectionStaticLoadAnalysisCase:
        """Special nested class for casting ConnectionStaticLoadAnalysisCase to subclasses."""

        def __init__(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
            parent: "ConnectionStaticLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def connection_analysis_case(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2686,
            )

            return self._parent._cast(
                _2686.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def belt_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2697,
            )

            return self._parent._cast(_2697.BeltConnectionSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelGearMeshSystemDeflection)

        @property
        def clutch_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.ClutchConnectionSystemDeflection)

        @property
        def coaxial_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.CoaxialConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ConceptCouplingConnectionSystemDeflection)

        @property
        def concept_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2718,
            )

            return self._parent._cast(_2718.ConceptGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConicalGearMeshSystemDeflection)

        @property
        def connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConnectionSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.CouplingConnectionSystemDeflection)

        @property
        def cvt_belt_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.CVTBeltConnectionSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(
                _2734.CycloidalDiscCentralBearingConnectionSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(
                _2735.CycloidalDiscPlanetaryBearingConnectionSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2737,
            )

            return self._parent._cast(_2737.CylindricalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2739,
            )

            return self._parent._cast(
                _2739.CylindricalGearMeshSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.FaceGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.GearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.HypoidGearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(
                _2765.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(
                _2766.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(
                _2769.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(
                _2784.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def planetary_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PlanetaryConnectionSystemDeflection)

        @property
        def ring_pins_to_disc_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.RingPinsToDiscConnectionSystemDeflection)

        @property
        def rolling_ring_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(_2796.RollingRingConnectionSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(
                _2803.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.SpiralBevelGearMeshSystemDeflection)

        @property
        def spring_damper_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpringDamperConnectionSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.StraightBevelGearMeshSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.TorqueConverterConnectionSystemDeflection)

        @property
        def worm_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.WormGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.ZerolBevelGearMeshSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2984,
            )

            return self._parent._cast(
                _2984.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2985,
            )

            return self._parent._cast(
                _2985.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2990,
            )

            return self._parent._cast(
                _2990.BeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2992,
            )

            return self._parent._cast(
                _2992.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2997,
            )

            return self._parent._cast(_2997.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3002,
            )

            return self._parent._cast(
                _3002.ClutchConnectionSteadyStateSynchronousResponse
            )

        @property
        def coaxial_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(
                _3005.CoaxialConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3007,
            )

            return self._parent._cast(
                _3007.ConceptCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(
                _3010.ConceptGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(
                _3013.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ConnectionSteadyStateSynchronousResponse)

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(
                _3018.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3021,
            )

            return self._parent._cast(
                _3021.CVTBeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(
                _3025.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(
                _3026.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3028,
            )

            return self._parent._cast(
                _3028.CylindricalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3035,
            )

            return self._parent._cast(_3035.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.GearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3044,
            )

            return self._parent._cast(
                _3044.HypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(
                _3047.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3048,
            )

            return self._parent._cast(
                _3048.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3051,
            )

            return self._parent._cast(
                _3051.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3062,
            )

            return self._parent._cast(
                _3062.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(
                _3065.PlanetaryConnectionSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(
                _3072.RingPinsToDiscConnectionSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3074,
            )

            return self._parent._cast(
                _3074.RollingRingConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(
                _3079.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3081,
            )

            return self._parent._cast(
                _3081.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.SpringDamperConnectionSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(
                _3090.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(
                _3093.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3102,
            )

            return self._parent._cast(
                _3102.TorqueConverterConnectionSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3108,
            )

            return self._parent._cast(_3108.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(
                _3111.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3246,
            )

            return self._parent._cast(
                _3246.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3247,
            )

            return self._parent._cast(
                _3247.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3252,
            )

            return self._parent._cast(
                _3252.BeltConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3254,
            )

            return self._parent._cast(
                _3254.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3259,
            )

            return self._parent._cast(
                _3259.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3264,
            )

            return self._parent._cast(
                _3264.ClutchConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coaxial_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3267,
            )

            return self._parent._cast(
                _3267.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3269,
            )

            return self._parent._cast(
                _3269.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3272,
            )

            return self._parent._cast(
                _3272.ConceptGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3275,
            )

            return self._parent._cast(
                _3275.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.CouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3283,
            )

            return self._parent._cast(
                _3283.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(
                _3287.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3290,
            )

            return self._parent._cast(
                _3290.CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3296,
            )

            return self._parent._cast(
                _3296.FaceGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3305,
            )

            return self._parent._cast(
                _3305.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3308,
            )

            return self._parent._cast(
                _3308.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3309,
            )

            return self._parent._cast(
                _3309.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3315,
            )

            return self._parent._cast(
                _3315.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3323,
            )

            return self._parent._cast(
                _3323.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(
                _3326.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3333,
            )

            return self._parent._cast(
                _3333.RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3335,
            )

            return self._parent._cast(
                _3335.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3340,
            )

            return self._parent._cast(
                _3340.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3342,
            )

            return self._parent._cast(
                _3342.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(
                _3345.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3361,
            )

            return self._parent._cast(
                _3361.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3367,
            )

            return self._parent._cast(
                _3367.WormGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3370,
            )

            return self._parent._cast(
                _3370.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3505,
            )

            return self._parent._cast(
                _3505.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3506,
            )

            return self._parent._cast(
                _3506.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3511,
            )

            return self._parent._cast(
                _3511.BeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3513,
            )

            return self._parent._cast(
                _3513.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3518,
            )

            return self._parent._cast(
                _3518.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3523,
            )

            return self._parent._cast(
                _3523.ClutchConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coaxial_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3528,
            )

            return self._parent._cast(
                _3528.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3534,
            )

            return self._parent._cast(
                _3534.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3546,
            )

            return self._parent._cast(
                _3546.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3549,
            )

            return self._parent._cast(
                _3549.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3555,
            )

            return self._parent._cast(
                _3555.FaceGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(
                _3564.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3567,
            )

            return self._parent._cast(
                _3567.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3568,
            )

            return self._parent._cast(
                _3568.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3574,
            )

            return self._parent._cast(
                _3574.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3592,
            )

            return self._parent._cast(
                _3592.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3594,
            )

            return self._parent._cast(
                _3594.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3608,
            )

            return self._parent._cast(
                _3608.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3611,
            )

            return self._parent._cast(
                _3611.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.WormGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3764,
            )

            return self._parent._cast(
                _3764.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def belt_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3770,
            )

            return self._parent._cast(_3770.BeltConnectionStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3772,
            )

            return self._parent._cast(_3772.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(_3777.BevelGearMeshStabilityAnalysis)

        @property
        def clutch_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3782,
            )

            return self._parent._cast(_3782.ClutchConnectionStabilityAnalysis)

        @property
        def coaxial_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.CoaxialConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def concept_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ConceptGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.ConicalGearMeshStabilityAnalysis)

        @property
        def connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ConnectionStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.CouplingConnectionStabilityAnalysis)

        @property
        def cvt_belt_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.CVTBeltConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(
                _3806.CycloidalDiscCentralBearingConnectionStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(
                _3807.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
            )

        @property
        def cylindrical_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.CylindricalGearMeshStabilityAnalysis)

        @property
        def face_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.FaceGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.GearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.HypoidGearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(
                _3828.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(
                _3829.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(
                _3835.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(
                _3843.PartToPartShearCouplingConnectionStabilityAnalysis
            )

        @property
        def planetary_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PlanetaryConnectionStabilityAnalysis)

        @property
        def ring_pins_to_disc_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(_3853.RingPinsToDiscConnectionStabilityAnalysis)

        @property
        def rolling_ring_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(_3855.RollingRingConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(
                _3860.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(_3862.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def spring_damper_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.SpringDamperConnectionStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.StraightBevelGearMeshStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.TorqueConverterConnectionStabilityAnalysis)

        @property
        def worm_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.WormGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4033

            return self._parent._cast(
                _4033.AbstractShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def belt_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4039

            return self._parent._cast(_4039.BeltConnectionPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4041

            return self._parent._cast(_4041.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelGearMeshPowerFlow)

        @property
        def clutch_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4051

            return self._parent._cast(_4051.ClutchConnectionPowerFlow)

        @property
        def coaxial_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.CoaxialConnectionPowerFlow)

        @property
        def concept_coupling_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4056

            return self._parent._cast(_4056.ConceptCouplingConnectionPowerFlow)

        @property
        def concept_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConicalGearMeshPowerFlow)

        @property
        def connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConnectionPowerFlow)

        @property
        def coupling_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.CouplingConnectionPowerFlow)

        @property
        def cvt_belt_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.CVTBeltConnectionPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(
                _4074.CycloidalDiscCentralBearingConnectionPowerFlow
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(
                _4075.CycloidalDiscPlanetaryBearingConnectionPowerFlow
            )

        @property
        def cylindrical_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.FaceGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.GearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.HypoidGearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.InterMountableComponentConnectionPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(
                _4098.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(
                _4101.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(
                _4104.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
            )

        @property
        def part_to_part_shear_coupling_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def planetary_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.PlanetaryConnectionPowerFlow)

        @property
        def ring_pins_to_disc_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(_4124.RingPinsToDiscConnectionPowerFlow)

        @property
        def rolling_ring_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(_4126.RollingRingConnectionPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(
                _4131.ShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.SpiralBevelGearMeshPowerFlow)

        @property
        def spring_damper_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.SpringDamperConnectionPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.StraightBevelGearMeshPowerFlow)

        @property
        def torque_converter_connection_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.TorqueConverterConnectionPowerFlow)

        @property
        def worm_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.ZerolBevelGearMeshPowerFlow)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572

            return self._parent._cast(
                _4572.AbstractShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573

            return self._parent._cast(_4573.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def belt_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578

            return self._parent._cast(_4578.BeltConnectionModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelGearMeshModalAnalysis)

        @property
        def clutch_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.ClutchConnectionModalAnalysis)

        @property
        def coaxial_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.CoaxialConnectionModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.ConceptCouplingConnectionModalAnalysis)

        @property
        def concept_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.ConceptGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.ConicalGearMeshModalAnalysis)

        @property
        def connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConnectionModalAnalysis)

        @property
        def coupling_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.CouplingConnectionModalAnalysis)

        @property
        def cvt_belt_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.CVTBeltConnectionModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(
                _4614.CycloidalDiscCentralBearingConnectionModalAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(
                _4616.CycloidalDiscPlanetaryBearingConnectionModalAnalysis
            )

        @property
        def cylindrical_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.CylindricalGearMeshModalAnalysis)

        @property
        def face_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.FaceGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.GearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.HypoidGearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(
                _4639.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(
                _4640.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(
                _4643.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(
                _4646.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(
                _4660.PartToPartShearCouplingConnectionModalAnalysis
            )

        @property
        def planetary_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(_4663.PlanetaryConnectionModalAnalysis)

        @property
        def ring_pins_to_disc_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.RingPinsToDiscConnectionModalAnalysis)

        @property
        def rolling_ring_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(_4672.RollingRingConnectionModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(
                _4678.ShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680

            return self._parent._cast(_4680.SpiralBevelGearMeshModalAnalysis)

        @property
        def spring_damper_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.SpringDamperConnectionModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.StraightBevelGearMeshModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.TorqueConverterConnectionModalAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.WormGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.ZerolBevelGearMeshModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4857,
            )

            return self._parent._cast(
                _4857.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4858,
            )

            return self._parent._cast(
                _4858.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def belt_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4863,
            )

            return self._parent._cast(_4863.BeltConnectionModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(
                _4865.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4870,
            )

            return self._parent._cast(_4870.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def clutch_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4875,
            )

            return self._parent._cast(_4875.ClutchConnectionModalAnalysisAtAStiffness)

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.CoaxialConnectionModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(
                _4880.ConceptCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4883,
            )

            return self._parent._cast(_4883.ConceptGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(_4886.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(_4889.ConnectionModalAnalysisAtAStiffness)

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def cvt_belt_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(_4894.CVTBeltConnectionModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4898,
            )

            return self._parent._cast(
                _4898.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4900,
            )

            return self._parent._cast(
                _4900.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4901,
            )

            return self._parent._cast(
                _4901.CylindricalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4908,
            )

            return self._parent._cast(_4908.FaceGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.GearMeshModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.HypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4920,
            )

            return self._parent._cast(
                _4920.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4921,
            )

            return self._parent._cast(
                _4921.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4924,
            )

            return self._parent._cast(
                _4924.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4927,
            )

            return self._parent._cast(
                _4927.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(
                _4936.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4939,
            )

            return self._parent._cast(
                _4939.PlanetaryConnectionModalAnalysisAtAStiffness
            )

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(
                _4946.RingPinsToDiscConnectionModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4948,
            )

            return self._parent._cast(
                _4948.RollingRingConnectionModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4953,
            )

            return self._parent._cast(
                _4953.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4955,
            )

            return self._parent._cast(
                _4955.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4958,
            )

            return self._parent._cast(
                _4958.SpringDamperConnectionModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(
                _4961.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4964,
            )

            return self._parent._cast(
                _4964.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4973,
            )

            return self._parent._cast(
                _4973.TorqueConverterConnectionModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4979,
            )

            return self._parent._cast(_4979.WormGearMeshModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4982,
            )

            return self._parent._cast(_4982.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(
                _5117.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5118,
            )

            return self._parent._cast(
                _5118.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def belt_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5123,
            )

            return self._parent._cast(_5123.BeltConnectionModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(
                _5125.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5130,
            )

            return self._parent._cast(_5130.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def clutch_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5135,
            )

            return self._parent._cast(_5135.ClutchConnectionModalAnalysisAtASpeed)

        @property
        def coaxial_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5138,
            )

            return self._parent._cast(_5138.CoaxialConnectionModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(
                _5140.ConceptCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5143,
            )

            return self._parent._cast(_5143.ConceptGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5146,
            )

            return self._parent._cast(_5146.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5149,
            )

            return self._parent._cast(_5149.ConnectionModalAnalysisAtASpeed)

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(_5151.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def cvt_belt_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(_5154.CVTBeltConnectionModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5158,
            )

            return self._parent._cast(
                _5158.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(
                _5160.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5161,
            )

            return self._parent._cast(_5161.CylindricalGearMeshModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5167,
            )

            return self._parent._cast(_5167.FaceGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.GearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5176,
            )

            return self._parent._cast(_5176.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(
                _5179.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5180,
            )

            return self._parent._cast(
                _5180.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5183,
            )

            return self._parent._cast(
                _5183.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5186,
            )

            return self._parent._cast(
                _5186.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(
                _5195.PartToPartShearCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5198,
            )

            return self._parent._cast(_5198.PlanetaryConnectionModalAnalysisAtASpeed)

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(
                _5205.RingPinsToDiscConnectionModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5207,
            )

            return self._parent._cast(_5207.RollingRingConnectionModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(
                _5212.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5214,
            )

            return self._parent._cast(_5214.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5217,
            )

            return self._parent._cast(_5217.SpringDamperConnectionModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(
                _5220.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5223,
            )

            return self._parent._cast(_5223.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5232,
            )

            return self._parent._cast(
                _5232.TorqueConverterConnectionModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5238,
            )

            return self._parent._cast(_5238.WormGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5241,
            )

            return self._parent._cast(_5241.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5679,
            )

            return self._parent._cast(
                _5679.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5681,
            )

            return self._parent._cast(_5681.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def belt_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5685,
            )

            return self._parent._cast(_5685.BeltConnectionHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5688,
            )

            return self._parent._cast(_5688.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.BevelGearMeshHarmonicAnalysis)

        @property
        def clutch_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5697,
            )

            return self._parent._cast(_5697.ClutchConnectionHarmonicAnalysis)

        @property
        def coaxial_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.CoaxialConnectionHarmonicAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.ConceptCouplingConnectionHarmonicAnalysis)

        @property
        def concept_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.ConceptGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ConicalGearMeshHarmonicAnalysis)

        @property
        def connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.ConnectionHarmonicAnalysis)

        @property
        def coupling_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.CouplingConnectionHarmonicAnalysis)

        @property
        def cvt_belt_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.CVTBeltConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(
                _5721.CycloidalDiscCentralBearingConnectionHarmonicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(
                _5723.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5725,
            )

            return self._parent._cast(_5725.CylindricalGearMeshHarmonicAnalysis)

        @property
        def face_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5745,
            )

            return self._parent._cast(_5745.FaceGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5752,
            )

            return self._parent._cast(_5752.GearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5769,
            )

            return self._parent._cast(_5769.HypoidGearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(
                _5771.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(
                _5773.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(
                _5776.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(
                _5779.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(
                _5786.PartToPartShearCouplingConnectionHarmonicAnalysis
            )

        @property
        def planetary_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(_5790.PlanetaryConnectionHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(_5798.RingPinsToDiscConnectionHarmonicAnalysis)

        @property
        def rolling_ring_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.RollingRingConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(
                _5805.ShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def spring_damper_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.SpringDamperConnectionHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.TorqueConverterConnectionHarmonicAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.WormGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6008,
            )

            return self._parent._cast(
                _6008.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6010,
            )

            return self._parent._cast(
                _6010.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6014,
            )

            return self._parent._cast(
                _6014.BeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6017,
            )

            return self._parent._cast(
                _6017.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6022,
            )

            return self._parent._cast(
                _6022.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6026,
            )

            return self._parent._cast(
                _6026.ClutchConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(
                _6029.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6031,
            )

            return self._parent._cast(
                _6031.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(
                _6035.ConceptGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.CouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_belt_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(
                _6045.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(
                _6049.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6053,
            )

            return self._parent._cast(
                _6053.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(
                _6059.FaceGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(_6064.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.HypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(
                _6071.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(
                _6073.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(
                _6076.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6090,
            )

            return self._parent._cast(
                _6090.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_to_disc_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(
                _6097.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(
                _6099.RollingRingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(
                _6104.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6107,
            )

            return self._parent._cast(
                _6107.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(
                _6109.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(
                _6131.WormGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277

            return self._parent._cast(
                _6277.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def belt_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.BeltConnectionDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelGearMeshDynamicAnalysis)

        @property
        def clutch_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.ClutchConnectionDynamicAnalysis)

        @property
        def coaxial_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.CoaxialConnectionDynamicAnalysis)

        @property
        def concept_coupling_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300

            return self._parent._cast(_6300.ConceptCouplingConnectionDynamicAnalysis)

        @property
        def concept_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ConceptGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConicalGearMeshDynamicAnalysis)

        @property
        def connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConnectionDynamicAnalysis)

        @property
        def coupling_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.CouplingConnectionDynamicAnalysis)

        @property
        def cvt_belt_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.CVTBeltConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(
                _6318.CycloidalDiscCentralBearingConnectionDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(
                _6320.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis
            )

        @property
        def cylindrical_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.CylindricalGearMeshDynamicAnalysis)

        @property
        def face_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.FaceGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.GearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.HypoidGearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(
                _6341.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(
                _6343.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(
                _6356.PartToPartShearCouplingConnectionDynamicAnalysis
            )

        @property
        def planetary_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(_6359.PlanetaryConnectionDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.RingPinsToDiscConnectionDynamicAnalysis)

        @property
        def rolling_ring_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.RollingRingConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(
                _6373.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def spring_damper_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.SpringDamperConnectionDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelGearMeshDynamicAnalysis)

        @property
        def torque_converter_connection_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.TorqueConverterConnectionDynamicAnalysis)

        @property
        def worm_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.WormGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(
                _6543.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6545,
            )

            return self._parent._cast(
                _6545.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def belt_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6549,
            )

            return self._parent._cast(_6549.BeltConnectionCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6552,
            )

            return self._parent._cast(
                _6552.BevelDifferentialGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6557,
            )

            return self._parent._cast(_6557.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def clutch_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6561,
            )

            return self._parent._cast(_6561.ClutchConnectionCriticalSpeedAnalysis)

        @property
        def coaxial_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6566,
            )

            return self._parent._cast(
                _6566.ConceptCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def concept_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ConceptGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.ConnectionCriticalSpeedAnalysis)

        @property
        def coupling_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(_6583.CVTBeltConnectionCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6587,
            )

            return self._parent._cast(
                _6587.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(
                _6589.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6591,
            )

            return self._parent._cast(_6591.CylindricalGearMeshCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6597,
            )

            return self._parent._cast(_6597.FaceGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.GearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6606,
            )

            return self._parent._cast(_6606.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(
                _6608.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(
                _6610.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(
                _6613.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6616,
            )

            return self._parent._cast(
                _6616.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(
                _6623.PartToPartShearCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6626,
            )

            return self._parent._cast(_6626.PlanetaryConnectionCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(
                _6633.RingPinsToDiscConnectionCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(_6635.RollingRingConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(
                _6640.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6643,
            )

            return self._parent._cast(_6643.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6645,
            )

            return self._parent._cast(_6645.SpringDamperConnectionCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(
                _6649.StraightBevelDiffGearMeshCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(_6652.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(
                _6660.TorqueConverterConnectionCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6667,
            )

            return self._parent._cast(_6667.WormGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6670,
            )

            return self._parent._cast(_6670.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7006,
            )

            return self._parent._cast(
                _7006.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7012,
            )

            return self._parent._cast(
                _7012.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7017,
            )

            return self._parent._cast(
                _7017.BeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7020,
            )

            return self._parent._cast(
                _7020.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7025,
            )

            return self._parent._cast(
                _7025.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7030,
            )

            return self._parent._cast(
                _7030.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7038,
            )

            return self._parent._cast(
                _7038.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7049,
            )

            return self._parent._cast(
                _7049.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7056,
            )

            return self._parent._cast(
                _7056.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7067,
            )

            return self._parent._cast(
                _7067.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7074,
            )

            return self._parent._cast(
                _7074.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7102,
            )

            return self._parent._cast(
                _7102.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7109,
            )

            return self._parent._cast(
                _7109.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7127,
            )

            return self._parent._cast(
                _7127.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7133,
            )

            return self._parent._cast(
                _7133.WormGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7270,
            )

            return self._parent._cast(
                _7270.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7275,
            )

            return self._parent._cast(
                _7275.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def belt_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7279,
            )

            return self._parent._cast(_7279.BeltConnectionAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7282,
            )

            return self._parent._cast(
                _7282.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(_7287.BevelGearMeshAdvancedSystemDeflection)

        @property
        def clutch_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(_7292.ClutchConnectionAdvancedSystemDeflection)

        @property
        def coaxial_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(_7294.CoaxialConnectionAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(
                _7297.ConceptCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.ConceptGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConnectionAdvancedSystemDeflection)

        @property
        def coupling_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(_7309.CouplingConnectionAdvancedSystemDeflection)

        @property
        def cvt_belt_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.CVTBeltConnectionAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(
                _7316.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(
                _7317.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.CylindricalGearMeshAdvancedSystemDeflection)

        @property
        def face_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7326,
            )

            return self._parent._cast(_7326.FaceGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.GearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(
                _7337.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(
                _7339.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(
                _7342.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7345,
            )

            return self._parent._cast(
                _7345.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(
                _7354.PartToPartShearCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def planetary_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.PlanetaryConnectionAdvancedSystemDeflection)

        @property
        def ring_pins_to_disc_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(
                _7363.RingPinsToDiscConnectionAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(
                _7366.RollingRingConnectionAdvancedSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(
                _7370.ShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(_7373.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def spring_damper_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(
                _7376.SpringDamperConnectionAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(
                _7379.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(
                _7391.TorqueConverterConnectionAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.WormGearMeshAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
        ) -> "ConnectionStaticLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionStaticLoadAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionStaticLoadAnalysisCase._Cast_ConnectionStaticLoadAnalysisCase":
        return self._Cast_ConnectionStaticLoadAnalysisCase(self)
