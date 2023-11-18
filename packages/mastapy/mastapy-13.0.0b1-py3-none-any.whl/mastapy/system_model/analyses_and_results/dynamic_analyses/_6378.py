"""SpringDamperConnectionDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "SpringDamperConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.static_loads import _6954


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="SpringDamperConnectionDynamicAnalysis")


class SpringDamperConnectionDynamicAnalysis(_6311.CouplingConnectionDynamicAnalysis):
    """SpringDamperConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionDynamicAnalysis"
    )

    class _Cast_SpringDamperConnectionDynamicAnalysis:
        """Special nested class for casting SpringDamperConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
            parent: "SpringDamperConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_dynamic_analysis(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
        ):
            return self._parent._cast(_6311.CouplingConnectionDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(
                _6341.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_connection_dynamic_analysis(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
        ) -> "SpringDamperConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperConnectionDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2348.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6954.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperConnectionDynamicAnalysis._Cast_SpringDamperConnectionDynamicAnalysis":
        return self._Cast_SpringDamperConnectionDynamicAnalysis(self)
