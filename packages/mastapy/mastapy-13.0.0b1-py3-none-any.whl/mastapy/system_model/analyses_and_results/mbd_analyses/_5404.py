"""ConceptCouplingMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5415
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConceptCouplingMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.static_loads import _6838


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingMultibodyDynamicsAnalysis")


class ConceptCouplingMultibodyDynamicsAnalysis(_5415.CouplingMultibodyDynamicsAnalysis):
    """ConceptCouplingMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingMultibodyDynamicsAnalysis"
    )

    class _Cast_ConceptCouplingMultibodyDynamicsAnalysis:
        """Special nested class for casting ConceptCouplingMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
            parent: "ConceptCouplingMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_multibody_dynamics_analysis(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5415.CouplingMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(
                _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5373

            return self._parent._cast(_5373.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
        ) -> "ConceptCouplingMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConceptCouplingMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2579.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6838.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

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
    ) -> "ConceptCouplingMultibodyDynamicsAnalysis._Cast_ConceptCouplingMultibodyDynamicsAnalysis":
        return self._Cast_ConceptCouplingMultibodyDynamicsAnalysis(self)
