"""VirtualComponentCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6749,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "VirtualComponentCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6665


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentCompoundCriticalSpeedAnalysis")


class VirtualComponentCompoundCriticalSpeedAnalysis(
    _6749.MountableComponentCompoundCriticalSpeedAnalysis
):
    """VirtualComponentCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundCriticalSpeedAnalysis"
    )

    class _Cast_VirtualComponentCompoundCriticalSpeedAnalysis:
        """Special nested class for casting VirtualComponentCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
            parent: "VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6749.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(_6697.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(_6751.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def mass_disc_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6747,
            )

            return self._parent._cast(_6747.MassDiscCompoundCriticalSpeedAnalysis)

        @property
        def measurement_component_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.MeasurementComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def point_load_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6758,
            )

            return self._parent._cast(_6758.PointLoadCompoundCriticalSpeedAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(_6759.PowerLoadCompoundCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6793,
            )

            return self._parent._cast(_6793.UnbalancedMassCompoundCriticalSpeedAnalysis)

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
        ) -> "VirtualComponentCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "VirtualComponentCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6665.VirtualComponentCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.VirtualComponentCriticalSpeedAnalysis]

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
    ) -> "List[_6665.VirtualComponentCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.VirtualComponentCriticalSpeedAnalysis]

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
    ) -> "VirtualComponentCompoundCriticalSpeedAnalysis._Cast_VirtualComponentCompoundCriticalSpeedAnalysis":
        return self._Cast_VirtualComponentCompoundCriticalSpeedAnalysis(self)
