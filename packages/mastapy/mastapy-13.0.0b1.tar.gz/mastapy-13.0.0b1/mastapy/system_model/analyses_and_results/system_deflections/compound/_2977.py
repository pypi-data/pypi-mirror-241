"""ZerolBevelGearCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2865
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ZerolBevelGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.system_deflections import _2839


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearCompoundSystemDeflection")


class ZerolBevelGearCompoundSystemDeflection(_2865.BevelGearCompoundSystemDeflection):
    """ZerolBevelGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearCompoundSystemDeflection"
    )

    class _Cast_ZerolBevelGearCompoundSystemDeflection:
        """Special nested class for casting ZerolBevelGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
            parent: "ZerolBevelGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ):
            return self._parent._cast(_2865.BevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2853,
            )

            return self._parent._cast(
                _2853.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2881,
            )

            return self._parent._cast(_2881.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2908,
            )

            return self._parent._cast(_2908.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2927,
            )

            return self._parent._cast(_2927.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
        ) -> "ZerolBevelGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ZerolBevelGearCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

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
    ) -> "List[_2839.ZerolBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2839.ZerolBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection]

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
    ) -> "ZerolBevelGearCompoundSystemDeflection._Cast_ZerolBevelGearCompoundSystemDeflection":
        return self._Cast_ZerolBevelGearCompoundSystemDeflection(self)
