"""GearSetCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5624
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "GearSetCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5437


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="GearSetCompoundMultibodyDynamicsAnalysis")


class GearSetCompoundMultibodyDynamicsAnalysis(
    _5624.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
):
    """GearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_GearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting GearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
            parent: "GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5624.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5526,
            )

            return self._parent._cast(
                _5526.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(_5605.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5532,
            )

            return self._parent._cast(
                _5532.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5539,
            )

            return self._parent._cast(
                _5539.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(
                _5544.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5575,
            )

            return self._parent._cast(
                _5575.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(
                _5581.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5590,
            )

            return self._parent._cast(
                _5590.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(
                _5597.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5600,
            )

            return self._parent._cast(
                _5600.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(
                _5610.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(
                _5633.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5654,
            )

            return self._parent._cast(
                _5654.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "GearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "GearSetCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5437.GearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearSetMultibodyDynamicsAnalysis]

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
    ) -> "List[_5437.GearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearSetMultibodyDynamicsAnalysis]

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
    ) -> "GearSetCompoundMultibodyDynamicsAnalysis._Cast_GearSetCompoundMultibodyDynamicsAnalysis":
        return self._Cast_GearSetCompoundMultibodyDynamicsAnalysis(self)
