"""TorqueConverterPumpHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6043,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.static_loads import _6972


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="TorqueConverterPumpHarmonicAnalysisOfSingleExcitation")


class TorqueConverterPumpHarmonicAnalysisOfSingleExcitation(
    _6043.CouplingHalfHarmonicAnalysisOfSingleExcitation
):
    """TorqueConverterPumpHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting TorqueConverterPumpHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
            parent: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6043.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(_6030.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
        ) -> "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6972.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterPumpHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation":
        return self._Cast_TorqueConverterPumpHarmonicAnalysisOfSingleExcitation(self)
