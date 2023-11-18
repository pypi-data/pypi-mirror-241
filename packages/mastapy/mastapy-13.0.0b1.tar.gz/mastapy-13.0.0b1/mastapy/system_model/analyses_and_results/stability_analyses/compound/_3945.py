"""CylindricalPlanetGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3942
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CylindricalPlanetGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3812


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundStabilityAnalysis")


class CylindricalPlanetGearCompoundStabilityAnalysis(
    _3942.CylindricalGearCompoundStabilityAnalysis
):
    """CylindricalPlanetGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCompoundStabilityAnalysis"
    )

    class _Cast_CylindricalPlanetGearCompoundStabilityAnalysis:
        """Special nested class for casting CylindricalPlanetGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
            parent: "CylindricalPlanetGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3942.CylindricalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
        ) -> "CylindricalPlanetGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3812.CylindricalPlanetGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CylindricalPlanetGearStabilityAnalysis]

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
    ) -> "List[_3812.CylindricalPlanetGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CylindricalPlanetGearStabilityAnalysis]

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
    ) -> "CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis":
        return self._Cast_CylindricalPlanetGearCompoundStabilityAnalysis(self)
