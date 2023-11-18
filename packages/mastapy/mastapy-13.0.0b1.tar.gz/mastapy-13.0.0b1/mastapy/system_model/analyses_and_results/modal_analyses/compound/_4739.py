"""BevelDifferentialPlanetGearCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4736
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BevelDifferentialPlanetGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4583


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCompoundModalAnalysis")


class BevelDifferentialPlanetGearCompoundModalAnalysis(
    _4736.BevelDifferentialGearCompoundModalAnalysis
):
    """BevelDifferentialPlanetGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearCompoundModalAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearCompoundModalAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
            parent: "BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            return self._parent._cast(_4736.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_gear_compound_modal_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(_4741.BevelGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4729,
            )

            return self._parent._cast(_4729.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4757,
            )

            return self._parent._cast(_4757.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(_4802.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
        ) -> "BevelDifferentialPlanetGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4583.BevelDifferentialPlanetGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialPlanetGearModalAnalysis]

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
    ) -> "List[_4583.BevelDifferentialPlanetGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialPlanetGearModalAnalysis]

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
    ) -> "BevelDifferentialPlanetGearCompoundModalAnalysis._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis":
        return self._Cast_BevelDifferentialPlanetGearCompoundModalAnalysis(self)
