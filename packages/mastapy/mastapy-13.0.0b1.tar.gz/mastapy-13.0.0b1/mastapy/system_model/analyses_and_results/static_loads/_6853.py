"""CVTLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6819
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CVTLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584
    from mastapy.system_model.analyses_and_results.static_loads import _6854


__docformat__ = "restructuredtext en"
__all__ = ("CVTLoadCase",)


Self = TypeVar("Self", bound="CVTLoadCase")


class CVTLoadCase(_6819.BeltDriveLoadCase):
    """CVTLoadCase

    This is a mastapy class.
    """

    TYPE = _CVT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTLoadCase")

    class _Cast_CVTLoadCase:
        """Special nested class for casting CVTLoadCase to subclasses."""

        def __init__(self: "CVTLoadCase._Cast_CVTLoadCase", parent: "CVTLoadCase"):
            self._parent = parent

        @property
        def belt_drive_load_case(self: "CVTLoadCase._Cast_CVTLoadCase"):
            return self._parent._cast(_6819.BeltDriveLoadCase)

        @property
        def specialised_assembly_load_case(self: "CVTLoadCase._Cast_CVTLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(self: "CVTLoadCase._Cast_CVTLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6804

            return self._parent._cast(_6804.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self: "CVTLoadCase._Cast_CVTLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_analysis(self: "CVTLoadCase._Cast_CVTLoadCase"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTLoadCase._Cast_CVTLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "CVTLoadCase._Cast_CVTLoadCase"):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_load_case(self: "CVTLoadCase._Cast_CVTLoadCase") -> "CVTLoadCase":
            return self._parent

        def __getattr__(self: "CVTLoadCase._Cast_CVTLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpeedRatio

        if temp is None:
            return 0.0

        return temp

    @speed_ratio.setter
    @enforce_parameter_types
    def speed_ratio(self: Self, value: "float"):
        self.wrapped.SpeedRatio = float(value) if value is not None else 0.0

    @property
    def assembly_design(self: Self) -> "_2584.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pulleys(self: Self) -> "List[_6854.CVTPulleyLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Pulleys

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "CVTLoadCase._Cast_CVTLoadCase":
        return self._Cast_CVTLoadCase(self)
