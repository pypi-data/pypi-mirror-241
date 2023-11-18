"""AbstractShaftOrHousingStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3786
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AbstractShaftOrHousingStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2434


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingStabilityAnalysis")


class AbstractShaftOrHousingStabilityAnalysis(_3786.ComponentStabilityAnalysis):
    """AbstractShaftOrHousingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingStabilityAnalysis"
    )

    class _Cast_AbstractShaftOrHousingStabilityAnalysis:
        """Special nested class for casting AbstractShaftOrHousingStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
            parent: "AbstractShaftOrHousingStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3763,
            )

            return self._parent._cast(_3763.AbstractShaftStabilityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3808,
            )

            return self._parent._cast(_3808.CycloidalDiscStabilityAnalysis)

        @property
        def fe_part_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.FEPartStabilityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(_3859.ShaftStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ) -> "AbstractShaftOrHousingStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2434.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis":
        return self._Cast_AbstractShaftOrHousingStabilityAnalysis(self)
