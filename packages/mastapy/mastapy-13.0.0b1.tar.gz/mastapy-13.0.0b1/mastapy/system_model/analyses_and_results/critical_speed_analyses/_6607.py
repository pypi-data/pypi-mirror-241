"""HypoidGearSetCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6546
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "HypoidGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.static_loads import _6905
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6605,
        _6606,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="HypoidGearSetCriticalSpeedAnalysis")


class HypoidGearSetCriticalSpeedAnalysis(
    _6546.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
):
    """HypoidGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetCriticalSpeedAnalysis")

    class _Cast_HypoidGearSetCriticalSpeedAnalysis:
        """Special nested class for casting HypoidGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
            parent: "HypoidGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6546.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(_6641.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6540,
            )

            return self._parent._cast(_6540.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
        ) -> "HypoidGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "HypoidGearSetCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2533.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6905.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gears_critical_speed_analysis(
        self: Self,
    ) -> "List[_6605.HypoidGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.HypoidGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_critical_speed_analysis(
        self: Self,
    ) -> "List[_6606.HypoidGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.HypoidGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetCriticalSpeedAnalysis._Cast_HypoidGearSetCriticalSpeedAnalysis":
        return self._Cast_HypoidGearSetCriticalSpeedAnalysis(self)
