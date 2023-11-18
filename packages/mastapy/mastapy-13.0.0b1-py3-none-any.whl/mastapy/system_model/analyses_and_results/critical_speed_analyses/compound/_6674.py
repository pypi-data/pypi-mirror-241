"""AbstractShaftOrHousingCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6697,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6542


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundCriticalSpeedAnalysis")


class AbstractShaftOrHousingCompoundCriticalSpeedAnalysis(
    _6697.ComponentCompoundCriticalSpeedAnalysis
):
    """AbstractShaftOrHousingCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis"
    )

    class _Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
            parent: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6697.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(_6751.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6673,
            )

            return self._parent._cast(_6673.AbstractShaftCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6717,
            )

            return self._parent._cast(_6717.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6728,
            )

            return self._parent._cast(_6728.FEPartCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6767,
            )

            return self._parent._cast(_6767.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ) -> "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6542.AbstractShaftOrHousingCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractShaftOrHousingCriticalSpeedAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6542.AbstractShaftOrHousingCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractShaftOrHousingCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
        return self._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis(self)
