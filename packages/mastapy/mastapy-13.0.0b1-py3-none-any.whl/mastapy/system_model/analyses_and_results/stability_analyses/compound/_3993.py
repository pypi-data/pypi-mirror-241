"""SpecialisedAssemblyCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3895
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SpecialisedAssemblyCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3861


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundStabilityAnalysis")


class SpecialisedAssemblyCompoundStabilityAnalysis(
    _3895.AbstractAssemblyCompoundStabilityAnalysis
):
    """SpecialisedAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundStabilityAnalysis"
    )

    class _Cast_SpecialisedAssemblyCompoundStabilityAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
            parent: "SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3895.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3901,
            )

            return self._parent._cast(
                _3901.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def belt_drive_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(_3905.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3908,
            )

            return self._parent._cast(
                _3908.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3913,
            )

            return self._parent._cast(_3913.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3915,
            )

            return self._parent._cast(_3915.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3916,
            )

            return self._parent._cast(_3916.ClutchCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3921,
            )

            return self._parent._cast(_3921.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(_3926.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(_3929.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3932,
            )

            return self._parent._cast(_3932.CouplingCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.CVTCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3938,
            )

            return self._parent._cast(_3938.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3944,
            )

            return self._parent._cast(_3944.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.FaceGearSetCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(
                _3952.FlexiblePinAssemblyCompoundStabilityAnalysis
            )

        @property
        def gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(_3955.GearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3959,
            )

            return self._parent._cast(_3959.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(
                _3963.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(
                _3966.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3969,
            )

            return self._parent._cast(
                _3969.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3975,
            )

            return self._parent._cast(
                _3975.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(_3979.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3986,
            )

            return self._parent._cast(
                _3986.RollingRingAssemblyCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(_3996.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.SpringDamperCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(
                _4002.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(
                _4005.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def synchroniser_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4008,
            )

            return self._parent._cast(_4008.SynchroniserCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4012,
            )

            return self._parent._cast(_4012.TorqueConverterCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4020,
            )

            return self._parent._cast(_4020.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4023,
            )

            return self._parent._cast(_4023.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ) -> "SpecialisedAssemblyCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3861.SpecialisedAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpecialisedAssemblyStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3861.SpecialisedAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpecialisedAssemblyStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis":
        return self._Cast_SpecialisedAssemblyCompoundStabilityAnalysis(self)
