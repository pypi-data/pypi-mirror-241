"""ConicalMeshLoadDistributionAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.ltca import _839
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Conical", "ConicalMeshLoadDistributionAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.load_case.conical import _885
    from mastapy.gears.manufacturing.bevel import _782
    from mastapy.gears.ltca.conical import _867


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="ConicalMeshLoadDistributionAnalysis")


class ConicalMeshLoadDistributionAnalysis(_839.GearMeshLoadDistributionAnalysis):
    """ConicalMeshLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshLoadDistributionAnalysis")

    class _Cast_ConicalMeshLoadDistributionAnalysis:
        """Special nested class for casting ConicalMeshLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "ConicalMeshLoadDistributionAnalysis._Cast_ConicalMeshLoadDistributionAnalysis",
            parent: "ConicalMeshLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_load_distribution_analysis(
            self: "ConicalMeshLoadDistributionAnalysis._Cast_ConicalMeshLoadDistributionAnalysis",
        ):
            return self._parent._cast(_839.GearMeshLoadDistributionAnalysis)

        @property
        def gear_mesh_implementation_analysis(
            self: "ConicalMeshLoadDistributionAnalysis._Cast_ConicalMeshLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_design_analysis(
            self: "ConicalMeshLoadDistributionAnalysis._Cast_ConicalMeshLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1220

            return self._parent._cast(_1220.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConicalMeshLoadDistributionAnalysis._Cast_ConicalMeshLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1214

            return self._parent._cast(_1214.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "ConicalMeshLoadDistributionAnalysis._Cast_ConicalMeshLoadDistributionAnalysis",
        ) -> "ConicalMeshLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalMeshLoadDistributionAnalysis._Cast_ConicalMeshLoadDistributionAnalysis",
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
        self: Self, instance_to_wrap: "ConicalMeshLoadDistributionAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_roll_angles(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfRollAngles

        if temp is None:
            return 0

        return temp

    @property
    def pinion_mean_te(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionMeanTE

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_peak_to_peak_te(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionPeakToPeakTE

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_peak_to_peak_te(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelPeakToPeakTE

        if temp is None:
            return 0.0

        return temp

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
    def conical_mesh_manufacturing_analysis(
        self: Self,
    ) -> "_782.ConicalMeshManufacturingAnalysis":
        """mastapy.gears.manufacturing.bevel.ConicalMeshManufacturingAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshManufacturingAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def meshed_gears(
        self: Self,
    ) -> "List[_867.ConicalMeshedGearLoadDistributionAnalysis]":
        """List[mastapy.gears.ltca.conical.ConicalMeshedGearLoadDistributionAnalysis]

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
    ) -> (
        "ConicalMeshLoadDistributionAnalysis._Cast_ConicalMeshLoadDistributionAnalysis"
    ):
        return self._Cast_ConicalMeshLoadDistributionAnalysis(self)
