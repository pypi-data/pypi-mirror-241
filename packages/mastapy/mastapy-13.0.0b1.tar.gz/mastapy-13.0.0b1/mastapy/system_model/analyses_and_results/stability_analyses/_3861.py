"""SpecialisedAssemblyStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3761
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SpecialisedAssemblyStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyStabilityAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyStabilityAnalysis")


class SpecialisedAssemblyStabilityAnalysis(_3761.AbstractAssemblyStabilityAnalysis):
    """SpecialisedAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyStabilityAnalysis")

    class _Cast_SpecialisedAssemblyStabilityAnalysis:
        """Special nested class for casting SpecialisedAssemblyStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
            parent: "SpecialisedAssemblyStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            return self._parent._cast(_3761.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3766,
            )

            return self._parent._cast(_3766.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3773,
            )

            return self._parent._cast(_3773.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelGearSetStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3780,
            )

            return self._parent._cast(_3780.BoltedJointStabilityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3789,
            )

            return self._parent._cast(_3789.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.ConceptGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConicalGearSetStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(_3800.CouplingStabilityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3805,
            )

            return self._parent._cast(_3805.CycloidalAssemblyStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(_3810.CylindricalGearSetStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.FaceGearSetStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3826,
            )

            return self._parent._cast(_3826.HypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(
                _3830.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(
                _3833.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(
                _3836.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.PlanetaryGearSetStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3854,
            )

            return self._parent._cast(_3854.RollingRingAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelGearSetStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3882,
            )

            return self._parent._cast(_3882.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.TorqueConverterStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3890,
            )

            return self._parent._cast(_3890.WormGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.ZerolBevelGearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ) -> "SpecialisedAssemblyStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyStabilityAnalysis.TYPE"
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
    ) -> "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis":
        return self._Cast_SpecialisedAssemblyStabilityAnalysis(self)
