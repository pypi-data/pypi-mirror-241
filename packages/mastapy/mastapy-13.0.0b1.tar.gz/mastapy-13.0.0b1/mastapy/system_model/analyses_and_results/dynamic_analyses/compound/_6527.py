"""VirtualComponentCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6482
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "VirtualComponentCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCompoundDynamicAnalysis")


class VirtualComponentCompoundDynamicAnalysis(
    _6482.MountableComponentCompoundDynamicAnalysis
):
    """VirtualComponentCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundDynamicAnalysis"
    )

    class _Cast_VirtualComponentCompoundDynamicAnalysis:
        """Special nested class for casting VirtualComponentCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
            parent: "VirtualComponentCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6482.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6480,
            )

            return self._parent._cast(_6480.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(_6481.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6491,
            )

            return self._parent._cast(_6491.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(_6492.PowerLoadCompoundDynamicAnalysis)

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(_6526.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
        ) -> "VirtualComponentCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6398.VirtualComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.VirtualComponentDynamicAnalysis]

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
    ) -> "List[_6398.VirtualComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.VirtualComponentDynamicAnalysis]

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
    ) -> "VirtualComponentCompoundDynamicAnalysis._Cast_VirtualComponentCompoundDynamicAnalysis":
        return self._Cast_VirtualComponentCompoundDynamicAnalysis(self)
