"""SpecialisedAssemblyCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5244,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5213,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundModalAnalysisAtASpeed")


class SpecialisedAssemblyCompoundModalAnalysisAtASpeed(
    _5244.AbstractAssemblyCompoundModalAnalysisAtASpeed
):
    """SpecialisedAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed"
    )

    class _Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SpecialisedAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
            parent: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5244.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(_5323.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5250,
            )

            return self._parent._cast(
                _5250.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5254,
            )

            return self._parent._cast(_5254.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5257,
            )

            return self._parent._cast(
                _5257.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5262,
            )

            return self._parent._cast(_5262.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5264,
            )

            return self._parent._cast(_5264.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5265,
            )

            return self._parent._cast(_5265.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(
                _5270.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5275,
            )

            return self._parent._cast(_5275.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(_5281.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(_5285.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5287,
            )

            return self._parent._cast(
                _5287.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(
                _5293.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5299,
            )

            return self._parent._cast(_5299.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5301,
            )

            return self._parent._cast(
                _5301.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(_5304.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5308,
            )

            return self._parent._cast(_5308.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(
                _5312.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(
                _5315.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5318,
            )

            return self._parent._cast(
                _5318.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5324,
            )

            return self._parent._cast(
                _5324.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(
                _5328.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(
                _5335.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5346,
            )

            return self._parent._cast(_5346.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5351,
            )

            return self._parent._cast(
                _5351.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(_5357.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5361,
            )

            return self._parent._cast(
                _5361.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(_5369.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5372,
            )

            return self._parent._cast(
                _5372.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5213.SpecialisedAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpecialisedAssemblyModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5213.SpecialisedAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpecialisedAssemblyModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundModalAnalysisAtASpeed._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
        return self._Cast_SpecialisedAssemblyCompoundModalAnalysisAtASpeed(self)
