"""PlanetaryGearSetStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3810
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PlanetaryGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetStabilityAnalysis")


class PlanetaryGearSetStabilityAnalysis(_3810.CylindricalGearSetStabilityAnalysis):
    """PlanetaryGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetStabilityAnalysis")

    class _Cast_PlanetaryGearSetStabilityAnalysis:
        """Special nested class for casting PlanetaryGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
            parent: "PlanetaryGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ):
            return self._parent._cast(_3810.CylindricalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3761,
            )

            return self._parent._cast(_3761.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
        ) -> "PlanetaryGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2540.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis":
        return self._Cast_PlanetaryGearSetStabilityAnalysis(self)
