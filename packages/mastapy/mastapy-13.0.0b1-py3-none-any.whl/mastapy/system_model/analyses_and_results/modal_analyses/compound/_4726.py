"""AbstractShaftCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4727
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AbstractShaftCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4570


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundModalAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundModalAnalysis")


class AbstractShaftCompoundModalAnalysis(
    _4727.AbstractShaftOrHousingCompoundModalAnalysis
):
    """AbstractShaftCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftCompoundModalAnalysis")

    class _Cast_AbstractShaftCompoundModalAnalysis:
        """Special nested class for casting AbstractShaftCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
            parent: "AbstractShaftCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            return self._parent._cast(_4727.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4770,
            )

            return self._parent._cast(_4770.CycloidalDiscCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(_4820.ShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ) -> "AbstractShaftCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4570.AbstractShaftModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftModalAnalysis]

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
    ) -> "List[_4570.AbstractShaftModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftModalAnalysis]

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
    ) -> "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis":
        return self._Cast_AbstractShaftCompoundModalAnalysis(self)
