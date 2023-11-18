"""MeasurementComponentLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6979
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MeasurementComponentLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentLoadCase",)


Self = TypeVar("Self", bound="MeasurementComponentLoadCase")


class MeasurementComponentLoadCase(_6979.VirtualComponentLoadCase):
    """MeasurementComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeasurementComponentLoadCase")

    class _Cast_MeasurementComponentLoadCase:
        """Special nested class for casting MeasurementComponentLoadCase to subclasses."""

        def __init__(
            self: "MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase",
            parent: "MeasurementComponentLoadCase",
        ):
            self._parent = parent

        @property
        def virtual_component_load_case(
            self: "MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase",
        ):
            return self._parent._cast(_6979.VirtualComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ComponentLoadCase)

        @property
        def part_load_case(
            self: "MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_analysis(
            self: "MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def measurement_component_load_case(
            self: "MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase",
        ) -> "MeasurementComponentLoadCase":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeasurementComponentLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2461.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase":
        return self._Cast_MeasurementComponentLoadCase(self)
