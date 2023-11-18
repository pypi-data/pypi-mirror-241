"""RootAssemblyParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4300
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "RootAssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4385,
        _4387,
    )
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2901,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyParametricStudyTool",)


Self = TypeVar("Self", bound="RootAssemblyParametricStudyTool")


class RootAssemblyParametricStudyTool(_4300.AssemblyParametricStudyTool):
    """RootAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyParametricStudyTool")

    class _Cast_RootAssemblyParametricStudyTool:
        """Special nested class for casting RootAssemblyParametricStudyTool to subclasses."""

        def __init__(
            self: "RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool",
            parent: "RootAssemblyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def assembly_parametric_study_tool(
            self: "RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool",
        ):
            return self._parent._cast(_4300.AssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4293,
            )

            return self._parent._cast(_4293.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def root_assembly_parametric_study_tool(
            self: "RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool",
        ) -> "RootAssemblyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RootAssemblyParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2472.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parametric_study_tool_inputs(self: Self) -> "_4385.ParametricStudyTool":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyTool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricStudyToolInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_for_reporting(
        self: Self,
    ) -> "_4387.ParametricStudyToolResultsForReporting":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyToolResultsForReporting

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForReporting

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def root_assembly_duty_cycle_results(
        self: Self,
    ) -> "List[_2901.DutyCycleEfficiencyResults]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.DutyCycleEfficiencyResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootAssemblyDutyCycleResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyParametricStudyTool._Cast_RootAssemblyParametricStudyTool":
        return self._Cast_RootAssemblyParametricStudyTool(self)
