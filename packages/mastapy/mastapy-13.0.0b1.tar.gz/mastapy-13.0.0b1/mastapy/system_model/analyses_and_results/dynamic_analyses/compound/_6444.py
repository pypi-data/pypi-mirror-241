"""CouplingHalfCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6482
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CouplingHalfCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundDynamicAnalysis")


class CouplingHalfCompoundDynamicAnalysis(
    _6482.MountableComponentCompoundDynamicAnalysis
):
    """CouplingHalfCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundDynamicAnalysis")

    class _Cast_CouplingHalfCompoundDynamicAnalysis:
        """Special nested class for casting CouplingHalfCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
            parent: "CouplingHalfCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6482.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6428,
            )

            return self._parent._cast(_6428.ClutchHalfCompoundDynamicAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.CVTPulleyCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(
                _6487.PartToPartShearCouplingHalfCompoundDynamicAnalysis
            )

        @property
        def pulley_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.PulleyCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6497,
            )

            return self._parent._cast(_6497.RollingRingCompoundDynamicAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6519,
            )

            return self._parent._cast(_6519.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(_6521.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(_6524.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(
                _6525.TorqueConverterTurbineCompoundDynamicAnalysis
            )

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
        ) -> "CouplingHalfCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6313.CouplingHalfDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingHalfDynamicAnalysis]

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
    ) -> "List[_6313.CouplingHalfDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingHalfDynamicAnalysis]

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
    ) -> (
        "CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis"
    ):
        return self._Cast_CouplingHalfCompoundDynamicAnalysis(self)
