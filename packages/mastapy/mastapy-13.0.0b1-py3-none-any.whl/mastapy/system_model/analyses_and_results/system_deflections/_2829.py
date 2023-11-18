"""TorqueConverterTurbineSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2728
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "TorqueConverterTurbineSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.power_flows import _4155


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterTurbineSystemDeflection")


class TorqueConverterTurbineSystemDeflection(_2728.CouplingHalfSystemDeflection):
    """TorqueConverterTurbineSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineSystemDeflection"
    )

    class _Cast_TorqueConverterTurbineSystemDeflection:
        """Special nested class for casting TorqueConverterTurbineSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
            parent: "TorqueConverterTurbineSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            return self._parent._cast(_2728.CouplingHalfSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "TorqueConverterTurbineSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6973.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4155.TorqueConverterTurbinePowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.TorqueConverterTurbinePowerFlow

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
    ) -> "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection":
        return self._Cast_TorqueConverterTurbineSystemDeflection(self)
