"""KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6912
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.static_loads import _6916, _6917


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase")


class KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase(
    _6912.KlingelnbergCycloPalloidConicalGearSetLoadCase
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ):
            return self._parent._cast(
                _6912.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def conical_gear_set_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6804

            return self._parent._cast(_6804.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(
        self: Self,
    ) -> "_2539.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(
        self: Self,
    ) -> "List[_6916.KlingelnbergCycloPalloidSpiralBevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_load_case(
        self: Self,
    ) -> "List[_6916.KlingelnbergCycloPalloidSpiralBevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_load_case(
        self: Self,
    ) -> "List[_6917.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase(self)
