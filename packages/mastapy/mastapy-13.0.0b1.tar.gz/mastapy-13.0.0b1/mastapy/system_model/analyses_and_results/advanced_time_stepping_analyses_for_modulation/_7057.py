"""CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7068,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.system_deflections import _2740
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7055,
        _7056,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation"
)


class CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7068.GearSetAdvancedTimeSteppingAnalysisForModulation
):
    """CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7068.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7003,
            )

            return self._parent._cast(
                _7003.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7093,
            )

            return self._parent._cast(
                _7093.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2524.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6863.CylindricalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

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
    ) -> "_2740.CylindricalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7055.CylindricalGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CylindricalGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7056.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation(
            self
        )
