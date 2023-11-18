"""BeltDriveDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BeltDriveDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2574
    from mastapy.system_model.analyses_and_results.static_loads import _6819


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveDynamicAnalysis",)


Self = TypeVar("Self", bound="BeltDriveDynamicAnalysis")


class BeltDriveDynamicAnalysis(_6374.SpecialisedAssemblyDynamicAnalysis):
    """BeltDriveDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveDynamicAnalysis")

    class _Cast_BeltDriveDynamicAnalysis:
        """Special nested class for casting BeltDriveDynamicAnalysis to subclasses."""

        def __init__(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
            parent: "BeltDriveDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
        ):
            return self._parent._cast(_6374.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6274

            return self._parent._cast(_6274.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.CVTDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis",
        ) -> "BeltDriveDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDriveDynamicAnalysis.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "BeltDriveDynamicAnalysis._Cast_BeltDriveDynamicAnalysis":
        return self._Cast_BeltDriveDynamicAnalysis(self)
