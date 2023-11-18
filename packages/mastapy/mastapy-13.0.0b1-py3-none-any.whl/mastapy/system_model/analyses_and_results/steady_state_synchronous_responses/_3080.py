"""SpecialisedAssemblySteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2981,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SpecialisedAssemblySteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblySteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SpecialisedAssemblySteadyStateSynchronousResponse")


class SpecialisedAssemblySteadyStateSynchronousResponse(
    _2981.AbstractAssemblySteadyStateSynchronousResponse
):
    """SpecialisedAssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblySteadyStateSynchronousResponse"
    )

    class _Cast_SpecialisedAssemblySteadyStateSynchronousResponse:
        """Special nested class for casting SpecialisedAssemblySteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
            parent: "SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _2981.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2986,
            )

            return self._parent._cast(
                _2986.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def belt_drive_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(_2991.BeltDriveSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2993,
            )

            return self._parent._cast(
                _2993.BevelDifferentialGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2998,
            )

            return self._parent._cast(_2998.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def bolted_joint_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3000,
            )

            return self._parent._cast(_3000.BoltedJointSteadyStateSynchronousResponse)

        @property
        def clutch_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(_3004.ClutchSteadyStateSynchronousResponse)

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3009,
            )

            return self._parent._cast(
                _3009.ConceptCouplingSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3011,
            )

            return self._parent._cast(
                _3011.ConceptGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(
                _3014.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def coupling_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(_3020.CouplingSteadyStateSynchronousResponse)

        @property
        def cvt_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(_3023.CVTSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3024,
            )

            return self._parent._cast(
                _3024.CycloidalAssemblySteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(
                _3029.CylindricalGearSetSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3036,
            )

            return self._parent._cast(_3036.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(
                _3039.FlexiblePinAssemblySteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.GearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3049,
            )

            return self._parent._cast(
                _3049.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(
                _3052.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3055,
            )

            return self._parent._cast(
                _3055.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(
                _3064.PartToPartShearCouplingSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(
                _3066.PlanetaryGearSetSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3073,
            )

            return self._parent._cast(
                _3073.RollingRingAssemblySteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.SpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.SpringDamperSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3091,
            )

            return self._parent._cast(
                _3091.StraightBevelDiffGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3094,
            )

            return self._parent._cast(
                _3094.StraightBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3101,
            )

            return self._parent._cast(_3101.SynchroniserSteadyStateSynchronousResponse)

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3104,
            )

            return self._parent._cast(
                _3104.TorqueConverterSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3109,
            )

            return self._parent._cast(_3109.WormGearSetSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3112,
            )

            return self._parent._cast(
                _3112.ZerolBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
        ) -> "SpecialisedAssemblySteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse",
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
        instance_to_wrap: "SpecialisedAssemblySteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2474.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblySteadyStateSynchronousResponse._Cast_SpecialisedAssemblySteadyStateSynchronousResponse":
        return self._Cast_SpecialisedAssemblySteadyStateSynchronousResponse(self)
