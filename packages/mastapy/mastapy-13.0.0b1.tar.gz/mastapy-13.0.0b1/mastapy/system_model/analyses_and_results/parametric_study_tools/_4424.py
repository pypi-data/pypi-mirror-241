"""SynchroniserHalfParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4426
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SynchroniserHalfParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.static_loads import _6965
    from mastapy.system_model.analyses_and_results.system_deflections import _2819


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfParametricStudyTool",)


Self = TypeVar("Self", bound="SynchroniserHalfParametricStudyTool")


class SynchroniserHalfParametricStudyTool(_4426.SynchroniserPartParametricStudyTool):
    """SynchroniserHalfParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserHalfParametricStudyTool")

    class _Cast_SynchroniserHalfParametricStudyTool:
        """Special nested class for casting SynchroniserHalfParametricStudyTool to subclasses."""

        def __init__(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
            parent: "SynchroniserHalfParametricStudyTool",
        ):
            self._parent = parent

        @property
        def synchroniser_part_parametric_study_tool(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
        ):
            return self._parent._cast(_4426.SynchroniserPartParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
        ) -> "SynchroniserHalfParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool",
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
        self: Self, instance_to_wrap: "SynchroniserHalfParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2602.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6965.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2819.SynchroniserHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "SynchroniserHalfParametricStudyTool._Cast_SynchroniserHalfParametricStudyTool"
    ):
        return self._Cast_SynchroniserHalfParametricStudyTool(self)
