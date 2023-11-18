"""KlingelnbergCycloPalloidSpiralBevelGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _973
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.connections_and_sockets.gears import _2318


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSet",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSet")


class KlingelnbergCycloPalloidSpiralBevelGearSet(
    _2535.KlingelnbergCycloPalloidConicalGearSet
):
    """KlingelnbergCycloPalloidSpiralBevelGearSet

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSet"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSet:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSet to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSet",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ):
            return self._parent._cast(_2535.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def conical_gear_set(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.ConicalGearSet)

        @property
        def gear_set(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.GearSet)

        @property
        def specialised_assembly(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ):
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ):
            from mastapy.system_model.part_model import _2432

            return self._parent._cast(_2432.AbstractAssembly)

        @property
        def part(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Part)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSet":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_conical_gear_set_design(
        self: Self,
    ) -> "_973.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(
        self: Self,
    ) -> "_973.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears(
        self: Self,
    ) -> "List[_2538.KlingelnbergCycloPalloidSpiralBevelGear]":
        """List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes(
        self: Self,
    ) -> "List[_2318.KlingelnbergCycloPalloidSpiralBevelGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSet._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSet(self)
