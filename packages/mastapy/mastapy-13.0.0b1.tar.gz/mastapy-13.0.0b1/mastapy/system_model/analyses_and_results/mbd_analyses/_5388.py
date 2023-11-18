"""BevelDifferentialGearSetMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5393
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BevelDifferentialGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.system_model.analyses_and_results.static_loads import _6822
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5387, _5386


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetMultibodyDynamicsAnalysis")


class BevelDifferentialGearSetMultibodyDynamicsAnalysis(
    _5393.BevelGearSetMultibodyDynamicsAnalysis
):
    """BevelDifferentialGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelDifferentialGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
            parent: "BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5393.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379

            return self._parent._cast(
                _5379.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(
                _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5373

            return self._parent._cast(_5373.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
        ) -> "BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearSetMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2514.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6822.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(
        self: Self,
    ) -> "List[_5387.BevelDifferentialGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearMultibodyDynamicsAnalysis]

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
    def bevel_differential_gears_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5387.BevelDifferentialGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5386.BevelDifferentialGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis":
        return self._Cast_BevelDifferentialGearSetMultibodyDynamicsAnalysis(self)
