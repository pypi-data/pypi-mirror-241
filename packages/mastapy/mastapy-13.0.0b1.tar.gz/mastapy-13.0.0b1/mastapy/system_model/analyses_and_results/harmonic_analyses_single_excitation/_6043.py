"""CouplingHalfHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6084,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CouplingHalfHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CouplingHalfHarmonicAnalysisOfSingleExcitation")


class CouplingHalfHarmonicAnalysisOfSingleExcitation(
    _6084.MountableComponentHarmonicAnalysisOfSingleExcitation
):
    """CouplingHalfHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingHalfHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
            parent: "CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6084.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(_6030.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6027,
            )

            return self._parent._cast(
                _6027.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6032,
            )

            return self._parent._cast(
                _6032.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(_6047.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(
                _6088.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(_6095.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6100,
            )

            return self._parent._cast(
                _6100.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(
                _6110.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(
                _6122.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6123,
            )

            return self._parent._cast(
                _6123.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(
                _6126.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "CouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CouplingHalfHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2582.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CouplingHalfHarmonicAnalysisOfSingleExcitation(self)
