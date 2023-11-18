"""ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5403


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis")


class ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis(
    _5565.CouplingHalfCompoundMultibodyDynamicsAnalysis
):
    """ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
            parent: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5565.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(
                _5603.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(_5551.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(_5605.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2580.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5403.ConceptCouplingHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConceptCouplingHalfMultibodyDynamicsAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5403.ConceptCouplingHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConceptCouplingHalfMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis(self)
