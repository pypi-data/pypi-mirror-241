"""FaceGearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2759
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "FaceGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.gears.rating.face import _446
    from mastapy.system_model.analyses_and_results.static_loads import _6882
    from mastapy.system_model.analyses_and_results.power_flows import _4085


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSystemDeflection",)


Self = TypeVar("Self", bound="FaceGearSystemDeflection")


class FaceGearSystemDeflection(_2759.GearSystemDeflection):
    """FaceGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSystemDeflection")

    class _Cast_FaceGearSystemDeflection:
        """Special nested class for casting FaceGearSystemDeflection to subclasses."""

        def __init__(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
            parent: "FaceGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_system_deflection(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
        ):
            return self._parent._cast(_2759.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def face_gear_system_deflection(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection",
        ) -> "FaceGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2526.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_446.FaceGearRating":
        """mastapy.gears.rating.face.FaceGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6882.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4085.FaceGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.FaceGearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSystemDeflection._Cast_FaceGearSystemDeflection":
        return self._Cast_FaceGearSystemDeflection(self)
