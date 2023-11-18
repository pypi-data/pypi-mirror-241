"""ConnectorLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectorLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2445


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorLoadCase",)


Self = TypeVar("Self", bound="ConnectorLoadCase")


class ConnectorLoadCase(_6922.MountableComponentLoadCase):
    """ConnectorLoadCase

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorLoadCase")

    class _Cast_ConnectorLoadCase:
        """Special nested class for casting ConnectorLoadCase to subclasses."""

        def __init__(
            self: "ConnectorLoadCase._Cast_ConnectorLoadCase",
            parent: "ConnectorLoadCase",
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "ConnectorLoadCase._Cast_ConnectorLoadCase",
        ):
            return self._parent._cast(_6922.MountableComponentLoadCase)

        @property
        def component_load_case(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ComponentLoadCase)

        @property
        def part_load_case(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_analysis(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorLoadCase._Cast_ConnectorLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bearing_load_case(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.BearingLoadCase)

        @property
        def oil_seal_load_case(self: "ConnectorLoadCase._Cast_ConnectorLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.OilSealLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "ConnectorLoadCase._Cast_ConnectorLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(_6947.ShaftHubConnectionLoadCase)

        @property
        def connector_load_case(
            self: "ConnectorLoadCase._Cast_ConnectorLoadCase",
        ) -> "ConnectorLoadCase":
            return self._parent

        def __getattr__(self: "ConnectorLoadCase._Cast_ConnectorLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2445.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectorLoadCase._Cast_ConnectorLoadCase":
        return self._Cast_ConnectorLoadCase(self)
