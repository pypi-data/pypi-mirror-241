"""AbstractShaftSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2684
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AbstractShaftSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2433
    from mastapy.system_model.analyses_and_results.power_flows import _4032


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftSystemDeflection")


class AbstractShaftSystemDeflection(_2684.AbstractShaftOrHousingSystemDeflection):
    """AbstractShaftSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftSystemDeflection")

    class _Cast_AbstractShaftSystemDeflection:
        """Special nested class for casting AbstractShaftSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
            parent: "AbstractShaftSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            return self._parent._cast(_2684.AbstractShaftOrHousingSystemDeflection)

        @property
        def component_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.CycloidalDiscSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.ShaftSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
        ) -> "AbstractShaftSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2433.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4032.AbstractShaftPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AbstractShaftPowerFlow

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
    ) -> "AbstractShaftSystemDeflection._Cast_AbstractShaftSystemDeflection":
        return self._Cast_AbstractShaftSystemDeflection(self)
