"""GearImplementationDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearImplementationDetail"
)

if TYPE_CHECKING:
    from mastapy.utility.scripting import _1739


__docformat__ = "restructuredtext en"
__all__ = ("GearImplementationDetail",)


Self = TypeVar("Self", bound="GearImplementationDetail")


class GearImplementationDetail(_1216.GearDesignAnalysis):
    """GearImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_IMPLEMENTATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearImplementationDetail")

    class _Cast_GearImplementationDetail:
        """Special nested class for casting GearImplementationDetail to subclasses."""

        def __init__(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
            parent: "GearImplementationDetail",
        ):
            self._parent = parent

        @property
        def gear_design_analysis(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            return self._parent._cast(_1216.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.analysis import _1213

            return self._parent._cast(_1213.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.cylindrical import _610

            return self._parent._cast(_610.CylindricalGearManufacturingConfig)

        @property
        def conical_gear_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _774

            return self._parent._cast(_774.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _775

            return self._parent._cast(_775.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _776

            return self._parent._cast(_776.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _786

            return self._parent._cast(_786.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _787

            return self._parent._cast(_787.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _792

            return self._parent._cast(_792.ConicalWheelManufacturingConfig)

        @property
        def face_gear_micro_geometry(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.gear_designs.face import _991

            return self._parent._cast(_991.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1098

            return self._parent._cast(_1098.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1099

            return self._parent._cast(_1099.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102

            return self._parent._cast(_1102.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.fe_model import _1195

            return self._parent._cast(_1195.GearFEModel)

        @property
        def cylindrical_gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.fe_model.cylindrical import _1199

            return self._parent._cast(_1199.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ):
            from mastapy.gears.fe_model.conical import _1202

            return self._parent._cast(_1202.ConicalGearFEModel)

        @property
        def gear_implementation_detail(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "GearImplementationDetail":
            return self._parent

        def __getattr__(
            self: "GearImplementationDetail._Cast_GearImplementationDetail", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearImplementationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def user_specified_data(self: Self) -> "_1739.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearImplementationDetail._Cast_GearImplementationDetail":
        return self._Cast_GearImplementationDetail(self)
