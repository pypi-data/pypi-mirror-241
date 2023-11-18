"""BoltedJointHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6105,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "BoltedJointHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.static_loads import _6828


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BoltedJointHarmonicAnalysisOfSingleExcitation")


class BoltedJointHarmonicAnalysisOfSingleExcitation(
    _6105.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
):
    """BoltedJointHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BoltedJointHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_BoltedJointHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BoltedJointHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation",
            parent: "BoltedJointHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6105.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6005,
            )

            return self._parent._cast(
                _6005.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation",
        ) -> "BoltedJointHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BoltedJointHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2441.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6828.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BoltedJointHarmonicAnalysisOfSingleExcitation._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BoltedJointHarmonicAnalysisOfSingleExcitation(self)
