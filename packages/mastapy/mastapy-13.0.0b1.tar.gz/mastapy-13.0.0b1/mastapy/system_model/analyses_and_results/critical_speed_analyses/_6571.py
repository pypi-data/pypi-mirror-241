"""ConceptGearSetCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6603
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConceptGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520
    from mastapy.system_model.analyses_and_results.static_loads import _6841
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6569,
        _6570,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConceptGearSetCriticalSpeedAnalysis")


class ConceptGearSetCriticalSpeedAnalysis(_6603.GearSetCriticalSpeedAnalysis):
    """ConceptGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetCriticalSpeedAnalysis")

    class _Cast_ConceptGearSetCriticalSpeedAnalysis:
        """Special nested class for casting ConceptGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
            parent: "ConceptGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_critical_speed_analysis(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6603.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(_6641.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6540,
            )

            return self._parent._cast(_6540.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
        ) -> "ConceptGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ConceptGearSetCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2520.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6841.ConceptGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gears_critical_speed_analysis(
        self: Self,
    ) -> "List[_6569.ConceptGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_critical_speed_analysis(
        self: Self,
    ) -> "List[_6570.ConceptGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConceptGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConceptGearSetCriticalSpeedAnalysis._Cast_ConceptGearSetCriticalSpeedAnalysis"
    ):
        return self._Cast_ConceptGearSetCriticalSpeedAnalysis(self)
