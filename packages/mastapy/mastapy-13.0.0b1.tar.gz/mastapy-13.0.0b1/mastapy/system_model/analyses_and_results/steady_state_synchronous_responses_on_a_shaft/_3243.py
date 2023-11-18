"""AbstractAssemblySteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3322,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2432


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblySteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="AbstractAssemblySteadyStateSynchronousResponseOnAShaft")


class AbstractAssemblySteadyStateSynchronousResponseOnAShaft(
    _3322.PartSteadyStateSynchronousResponseOnAShaft
):
    """AbstractAssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AbstractAssemblySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
            parent: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(_3322.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3248,
            )

            return self._parent._cast(
                _3248.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3250,
            )

            return self._parent._cast(
                _3250.AssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3253,
            )

            return self._parent._cast(
                _3253.BeltDriveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3255,
            )

            return self._parent._cast(
                _3255.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3260,
            )

            return self._parent._cast(
                _3260.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3262,
            )

            return self._parent._cast(
                _3262.BoltedJointSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3266,
            )

            return self._parent._cast(
                _3266.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3271,
            )

            return self._parent._cast(
                _3271.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.ConceptGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3276,
            )

            return self._parent._cast(
                _3276.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3282,
            )

            return self._parent._cast(
                _3282.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3285,
            )

            return self._parent._cast(_3285.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3286,
            )

            return self._parent._cast(
                _3286.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3297,
            )

            return self._parent._cast(
                _3297.FaceGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3300,
            )

            return self._parent._cast(
                _3300.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(
                _3302.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3306,
            )

            return self._parent._cast(
                _3306.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3310,
            )

            return self._parent._cast(
                _3310.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3313,
            )

            return self._parent._cast(
                _3313.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3316,
            )

            return self._parent._cast(
                _3316.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3325,
            )

            return self._parent._cast(
                _3325.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3334,
            )

            return self._parent._cast(
                _3334.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3337,
            )

            return self._parent._cast(
                _3337.RootAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(
                _3347.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3350,
            )

            return self._parent._cast(
                _3350.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3353,
            )

            return self._parent._cast(
                _3353.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3360,
            )

            return self._parent._cast(
                _3360.SynchroniserSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3363,
            )

            return self._parent._cast(
                _3363.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3368,
            )

            return self._parent._cast(
                _3368.WormGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3371,
            )

            return self._parent._cast(
                _3371.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AbstractAssemblySteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2432.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2432.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

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
    ) -> "AbstractAssemblySteadyStateSynchronousResponseOnAShaft._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
        return self._Cast_AbstractAssemblySteadyStateSynchronousResponseOnAShaft(self)
