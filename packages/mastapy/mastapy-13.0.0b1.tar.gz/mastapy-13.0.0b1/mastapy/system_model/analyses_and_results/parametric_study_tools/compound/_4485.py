"""CycloidalDiscCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4441,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CycloidalDiscCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2567
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4338


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundParametricStudyTool")


class CycloidalDiscCompoundParametricStudyTool(
    _4441.AbstractShaftCompoundParametricStudyTool
):
    """CycloidalDiscCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCompoundParametricStudyTool"
    )

    class _Cast_CycloidalDiscCompoundParametricStudyTool:
        """Special nested class for casting CycloidalDiscCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
            parent: "CycloidalDiscCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4441.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4442,
            )

            return self._parent._cast(
                _4442.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
        ) -> "CycloidalDiscCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "CycloidalDiscCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4338.CycloidalDiscParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CycloidalDiscParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4338.CycloidalDiscParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CycloidalDiscParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCompoundParametricStudyTool._Cast_CycloidalDiscCompoundParametricStudyTool":
        return self._Cast_CycloidalDiscCompoundParametricStudyTool(self)
