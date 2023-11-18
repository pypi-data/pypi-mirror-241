"""FEPartParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "FEPartParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.analyses_and_results.static_loads import _6885
    from mastapy.system_model.analyses_and_results.system_deflections import _2755


__docformat__ = "restructuredtext en"
__all__ = ("FEPartParametricStudyTool",)


Self = TypeVar("Self", bound="FEPartParametricStudyTool")


class FEPartParametricStudyTool(_4294.AbstractShaftOrHousingParametricStudyTool):
    """FEPartParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _FE_PART_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartParametricStudyTool")

    class _Cast_FEPartParametricStudyTool:
        """Special nested class for casting FEPartParametricStudyTool to subclasses."""

        def __init__(
            self: "FEPartParametricStudyTool._Cast_FEPartParametricStudyTool",
            parent: "FEPartParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "FEPartParametricStudyTool._Cast_FEPartParametricStudyTool",
        ):
            return self._parent._cast(_4294.AbstractShaftOrHousingParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "FEPartParametricStudyTool._Cast_FEPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "FEPartParametricStudyTool._Cast_FEPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "FEPartParametricStudyTool._Cast_FEPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartParametricStudyTool._Cast_FEPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartParametricStudyTool._Cast_FEPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartParametricStudyTool._Cast_FEPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def fe_part_parametric_study_tool(
            self: "FEPartParametricStudyTool._Cast_FEPartParametricStudyTool",
        ) -> "FEPartParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "FEPartParametricStudyTool._Cast_FEPartParametricStudyTool", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2451.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6885.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

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
    ) -> "List[_2755.FEPartSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection]

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
    def planetaries(self: Self) -> "List[FEPartParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.FEPartParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FEPartParametricStudyTool._Cast_FEPartParametricStudyTool":
        return self._Cast_FEPartParametricStudyTool(self)
