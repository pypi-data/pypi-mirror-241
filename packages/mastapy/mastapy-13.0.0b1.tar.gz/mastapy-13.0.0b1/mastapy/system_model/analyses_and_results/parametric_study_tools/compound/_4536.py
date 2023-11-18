"""ShaftHubConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4476,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ShaftHubConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4406


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ShaftHubConnectionCompoundParametricStudyTool")


class ShaftHubConnectionCompoundParametricStudyTool(
    _4476.ConnectorCompoundParametricStudyTool
):
    """ShaftHubConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHubConnectionCompoundParametricStudyTool"
    )

    class _Cast_ShaftHubConnectionCompoundParametricStudyTool:
        """Special nested class for casting ShaftHubConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool",
            parent: "ShaftHubConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def connector_compound_parametric_study_tool(
            self: "ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4476.ConnectorCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool",
        ) -> "ShaftHubConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "ShaftHubConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2596.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

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
    ) -> "List[_4406.ShaftHubConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftHubConnectionParametricStudyTool]

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
    def planetaries(
        self: Self,
    ) -> "List[ShaftHubConnectionCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ShaftHubConnectionCompoundParametricStudyTool]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4406.ShaftHubConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ShaftHubConnectionParametricStudyTool]

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
    ) -> "ShaftHubConnectionCompoundParametricStudyTool._Cast_ShaftHubConnectionCompoundParametricStudyTool":
        return self._Cast_ShaftHubConnectionCompoundParametricStudyTool(self)
