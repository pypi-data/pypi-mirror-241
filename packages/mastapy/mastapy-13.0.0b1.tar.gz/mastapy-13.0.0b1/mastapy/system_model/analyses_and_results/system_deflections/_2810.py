"""SpringDamperSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2729
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SpringDamperSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6956
    from mastapy.system_model.analyses_and_results.power_flows import _4138


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperSystemDeflection",)


Self = TypeVar("Self", bound="SpringDamperSystemDeflection")


class SpringDamperSystemDeflection(_2729.CouplingSystemDeflection):
    """SpringDamperSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperSystemDeflection")

    class _Cast_SpringDamperSystemDeflection:
        """Special nested class for casting SpringDamperSystemDeflection to subclasses."""

        def __init__(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
            parent: "SpringDamperSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ):
            return self._parent._cast(_2729.CouplingSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2683,
            )

            return self._parent._cast(_2683.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "SpringDamperSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2598.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6956.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4138.SpringDamperPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SpringDamperPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection":
        return self._Cast_SpringDamperSystemDeflection(self)
