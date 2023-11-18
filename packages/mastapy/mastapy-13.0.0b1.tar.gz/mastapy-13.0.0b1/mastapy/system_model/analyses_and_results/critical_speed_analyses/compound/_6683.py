"""BevelDifferentialGearCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6688,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BevelDifferentialGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6551


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearCompoundCriticalSpeedAnalysis")


class BevelDifferentialGearCompoundCriticalSpeedAnalysis(
    _6688.BevelGearCompoundCriticalSpeedAnalysis
):
    """BevelDifferentialGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
            parent: "BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6688.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6676,
            )

            return self._parent._cast(
                _6676.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6704,
            )

            return self._parent._cast(_6704.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(_6730.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(
                _6749.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(_6697.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(_6751.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6686,
            )

            return self._parent._cast(
                _6686.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(
                _6687.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "BevelDifferentialGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2513.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

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
    ) -> "List[_6551.BevelDifferentialGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialGearCriticalSpeedAnalysis]

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
    ) -> "List[_6551.BevelDifferentialGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialGearCriticalSpeedAnalysis]

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
    ) -> "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis":
        return self._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis(self)
