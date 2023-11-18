"""ShaftCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5527
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ShaftCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2480
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5483


__docformat__ = "restructuredtext en"
__all__ = ("ShaftCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ShaftCompoundMultibodyDynamicsAnalysis")


class ShaftCompoundMultibodyDynamicsAnalysis(
    _5527.AbstractShaftCompoundMultibodyDynamicsAnalysis
):
    """ShaftCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ShaftCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ShaftCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ShaftCompoundMultibodyDynamicsAnalysis._Cast_ShaftCompoundMultibodyDynamicsAnalysis",
            parent: "ShaftCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "ShaftCompoundMultibodyDynamicsAnalysis._Cast_ShaftCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5527.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "ShaftCompoundMultibodyDynamicsAnalysis._Cast_ShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5528,
            )

            return self._parent._cast(
                _5528.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "ShaftCompoundMultibodyDynamicsAnalysis._Cast_ShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(_5551.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ShaftCompoundMultibodyDynamicsAnalysis._Cast_ShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(_5605.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ShaftCompoundMultibodyDynamicsAnalysis._Cast_ShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftCompoundMultibodyDynamicsAnalysis._Cast_ShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftCompoundMultibodyDynamicsAnalysis._Cast_ShaftCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "ShaftCompoundMultibodyDynamicsAnalysis._Cast_ShaftCompoundMultibodyDynamicsAnalysis",
        ) -> "ShaftCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftCompoundMultibodyDynamicsAnalysis._Cast_ShaftCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ShaftCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2480.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

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
    ) -> "List[_5483.ShaftMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ShaftMultibodyDynamicsAnalysis]

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
    def planetaries(self: Self) -> "List[ShaftCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ShaftCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5483.ShaftMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ShaftMultibodyDynamicsAnalysis]

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
    ) -> "ShaftCompoundMultibodyDynamicsAnalysis._Cast_ShaftCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ShaftCompoundMultibodyDynamicsAnalysis(self)
