"""FaceGearSetStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3822
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "FaceGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.static_loads import _6884
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3818,
        _3816,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="FaceGearSetStabilityAnalysis")


class FaceGearSetStabilityAnalysis(_3822.GearSetStabilityAnalysis):
    """FaceGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetStabilityAnalysis")

    class _Cast_FaceGearSetStabilityAnalysis:
        """Special nested class for casting FaceGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
            parent: "FaceGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ):
            return self._parent._cast(_3822.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3761,
            )

            return self._parent._cast(_3761.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "FaceGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2527.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6884.FaceGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears_stability_analysis(
        self: Self,
    ) -> "List[_3818.FaceGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FaceGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3816.FaceGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FaceGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis":
        return self._Cast_FaceGearSetStabilityAnalysis(self)
