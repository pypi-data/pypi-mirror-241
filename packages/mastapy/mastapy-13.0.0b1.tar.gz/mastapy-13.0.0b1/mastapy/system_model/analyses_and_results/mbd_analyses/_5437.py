"""GearSetMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5486
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "GearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5436, _5434


__docformat__ = "restructuredtext en"
__all__ = ("GearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="GearSetMultibodyDynamicsAnalysis")


class GearSetMultibodyDynamicsAnalysis(
    _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
):
    """GearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetMultibodyDynamicsAnalysis")

    class _Cast_GearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting GearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
            parent: "GearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5373

            return self._parent._cast(_5373.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379

            return self._parent._cast(
                _5379.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388

            return self._parent._cast(
                _5388.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393

            return self._parent._cast(_5393.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431

            return self._parent._cast(_5431.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441

            return self._parent._cast(_5441.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(
                _5452.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455

            return self._parent._cast(
                _5455.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(_5469.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(_5489.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(
                _5495.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
        ) -> "GearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetMultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2530.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_5436.GearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearMultibodyDynamicsAnalysis]

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
    def meshes(self: Self) -> "List[_5434.GearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Meshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetMultibodyDynamicsAnalysis._Cast_GearSetMultibodyDynamicsAnalysis":
        return self._Cast_GearSetMultibodyDynamicsAnalysis(self)
