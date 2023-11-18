"""SpringDamperHalfCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5491


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpringDamperHalfCompoundMultibodyDynamicsAnalysis")


class SpringDamperHalfCompoundMultibodyDynamicsAnalysis(
    _5565.CouplingHalfCompoundMultibodyDynamicsAnalysis
):
    """SpringDamperHalfCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SpringDamperHalfCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
            parent: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5565.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(
                _5603.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(_5551.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(_5605.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "SpringDamperHalfCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SpringDamperHalfCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2599.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

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
    ) -> "List[_5491.SpringDamperHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpringDamperHalfMultibodyDynamicsAnalysis]

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
    ) -> "List[_5491.SpringDamperHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpringDamperHalfMultibodyDynamicsAnalysis]

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
    ) -> "SpringDamperHalfCompoundMultibodyDynamicsAnalysis._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis":
        return self._Cast_SpringDamperHalfCompoundMultibodyDynamicsAnalysis(self)
