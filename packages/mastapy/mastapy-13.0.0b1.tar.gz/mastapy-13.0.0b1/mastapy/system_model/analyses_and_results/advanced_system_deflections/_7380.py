"""StraightBevelDiffGearSetAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7288
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "StraightBevelDiffGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.static_loads import _6959
    from mastapy.gears.rating.straight_bevel_diff import _398
    from mastapy.system_model.analyses_and_results.system_deflections import _2812
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7378,
        _7379,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetAdvancedSystemDeflection")


class StraightBevelDiffGearSetAdvancedSystemDeflection(
    _7288.BevelGearSetAdvancedSystemDeflection
):
    """StraightBevelDiffGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetAdvancedSystemDeflection"
    )

    class _Cast_StraightBevelDiffGearSetAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelDiffGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
            parent: "StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7288.BevelGearSetAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7276,
            )

            return self._parent._cast(
                _7276.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(_7304.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7332,
            )

            return self._parent._cast(_7332.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(_7371.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7267,
            )

            return self._parent._cast(_7267.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
        ) -> "StraightBevelDiffGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection",
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
        instance_to_wrap: "StraightBevelDiffGearSetAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6959.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_398.StraightBevelDiffGearSetRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_398.StraightBevelDiffGearSetRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2812.StraightBevelDiffGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_gears_advanced_system_deflection(
        self: Self,
    ) -> "List[_7378.StraightBevelDiffGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelDiffGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_advanced_system_deflection(
        self: Self,
    ) -> "List[_7379.StraightBevelDiffGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelDiffGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetAdvancedSystemDeflection._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection":
        return self._Cast_StraightBevelDiffGearSetAdvancedSystemDeflection(self)
