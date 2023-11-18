"""GearMeshImplementationDetail"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1220
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshImplementationDetail"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshImplementationDetail",)


Self = TypeVar("Self", bound="GearMeshImplementationDetail")


class GearMeshImplementationDetail(_1220.GearMeshDesignAnalysis):
    """GearMeshImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_IMPLEMENTATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshImplementationDetail")

    class _Cast_GearMeshImplementationDetail:
        """Special nested class for casting GearMeshImplementationDetail to subclasses."""

        def __init__(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
            parent: "GearMeshImplementationDetail",
        ):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ):
            return self._parent._cast(_1220.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ):
            from mastapy.gears.analysis import _1214

            return self._parent._cast(_1214.AbstractGearMeshAnalysis)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ):
            from mastapy.gears.manufacturing.cylindrical import _620

            return self._parent._cast(_620.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_config(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _783

            return self._parent._cast(_783.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _784

            return self._parent._cast(_784.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ):
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalMeshMicroGeometryConfigBase)

        @property
        def face_gear_mesh_micro_geometry(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ):
            from mastapy.gears.gear_designs.face import _990

            return self._parent._cast(_990.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1096

            return self._parent._cast(_1096.CylindricalGearMeshMicroGeometry)

        @property
        def gear_mesh_fe_model(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ):
            from mastapy.gears.fe_model import _1196

            return self._parent._cast(_1196.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ):
            from mastapy.gears.fe_model.cylindrical import _1200

            return self._parent._cast(_1200.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ):
            from mastapy.gears.fe_model.conical import _1203

            return self._parent._cast(_1203.ConicalMeshFEModel)

        @property
        def gear_mesh_implementation_detail(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "GearMeshImplementationDetail":
            return self._parent

        def __getattr__(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshImplementationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail":
        return self._Cast_GearMeshImplementationDetail(self)
