"""ConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.materials.efficiency import _300
    from mastapy.system_model.analyses_and_results.system_deflections import _2823
    from mastapy.system_model.analyses_and_results.power_flows import _4065


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionSystemDeflection",)


Self = TypeVar("Self", bound="ConnectionSystemDeflection")


class ConnectionSystemDeflection(_7537.ConnectionFEAnalysis):
    """ConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionSystemDeflection")

    class _Cast_ConnectionSystemDeflection:
        """Special nested class for casting ConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
            parent: "ConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_fe_analysis(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            return self._parent._cast(_7537.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2686,
            )

            return self._parent._cast(
                _2686.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def belt_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2697,
            )

            return self._parent._cast(_2697.BeltConnectionSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelGearMeshSystemDeflection)

        @property
        def clutch_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.ClutchConnectionSystemDeflection)

        @property
        def coaxial_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.CoaxialConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ConceptCouplingConnectionSystemDeflection)

        @property
        def concept_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2718,
            )

            return self._parent._cast(_2718.ConceptGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConicalGearMeshSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.CouplingConnectionSystemDeflection)

        @property
        def cvt_belt_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.CVTBeltConnectionSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(
                _2734.CycloidalDiscCentralBearingConnectionSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(
                _2735.CycloidalDiscPlanetaryBearingConnectionSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2737,
            )

            return self._parent._cast(_2737.CylindricalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2739,
            )

            return self._parent._cast(
                _2739.CylindricalGearMeshSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.FaceGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.GearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.HypoidGearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(
                _2765.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(
                _2766.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(
                _2769.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(
                _2784.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def planetary_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PlanetaryConnectionSystemDeflection)

        @property
        def ring_pins_to_disc_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.RingPinsToDiscConnectionSystemDeflection)

        @property
        def rolling_ring_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(_2796.RollingRingConnectionSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(
                _2803.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.SpiralBevelGearMeshSystemDeflection)

        @property
        def spring_damper_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpringDamperConnectionSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.StraightBevelGearMeshSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.TorqueConverterConnectionSystemDeflection)

        @property
        def worm_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.WormGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.ZerolBevelGearMeshSystemDeflection)

        @property
        def connection_system_deflection(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
        ) -> "ConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def convergence_status(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConvergenceStatus

        if temp is None:
            return 0.0

        return temp

    @property
    def efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Efficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def energy_loss_during_load_case(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyLossDuringLoadCase

        if temp is None:
            return 0.0

        return temp

    @property
    def has_converged(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasConverged

        if temp is None:
            return False

        return temp

    @property
    def is_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def largest_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LargestPower

        if temp is None:
            return 0.0

        return temp

    @property
    def percentage_of_iterations_converged(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageOfIterationsConverged

        if temp is None:
            return 0.0

        return temp

    @property
    def reason_for_non_convergence(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonForNonConvergence

        if temp is None:
            return ""

        return temp

    @property
    def relaxation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Relaxation

        if temp is None:
            return 0.0

        return temp

    @property
    def socket_a_planetary_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketAPlanetaryPower

        if temp is None:
            return 0.0

        return temp

    @property
    def socket_a_planetary_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketAPlanetaryTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def socket_a_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketAPower

        if temp is None:
            return 0.0

        return temp

    @property
    def socket_a_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketATorque

        if temp is None:
            return 0.0

        return temp

    @property
    def socket_a_total_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketATotalPower

        if temp is None:
            return 0.0

        return temp

    @property
    def socket_b_planetary_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketBPlanetaryPower

        if temp is None:
            return 0.0

        return temp

    @property
    def socket_b_planetary_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketBPlanetaryTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def socket_b_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketBPower

        if temp is None:
            return 0.0

        return temp

    @property
    def socket_b_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketBTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def socket_b_total_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketBTotalPower

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2270.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2270.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_loss(self: Self) -> "_300.PowerLoss":
        """mastapy.materials.efficiency.PowerLoss

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection(self: Self) -> "_2823.SystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4065.ConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionSystemDeflection._Cast_ConnectionSystemDeflection":
        return self._Cast_ConnectionSystemDeflection(self)
