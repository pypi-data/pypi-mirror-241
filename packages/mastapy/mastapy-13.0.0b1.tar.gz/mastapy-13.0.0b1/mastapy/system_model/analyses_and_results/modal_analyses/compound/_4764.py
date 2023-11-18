"""CouplingHalfCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4802
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CouplingHalfCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4608


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundModalAnalysis")


class CouplingHalfCompoundModalAnalysis(_4802.MountableComponentCompoundModalAnalysis):
    """CouplingHalfCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundModalAnalysis")

    class _Cast_CouplingHalfCompoundModalAnalysis:
        """Special nested class for casting CouplingHalfCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
            parent: "CouplingHalfCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            return self._parent._cast(_4802.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4748,
            )

            return self._parent._cast(_4748.ClutchHalfCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.CVTPulleyCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(
                _4807.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def pulley_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.PulleyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4817,
            )

            return self._parent._cast(_4817.RollingRingCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.SpringDamperHalfCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(_4839.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4845,
            )

            return self._parent._cast(_4845.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
        ) -> "CouplingHalfCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4608.CouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis]

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
    ) -> "List[_4608.CouplingHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis]

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
    ) -> "CouplingHalfCompoundModalAnalysis._Cast_CouplingHalfCompoundModalAnalysis":
        return self._Cast_CouplingHalfCompoundModalAnalysis(self)
