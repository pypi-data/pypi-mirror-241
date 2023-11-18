"""KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6074,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6078,
        _6079,
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
)


class KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation(
    _6074.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6074.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(_6065.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(
                _6105.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6005,
            )

            return self._parent._cast(
                _6005.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(
        self: Self,
    ) -> "_6918.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6078.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsHarmonicAnalysisOfSingleExcitation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6079.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesHarmonicAnalysisOfSingleExcitation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation(
            self
        )
