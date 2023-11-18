"""CouplingHalfMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5461
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CouplingHalfMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfMultibodyDynamicsAnalysis")


class CouplingHalfMultibodyDynamicsAnalysis(
    _5461.MountableComponentMultibodyDynamicsAnalysis
):
    """CouplingHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfMultibodyDynamicsAnalysis"
    )

    class _Cast_CouplingHalfMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingHalfMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
            parent: "CouplingHalfMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5461.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(_5401.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(
                _5403.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(
                _5466.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def pulley_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(_5473.PulleyMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(_5478.RollingRingMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(_5501.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(_5503.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5504

            return self._parent._cast(_5504.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(
                _5508.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
        ) -> "CouplingHalfMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfMultibodyDynamicsAnalysis.TYPE"
    ):
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
    ) -> "CouplingHalfMultibodyDynamicsAnalysis._Cast_CouplingHalfMultibodyDynamicsAnalysis":
        return self._Cast_CouplingHalfMultibodyDynamicsAnalysis(self)
