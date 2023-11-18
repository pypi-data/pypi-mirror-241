"""KlingelnbergCycloPalloidHypoidGearDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import _6913


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearDynamicAnalysis")


class KlingelnbergCycloPalloidHypoidGearDynamicAnalysis(
    _6342.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            return self._parent._cast(
                _6342.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def conical_gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306

            return self._parent._cast(_6306.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2536.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6913.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearDynamicAnalysis(self)
