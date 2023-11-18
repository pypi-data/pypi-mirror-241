"""ShaftToMountableComponentConnectionCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4728
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ShaftToMountableComponentConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4678


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionCompoundModalAnalysis")


class ShaftToMountableComponentConnectionCompoundModalAnalysis(
    _4728.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
):
    """ShaftToMountableComponentConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
            parent: "ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            return self._parent._cast(
                _4728.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.CoaxialConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(
                _4769.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
            )

        @property
        def planetary_connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(_4808.PlanetaryConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "ShaftToMountableComponentConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4678.ShaftToMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ShaftToMountableComponentConnectionModalAnalysis]

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
    ) -> "List[_4678.ShaftToMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ShaftToMountableComponentConnectionModalAnalysis]

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
    ) -> "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis(self)
