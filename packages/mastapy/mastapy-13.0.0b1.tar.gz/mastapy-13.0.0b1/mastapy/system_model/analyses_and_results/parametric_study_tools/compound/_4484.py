"""CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4464,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4337


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"
)


class CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool(
    _4464.CoaxialConnectionCompoundParametricStudyTool
):
    """CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
            parent: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4464.CoaxialConnectionCompoundParametricStudyTool
            )

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(
                _4537.ShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(
                _4443.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4337.CycloidalDiscCentralBearingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CycloidalDiscCentralBearingConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4337.CycloidalDiscCentralBearingConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CycloidalDiscCentralBearingConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool":
        return (
            self._Cast_CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool(
                self
            )
        )
