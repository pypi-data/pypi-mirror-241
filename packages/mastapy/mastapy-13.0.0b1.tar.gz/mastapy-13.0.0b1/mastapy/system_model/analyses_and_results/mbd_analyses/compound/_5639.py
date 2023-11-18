"""SynchroniserCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5624
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "SynchroniserCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5502


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SynchroniserCompoundMultibodyDynamicsAnalysis")


class SynchroniserCompoundMultibodyDynamicsAnalysis(
    _5624.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
):
    """SynchroniserCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_SynchroniserCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserCompoundMultibodyDynamicsAnalysis",
            parent: "SynchroniserCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "SynchroniserCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5624.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "SynchroniserCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5526,
            )

            return self._parent._cast(
                _5526.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "SynchroniserCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(_5605.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "SynchroniserCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserCompoundMultibodyDynamicsAnalysis",
        ) -> "SynchroniserCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SynchroniserCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2600.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2600.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5502.SynchroniserMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SynchroniserMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5502.SynchroniserMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SynchroniserMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserCompoundMultibodyDynamicsAnalysis":
        return self._Cast_SynchroniserCompoundMultibodyDynamicsAnalysis(self)
