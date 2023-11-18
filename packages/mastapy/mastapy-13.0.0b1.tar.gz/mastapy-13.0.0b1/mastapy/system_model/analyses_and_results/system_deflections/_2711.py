"""ClutchSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2729
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ClutchSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6832
    from mastapy.system_model.analyses_and_results.system_deflections import _2709
    from mastapy.system_model.analyses_and_results.power_flows import _4053


__docformat__ = "restructuredtext en"
__all__ = ("ClutchSystemDeflection",)


Self = TypeVar("Self", bound="ClutchSystemDeflection")


class ClutchSystemDeflection(_2729.CouplingSystemDeflection):
    """ClutchSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CLUTCH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchSystemDeflection")

    class _Cast_ClutchSystemDeflection:
        """Special nested class for casting ClutchSystemDeflection to subclasses."""

        def __init__(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection",
            parent: "ClutchSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_system_deflection(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection",
        ):
            return self._parent._cast(_2729.CouplingSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2683,
            )

            return self._parent._cast(_2683.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_system_deflection(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection",
        ) -> "ClutchSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ClutchSystemDeflection._Cast_ClutchSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2576.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6832.ClutchLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def clutch_connection(self: Self) -> "_2709.ClutchConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ClutchConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4053.ClutchPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ClutchPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClutchSystemDeflection._Cast_ClutchSystemDeflection":
        return self._Cast_ClutchSystemDeflection(self)
