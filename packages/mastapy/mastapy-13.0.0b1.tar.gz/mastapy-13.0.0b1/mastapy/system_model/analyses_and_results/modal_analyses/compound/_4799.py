"""KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4793
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.modal_analyses import _4648
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4797,
        _4798,
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis(
    _4793.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
        ):
            return self._parent._cast(
                _4793.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4725,
            )

            return self._parent._cast(_4725.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(
        self: Self,
    ) -> "_2539.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(
        self: Self,
    ) -> "_2539.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

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
    ) -> "List[_4648.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis]

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
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_modal_analysis(
        self: Self,
    ) -> "List[_4797.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundModalAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_modal_analysis(
        self: Self,
    ) -> "List[_4798.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundModalAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4648.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis]

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis(
                self
            )
        )
