"""CouplingHalfCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5953
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "CouplingHalfCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5715


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundHarmonicAnalysis")


class CouplingHalfCompoundHarmonicAnalysis(
    _5953.MountableComponentCompoundHarmonicAnalysis
):
    """CouplingHalfCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundHarmonicAnalysis")

    class _Cast_CouplingHalfCompoundHarmonicAnalysis:
        """Special nested class for casting CouplingHalfCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
            parent: "CouplingHalfCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5953.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(_5901.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(_5955.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5899,
            )

            return self._parent._cast(_5899.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5918,
            )

            return self._parent._cast(_5918.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(
                _5958.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
            )

        @property
        def pulley_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.PulleyCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5968,
            )

            return self._parent._cast(_5968.RollingRingCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5980,
            )

            return self._parent._cast(_5980.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5990,
            )

            return self._parent._cast(_5990.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(_5991.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5992,
            )

            return self._parent._cast(_5992.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5995,
            )

            return self._parent._cast(_5995.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5996,
            )

            return self._parent._cast(
                _5996.TorqueConverterTurbineCompoundHarmonicAnalysis
            )

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "CouplingHalfCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5715.CouplingHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHalfHarmonicAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5715.CouplingHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHalfHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis":
        return self._Cast_CouplingHalfCompoundHarmonicAnalysis(self)
