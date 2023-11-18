"""BeltDriveSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2804
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BeltDriveSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2574
    from mastapy.system_model.analyses_and_results.static_loads import _6819
    from mastapy.system_model.analyses_and_results.power_flows import _4040
    from mastapy.system_model.analyses_and_results.system_deflections import _2697


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveSystemDeflection",)


Self = TypeVar("Self", bound="BeltDriveSystemDeflection")


class BeltDriveSystemDeflection(_2804.SpecialisedAssemblySystemDeflection):
    """BeltDriveSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveSystemDeflection")

    class _Cast_BeltDriveSystemDeflection:
        """Special nested class for casting BeltDriveSystemDeflection to subclasses."""

        def __init__(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
            parent: "BeltDriveSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_system_deflection(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
        ):
            return self._parent._cast(_2804.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2683,
            )

            return self._parent._cast(_2683.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_system_deflection(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CVTSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection",
        ) -> "BeltDriveSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDriveSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2574.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6819.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4040.BeltDrivePowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BeltDrivePowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def belts(self: Self) -> "List[_2697.BeltConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Belts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveSystemDeflection._Cast_BeltDriveSystemDeflection":
        return self._Cast_BeltDriveSystemDeflection(self)
