"""TorqueConverterCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "TorqueConverterCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5507


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterCompoundMultibodyDynamicsAnalysis")


class TorqueConverterCompoundMultibodyDynamicsAnalysis(
    _5563.CouplingCompoundMultibodyDynamicsAnalysis
):
    """TorqueConverterCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting TorqueConverterCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis",
            parent: "TorqueConverterCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "TorqueConverterCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5563.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "TorqueConverterCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(
                _5624.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "TorqueConverterCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5526,
            )

            return self._parent._cast(
                _5526.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "TorqueConverterCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(_5605.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "TorqueConverterCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "TorqueConverterCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis",
        ) -> "TorqueConverterCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "TorqueConverterCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2605.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

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
    ) -> "List[_5507.TorqueConverterMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.TorqueConverterMultibodyDynamicsAnalysis]

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
    ) -> "List[_5507.TorqueConverterMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.TorqueConverterMultibodyDynamicsAnalysis]

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
    ) -> "TorqueConverterCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis":
        return self._Cast_TorqueConverterCompoundMultibodyDynamicsAnalysis(self)
