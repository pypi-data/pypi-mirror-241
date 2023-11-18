"""WormGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2530
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.worm import _957
    from mastapy.system_model.part_model.gears import _2549
    from mastapy.system_model.connections_and_sockets.gears import _2327


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSet",)


Self = TypeVar("Self", bound="WormGearSet")


class WormGearSet(_2530.GearSet):
    """WormGearSet

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSet")

    class _Cast_WormGearSet:
        """Special nested class for casting WormGearSet to subclasses."""

        def __init__(self: "WormGearSet._Cast_WormGearSet", parent: "WormGearSet"):
            self._parent = parent

        @property
        def gear_set(self: "WormGearSet._Cast_WormGearSet"):
            return self._parent._cast(_2530.GearSet)

        @property
        def specialised_assembly(self: "WormGearSet._Cast_WormGearSet"):
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.SpecialisedAssembly)

        @property
        def abstract_assembly(self: "WormGearSet._Cast_WormGearSet"):
            from mastapy.system_model.part_model import _2432

            return self._parent._cast(_2432.AbstractAssembly)

        @property
        def part(self: "WormGearSet._Cast_WormGearSet"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Part)

        @property
        def design_entity(self: "WormGearSet._Cast_WormGearSet"):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def worm_gear_set(self: "WormGearSet._Cast_WormGearSet") -> "WormGearSet":
            return self._parent

        def __getattr__(self: "WormGearSet._Cast_WormGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self: Self) -> "_957.WormGearSetDesign":
        """mastapy.gears.gear_designs.worm.WormGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gear_set_design(self: Self) -> "_957.WormGearSetDesign":
        """mastapy.gears.gear_designs.worm.WormGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gears(self: Self) -> "List[_2549.WormGear]":
        """List[mastapy.system_model.part_model.gears.WormGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_meshes(self: Self) -> "List[_2327.WormGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.WormGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "WormGearSet._Cast_WormGearSet":
        return self._Cast_WormGearSet(self)
