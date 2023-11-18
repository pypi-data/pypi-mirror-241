"""ConceptCouplingHalf"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.couplings import _2582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCouplingHalf"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalf",)


Self = TypeVar("Self", bound="ConceptCouplingHalf")


class ConceptCouplingHalf(_2582.CouplingHalf):
    """ConceptCouplingHalf

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingHalf")

    class _Cast_ConceptCouplingHalf:
        """Special nested class for casting ConceptCouplingHalf to subclasses."""

        def __init__(
            self: "ConceptCouplingHalf._Cast_ConceptCouplingHalf",
            parent: "ConceptCouplingHalf",
        ):
            self._parent = parent

        @property
        def coupling_half(self: "ConceptCouplingHalf._Cast_ConceptCouplingHalf"):
            return self._parent._cast(_2582.CouplingHalf)

        @property
        def mountable_component(self: "ConceptCouplingHalf._Cast_ConceptCouplingHalf"):
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.MountableComponent)

        @property
        def component(self: "ConceptCouplingHalf._Cast_ConceptCouplingHalf"):
            from mastapy.system_model.part_model import _2442

            return self._parent._cast(_2442.Component)

        @property
        def part(self: "ConceptCouplingHalf._Cast_ConceptCouplingHalf"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Part)

        @property
        def design_entity(self: "ConceptCouplingHalf._Cast_ConceptCouplingHalf"):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def concept_coupling_half(
            self: "ConceptCouplingHalf._Cast_ConceptCouplingHalf",
        ) -> "ConceptCouplingHalf":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalf._Cast_ConceptCouplingHalf", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCouplingHalf.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConceptCouplingHalf._Cast_ConceptCouplingHalf":
        return self._Cast_ConceptCouplingHalf(self)
