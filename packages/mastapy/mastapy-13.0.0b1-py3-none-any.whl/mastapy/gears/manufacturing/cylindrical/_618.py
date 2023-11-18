"""CylindricalManufacturedGearSetDutyCycle"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1228
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_SET_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "CylindricalManufacturedGearSetDutyCycle",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _623
    from mastapy.gears.rating.cylindrical import _461


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalManufacturedGearSetDutyCycle",)


Self = TypeVar("Self", bound="CylindricalManufacturedGearSetDutyCycle")


class CylindricalManufacturedGearSetDutyCycle(
    _1228.GearSetImplementationAnalysisDutyCycle
):
    """CylindricalManufacturedGearSetDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_SET_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalManufacturedGearSetDutyCycle"
    )

    class _Cast_CylindricalManufacturedGearSetDutyCycle:
        """Special nested class for casting CylindricalManufacturedGearSetDutyCycle to subclasses."""

        def __init__(
            self: "CylindricalManufacturedGearSetDutyCycle._Cast_CylindricalManufacturedGearSetDutyCycle",
            parent: "CylindricalManufacturedGearSetDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "CylindricalManufacturedGearSetDutyCycle._Cast_CylindricalManufacturedGearSetDutyCycle",
        ):
            return self._parent._cast(_1228.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "CylindricalManufacturedGearSetDutyCycle._Cast_CylindricalManufacturedGearSetDutyCycle",
        ):
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "CylindricalManufacturedGearSetDutyCycle._Cast_CylindricalManufacturedGearSetDutyCycle",
        ):
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalManufacturedGearSetDutyCycle._Cast_CylindricalManufacturedGearSetDutyCycle",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "CylindricalManufacturedGearSetDutyCycle._Cast_CylindricalManufacturedGearSetDutyCycle",
        ) -> "CylindricalManufacturedGearSetDutyCycle":
            return self._parent

        def __getattr__(
            self: "CylindricalManufacturedGearSetDutyCycle._Cast_CylindricalManufacturedGearSetDutyCycle",
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
        self: Self, instance_to_wrap: "CylindricalManufacturedGearSetDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def manufacturing_configuration(
        self: Self,
    ) -> "_623.CylindricalSetManufacturingConfig":
        """mastapy.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturingConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_461.CylindricalGearSetDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalManufacturedGearSetDutyCycle._Cast_CylindricalManufacturedGearSetDutyCycle":
        return self._Cast_CylindricalManufacturedGearSetDutyCycle(self)
