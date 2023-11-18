"""TorqueConverterTurbineCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5915
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "TorqueConverterTurbineCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5831


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineCompoundHarmonicAnalysis")


class TorqueConverterTurbineCompoundHarmonicAnalysis(
    _5915.CouplingHalfCompoundHarmonicAnalysis
):
    """TorqueConverterTurbineCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineCompoundHarmonicAnalysis"
    )

    class _Cast_TorqueConverterTurbineCompoundHarmonicAnalysis:
        """Special nested class for casting TorqueConverterTurbineCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis",
            parent: "TorqueConverterTurbineCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5915.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5953,
            )

            return self._parent._cast(_5953.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(_5901.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(_5955.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis",
        ) -> "TorqueConverterTurbineCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis",
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
        instance_to_wrap: "TorqueConverterTurbineCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5831.TorqueConverterTurbineHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterTurbineHarmonicAnalysis]

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
    ) -> "List[_5831.TorqueConverterTurbineHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterTurbineHarmonicAnalysis]

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
    ) -> "TorqueConverterTurbineCompoundHarmonicAnalysis._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis":
        return self._Cast_TorqueConverterTurbineCompoundHarmonicAnalysis(self)
