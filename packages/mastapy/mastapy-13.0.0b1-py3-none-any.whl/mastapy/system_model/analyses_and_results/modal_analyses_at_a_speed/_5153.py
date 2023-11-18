"""CouplingModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CouplingModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581


__docformat__ = "restructuredtext en"
__all__ = ("CouplingModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CouplingModalAnalysisAtASpeed")


class CouplingModalAnalysisAtASpeed(_5213.SpecialisedAssemblyModalAnalysisAtASpeed):
    """CouplingModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingModalAnalysisAtASpeed")

    class _Cast_CouplingModalAnalysisAtASpeed:
        """Special nested class for casting CouplingModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
            parent: "CouplingModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5213.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5114,
            )

            return self._parent._cast(_5114.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5137,
            )

            return self._parent._cast(_5137.ClutchModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(
                _5197.PartToPartShearCouplingModalAnalysisAtASpeed
            )

        @property
        def spring_damper_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5219,
            )

            return self._parent._cast(_5219.SpringDamperModalAnalysisAtASpeed)

        @property
        def torque_converter_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5233,
            )

            return self._parent._cast(_5233.TorqueConverterModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
        ) -> "CouplingModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2581.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

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
    ) -> "CouplingModalAnalysisAtASpeed._Cast_CouplingModalAnalysisAtASpeed":
        return self._Cast_CouplingModalAnalysisAtASpeed(self)
