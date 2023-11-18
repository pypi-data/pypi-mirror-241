"""GearLoadDistributionAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1217
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearLoadDistributionAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="GearLoadDistributionAnalysis")


class GearLoadDistributionAnalysis(_1217.GearImplementationAnalysis):
    """GearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearLoadDistributionAnalysis")

    class _Cast_GearLoadDistributionAnalysis:
        """Special nested class for casting GearLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
            parent: "GearLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_implementation_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ):
            return self._parent._cast(_1217.GearImplementationAnalysis)

        @property
        def gear_design_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1213

            return self._parent._cast(_1213.AbstractGearAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _854

            return self._parent._cast(_854.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ):
            from mastapy.gears.ltca.conical import _865

            return self._parent._cast(_865.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_distribution_analysis(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
        ) -> "GearLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearLoadDistributionAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis":
        return self._Cast_GearLoadDistributionAnalysis(self)
