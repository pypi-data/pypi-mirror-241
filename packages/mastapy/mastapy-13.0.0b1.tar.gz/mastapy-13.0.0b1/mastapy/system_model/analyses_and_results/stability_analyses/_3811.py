"""CylindricalGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3823
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CylindricalGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.static_loads import _6859


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearStabilityAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearStabilityAnalysis")


class CylindricalGearStabilityAnalysis(_3823.GearStabilityAnalysis):
    """CylindricalGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearStabilityAnalysis")

    class _Cast_CylindricalGearStabilityAnalysis:
        """Special nested class for casting CylindricalGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
            parent: "CylindricalGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_stability_analysis(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
        ):
            return self._parent._cast(_3823.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3812,
            )

            return self._parent._cast(_3812.CylindricalPlanetGearStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
        ) -> "CylindricalGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2523.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6859.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CylindricalGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearStabilityAnalysis._Cast_CylindricalGearStabilityAnalysis":
        return self._Cast_CylindricalGearStabilityAnalysis(self)
