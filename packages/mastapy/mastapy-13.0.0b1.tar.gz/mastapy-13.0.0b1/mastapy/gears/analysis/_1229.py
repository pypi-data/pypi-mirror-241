"""GearSetImplementationDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetImplementationDetail"
)

if TYPE_CHECKING:
    from mastapy.utility.scripting import _1739


__docformat__ = "restructuredtext en"
__all__ = ("GearSetImplementationDetail",)


Self = TypeVar("Self", bound="GearSetImplementationDetail")


class GearSetImplementationDetail(_1224.GearSetDesignAnalysis):
    """GearSetImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetImplementationDetail")

    class _Cast_GearSetImplementationDetail:
        """Special nested class for casting GearSetImplementationDetail to subclasses."""

        def __init__(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
            parent: "GearSetImplementationDetail",
        ):
            self._parent = parent

        @property
        def gear_set_design_analysis(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ):
            return self._parent._cast(_1224.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def cylindrical_set_manufacturing_config(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ):
            from mastapy.gears.manufacturing.cylindrical import _623

            return self._parent._cast(_623.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_config(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _789

            return self._parent._cast(_789.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _790

            return self._parent._cast(_790.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _791

            return self._parent._cast(_791.ConicalSetMicroGeometryConfigBase)

        @property
        def face_gear_set_micro_geometry(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ):
            from mastapy.gears.gear_designs.face import _994

            return self._parent._cast(_994.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1105

            return self._parent._cast(_1105.CylindricalGearSetMicroGeometry)

        @property
        def gear_set_fe_model(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ):
            from mastapy.gears.fe_model import _1198

            return self._parent._cast(_1198.GearSetFEModel)

        @property
        def cylindrical_gear_set_fe_model(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ):
            from mastapy.gears.fe_model.cylindrical import _1201

            return self._parent._cast(_1201.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ):
            from mastapy.gears.fe_model.conical import _1204

            return self._parent._cast(_1204.ConicalSetFEModel)

        @property
        def gear_set_implementation_detail(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
        ) -> "GearSetImplementationDetail":
            return self._parent

        def __getattr__(
            self: "GearSetImplementationDetail._Cast_GearSetImplementationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetImplementationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

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
    ) -> "GearSetImplementationDetail._Cast_GearSetImplementationDetail":
        return self._Cast_GearSetImplementationDetail(self)
