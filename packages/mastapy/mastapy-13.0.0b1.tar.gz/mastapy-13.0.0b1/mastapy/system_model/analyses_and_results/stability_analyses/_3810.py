"""CylindricalGearSetStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3822
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CylindricalGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3811,
        _3809,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearSetStabilityAnalysis")


class CylindricalGearSetStabilityAnalysis(_3822.GearSetStabilityAnalysis):
    """CylindricalGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetStabilityAnalysis")

    class _Cast_CylindricalGearSetStabilityAnalysis:
        """Special nested class for casting CylindricalGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
            parent: "CylindricalGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_stability_analysis(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
        ):
            return self._parent._cast(_3822.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3761,
            )

            return self._parent._cast(_3761.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.PlanetaryGearSetStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
        ) -> "CylindricalGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearSetStabilityAnalysis.TYPE"
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
    def cylindrical_gears_stability_analysis(
        self: Self,
    ) -> "List[_3811.CylindricalGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CylindricalGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3809.CylindricalGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CylindricalGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalGearSetStabilityAnalysis._Cast_CylindricalGearSetStabilityAnalysis"
    ):
        return self._Cast_CylindricalGearSetStabilityAnalysis(self)
