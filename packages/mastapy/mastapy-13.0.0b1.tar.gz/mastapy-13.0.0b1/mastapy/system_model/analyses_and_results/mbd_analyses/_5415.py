"""CouplingMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5486
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CouplingMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581


__docformat__ = "restructuredtext en"
__all__ = ("CouplingMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CouplingMultibodyDynamicsAnalysis")


class CouplingMultibodyDynamicsAnalysis(
    _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
):
    """CouplingMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingMultibodyDynamicsAnalysis")

    class _Cast_CouplingMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
            parent: "CouplingMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5373

            return self._parent._cast(_5373.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398

            return self._parent._cast(_5398.ClutchMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(
                _5467.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(_5492.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5507

            return self._parent._cast(_5507.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
        ) -> "CouplingMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CouplingMultibodyDynamicsAnalysis.TYPE"
    ):
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
    def cast_to(
        self: Self,
    ) -> "CouplingMultibodyDynamicsAnalysis._Cast_CouplingMultibodyDynamicsAnalysis":
        return self._Cast_CouplingMultibodyDynamicsAnalysis(self)
