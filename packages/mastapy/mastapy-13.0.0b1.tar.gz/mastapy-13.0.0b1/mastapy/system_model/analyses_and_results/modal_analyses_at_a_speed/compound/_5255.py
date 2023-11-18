"""BevelDifferentialGearCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5260,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "BevelDifferentialGearCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5126,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BevelDifferentialGearCompoundModalAnalysisAtASpeed")


class BevelDifferentialGearCompoundModalAnalysisAtASpeed(
    _5260.BevelGearCompoundModalAnalysisAtASpeed
):
    """BevelDifferentialGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed"
    )

    class _Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting BevelDifferentialGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
            parent: "BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5260.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5248,
            )

            return self._parent._cast(
                _5248.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5276,
            )

            return self._parent._cast(_5276.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5302,
            )

            return self._parent._cast(_5302.GearCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(
                _5321.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(_5269.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(_5323.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5258,
            )

            return self._parent._cast(
                _5258.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(
                _5259.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
        ) -> "BevelDifferentialGearCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "BevelDifferentialGearCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2513.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5126.BevelDifferentialGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BevelDifferentialGearModalAnalysisAtASpeed]

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
    ) -> "List[_5126.BevelDifferentialGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BevelDifferentialGearModalAnalysisAtASpeed]

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
    ) -> "BevelDifferentialGearCompoundModalAnalysisAtASpeed._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed":
        return self._Cast_BevelDifferentialGearCompoundModalAnalysisAtASpeed(self)
