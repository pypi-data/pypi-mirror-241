"""VirtualComponentLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "VirtualComponentLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentLoadCase",)


Self = TypeVar("Self", bound="VirtualComponentLoadCase")


class VirtualComponentLoadCase(_6922.MountableComponentLoadCase):
    """VirtualComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentLoadCase")

    class _Cast_VirtualComponentLoadCase:
        """Special nested class for casting VirtualComponentLoadCase to subclasses."""

        def __init__(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
            parent: "VirtualComponentLoadCase",
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ):
            return self._parent._cast(_6922.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ComponentLoadCase)

        @property
        def part_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_analysis(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def mass_disc_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6919

            return self._parent._cast(_6919.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(_6920.MeasurementComponentLoadCase)

        @property
        def point_load_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6936

            return self._parent._cast(_6936.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PowerLoadLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6978

            return self._parent._cast(_6978.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "VirtualComponentLoadCase":
            return self._parent

        def __getattr__(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase":
        return self._Cast_VirtualComponentLoadCase(self)
