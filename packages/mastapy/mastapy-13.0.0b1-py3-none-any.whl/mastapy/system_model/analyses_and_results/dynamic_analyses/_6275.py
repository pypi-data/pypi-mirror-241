"""AbstractShaftDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AbstractShaftDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2433


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftDynamicAnalysis")


class AbstractShaftDynamicAnalysis(_6276.AbstractShaftOrHousingDynamicAnalysis):
    """AbstractShaftDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftDynamicAnalysis")

    class _Cast_AbstractShaftDynamicAnalysis:
        """Special nested class for casting AbstractShaftDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
            parent: "AbstractShaftDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ):
            return self._parent._cast(_6276.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.CycloidalDiscDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.ShaftDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
        ) -> "AbstractShaftDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2433.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftDynamicAnalysis._Cast_AbstractShaftDynamicAnalysis":
        return self._Cast_AbstractShaftDynamicAnalysis(self)
