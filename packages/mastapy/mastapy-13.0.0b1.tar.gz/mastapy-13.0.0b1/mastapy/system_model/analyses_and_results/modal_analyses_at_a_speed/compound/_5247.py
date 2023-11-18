"""AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5279,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5117,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
)


class AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed(
    _5279.ConnectionCompoundModalAnalysisAtASpeed
):
    """AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
            parent: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5279.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(
                _5268.CoaxialConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(
                _5288.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(
                _5290.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.PlanetaryConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(
                _5341.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5117.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5117.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed]

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
    ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed(
            self
        )
