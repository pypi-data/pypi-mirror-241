"""GearSetLoadDistributionAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1226
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearSetLoadDistributionAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearSetLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="GearSetLoadDistributionAnalysis")


class GearSetLoadDistributionAnalysis(_1226.GearSetImplementationAnalysis):
    """GearSetLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetLoadDistributionAnalysis")

    class _Cast_GearSetLoadDistributionAnalysis:
        """Special nested class for casting GearSetLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
            parent: "GearSetLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ):
            return self._parent._cast(_1226.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _858

            return self._parent._cast(_858.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _860

            return self._parent._cast(_860.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ):
            from mastapy.gears.ltca.conical import _866

            return self._parent._cast(_866.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_distribution_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ) -> "GearSetLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetLoadDistributionAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_a_system_deflection_analysis(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsASystemDeflectionAnalysis

        if temp is None:
            return False

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis":
        return self._Cast_GearSetLoadDistributionAnalysis(self)
