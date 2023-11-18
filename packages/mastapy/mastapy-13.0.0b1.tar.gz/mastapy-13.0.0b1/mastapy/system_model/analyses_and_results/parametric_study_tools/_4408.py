"""ShaftToMountableComponentConnectionParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4296
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ShaftToMountableComponentConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2293


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionParametricStudyTool")


class ShaftToMountableComponentConnectionParametricStudyTool(
    _4296.AbstractShaftToMountableComponentConnectionParametricStudyTool
):
    """ShaftToMountableComponentConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionParametricStudyTool",
    )

    class _Cast_ShaftToMountableComponentConnectionParametricStudyTool:
        """Special nested class for casting ShaftToMountableComponentConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
            parent: "ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            return self._parent._cast(
                _4296.AbstractShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def coaxial_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.CoaxialConnectionParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(
                _4337.CycloidalDiscCentralBearingConnectionParametricStudyTool
            )

        @property
        def planetary_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(_4394.PlanetaryConnectionParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
        ) -> "ShaftToMountableComponentConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2293.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionParametricStudyTool._Cast_ShaftToMountableComponentConnectionParametricStudyTool":
        return self._Cast_ShaftToMountableComponentConnectionParametricStudyTool(self)
