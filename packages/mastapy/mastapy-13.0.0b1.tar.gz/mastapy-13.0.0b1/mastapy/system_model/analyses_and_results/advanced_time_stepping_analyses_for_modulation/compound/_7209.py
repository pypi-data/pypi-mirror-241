"""KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7206,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7080,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7207,
        _7208,
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7206.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7206.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7172,
            )

            return self._parent._cast(
                _7172.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7198,
            )

            return self._parent._cast(
                _7198.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7236,
            )

            return self._parent._cast(
                _7236.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7138,
            )

            return self._parent._cast(
                _7138.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7217,
            )

            return self._parent._cast(
                _7217.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2537.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2537.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

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
    ) -> "List[_7080.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation]

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
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7207.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundAdvancedTimeSteppingAnalysisForModulation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7208.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundAdvancedTimeSteppingAnalysisForModulation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7080.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
