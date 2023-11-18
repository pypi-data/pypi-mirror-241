"""ConceptCouplingHalfMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5414
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConceptCouplingHalfMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580
    from mastapy.system_model.analyses_and_results.static_loads import _6837


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingHalfMultibodyDynamicsAnalysis")


class ConceptCouplingHalfMultibodyDynamicsAnalysis(
    _5414.CouplingHalfMultibodyDynamicsAnalysis
):
    """ConceptCouplingHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis"
    )

    class _Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis:
        """Special nested class for casting ConceptCouplingHalfMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
            parent: "ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5414.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(_5401.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "ConceptCouplingHalfMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ConceptCouplingHalfMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2580.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6837.ConceptCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

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
    ) -> "ConceptCouplingHalfMultibodyDynamicsAnalysis._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis":
        return self._Cast_ConceptCouplingHalfMultibodyDynamicsAnalysis(self)
