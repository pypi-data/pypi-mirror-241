"""CycloidalDiscDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6275
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CycloidalDiscDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2567
    from mastapy.system_model.analyses_and_results.static_loads import _6857


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscDynamicAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscDynamicAnalysis")


class CycloidalDiscDynamicAnalysis(_6275.AbstractShaftDynamicAnalysis):
    """CycloidalDiscDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscDynamicAnalysis")

    class _Cast_CycloidalDiscDynamicAnalysis:
        """Special nested class for casting CycloidalDiscDynamicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
            parent: "CycloidalDiscDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_dynamic_analysis(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
        ):
            return self._parent._cast(_6275.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276

            return self._parent._cast(_6276.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
        ) -> "CycloidalDiscDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscDynamicAnalysis.TYPE"):
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
    def component_load_case(self: Self) -> "_6857.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscDynamicAnalysis._Cast_CycloidalDiscDynamicAnalysis":
        return self._Cast_CycloidalDiscDynamicAnalysis(self)
