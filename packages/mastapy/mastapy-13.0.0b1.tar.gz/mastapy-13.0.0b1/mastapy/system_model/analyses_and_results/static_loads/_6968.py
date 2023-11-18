"""SynchroniserSleeveLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6967
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserSleeveLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveLoadCase",)


Self = TypeVar("Self", bound="SynchroniserSleeveLoadCase")


class SynchroniserSleeveLoadCase(_6967.SynchroniserPartLoadCase):
    """SynchroniserSleeveLoadCase

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleeveLoadCase")

    class _Cast_SynchroniserSleeveLoadCase:
        """Special nested class for casting SynchroniserSleeveLoadCase to subclasses."""

        def __init__(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
            parent: "SynchroniserSleeveLoadCase",
        ):
            self._parent = parent

        @property
        def synchroniser_part_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ):
            return self._parent._cast(_6967.SynchroniserPartLoadCase)

        @property
        def coupling_half_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ComponentLoadCase)

        @property
        def part_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_load_case(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
        ) -> "SynchroniserSleeveLoadCase":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserSleeveLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2604.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "SynchroniserSleeveLoadCase._Cast_SynchroniserSleeveLoadCase":
        return self._Cast_SynchroniserSleeveLoadCase(self)
