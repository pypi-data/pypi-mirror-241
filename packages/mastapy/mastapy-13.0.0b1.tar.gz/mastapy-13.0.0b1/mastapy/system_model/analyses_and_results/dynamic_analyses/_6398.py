"""VirtualComponentDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "VirtualComponentDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentDynamicAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentDynamicAnalysis")


class VirtualComponentDynamicAnalysis(_6353.MountableComponentDynamicAnalysis):
    """VirtualComponentDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentDynamicAnalysis")

    class _Cast_VirtualComponentDynamicAnalysis:
        """Special nested class for casting VirtualComponentDynamicAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
            parent: "VirtualComponentDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            return self._parent._cast(_6353.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def mass_disc_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(_6351.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.MeasurementComponentDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PowerLoadDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
        ) -> "VirtualComponentDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentDynamicAnalysis._Cast_VirtualComponentDynamicAnalysis":
        return self._Cast_VirtualComponentDynamicAnalysis(self)
