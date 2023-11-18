"""FaceGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3823
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "FaceGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.static_loads import _6882


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearStabilityAnalysis",)


Self = TypeVar("Self", bound="FaceGearStabilityAnalysis")


class FaceGearStabilityAnalysis(_3823.GearStabilityAnalysis):
    """FaceGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearStabilityAnalysis")

    class _Cast_FaceGearStabilityAnalysis:
        """Special nested class for casting FaceGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis",
            parent: "FaceGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_stability_analysis(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis",
        ):
            return self._parent._cast(_3823.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis",
        ) -> "FaceGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearStabilityAnalysis.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "FaceGearStabilityAnalysis._Cast_FaceGearStabilityAnalysis":
        return self._Cast_FaceGearStabilityAnalysis(self)
