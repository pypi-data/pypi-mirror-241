"""AbstractShaftOrHousing"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model import _2442
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaftOrHousing"
)


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousing",)


Self = TypeVar("Self", bound="AbstractShaftOrHousing")


class AbstractShaftOrHousing(_2442.Component):
    """AbstractShaftOrHousing

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftOrHousing")

    class _Cast_AbstractShaftOrHousing:
        """Special nested class for casting AbstractShaftOrHousing to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousing._Cast_AbstractShaftOrHousing",
            parent: "AbstractShaftOrHousing",
        ):
            self._parent = parent

        @property
        def component(self: "AbstractShaftOrHousing._Cast_AbstractShaftOrHousing"):
            return self._parent._cast(_2442.Component)

        @property
        def part(self: "AbstractShaftOrHousing._Cast_AbstractShaftOrHousing"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Part)

        @property
        def design_entity(self: "AbstractShaftOrHousing._Cast_AbstractShaftOrHousing"):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def abstract_shaft(self: "AbstractShaftOrHousing._Cast_AbstractShaftOrHousing"):
            from mastapy.system_model.part_model import _2433

            return self._parent._cast(_2433.AbstractShaft)

        @property
        def fe_part(self: "AbstractShaftOrHousing._Cast_AbstractShaftOrHousing"):
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.FEPart)

        @property
        def shaft(self: "AbstractShaftOrHousing._Cast_AbstractShaftOrHousing"):
            from mastapy.system_model.part_model.shaft_model import _2480

            return self._parent._cast(_2480.Shaft)

        @property
        def cycloidal_disc(self: "AbstractShaftOrHousing._Cast_AbstractShaftOrHousing"):
            from mastapy.system_model.part_model.cycloidal import _2567

            return self._parent._cast(_2567.CycloidalDisc)

        @property
        def abstract_shaft_or_housing(
            self: "AbstractShaftOrHousing._Cast_AbstractShaftOrHousing",
        ) -> "AbstractShaftOrHousing":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousing._Cast_AbstractShaftOrHousing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftOrHousing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AbstractShaftOrHousing._Cast_AbstractShaftOrHousing":
        return self._Cast_AbstractShaftOrHousing(self)
