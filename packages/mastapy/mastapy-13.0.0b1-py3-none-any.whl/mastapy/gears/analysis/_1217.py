"""GearImplementationAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearImplementationAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearImplementationAnalysis",)


Self = TypeVar("Self", bound="GearImplementationAnalysis")


class GearImplementationAnalysis(_1216.GearDesignAnalysis):
    """GearImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_IMPLEMENTATION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearImplementationAnalysis")

    class _Cast_GearImplementationAnalysis:
        """Special nested class for casting GearImplementationAnalysis to subclasses."""

        def __init__(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
            parent: "GearImplementationAnalysis",
        ):
            self._parent = parent

        @property
        def gear_design_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            return self._parent._cast(_1216.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.analysis import _1213

            return self._parent._cast(_1213.AbstractGearAnalysis)

        @property
        def cylindrical_manufactured_gear_load_case(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _615

            return self._parent._cast(_615.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _773

            return self._parent._cast(_773.ConicalGearManufacturingAnalysis)

        @property
        def gear_load_distribution_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.ltca import _838

            return self._parent._cast(_838.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _854

            return self._parent._cast(_854.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ):
            from mastapy.gears.ltca.conical import _865

            return self._parent._cast(_865.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_implementation_analysis(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
        ) -> "GearImplementationAnalysis":
            return self._parent

        def __getattr__(
            self: "GearImplementationAnalysis._Cast_GearImplementationAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearImplementationAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearImplementationAnalysis._Cast_GearImplementationAnalysis":
        return self._Cast_GearImplementationAnalysis(self)
