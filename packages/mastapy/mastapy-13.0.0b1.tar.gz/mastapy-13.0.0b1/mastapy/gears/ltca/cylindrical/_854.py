"""CylindricalGearLoadDistributionAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.ltca import _838
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalGearLoadDistributionAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _458
    from mastapy.gears.gear_two_d_fe_analysis import _896


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearLoadDistributionAnalysis")


class CylindricalGearLoadDistributionAnalysis(_838.GearLoadDistributionAnalysis):
    """CylindricalGearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearLoadDistributionAnalysis"
    )

    class _Cast_CylindricalGearLoadDistributionAnalysis:
        """Special nested class for casting CylindricalGearLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
            parent: "CylindricalGearLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_load_distribution_analysis(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
        ):
            return self._parent._cast(_838.GearLoadDistributionAnalysis)

        @property
        def gear_implementation_analysis(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.GearImplementationAnalysis)

        @property
        def gear_design_analysis(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1213

            return self._parent._cast(_1213.AbstractGearAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
        ) -> "CylindricalGearLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearLoadDistributionAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_458.CylindricalGearRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tiff_analysis(self: Self) -> "_896.CylindricalGearTIFFAnalysis":
        """mastapy.gears.gear_two_d_fe_analysis.CylindricalGearTIFFAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TIFFAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearLoadDistributionAnalysis._Cast_CylindricalGearLoadDistributionAnalysis":
        return self._Cast_CylindricalGearLoadDistributionAnalysis(self)
