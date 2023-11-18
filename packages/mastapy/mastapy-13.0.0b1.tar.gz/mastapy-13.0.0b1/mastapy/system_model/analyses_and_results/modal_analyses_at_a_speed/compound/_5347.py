"""SpringDamperConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5282,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "SpringDamperConnectionCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5217,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpringDamperConnectionCompoundModalAnalysisAtASpeed")


class SpringDamperConnectionCompoundModalAnalysisAtASpeed(
    _5282.CouplingConnectionCompoundModalAnalysisAtASpeed
):
    """SpringDamperConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed"
    )

    class _Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SpringDamperConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
            parent: "SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5282.CouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(
                _5309.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5279,
            )

            return self._parent._cast(_5279.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
        ) -> "SpringDamperConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "SpringDamperConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2348.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5217.SpringDamperConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpringDamperConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5217.SpringDamperConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpringDamperConnectionModalAnalysisAtASpeed]

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
    ) -> "SpringDamperConnectionCompoundModalAnalysisAtASpeed._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_SpringDamperConnectionCompoundModalAnalysisAtASpeed(self)
