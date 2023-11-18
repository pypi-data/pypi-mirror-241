"""BevelGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2518


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetLoadCase",)


Self = TypeVar("Self", bound="BevelGearSetLoadCase")


class BevelGearSetLoadCase(_6813.AGMAGleasonConicalGearSetLoadCase):
    """BevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetLoadCase")

    class _Cast_BevelGearSetLoadCase:
        """Special nested class for casting BevelGearSetLoadCase to subclasses."""

        def __init__(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
            parent: "BevelGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ):
            return self._parent._cast(_6813.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6804

            return self._parent._cast(_6804.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_analysis(self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.BevelDifferentialGearSetLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.StraightBevelGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.ZerolBevelGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "BevelGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2518.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase":
        return self._Cast_BevelGearSetLoadCase(self)
