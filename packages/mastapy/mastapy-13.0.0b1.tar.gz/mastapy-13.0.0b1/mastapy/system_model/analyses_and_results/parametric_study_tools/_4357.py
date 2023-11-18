"""FlexiblePinAssemblyParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4409
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "FlexiblePinAssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.static_loads import _6886
    from mastapy.system_model.analyses_and_results.system_deflections import _2756


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyParametricStudyTool",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyParametricStudyTool")


class FlexiblePinAssemblyParametricStudyTool(
    _4409.SpecialisedAssemblyParametricStudyTool
):
    """FlexiblePinAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyParametricStudyTool"
    )

    class _Cast_FlexiblePinAssemblyParametricStudyTool:
        """Special nested class for casting FlexiblePinAssemblyParametricStudyTool to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyParametricStudyTool._Cast_FlexiblePinAssemblyParametricStudyTool",
            parent: "FlexiblePinAssemblyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def specialised_assembly_parametric_study_tool(
            self: "FlexiblePinAssemblyParametricStudyTool._Cast_FlexiblePinAssemblyParametricStudyTool",
        ):
            return self._parent._cast(_4409.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "FlexiblePinAssemblyParametricStudyTool._Cast_FlexiblePinAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4293,
            )

            return self._parent._cast(_4293.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "FlexiblePinAssemblyParametricStudyTool._Cast_FlexiblePinAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyParametricStudyTool._Cast_FlexiblePinAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyParametricStudyTool._Cast_FlexiblePinAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyParametricStudyTool._Cast_FlexiblePinAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyParametricStudyTool._Cast_FlexiblePinAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "FlexiblePinAssemblyParametricStudyTool._Cast_FlexiblePinAssemblyParametricStudyTool",
        ) -> "FlexiblePinAssemblyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyParametricStudyTool._Cast_FlexiblePinAssemblyParametricStudyTool",
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
        self: Self, instance_to_wrap: "FlexiblePinAssemblyParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2452.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6886.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2756.FlexiblePinAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyParametricStudyTool._Cast_FlexiblePinAssemblyParametricStudyTool":
        return self._Cast_FlexiblePinAssemblyParametricStudyTool(self)
