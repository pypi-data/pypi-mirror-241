"""CVTBeltConnectionCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3904
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CVTBeltConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3802


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundStabilityAnalysis")


class CVTBeltConnectionCompoundStabilityAnalysis(
    _3904.BeltConnectionCompoundStabilityAnalysis
):
    """CVTBeltConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundStabilityAnalysis"
    )

    class _Cast_CVTBeltConnectionCompoundStabilityAnalysis:
        """Special nested class for casting CVTBeltConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundStabilityAnalysis._Cast_CVTBeltConnectionCompoundStabilityAnalysis",
            parent: "CVTBeltConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_stability_analysis(
            self: "CVTBeltConnectionCompoundStabilityAnalysis._Cast_CVTBeltConnectionCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3904.BeltConnectionCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "CVTBeltConnectionCompoundStabilityAnalysis._Cast_CVTBeltConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(
                _3960.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "CVTBeltConnectionCompoundStabilityAnalysis._Cast_CVTBeltConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundStabilityAnalysis._Cast_CVTBeltConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundStabilityAnalysis._Cast_CVTBeltConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundStabilityAnalysis._Cast_CVTBeltConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_stability_analysis(
            self: "CVTBeltConnectionCompoundStabilityAnalysis._Cast_CVTBeltConnectionCompoundStabilityAnalysis",
        ) -> "CVTBeltConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundStabilityAnalysis._Cast_CVTBeltConnectionCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3802.CVTBeltConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CVTBeltConnectionStabilityAnalysis]

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
    ) -> "List[_3802.CVTBeltConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CVTBeltConnectionStabilityAnalysis]

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
    ) -> "CVTBeltConnectionCompoundStabilityAnalysis._Cast_CVTBeltConnectionCompoundStabilityAnalysis":
        return self._Cast_CVTBeltConnectionCompoundStabilityAnalysis(self)
