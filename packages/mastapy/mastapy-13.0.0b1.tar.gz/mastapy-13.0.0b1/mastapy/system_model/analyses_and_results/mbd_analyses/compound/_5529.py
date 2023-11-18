"""AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5561
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5376


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
)


class AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
    _5561.ConnectionCompoundMultibodyDynamicsAnalysis
):
    """AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5561.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(
                _5550.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(
                _5570.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(
                _5572.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(
                _5609.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5376.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5376.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
            self
        )
