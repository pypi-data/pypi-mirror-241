"""GearSetCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6503
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "GearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="GearSetCompoundDynamicAnalysis")


class GearSetCompoundDynamicAnalysis(_6503.SpecialisedAssemblyCompoundDynamicAnalysis):
    """GearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCompoundDynamicAnalysis")

    class _Cast_GearSetCompoundDynamicAnalysis:
        """Special nested class for casting GearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
            parent: "GearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6503.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6405,
            )

            return self._parent._cast(_6405.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6411,
            )

            return self._parent._cast(
                _6411.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6418,
            )

            return self._parent._cast(
                _6418.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6423,
            )

            return self._parent._cast(_6423.BevelGearSetCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6439,
            )

            return self._parent._cast(_6439.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(_6454.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6460,
            )

            return self._parent._cast(_6460.FaceGearSetCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(_6469.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(
                _6473.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(
                _6476.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(
                _6479.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(_6489.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(
                _6512.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(_6515.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6530,
            )

            return self._parent._cast(_6530.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6533,
            )

            return self._parent._cast(_6533.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
        ) -> "GearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_6336.GearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.GearSetDynamicAnalysis]

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
    ) -> "List[_6336.GearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.GearSetDynamicAnalysis]

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
    ) -> "GearSetCompoundDynamicAnalysis._Cast_GearSetCompoundDynamicAnalysis":
        return self._Cast_GearSetCompoundDynamicAnalysis(self)
