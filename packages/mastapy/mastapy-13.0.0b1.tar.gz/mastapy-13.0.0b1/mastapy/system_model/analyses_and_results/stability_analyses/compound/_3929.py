"""ConicalGearSetCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3955
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ConicalGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3794


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundStabilityAnalysis")


class ConicalGearSetCompoundStabilityAnalysis(_3955.GearSetCompoundStabilityAnalysis):
    """ConicalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetCompoundStabilityAnalysis"
    )

    class _Cast_ConicalGearSetCompoundStabilityAnalysis:
        """Special nested class for casting ConicalGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
            parent: "ConicalGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3955.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(
                _3993.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3895,
            )

            return self._parent._cast(_3895.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3901,
            )

            return self._parent._cast(
                _3901.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3908,
            )

            return self._parent._cast(
                _3908.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3913,
            )

            return self._parent._cast(_3913.BevelGearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3959,
            )

            return self._parent._cast(_3959.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(
                _3963.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(
                _3966.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3969,
            )

            return self._parent._cast(
                _3969.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(_3996.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(
                _4002.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(
                _4005.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4023,
            )

            return self._parent._cast(_4023.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "ConicalGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3794.ConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConicalGearSetStabilityAnalysis]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3794.ConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConicalGearSetStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis":
        return self._Cast_ConicalGearSetCompoundStabilityAnalysis(self)
