"""BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6023,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.system_model.analyses_and_results.static_loads import _6822
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6016,
        _6017,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation"
)


class BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation(
    _6023.BevelGearSetHarmonicAnalysisOfSingleExcitation
):
    """BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
            parent: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6023.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6011,
            )

            return self._parent._cast(
                _6011.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(_6065.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(
                _6105.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6005,
            )

            return self._parent._cast(
                _6005.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self: Self) -> "_6822.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_differential_gears_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6016.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6017.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation(
            self
        )
