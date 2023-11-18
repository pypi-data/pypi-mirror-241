"""AbstractAssemblyModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5194
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "AbstractAssemblyModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2432


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AbstractAssemblyModalAnalysisAtASpeed")


class AbstractAssemblyModalAnalysisAtASpeed(_5194.PartModalAnalysisAtASpeed):
    """AbstractAssemblyModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyModalAnalysisAtASpeed"
    )

    class _Cast_AbstractAssemblyModalAnalysisAtASpeed:
        """Special nested class for casting AbstractAssemblyModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
            parent: "AbstractAssemblyModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def part_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5194.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5120,
            )

            return self._parent._cast(
                _5120.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def assembly_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5121,
            )

            return self._parent._cast(_5121.AssemblyModalAnalysisAtASpeed)

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5124,
            )

            return self._parent._cast(_5124.BeltDriveModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5127,
            )

            return self._parent._cast(
                _5127.BevelDifferentialGearSetModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5132,
            )

            return self._parent._cast(_5132.BevelGearSetModalAnalysisAtASpeed)

        @property
        def bolted_joint_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5133,
            )

            return self._parent._cast(_5133.BoltedJointModalAnalysisAtASpeed)

        @property
        def clutch_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5137,
            )

            return self._parent._cast(_5137.ClutchModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def concept_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(_5145.ConceptGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5153,
            )

            return self._parent._cast(_5153.CouplingModalAnalysisAtASpeed)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(_5155.CVTModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5157,
            )

            return self._parent._cast(_5157.CycloidalAssemblyModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def face_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5169,
            )

            return self._parent._cast(_5169.FaceGearSetModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5171,
            )

            return self._parent._cast(_5171.FlexiblePinAssemblyModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5174,
            )

            return self._parent._cast(_5174.GearSetModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5178,
            )

            return self._parent._cast(_5178.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(
                _5182.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5185,
            )

            return self._parent._cast(
                _5185.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(
                _5188.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(
                _5197.PartToPartShearCouplingModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5206,
            )

            return self._parent._cast(_5206.RollingRingAssemblyModalAnalysisAtASpeed)

        @property
        def root_assembly_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5209,
            )

            return self._parent._cast(_5209.RootAssemblyModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def spring_damper_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5219,
            )

            return self._parent._cast(_5219.SpringDamperModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5222,
            )

            return self._parent._cast(
                _5222.StraightBevelDiffGearSetModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5225,
            )

            return self._parent._cast(_5225.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def synchroniser_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5229,
            )

            return self._parent._cast(_5229.SynchroniserModalAnalysisAtASpeed)

        @property
        def torque_converter_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5233,
            )

            return self._parent._cast(_5233.TorqueConverterModalAnalysisAtASpeed)

        @property
        def worm_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5240,
            )

            return self._parent._cast(_5240.WormGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5243,
            )

            return self._parent._cast(_5243.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
        ) -> "AbstractAssemblyModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "AbstractAssemblyModalAnalysisAtASpeed.TYPE"
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
    ) -> "AbstractAssemblyModalAnalysisAtASpeed._Cast_AbstractAssemblyModalAnalysisAtASpeed":
        return self._Cast_AbstractAssemblyModalAnalysisAtASpeed(self)
