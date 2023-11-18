"""RollingRingCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2888
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "RollingRingCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.system_deflections import _2797


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingCompoundSystemDeflection",)


Self = TypeVar("Self", bound="RollingRingCompoundSystemDeflection")


class RollingRingCompoundSystemDeflection(_2888.CouplingHalfCompoundSystemDeflection):
    """RollingRingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingCompoundSystemDeflection")

    class _Cast_RollingRingCompoundSystemDeflection:
        """Special nested class for casting RollingRingCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
            parent: "RollingRingCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_system_deflection(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ):
            return self._parent._cast(_2888.CouplingHalfCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2927,
            )

            return self._parent._cast(_2927.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def rolling_ring_compound_system_deflection(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ) -> "RollingRingCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "RollingRingCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2594.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

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
    ) -> "List[_2797.RollingRingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection]

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
    def planetaries(self: Self) -> "List[RollingRingCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.RollingRingCompoundSystemDeflection]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2797.RollingRingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection]

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
    ) -> (
        "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection"
    ):
        return self._Cast_RollingRingCompoundSystemDeflection(self)
