"""CouplingHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CouplingHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.system_deflections import _2729


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingHarmonicAnalysis")


class CouplingHarmonicAnalysis(_5807.SpecialisedAssemblyHarmonicAnalysis):
    """CouplingHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHarmonicAnalysis")

    class _Cast_CouplingHarmonicAnalysis:
        """Special nested class for casting CouplingHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
            parent: "CouplingHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            return self._parent._cast(_5807.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5675,
            )

            return self._parent._cast(_5675.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5699,
            )

            return self._parent._cast(_5699.ClutchHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5705,
            )

            return self._parent._cast(_5705.ConceptCouplingHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.SpringDamperHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.TorqueConverterHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "CouplingHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2581.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2729.CouplingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis":
        return self._Cast_CouplingHarmonicAnalysis(self)
