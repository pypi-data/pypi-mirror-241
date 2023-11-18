"""SpecialisedAssemblyMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5373
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SpecialisedAssemblyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyMultibodyDynamicsAnalysis")


class SpecialisedAssemblyMultibodyDynamicsAnalysis(
    _5373.AbstractAssemblyMultibodyDynamicsAnalysis
):
    """SpecialisedAssemblyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis"
    )

    class _Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis:
        """Special nested class for casting SpecialisedAssemblyMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
            parent: "SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5373.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379

            return self._parent._cast(
                _5379.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385

            return self._parent._cast(_5385.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388

            return self._parent._cast(
                _5388.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393

            return self._parent._cast(_5393.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394

            return self._parent._cast(_5394.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398

            return self._parent._cast(_5398.ClutchMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(_5415.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(_5417.CVTMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431

            return self._parent._cast(_5431.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(
                _5433.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GearSetMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441

            return self._parent._cast(_5441.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(
                _5452.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455

            return self._parent._cast(
                _5455.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(
                _5467.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(_5469.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476

            return self._parent._cast(
                _5476.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(_5489.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(_5492.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(
                _5495.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5502

            return self._parent._cast(_5502.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5507

            return self._parent._cast(_5507.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
        ) -> "SpecialisedAssemblyMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SpecialisedAssemblyMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2474.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

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
    ) -> "SpecialisedAssemblyMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis":
        return self._Cast_SpecialisedAssemblyMultibodyDynamicsAnalysis(self)
