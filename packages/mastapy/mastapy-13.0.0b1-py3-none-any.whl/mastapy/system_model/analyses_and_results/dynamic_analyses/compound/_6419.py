"""BevelDifferentialPlanetGearCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6416
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BevelDifferentialPlanetGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCompoundDynamicAnalysis")


class BevelDifferentialPlanetGearCompoundDynamicAnalysis(
    _6416.BevelDifferentialGearCompoundDynamicAnalysis
):
    """BevelDifferentialPlanetGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
            parent: "BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            return self._parent._cast(
                _6416.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(_6421.BevelGearCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6409,
            )

            return self._parent._cast(
                _6409.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6437,
            )

            return self._parent._cast(_6437.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6463,
            )

            return self._parent._cast(_6463.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
        ) -> "BevelDifferentialPlanetGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6288.BevelDifferentialPlanetGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialPlanetGearDynamicAnalysis]

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
    ) -> "List[_6288.BevelDifferentialPlanetGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialPlanetGearDynamicAnalysis]

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
    ) -> "BevelDifferentialPlanetGearCompoundDynamicAnalysis._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis":
        return self._Cast_BevelDifferentialPlanetGearCompoundDynamicAnalysis(self)
