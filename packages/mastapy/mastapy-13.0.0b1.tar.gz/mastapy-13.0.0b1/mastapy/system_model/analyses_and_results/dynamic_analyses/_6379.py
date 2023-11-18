"""SpringDamperDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "SpringDamperDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6956


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperDynamicAnalysis",)


Self = TypeVar("Self", bound="SpringDamperDynamicAnalysis")


class SpringDamperDynamicAnalysis(_6312.CouplingDynamicAnalysis):
    """SpringDamperDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperDynamicAnalysis")

    class _Cast_SpringDamperDynamicAnalysis:
        """Special nested class for casting SpringDamperDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
            parent: "SpringDamperDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_dynamic_analysis(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
        ):
            return self._parent._cast(_6312.CouplingDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6274

            return self._parent._cast(_6274.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
        ) -> "SpringDamperDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2598.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6956.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

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
    ) -> "SpringDamperDynamicAnalysis._Cast_SpringDamperDynamicAnalysis":
        return self._Cast_SpringDamperDynamicAnalysis(self)
