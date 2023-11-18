"""CylindricalGearHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6063,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CylindricalGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.static_loads import _6859


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CylindricalGearHarmonicAnalysisOfSingleExcitation")


class CylindricalGearHarmonicAnalysisOfSingleExcitation(
    _6063.GearHarmonicAnalysisOfSingleExcitation
):
    """CylindricalGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CylindricalGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
            parent: "CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_6063.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(_6030.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6055,
            )

            return self._parent._cast(
                _6055.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "CylindricalGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CylindricalGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2523.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6859.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CylindricalGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CylindricalGearHarmonicAnalysisOfSingleExcitation(self)
