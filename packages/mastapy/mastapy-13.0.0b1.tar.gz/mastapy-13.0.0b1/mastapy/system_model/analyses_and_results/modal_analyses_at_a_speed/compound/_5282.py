"""CouplingConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5309,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CouplingConnectionCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5151,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundModalAnalysisAtASpeed")


class CouplingConnectionCompoundModalAnalysisAtASpeed(
    _5309.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
):
    """CouplingConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CouplingConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CouplingConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
            parent: "CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5309.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5279,
            )

            return self._parent._cast(_5279.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5266,
            )

            return self._parent._cast(
                _5266.ClutchConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(
                _5271.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(
                _5325.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpringDamperConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(
                _5362.TorqueConverterConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "CouplingConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "CouplingConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5151.CouplingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CouplingConnectionModalAnalysisAtASpeed]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5151.CouplingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CouplingConnectionModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed(self)
