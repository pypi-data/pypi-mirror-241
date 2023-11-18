"""BevelDifferentialGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6825
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearLoadCase",)


Self = TypeVar("Self", bound="BevelDifferentialGearLoadCase")


class BevelDifferentialGearLoadCase(_6825.BevelGearLoadCase):
    """BevelDifferentialGearLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearLoadCase")

    class _Cast_BevelDifferentialGearLoadCase:
        """Special nested class for casting BevelDifferentialGearLoadCase to subclasses."""

        def __init__(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
            parent: "BevelDifferentialGearLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            return self._parent._cast(_6825.BevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6811

            return self._parent._cast(_6811.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ComponentLoadCase)

        @property
        def part_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
        ) -> "BevelDifferentialGearLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2513.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

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
    ) -> "BevelDifferentialGearLoadCase._Cast_BevelDifferentialGearLoadCase":
        return self._Cast_BevelDifferentialGearLoadCase(self)
