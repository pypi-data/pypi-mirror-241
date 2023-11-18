"""ConicalMeshManufacturingAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1221
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalMeshManufacturingAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.load_case.conical import _885
    from mastapy.gears.manufacturing.bevel import _793, _777


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshManufacturingAnalysis",)


Self = TypeVar("Self", bound="ConicalMeshManufacturingAnalysis")


class ConicalMeshManufacturingAnalysis(_1221.GearMeshImplementationAnalysis):
    """ConicalMeshManufacturingAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MANUFACTURING_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshManufacturingAnalysis")

    class _Cast_ConicalMeshManufacturingAnalysis:
        """Special nested class for casting ConicalMeshManufacturingAnalysis to subclasses."""

        def __init__(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
            parent: "ConicalMeshManufacturingAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_implementation_analysis(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
        ):
            return self._parent._cast(_1221.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_design_analysis(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
        ):
            from mastapy.gears.analysis import _1220

            return self._parent._cast(_1220.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
        ):
            from mastapy.gears.analysis import _1214

            return self._parent._cast(_1214.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
        ) -> "ConicalMeshManufacturingAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshManufacturingAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_mesh_load_case(self: Self) -> "_885.ConicalMeshLoadCase":
        """mastapy.gears.load_case.conical.ConicalMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tca(self: Self) -> "_793.EaseOffBasedTCA":
        """mastapy.gears.manufacturing.bevel.EaseOffBasedTCA

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TCA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def meshed_gears(self: Self) -> "List[_777.ConicalMeshedGearManufacturingAnalysis]":
        """List[mastapy.gears.manufacturing.bevel.ConicalMeshedGearManufacturingAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis":
        return self._Cast_ConicalMeshManufacturingAnalysis(self)
