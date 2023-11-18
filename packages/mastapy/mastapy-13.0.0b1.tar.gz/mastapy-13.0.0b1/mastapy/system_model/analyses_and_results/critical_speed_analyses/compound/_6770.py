"""SpecialisedAssemblyCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6672,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6641


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundCriticalSpeedAnalysis")


class SpecialisedAssemblyCompoundCriticalSpeedAnalysis(
    _6672.AbstractAssemblyCompoundCriticalSpeedAnalysis
):
    """SpecialisedAssemblyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis"
    )

    class _Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
            parent: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6672.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(_6751.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6678,
            )

            return self._parent._cast(
                _6678.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def belt_drive_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6682,
            )

            return self._parent._cast(_6682.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6685,
            )

            return self._parent._cast(
                _6685.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6690,
            )

            return self._parent._cast(_6690.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bolted_joint_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6692,
            )

            return self._parent._cast(_6692.BoltedJointCompoundCriticalSpeedAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6693,
            )

            return self._parent._cast(_6693.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6698,
            )

            return self._parent._cast(
                _6698.ConceptCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6703,
            )

            return self._parent._cast(_6703.ConceptGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def coupling_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(_6709.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(_6713.CVTCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6715,
            )

            return self._parent._cast(
                _6715.CycloidalAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(
                _6721.CylindricalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(_6727.FaceGearSetCompoundCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6729,
            )

            return self._parent._cast(
                _6729.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6732,
            )

            return self._parent._cast(_6732.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(_6736.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6743,
            )

            return self._parent._cast(
                _6743.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6746,
            )

            return self._parent._cast(
                _6746.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(
                _6752.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(
                _6756.PlanetaryGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_assembly_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6763,
            )

            return self._parent._cast(
                _6763.RollingRingAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6774,
            )

            return self._parent._cast(_6774.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6779,
            )

            return self._parent._cast(
                _6779.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6782,
            )

            return self._parent._cast(
                _6782.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6785,
            )

            return self._parent._cast(_6785.SynchroniserCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6789,
            )

            return self._parent._cast(
                _6789.TorqueConverterCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6797,
            )

            return self._parent._cast(_6797.WormGearSetCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6800,
            )

            return self._parent._cast(
                _6800.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6641.SpecialisedAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpecialisedAssemblyCriticalSpeedAnalysis]

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
    ) -> "List[_6641.SpecialisedAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpecialisedAssemblyCriticalSpeedAnalysis]

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
    ) -> "SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
        return self._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis(self)
