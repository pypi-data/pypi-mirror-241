"""SpiralBevelGearSetCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6690,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6644
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6771,
        _6772,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearSetCompoundCriticalSpeedAnalysis")


class SpiralBevelGearSetCompoundCriticalSpeedAnalysis(
    _6690.BevelGearSetCompoundCriticalSpeedAnalysis
):
    """SpiralBevelGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis"
    )

    class _Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting SpiralBevelGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
            parent: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6690.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6678,
            )

            return self._parent._cast(
                _6678.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6732,
            )

            return self._parent._cast(_6732.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(
                _6770.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6672,
            )

            return self._parent._cast(
                _6672.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(_6751.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "SpiralBevelGearSetCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2542.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

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
    ) -> "List[_6644.SpiralBevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpiralBevelGearSetCriticalSpeedAnalysis]

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
    def spiral_bevel_gears_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6771.SpiralBevelGearCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.SpiralBevelGearCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6772.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6644.SpiralBevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpiralBevelGearSetCriticalSpeedAnalysis]

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
    ) -> "SpiralBevelGearSetCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_SpiralBevelGearSetCompoundCriticalSpeedAnalysis(self)
