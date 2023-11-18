"""ConicalGearLoadDistributionAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.ltca import _838
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Conical", "ConicalGearLoadDistributionAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="ConicalGearLoadDistributionAnalysis")


class ConicalGearLoadDistributionAnalysis(_838.GearLoadDistributionAnalysis):
    """ConicalGearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearLoadDistributionAnalysis")

    class _Cast_ConicalGearLoadDistributionAnalysis:
        """Special nested class for casting ConicalGearLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearLoadDistributionAnalysis._Cast_ConicalGearLoadDistributionAnalysis",
            parent: "ConicalGearLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_load_distribution_analysis(
            self: "ConicalGearLoadDistributionAnalysis._Cast_ConicalGearLoadDistributionAnalysis",
        ):
            return self._parent._cast(_838.GearLoadDistributionAnalysis)

        @property
        def gear_implementation_analysis(
            self: "ConicalGearLoadDistributionAnalysis._Cast_ConicalGearLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.GearImplementationAnalysis)

        @property
        def gear_design_analysis(
            self: "ConicalGearLoadDistributionAnalysis._Cast_ConicalGearLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearLoadDistributionAnalysis._Cast_ConicalGearLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1213

            return self._parent._cast(_1213.AbstractGearAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "ConicalGearLoadDistributionAnalysis._Cast_ConicalGearLoadDistributionAnalysis",
        ) -> "ConicalGearLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearLoadDistributionAnalysis._Cast_ConicalGearLoadDistributionAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "ConicalGearLoadDistributionAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConicalGearLoadDistributionAnalysis._Cast_ConicalGearLoadDistributionAnalysis"
    ):
        return self._Cast_ConicalGearLoadDistributionAnalysis(self)
