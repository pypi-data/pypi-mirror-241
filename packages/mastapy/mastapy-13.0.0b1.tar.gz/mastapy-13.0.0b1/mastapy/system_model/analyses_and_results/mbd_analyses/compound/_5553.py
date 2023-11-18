"""ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2342
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5402


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis"
)


class ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis(
    _5564.CouplingConnectionCompoundMultibodyDynamicsAnalysis
):
    """ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5564.CouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(
                _5591.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(_5561.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2342.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2342.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

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
    ) -> "List[_5402.ConceptCouplingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConceptCouplingConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5402.ConceptCouplingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConceptCouplingConnectionMultibodyDynamicsAnalysis]

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
    ) -> "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis(
            self
        )
