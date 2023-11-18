"""AGMAGleasonConicalGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4759
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AGMAGleasonConicalGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4575


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundModalAnalysis")


class AGMAGleasonConicalGearSetCompoundModalAnalysis(
    _4759.ConicalGearSetCompoundModalAnalysis
):
    """AGMAGleasonConicalGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
            parent: "AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            return self._parent._cast(_4759.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4725,
            )

            return self._parent._cast(_4725.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(
                _4738.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(_4743.BevelGearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4789,
            )

            return self._parent._cast(_4789.HypoidGearSetCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(
                _4832.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(_4835.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "AGMAGleasonConicalGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4575.AGMAGleasonConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearSetModalAnalysis]

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
    ) -> "List[_4575.AGMAGleasonConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearSetModalAnalysis]

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
    ) -> "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis(self)
