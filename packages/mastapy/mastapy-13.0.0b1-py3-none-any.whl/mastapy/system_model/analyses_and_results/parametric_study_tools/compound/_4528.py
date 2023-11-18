"""PulleyCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4479,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "PulleyCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4399


__docformat__ = "restructuredtext en"
__all__ = ("PulleyCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="PulleyCompoundParametricStudyTool")


class PulleyCompoundParametricStudyTool(_4479.CouplingHalfCompoundParametricStudyTool):
    """PulleyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyCompoundParametricStudyTool")

    class _Cast_PulleyCompoundParametricStudyTool:
        """Special nested class for casting PulleyCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool",
            parent: "PulleyCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4479.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.CVTPulleyCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool",
        ) -> "PulleyCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "PulleyCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

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
    ) -> "List[_4399.PulleyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PulleyParametricStudyTool]

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
    def component_analysis_cases(self: Self) -> "List[_4399.PulleyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PulleyParametricStudyTool]

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
    ) -> "PulleyCompoundParametricStudyTool._Cast_PulleyCompoundParametricStudyTool":
        return self._Cast_PulleyCompoundParametricStudyTool(self)
