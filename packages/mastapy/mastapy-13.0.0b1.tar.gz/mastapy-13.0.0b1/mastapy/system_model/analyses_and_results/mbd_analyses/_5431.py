"""FaceGearSetMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5437
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "FaceGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.static_loads import _6884
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5430, _5429


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="FaceGearSetMultibodyDynamicsAnalysis")


class FaceGearSetMultibodyDynamicsAnalysis(_5437.GearSetMultibodyDynamicsAnalysis):
    """FaceGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetMultibodyDynamicsAnalysis")

    class _Cast_FaceGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting FaceGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
            parent: "FaceGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5437.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(
                _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5373

            return self._parent._cast(_5373.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
        ) -> "FaceGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "FaceGearSetMultibodyDynamicsAnalysis.TYPE"
    ):
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
    def gears(self: Self) -> "List[_5430.FaceGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.FaceGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gears_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5430.FaceGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.FaceGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5429.FaceGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.FaceGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetMultibodyDynamicsAnalysis._Cast_FaceGearSetMultibodyDynamicsAnalysis":
        return self._Cast_FaceGearSetMultibodyDynamicsAnalysis(self)
