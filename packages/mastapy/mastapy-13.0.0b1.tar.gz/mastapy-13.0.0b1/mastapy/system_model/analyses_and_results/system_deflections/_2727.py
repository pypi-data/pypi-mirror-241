"""CouplingConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2765
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CouplingConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2344
    from mastapy.system_model.analyses_and_results.power_flows import _4067


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionSystemDeflection",)


Self = TypeVar("Self", bound="CouplingConnectionSystemDeflection")


class CouplingConnectionSystemDeflection(
    _2765.InterMountableComponentConnectionSystemDeflection
):
    """CouplingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionSystemDeflection")

    class _Cast_CouplingConnectionSystemDeflection:
        """Special nested class for casting CouplingConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
            parent: "CouplingConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            return self._parent._cast(
                _2765.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.ClutchConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ConceptCouplingConnectionSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(
                _2784.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def spring_damper_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpringDamperConnectionSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.TorqueConverterConnectionSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "CouplingConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingConnectionSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2344.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4067.CouplingConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow

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
    ) -> "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection":
        return self._Cast_CouplingConnectionSystemDeflection(self)
