"""KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.stability_analyses import _3834


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis(
    _3961.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(
                _3961.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2536.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

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
    ) -> "List[_3834.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis]

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
    ) -> "List[_3834.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis(
            self
        )
