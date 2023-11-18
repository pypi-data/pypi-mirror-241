"""CVTBeltConnectionCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _4994,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4894,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundModalAnalysisAtAStiffness")


class CVTBeltConnectionCompoundModalAnalysisAtAStiffness(
    _4994.BeltConnectionCompoundModalAnalysisAtAStiffness
):
    """CVTBeltConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CVTBeltConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
            parent: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4994.BeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5050,
            )

            return self._parent._cast(
                _5050.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5020,
            )

            return self._parent._cast(_5020.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "CVTBeltConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CVTBeltConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4894.CVTBeltConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CVTBeltConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4894.CVTBeltConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CVTBeltConnectionModalAnalysisAtAStiffness]

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
    ) -> "CVTBeltConnectionCompoundModalAnalysisAtAStiffness._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_CVTBeltConnectionCompoundModalAnalysisAtAStiffness(self)
