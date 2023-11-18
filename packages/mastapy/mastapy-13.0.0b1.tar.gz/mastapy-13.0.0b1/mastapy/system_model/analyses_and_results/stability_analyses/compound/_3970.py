"""MassDiscCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4017
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "MassDiscCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.stability_analyses import _3838


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="MassDiscCompoundStabilityAnalysis")


class MassDiscCompoundStabilityAnalysis(
    _4017.VirtualComponentCompoundStabilityAnalysis
):
    """MassDiscCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscCompoundStabilityAnalysis")

    class _Cast_MassDiscCompoundStabilityAnalysis:
        """Special nested class for casting MassDiscCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "MassDiscCompoundStabilityAnalysis._Cast_MassDiscCompoundStabilityAnalysis",
            parent: "MassDiscCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_stability_analysis(
            self: "MassDiscCompoundStabilityAnalysis._Cast_MassDiscCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_4017.VirtualComponentCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "MassDiscCompoundStabilityAnalysis._Cast_MassDiscCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "MassDiscCompoundStabilityAnalysis._Cast_MassDiscCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "MassDiscCompoundStabilityAnalysis._Cast_MassDiscCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "MassDiscCompoundStabilityAnalysis._Cast_MassDiscCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MassDiscCompoundStabilityAnalysis._Cast_MassDiscCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscCompoundStabilityAnalysis._Cast_MassDiscCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def mass_disc_compound_stability_analysis(
            self: "MassDiscCompoundStabilityAnalysis._Cast_MassDiscCompoundStabilityAnalysis",
        ) -> "MassDiscCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "MassDiscCompoundStabilityAnalysis._Cast_MassDiscCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "MassDiscCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.MassDisc":
        """mastapy.system_model.part_model.MassDisc

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
    ) -> "List[_3838.MassDiscStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.MassDiscStabilityAnalysis]

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
    def planetaries(self: Self) -> "List[MassDiscCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.MassDiscCompoundStabilityAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_3838.MassDiscStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.MassDiscStabilityAnalysis]

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
    ) -> "MassDiscCompoundStabilityAnalysis._Cast_MassDiscCompoundStabilityAnalysis":
        return self._Cast_MassDiscCompoundStabilityAnalysis(self)
