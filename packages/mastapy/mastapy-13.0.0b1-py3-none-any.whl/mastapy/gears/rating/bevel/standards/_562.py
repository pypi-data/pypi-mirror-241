"""SpiralBevelRateableMesh"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.rating.agma_gleason_conical import _566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_RATEABLE_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Bevel.Standards", "SpiralBevelRateableMesh"
)


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelRateableMesh",)


Self = TypeVar("Self", bound="SpiralBevelRateableMesh")


class SpiralBevelRateableMesh(_566.AGMAGleasonConicalRateableMesh):
    """SpiralBevelRateableMesh

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_RATEABLE_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelRateableMesh")

    class _Cast_SpiralBevelRateableMesh:
        """Special nested class for casting SpiralBevelRateableMesh to subclasses."""

        def __init__(
            self: "SpiralBevelRateableMesh._Cast_SpiralBevelRateableMesh",
            parent: "SpiralBevelRateableMesh",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_rateable_mesh(
            self: "SpiralBevelRateableMesh._Cast_SpiralBevelRateableMesh",
        ):
            return self._parent._cast(_566.AGMAGleasonConicalRateableMesh)

        @property
        def conical_rateable_mesh(
            self: "SpiralBevelRateableMesh._Cast_SpiralBevelRateableMesh",
        ):
            from mastapy.gears.rating.conical import _545

            return self._parent._cast(_545.ConicalRateableMesh)

        @property
        def rateable_mesh(
            self: "SpiralBevelRateableMesh._Cast_SpiralBevelRateableMesh",
        ):
            from mastapy.gears.rating import _365

            return self._parent._cast(_365.RateableMesh)

        @property
        def spiral_bevel_rateable_mesh(
            self: "SpiralBevelRateableMesh._Cast_SpiralBevelRateableMesh",
        ) -> "SpiralBevelRateableMesh":
            return self._parent

        def __getattr__(
            self: "SpiralBevelRateableMesh._Cast_SpiralBevelRateableMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelRateableMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def safety_factor_scoring(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SafetyFactorScoring

        if temp is None:
            return 0.0

        return temp

    @safety_factor_scoring.setter
    @enforce_parameter_types
    def safety_factor_scoring(self: Self, value: "float"):
        self.wrapped.SafetyFactorScoring = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "SpiralBevelRateableMesh._Cast_SpiralBevelRateableMesh":
        return self._Cast_SpiralBevelRateableMesh(self)
