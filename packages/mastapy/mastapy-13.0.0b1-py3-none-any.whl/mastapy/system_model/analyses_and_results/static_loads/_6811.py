"""AGMAGleasonConicalGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearLoadCase",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearLoadCase")


class AGMAGleasonConicalGearLoadCase(_6842.ConicalGearLoadCase):
    """AGMAGleasonConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearLoadCase")

    class _Cast_AGMAGleasonConicalGearLoadCase:
        """Special nested class for casting AGMAGleasonConicalGearLoadCase to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
            parent: "AGMAGleasonConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def conical_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            return self._parent._cast(_6842.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ComponentLoadCase)

        @property
        def part_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6820

            return self._parent._cast(_6820.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelGearLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6903

            return self._parent._cast(_6903.HypoidGearLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.StraightBevelSunGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.ZerolBevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "AGMAGleasonConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2511.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase":
        return self._Cast_AGMAGleasonConicalGearLoadCase(self)
