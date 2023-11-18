"""KlingelnbergCycloPalloidConicalGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3795
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearStabilityAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearStabilityAnalysis")


class KlingelnbergCycloPalloidConicalGearStabilityAnalysis(
    _3795.ConicalGearStabilityAnalysis
):
    """KlingelnbergCycloPalloidConicalGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            return self._parent._cast(_3795.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3834,
            )

            return self._parent._cast(
                _3834.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(
                _3837.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis(self)
