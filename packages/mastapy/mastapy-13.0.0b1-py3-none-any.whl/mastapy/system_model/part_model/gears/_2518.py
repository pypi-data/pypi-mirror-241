"""BevelGearSet"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.gears import _2512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGearSet"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSet",)


Self = TypeVar("Self", bound="BevelGearSet")


class BevelGearSet(_2512.AGMAGleasonConicalGearSet):
    """BevelGearSet

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSet")

    class _Cast_BevelGearSet:
        """Special nested class for casting BevelGearSet to subclasses."""

        def __init__(self: "BevelGearSet._Cast_BevelGearSet", parent: "BevelGearSet"):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            return self._parent._cast(_2512.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.ConicalGearSet)

        @property
        def gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.GearSet)

        @property
        def specialised_assembly(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.SpecialisedAssembly)

        @property
        def abstract_assembly(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model import _2432

            return self._parent._cast(_2432.AbstractAssembly)

        @property
        def part(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Part)

        @property
        def design_entity(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def bevel_differential_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2514

            return self._parent._cast(_2514.BevelDifferentialGearSet)

        @property
        def spiral_bevel_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.StraightBevelGearSet)

        @property
        def zerol_bevel_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.ZerolBevelGearSet)

        @property
        def bevel_gear_set(self: "BevelGearSet._Cast_BevelGearSet") -> "BevelGearSet":
            return self._parent

        def __getattr__(self: "BevelGearSet._Cast_BevelGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelGearSet._Cast_BevelGearSet":
        return self._Cast_BevelGearSet(self)
