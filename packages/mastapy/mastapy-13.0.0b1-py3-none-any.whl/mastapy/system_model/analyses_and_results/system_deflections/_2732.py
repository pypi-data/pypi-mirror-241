"""CVTSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2698
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CVTSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584
    from mastapy.system_model.analyses_and_results.power_flows import _4071


__docformat__ = "restructuredtext en"
__all__ = ("CVTSystemDeflection",)


Self = TypeVar("Self", bound="CVTSystemDeflection")


class CVTSystemDeflection(_2698.BeltDriveSystemDeflection):
    """CVTSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTSystemDeflection")

    class _Cast_CVTSystemDeflection:
        """Special nested class for casting CVTSystemDeflection to subclasses."""

        def __init__(
            self: "CVTSystemDeflection._Cast_CVTSystemDeflection",
            parent: "CVTSystemDeflection",
        ):
            self._parent = parent

        @property
        def belt_drive_system_deflection(
            self: "CVTSystemDeflection._Cast_CVTSystemDeflection",
        ):
            return self._parent._cast(_2698.BeltDriveSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "CVTSystemDeflection._Cast_CVTSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "CVTSystemDeflection._Cast_CVTSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2683,
            )

            return self._parent._cast(_2683.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "CVTSystemDeflection._Cast_CVTSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(self: "CVTSystemDeflection._Cast_CVTSystemDeflection"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTSystemDeflection._Cast_CVTSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "CVTSystemDeflection._Cast_CVTSystemDeflection"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "CVTSystemDeflection._Cast_CVTSystemDeflection"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTSystemDeflection._Cast_CVTSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTSystemDeflection._Cast_CVTSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_system_deflection(
            self: "CVTSystemDeflection._Cast_CVTSystemDeflection",
        ) -> "CVTSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTSystemDeflection._Cast_CVTSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_belt_clamping_force_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumBeltClampingForceSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_required_clamping_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumRequiredClampingForce

        if temp is None:
            return 0.0

        return temp

    @property
    def assembly_design(self: Self) -> "_2584.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4071.CVTPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CVTPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTSystemDeflection._Cast_CVTSystemDeflection":
        return self._Cast_CVTSystemDeflection(self)
