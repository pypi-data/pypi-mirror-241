"""PartToPartShearCouplingConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2727
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PartToPartShearCouplingConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346
    from mastapy.system_model.analyses_and_results.static_loads import _6927
    from mastapy.system_model.analyses_and_results.power_flows import _4112


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionSystemDeflection",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionSystemDeflection")


class PartToPartShearCouplingConnectionSystemDeflection(
    _2727.CouplingConnectionSystemDeflection
):
    """PartToPartShearCouplingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingConnectionSystemDeflection"
    )

    class _Cast_PartToPartShearCouplingConnectionSystemDeflection:
        """Special nested class for casting PartToPartShearCouplingConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
            parent: "PartToPartShearCouplingConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_system_deflection(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ):
            return self._parent._cast(_2727.CouplingConnectionSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(
                _2765.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
        ) -> "PartToPartShearCouplingConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2346.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6927.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4112.PartToPartShearCouplingConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingConnectionPowerFlow

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
    ) -> "PartToPartShearCouplingConnectionSystemDeflection._Cast_PartToPartShearCouplingConnectionSystemDeflection":
        return self._Cast_PartToPartShearCouplingConnectionSystemDeflection(self)
