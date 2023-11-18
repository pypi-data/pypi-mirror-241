"""ZerolBevelGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4743
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ZerolBevelGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.modal_analyses import _4712
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4851,
        _4852,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearSetCompoundModalAnalysis")


class ZerolBevelGearSetCompoundModalAnalysis(_4743.BevelGearSetCompoundModalAnalysis):
    """ZerolBevelGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetCompoundModalAnalysis"
    )

    class _Cast_ZerolBevelGearSetCompoundModalAnalysis:
        """Special nested class for casting ZerolBevelGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
            parent: "ZerolBevelGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
        ):
            return self._parent._cast(_4743.BevelGearSetCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4731,
            )

            return self._parent._cast(
                _4731.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4725,
            )

            return self._parent._cast(_4725.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
        ) -> "ZerolBevelGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearSetCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2552.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2552.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

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
    ) -> "List[_4712.ZerolBevelGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearSetModalAnalysis]

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
    def zerol_bevel_gears_compound_modal_analysis(
        self: Self,
    ) -> "List[_4851.ZerolBevelGearCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_compound_modal_analysis(
        self: Self,
    ) -> "List[_4852.ZerolBevelGearMeshCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.ZerolBevelGearMeshCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4712.ZerolBevelGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearSetModalAnalysis]

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
    ) -> "ZerolBevelGearSetCompoundModalAnalysis._Cast_ZerolBevelGearSetCompoundModalAnalysis":
        return self._Cast_ZerolBevelGearSetCompoundModalAnalysis(self)
