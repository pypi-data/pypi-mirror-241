"""TorqueConverterPump"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.couplings import _2582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterPump"
)


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPump",)


Self = TypeVar("Self", bound="TorqueConverterPump")


class TorqueConverterPump(_2582.CouplingHalf):
    """TorqueConverterPump

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterPump")

    class _Cast_TorqueConverterPump:
        """Special nested class for casting TorqueConverterPump to subclasses."""

        def __init__(
            self: "TorqueConverterPump._Cast_TorqueConverterPump",
            parent: "TorqueConverterPump",
        ):
            self._parent = parent

        @property
        def coupling_half(self: "TorqueConverterPump._Cast_TorqueConverterPump"):
            return self._parent._cast(_2582.CouplingHalf)

        @property
        def mountable_component(self: "TorqueConverterPump._Cast_TorqueConverterPump"):
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.MountableComponent)

        @property
        def component(self: "TorqueConverterPump._Cast_TorqueConverterPump"):
            from mastapy.system_model.part_model import _2442

            return self._parent._cast(_2442.Component)

        @property
        def part(self: "TorqueConverterPump._Cast_TorqueConverterPump"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Part)

        @property
        def design_entity(self: "TorqueConverterPump._Cast_TorqueConverterPump"):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def torque_converter_pump(
            self: "TorqueConverterPump._Cast_TorqueConverterPump",
        ) -> "TorqueConverterPump":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPump._Cast_TorqueConverterPump", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterPump.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "TorqueConverterPump._Cast_TorqueConverterPump":
        return self._Cast_TorqueConverterPump(self)
