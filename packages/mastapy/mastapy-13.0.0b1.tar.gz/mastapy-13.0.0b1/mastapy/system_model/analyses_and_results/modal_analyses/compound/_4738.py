"""BevelDifferentialGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4743
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BevelDifferentialGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.system_model.analyses_and_results.modal_analyses import _4582
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4736,
        _4737,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetCompoundModalAnalysis")


class BevelDifferentialGearSetCompoundModalAnalysis(
    _4743.BevelGearSetCompoundModalAnalysis
):
    """BevelDifferentialGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetCompoundModalAnalysis"
    )

    class _Cast_BevelDifferentialGearSetCompoundModalAnalysis:
        """Special nested class for casting BevelDifferentialGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
            parent: "BevelDifferentialGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
        ):
            return self._parent._cast(_4743.BevelGearSetCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4731,
            )

            return self._parent._cast(
                _4731.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4725,
            )

            return self._parent._cast(_4725.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
        ) -> "BevelDifferentialGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearSetCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2514.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2514.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4582.BevelDifferentialGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearSetModalAnalysis]

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
    def bevel_differential_gears_compound_modal_analysis(
        self: Self,
    ) -> "List[_4736.BevelDifferentialGearCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_compound_modal_analysis(
        self: Self,
    ) -> "List[_4737.BevelDifferentialGearMeshCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.BevelDifferentialGearMeshCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4582.BevelDifferentialGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearSetModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetCompoundModalAnalysis._Cast_BevelDifferentialGearSetCompoundModalAnalysis":
        return self._Cast_BevelDifferentialGearSetCompoundModalAnalysis(self)
