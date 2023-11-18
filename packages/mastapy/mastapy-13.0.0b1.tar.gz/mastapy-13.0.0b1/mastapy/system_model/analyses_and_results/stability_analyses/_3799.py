"""CouplingHalfStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3840
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CouplingHalfStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfStabilityAnalysis")


class CouplingHalfStabilityAnalysis(_3840.MountableComponentStabilityAnalysis):
    """CouplingHalfStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfStabilityAnalysis")

    class _Cast_CouplingHalfStabilityAnalysis:
        """Special nested class for casting CouplingHalfStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
            parent: "CouplingHalfStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.ClutchHalfStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ConceptCouplingHalfStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.CVTPulleyStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(
                _3844.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def pulley_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.PulleyStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(_3856.RollingRingStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpringDamperHalfStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.SynchroniserSleeveStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.TorqueConverterTurbineStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "CouplingHalfStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2582.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

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
    ) -> "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis":
        return self._Cast_CouplingHalfStabilityAnalysis(self)
