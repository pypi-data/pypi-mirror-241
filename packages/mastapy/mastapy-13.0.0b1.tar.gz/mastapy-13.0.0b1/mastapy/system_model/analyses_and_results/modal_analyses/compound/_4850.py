"""WormGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "WormGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.modal_analyses import _4709
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4848,
        _4849,
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="WormGearSetCompoundModalAnalysis")


class WormGearSetCompoundModalAnalysis(_4785.GearSetCompoundModalAnalysis):
    """WormGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetCompoundModalAnalysis")

    class _Cast_WormGearSetCompoundModalAnalysis:
        """Special nested class for casting WormGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
            parent: "WormGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_modal_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ):
            return self._parent._cast(_4785.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4725,
            )

            return self._parent._cast(_4725.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
        ) -> "WormGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2550.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

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
    ) -> "List[_4709.WormGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearSetModalAnalysis]

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
    def worm_gears_compound_modal_analysis(
        self: Self,
    ) -> "List[_4848.WormGearCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.WormGearCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes_compound_modal_analysis(
        self: Self,
    ) -> "List[_4849.WormGearMeshCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.WormGearMeshCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4709.WormGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.WormGearSetModalAnalysis]

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
    ) -> "WormGearSetCompoundModalAnalysis._Cast_WormGearSetCompoundModalAnalysis":
        return self._Cast_WormGearSetCompoundModalAnalysis(self)
