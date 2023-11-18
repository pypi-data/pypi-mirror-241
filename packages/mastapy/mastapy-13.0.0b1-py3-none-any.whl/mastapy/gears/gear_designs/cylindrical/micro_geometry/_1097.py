"""CylindricalGearMeshMicroGeometryDutyCycle"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.ltca.cylindrical import _855
from mastapy.gears.analysis import _1220
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_MICRO_GEOMETRY_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearMeshMicroGeometryDutyCycle",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _461
    from mastapy.utility.property import _1840


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshMicroGeometryDutyCycle",)


Self = TypeVar("Self", bound="CylindricalGearMeshMicroGeometryDutyCycle")


class CylindricalGearMeshMicroGeometryDutyCycle(_1220.GearMeshDesignAnalysis):
    """CylindricalGearMeshMicroGeometryDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_MICRO_GEOMETRY_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshMicroGeometryDutyCycle"
    )

    class _Cast_CylindricalGearMeshMicroGeometryDutyCycle:
        """Special nested class for casting CylindricalGearMeshMicroGeometryDutyCycle to subclasses."""

        def __init__(
            self: "CylindricalGearMeshMicroGeometryDutyCycle._Cast_CylindricalGearMeshMicroGeometryDutyCycle",
            parent: "CylindricalGearMeshMicroGeometryDutyCycle",
        ):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(
            self: "CylindricalGearMeshMicroGeometryDutyCycle._Cast_CylindricalGearMeshMicroGeometryDutyCycle",
        ):
            return self._parent._cast(_1220.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "CylindricalGearMeshMicroGeometryDutyCycle._Cast_CylindricalGearMeshMicroGeometryDutyCycle",
        ):
            from mastapy.gears.analysis import _1214

            return self._parent._cast(_1214.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(
            self: "CylindricalGearMeshMicroGeometryDutyCycle._Cast_CylindricalGearMeshMicroGeometryDutyCycle",
        ) -> "CylindricalGearMeshMicroGeometryDutyCycle":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshMicroGeometryDutyCycle._Cast_CylindricalGearMeshMicroGeometryDutyCycle",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshMicroGeometryDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_set_duty_cycle_rating(
        self: Self,
    ) -> "_461.CylindricalGearSetDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def peak_to_peak_te(
        self: Self,
    ) -> "_1840.DutyCyclePropertySummaryVeryShortLength[_855.CylindricalGearMeshLoadDistributionAnalysis]":
        """mastapy.utility.property.DutyCyclePropertySummaryVeryShortLength[mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadDistributionAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakToPeakTE

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _855.CylindricalGearMeshLoadDistributionAnalysis
        ](temp)

    @property
    def meshes_analysis(
        self: Self,
    ) -> "List[_855.CylindricalGearMeshLoadDistributionAnalysis]":
        """List[mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadDistributionAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshMicroGeometryDutyCycle._Cast_CylindricalGearMeshMicroGeometryDutyCycle":
        return self._Cast_CylindricalGearMeshMicroGeometryDutyCycle(self)
