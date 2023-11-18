"""GuideDxfModelCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2874
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "GuideDxfModelCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.system_deflections import _2760


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelCompoundSystemDeflection",)


Self = TypeVar("Self", bound="GuideDxfModelCompoundSystemDeflection")


class GuideDxfModelCompoundSystemDeflection(_2874.ComponentCompoundSystemDeflection):
    """GuideDxfModelCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelCompoundSystemDeflection"
    )

    class _Cast_GuideDxfModelCompoundSystemDeflection:
        """Special nested class for casting GuideDxfModelCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "GuideDxfModelCompoundSystemDeflection._Cast_GuideDxfModelCompoundSystemDeflection",
            parent: "GuideDxfModelCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_compound_system_deflection(
            self: "GuideDxfModelCompoundSystemDeflection._Cast_GuideDxfModelCompoundSystemDeflection",
        ):
            return self._parent._cast(_2874.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "GuideDxfModelCompoundSystemDeflection._Cast_GuideDxfModelCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "GuideDxfModelCompoundSystemDeflection._Cast_GuideDxfModelCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GuideDxfModelCompoundSystemDeflection._Cast_GuideDxfModelCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelCompoundSystemDeflection._Cast_GuideDxfModelCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def guide_dxf_model_compound_system_deflection(
            self: "GuideDxfModelCompoundSystemDeflection._Cast_GuideDxfModelCompoundSystemDeflection",
        ) -> "GuideDxfModelCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelCompoundSystemDeflection._Cast_GuideDxfModelCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "GuideDxfModelCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

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
    ) -> "List[_2760.GuideDxfModelSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection]

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
    ) -> "List[_2760.GuideDxfModelSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection]

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
    ) -> "GuideDxfModelCompoundSystemDeflection._Cast_GuideDxfModelCompoundSystemDeflection":
        return self._Cast_GuideDxfModelCompoundSystemDeflection(self)
