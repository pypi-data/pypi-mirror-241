"""SpiralBevelGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2518
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.spiral_bevel import _969
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.connections_and_sockets.gears import _2321


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSet",)


Self = TypeVar("Self", bound="SpiralBevelGearSet")


class SpiralBevelGearSet(_2518.BevelGearSet):
    """SpiralBevelGearSet

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSet")

    class _Cast_SpiralBevelGearSet:
        """Special nested class for casting SpiralBevelGearSet to subclasses."""

        def __init__(
            self: "SpiralBevelGearSet._Cast_SpiralBevelGearSet",
            parent: "SpiralBevelGearSet",
        ):
            self._parent = parent

        @property
        def bevel_gear_set(self: "SpiralBevelGearSet._Cast_SpiralBevelGearSet"):
            return self._parent._cast(_2518.BevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "SpiralBevelGearSet._Cast_SpiralBevelGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2512

            return self._parent._cast(_2512.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(self: "SpiralBevelGearSet._Cast_SpiralBevelGearSet"):
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.ConicalGearSet)

        @property
        def gear_set(self: "SpiralBevelGearSet._Cast_SpiralBevelGearSet"):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.GearSet)

        @property
        def specialised_assembly(self: "SpiralBevelGearSet._Cast_SpiralBevelGearSet"):
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.SpecialisedAssembly)

        @property
        def abstract_assembly(self: "SpiralBevelGearSet._Cast_SpiralBevelGearSet"):
            from mastapy.system_model.part_model import _2432

            return self._parent._cast(_2432.AbstractAssembly)

        @property
        def part(self: "SpiralBevelGearSet._Cast_SpiralBevelGearSet"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Part)

        @property
        def design_entity(self: "SpiralBevelGearSet._Cast_SpiralBevelGearSet"):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def spiral_bevel_gear_set(
            self: "SpiralBevelGearSet._Cast_SpiralBevelGearSet",
        ) -> "SpiralBevelGearSet":
            return self._parent

        def __getattr__(self: "SpiralBevelGearSet._Cast_SpiralBevelGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self: Self) -> "_969.SpiralBevelGearSetDesign":
        """mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gear_set_design(self: Self) -> "_969.SpiralBevelGearSetDesign":
        """mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gears(self: Self) -> "List[_2541.SpiralBevelGear]":
        """List[mastapy.system_model.part_model.gears.SpiralBevelGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes(self: Self) -> "List[_2321.SpiralBevelGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "SpiralBevelGearSet._Cast_SpiralBevelGearSet":
        return self._Cast_SpiralBevelGearSet(self)
