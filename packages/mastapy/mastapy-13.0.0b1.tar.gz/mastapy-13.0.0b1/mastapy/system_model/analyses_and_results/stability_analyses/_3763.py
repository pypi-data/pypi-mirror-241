"""AbstractShaftStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3762
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AbstractShaftStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2433


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftStabilityAnalysis")


class AbstractShaftStabilityAnalysis(_3762.AbstractShaftOrHousingStabilityAnalysis):
    """AbstractShaftStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftStabilityAnalysis")

    class _Cast_AbstractShaftStabilityAnalysis:
        """Special nested class for casting AbstractShaftStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
            parent: "AbstractShaftStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ):
            return self._parent._cast(_3762.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3808,
            )

            return self._parent._cast(_3808.CycloidalDiscStabilityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(_3859.ShaftStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
        ) -> "AbstractShaftStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftStabilityAnalysis.TYPE"):
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
    ) -> "AbstractShaftStabilityAnalysis._Cast_AbstractShaftStabilityAnalysis":
        return self._Cast_AbstractShaftStabilityAnalysis(self)
