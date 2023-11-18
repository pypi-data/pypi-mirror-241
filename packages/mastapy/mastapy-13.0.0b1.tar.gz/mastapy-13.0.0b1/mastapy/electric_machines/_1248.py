"""CADStator"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.electric_machines import _1241
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_STATOR = python_net_import("SMT.MastaAPI.ElectricMachines", "CADStator")

if TYPE_CHECKING:
    from mastapy.electric_machines import _1249


__docformat__ = "restructuredtext en"
__all__ = ("CADStator",)


Self = TypeVar("Self", bound="CADStator")


class CADStator(_1241.AbstractStator):
    """CADStator

    This is a mastapy class.
    """

    TYPE = _CAD_STATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADStator")

    class _Cast_CADStator:
        """Special nested class for casting CADStator to subclasses."""

        def __init__(self: "CADStator._Cast_CADStator", parent: "CADStator"):
            self._parent = parent

        @property
        def abstract_stator(self: "CADStator._Cast_CADStator"):
            return self._parent._cast(_1241.AbstractStator)

        @property
        def cad_stator(self: "CADStator._Cast_CADStator") -> "CADStator":
            return self._parent

        def __getattr__(self: "CADStator._Cast_CADStator", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADStator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_stator_partitioning_lines(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AngleBetweenStatorPartitioningLines

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @angle_between_stator_partitioning_lines.setter
    @enforce_parameter_types
    def angle_between_stator_partitioning_lines(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AngleBetweenStatorPartitioningLines = value

    @property
    def importing_full_stator(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ImportingFullStator

        if temp is None:
            return False

        return temp

    @importing_full_stator.setter
    @enforce_parameter_types
    def importing_full_stator(self: Self, value: "bool"):
        self.wrapped.ImportingFullStator = bool(value) if value is not None else False

    @property
    def number_of_slots_for_imported_sector(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSlotsForImportedSector

        if temp is None:
            return 0

        return temp

    @number_of_slots_for_imported_sector.setter
    @enforce_parameter_types
    def number_of_slots_for_imported_sector(self: Self, value: "int"):
        self.wrapped.NumberOfSlotsForImportedSector = (
            int(value) if value is not None else 0
        )

    @property
    def tooth_and_slot(self: Self) -> "_1249.CADToothAndSlot":
        """mastapy.electric_machines.CADToothAndSlot

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothAndSlot

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CADStator._Cast_CADStator":
        return self._Cast_CADStator(self)
