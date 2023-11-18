"""TorqueConverterConnectionMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5413
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "TorqueConverterConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5509
    from mastapy.system_model.connections_and_sockets.couplings import _2350
    from mastapy.system_model.analyses_and_results.static_loads import _6970


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterConnectionMultibodyDynamicsAnalysis")


class TorqueConverterConnectionMultibodyDynamicsAnalysis(
    _5413.CouplingConnectionMultibodyDynamicsAnalysis
):
    """TorqueConverterConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting TorqueConverterConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
            parent: "TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5413.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5446

            return self._parent._cast(
                _5446.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
        ) -> "TorqueConverterConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "TorqueConverterConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def capacity_factor_k(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CapacityFactorK

        if temp is None:
            return 0.0

        return temp

    @property
    def inverse_capacity_factor_1k(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InverseCapacityFactor1K

        if temp is None:
            return 0.0

        return temp

    @property
    def is_locked(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLocked

        if temp is None:
            return False

        return temp

    @property
    def lock_up_clutch_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LockUpClutchTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def lock_up_viscous_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LockUpViscousTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def locked_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LockedTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def locking_status(self: Self) -> "_5509.TorqueConverterStatus":
        """mastapy.system_model.analyses_and_results.mbd_analyses.TorqueConverterStatus

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LockingStatus

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.TorqueConverterStatus",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5509",
            "TorqueConverterStatus",
        )(value)

    @property
    def percentage_applied_pressure(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PercentageAppliedPressure

        if temp is None:
            return 0.0

        return temp

    @percentage_applied_pressure.setter
    @enforce_parameter_types
    def percentage_applied_pressure(self: Self, value: "float"):
        self.wrapped.PercentageAppliedPressure = (
            float(value) if value is not None else 0.0
        )

    @property
    def power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def pump_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PumpTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def speed_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def turbine_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TurbineTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2350.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6970.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis":
        return self._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis(self)
