"""VirtualComponentStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3840
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "VirtualComponentStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentStabilityAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentStabilityAnalysis")


class VirtualComponentStabilityAnalysis(_3840.MountableComponentStabilityAnalysis):
    """VirtualComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentStabilityAnalysis")

    class _Cast_VirtualComponentStabilityAnalysis:
        """Special nested class for casting VirtualComponentStabilityAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
            parent: "VirtualComponentStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def mass_disc_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(_3838.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MeasurementComponentStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3849,
            )

            return self._parent._cast(_3849.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.PowerLoadStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
        ) -> "VirtualComponentStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentStabilityAnalysis._Cast_VirtualComponentStabilityAnalysis":
        return self._Cast_VirtualComponentStabilityAnalysis(self)
