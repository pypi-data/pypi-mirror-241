"""CouplingHalfDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CouplingHalfDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfDynamicAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfDynamicAnalysis")


class CouplingHalfDynamicAnalysis(_6353.MountableComponentDynamicAnalysis):
    """CouplingHalfDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfDynamicAnalysis")

    class _Cast_CouplingHalfDynamicAnalysis:
        """Special nested class for casting CouplingHalfDynamicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
            parent: "CouplingHalfDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            return self._parent._cast(_6353.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297

            return self._parent._cast(_6297.ClutchHalfDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ConceptCouplingHalfDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.CVTPulleyDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.PulleyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.RollingRingDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.SpringDamperHalfDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.TorqueConverterTurbineDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
        ) -> "CouplingHalfDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2582.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

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
    ) -> "CouplingHalfDynamicAnalysis._Cast_CouplingHalfDynamicAnalysis":
        return self._Cast_CouplingHalfDynamicAnalysis(self)
