"""TorqueConverterConnectionParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4330
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "TorqueConverterConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2350
    from mastapy.system_model.analyses_and_results.static_loads import _6970
    from mastapy.system_model.analyses_and_results.system_deflections import _2826


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="TorqueConverterConnectionParametricStudyTool")


class TorqueConverterConnectionParametricStudyTool(
    _4330.CouplingConnectionParametricStudyTool
):
    """TorqueConverterConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionParametricStudyTool"
    )

    class _Cast_TorqueConverterConnectionParametricStudyTool:
        """Special nested class for casting TorqueConverterConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool",
            parent: "TorqueConverterConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_connection_parametric_study_tool(
            self: "TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool",
        ):
            return self._parent._cast(_4330.CouplingConnectionParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(
                _4365.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_connection_parametric_study_tool(
            self: "TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool",
        ) -> "TorqueConverterConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool",
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
        instance_to_wrap: "TorqueConverterConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2350.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6970.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2826.TorqueConverterConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool":
        return self._Cast_TorqueConverterConnectionParametricStudyTool(self)
