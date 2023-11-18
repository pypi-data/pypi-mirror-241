"""StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7026,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6962
    from mastapy.system_model.analyses_and_results.system_deflections import _2815
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7117,
        _7118,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation"
)


class StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7026.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
):
    """StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7026.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7013,
            )

            return self._parent._cast(
                _7013.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7003,
            )

            return self._parent._cast(
                _7003.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2546.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6962.StraightBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2815.StraightBevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gears_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7117.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7118.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation(
            self
        )
