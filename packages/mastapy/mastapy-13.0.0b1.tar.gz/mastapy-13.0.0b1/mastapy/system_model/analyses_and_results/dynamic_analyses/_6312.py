"""CouplingDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CouplingDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581


__docformat__ = "restructuredtext en"
__all__ = ("CouplingDynamicAnalysis",)


Self = TypeVar("Self", bound="CouplingDynamicAnalysis")


class CouplingDynamicAnalysis(_6374.SpecialisedAssemblyDynamicAnalysis):
    """CouplingDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingDynamicAnalysis")

    class _Cast_CouplingDynamicAnalysis:
        """Special nested class for casting CouplingDynamicAnalysis to subclasses."""

        def __init__(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
            parent: "CouplingDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            return self._parent._cast(_6374.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6274

            return self._parent._cast(_6274.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.ClutchDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ConceptCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartToPartShearCouplingDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpringDamperDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.TorqueConverterDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "CouplingDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2581.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis":
        return self._Cast_CouplingDynamicAnalysis(self)
