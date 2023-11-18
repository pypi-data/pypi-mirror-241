"""PointLoadCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4562,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "PointLoadCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4397


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="PointLoadCompoundParametricStudyTool")


class PointLoadCompoundParametricStudyTool(
    _4562.VirtualComponentCompoundParametricStudyTool
):
    """PointLoadCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadCompoundParametricStudyTool")

    class _Cast_PointLoadCompoundParametricStudyTool:
        """Special nested class for casting PointLoadCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
            parent: "PointLoadCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4562.VirtualComponentCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def point_load_compound_parametric_study_tool(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
        ) -> "PointLoadCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "PointLoadCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.PointLoad":
        """mastapy.system_model.part_model.PointLoad

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
    ) -> "List[_4397.PointLoadParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PointLoadParametricStudyTool]

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
    ) -> "List[_4397.PointLoadParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PointLoadParametricStudyTool]

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
    ) -> "PointLoadCompoundParametricStudyTool._Cast_PointLoadCompoundParametricStudyTool":
        return self._Cast_PointLoadCompoundParametricStudyTool(self)
