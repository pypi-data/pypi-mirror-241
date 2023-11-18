"""HypoidGearSetMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5379
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "HypoidGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.static_loads import _6905
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5440, _5439


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="HypoidGearSetMultibodyDynamicsAnalysis")


class HypoidGearSetMultibodyDynamicsAnalysis(
    _5379.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
):
    """HypoidGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_HypoidGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting HypoidGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
            parent: "HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5379.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(
                _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5373

            return self._parent._cast(_5373.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
        ) -> "HypoidGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "HypoidGearSetMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2533.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6905.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_5440.HypoidGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.HypoidGearMultibodyDynamicsAnalysis]

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
    def hypoid_gears_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5440.HypoidGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.HypoidGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5439.HypoidGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.HypoidGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetMultibodyDynamicsAnalysis._Cast_HypoidGearSetMultibodyDynamicsAnalysis":
        return self._Cast_HypoidGearSetMultibodyDynamicsAnalysis(self)
