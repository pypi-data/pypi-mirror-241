"""GearCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5062,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "GearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4914,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="GearCompoundModalAnalysisAtAStiffness")


class GearCompoundModalAnalysisAtAStiffness(
    _5062.MountableComponentCompoundModalAnalysisAtAStiffness
):
    """GearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_GearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting GearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
            parent: "GearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5062.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5010,
            )

            return self._parent._cast(_5010.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(_5064.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4989,
            )

            return self._parent._cast(
                _4989.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(
                _4996.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4999,
            )

            return self._parent._cast(
                _4999.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5000,
            )

            return self._parent._cast(
                _5000.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5001,
            )

            return self._parent._cast(_5001.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5014,
            )

            return self._parent._cast(
                _5014.ConceptGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5017,
            )

            return self._parent._cast(
                _5017.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(
                _5032.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5035,
            )

            return self._parent._cast(
                _5035.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5038,
            )

            return self._parent._cast(_5038.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(_5047.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(
                _5051.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5054,
            )

            return self._parent._cast(
                _5054.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5057,
            )

            return self._parent._cast(
                _5057.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5084,
            )

            return self._parent._cast(
                _5084.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(
                _5090.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5093,
            )

            return self._parent._cast(
                _5093.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5096,
            )

            return self._parent._cast(
                _5096.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(
                _5097.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5108,
            )

            return self._parent._cast(_5108.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5111,
            )

            return self._parent._cast(
                _5111.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
        ) -> "GearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "GearCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4914.GearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.GearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4914.GearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.GearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearCompoundModalAnalysisAtAStiffness._Cast_GearCompoundModalAnalysisAtAStiffness":
        return self._Cast_GearCompoundModalAnalysisAtAStiffness(self)
