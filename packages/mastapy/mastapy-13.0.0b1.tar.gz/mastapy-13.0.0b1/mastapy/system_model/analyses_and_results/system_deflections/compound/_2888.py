"""CouplingHalfCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2927
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CouplingHalfCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2728


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CouplingHalfCompoundSystemDeflection")


class CouplingHalfCompoundSystemDeflection(
    _2927.MountableComponentCompoundSystemDeflection
):
    """CouplingHalfCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundSystemDeflection")

    class _Cast_CouplingHalfCompoundSystemDeflection:
        """Special nested class for casting CouplingHalfCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
            parent: "CouplingHalfCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            return self._parent._cast(_2927.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2872,
            )

            return self._parent._cast(_2872.ClutchHalfCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(_2877.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.CVTPulleyCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(
                _2932.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def pulley_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(_2938.PulleyCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(_2942.RollingRingCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(_2955.SpringDamperHalfCompoundSystemDeflection)

        @property
        def synchroniser_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2965,
            )

            return self._parent._cast(_2965.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(_2966.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2967,
            )

            return self._parent._cast(_2967.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2970,
            )

            return self._parent._cast(_2970.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(
                _2971.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def coupling_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "CouplingHalfCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2728.CouplingHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection]

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
    ) -> "List[_2728.CouplingHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection]

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
    ) -> "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection":
        return self._Cast_CouplingHalfCompoundSystemDeflection(self)
