"""StraightBevelSunGearCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4830
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "StraightBevelSunGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4693


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundModalAnalysis")


class StraightBevelSunGearCompoundModalAnalysis(
    _4830.StraightBevelDiffGearCompoundModalAnalysis
):
    """StraightBevelSunGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundModalAnalysis"
    )

    class _Cast_StraightBevelSunGearCompoundModalAnalysis:
        """Special nested class for casting StraightBevelSunGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
            parent: "StraightBevelSunGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ):
            return self._parent._cast(_4830.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def bevel_gear_compound_modal_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(_4741.BevelGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4729,
            )

            return self._parent._cast(_4729.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4757,
            )

            return self._parent._cast(_4757.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(_4802.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
        ) -> "StraightBevelSunGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4693.StraightBevelSunGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelSunGearModalAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4693.StraightBevelSunGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelSunGearModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearCompoundModalAnalysis._Cast_StraightBevelSunGearCompoundModalAnalysis":
        return self._Cast_StraightBevelSunGearCompoundModalAnalysis(self)
