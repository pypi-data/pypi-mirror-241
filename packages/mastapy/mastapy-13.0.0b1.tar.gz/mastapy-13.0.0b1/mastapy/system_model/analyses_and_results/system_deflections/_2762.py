"""HypoidGearSetSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2688
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "HypoidGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.static_loads import _6905
    from mastapy.gears.rating.hypoid import _438
    from mastapy.system_model.analyses_and_results.power_flows import _4096
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2763,
        _2761,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetSystemDeflection",)


Self = TypeVar("Self", bound="HypoidGearSetSystemDeflection")


class HypoidGearSetSystemDeflection(_2688.AGMAGleasonConicalGearSetSystemDeflection):
    """HypoidGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetSystemDeflection")

    class _Cast_HypoidGearSetSystemDeflection:
        """Special nested class for casting HypoidGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
            parent: "HypoidGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            return self._parent._cast(_2688.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConicalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2683,
            )

            return self._parent._cast(_2683.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_system_deflection(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
        ) -> "HypoidGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetSystemDeflection.TYPE"):
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
    def rating(self: Self) -> "_438.HypoidGearSetRating":
        """mastapy.gears.rating.hypoid.HypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_438.HypoidGearSetRating":
        """mastapy.gears.rating.hypoid.HypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4096.HypoidGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.HypoidGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gears_system_deflection(
        self: Self,
    ) -> "List[_2763.HypoidGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_system_deflection(
        self: Self,
    ) -> "List[_2761.HypoidGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetSystemDeflection._Cast_HypoidGearSetSystemDeflection":
        return self._Cast_HypoidGearSetSystemDeflection(self)
