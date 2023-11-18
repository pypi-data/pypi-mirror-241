"""Component"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._math.vector_3d import Vector3D
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model import _2466
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")

if TYPE_CHECKING:
    from mastapy.math_utility import _1496, _1497
    from mastapy.system_model.connections_and_sockets import _2268, _2270, _2294, _2289
    from mastapy.system_model.part_model import _2443


__docformat__ = "restructuredtext en"
__all__ = ("Component",)


Self = TypeVar("Self", bound="Component")


class Component(_2466.Part):
    """Component

    This is a mastapy class.
    """

    TYPE = _COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Component")

    class _Cast_Component:
        """Special nested class for casting Component to subclasses."""

        def __init__(self: "Component._Cast_Component", parent: "Component"):
            self._parent = parent

        @property
        def part(self: "Component._Cast_Component"):
            return self._parent._cast(_2466.Part)

        @property
        def design_entity(self: "Component._Cast_Component"):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def abstract_shaft(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2433

            return self._parent._cast(_2433.AbstractShaft)

        @property
        def abstract_shaft_or_housing(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2434

            return self._parent._cast(_2434.AbstractShaftOrHousing)

        @property
        def bearing(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2437

            return self._parent._cast(_2437.Bearing)

        @property
        def bolt(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2440

            return self._parent._cast(_2440.Bolt)

        @property
        def connector(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2445

            return self._parent._cast(_2445.Connector)

        @property
        def datum(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Datum)

        @property
        def external_cad_model(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2450

            return self._parent._cast(_2450.ExternalCADModel)

        @property
        def fe_part(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.FEPart)

        @property
        def guide_dxf_model(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2453

            return self._parent._cast(_2453.GuideDxfModel)

        @property
        def mass_disc(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2460

            return self._parent._cast(_2460.MassDisc)

        @property
        def measurement_component(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2461

            return self._parent._cast(_2461.MeasurementComponent)

        @property
        def mountable_component(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.MountableComponent)

        @property
        def oil_seal(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.OilSeal)

        @property
        def planet_carrier(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2467

            return self._parent._cast(_2467.PlanetCarrier)

        @property
        def point_load(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.PointLoad)

        @property
        def power_load(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.PowerLoad)

        @property
        def unbalanced_mass(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.UnbalancedMass)

        @property
        def virtual_component(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model import _2477

            return self._parent._cast(_2477.VirtualComponent)

        @property
        def shaft(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.shaft_model import _2480

            return self._parent._cast(_2480.Shaft)

        @property
        def agma_gleason_conical_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2511

            return self._parent._cast(_2511.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2513

            return self._parent._cast(_2513.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2516

            return self._parent._cast(_2516.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelGear)

        @property
        def concept_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.ConceptGear)

        @property
        def conical_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.ConicalGear)

        @property
        def cylindrical_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.CylindricalGear)

        @property
        def cylindrical_planet_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.CylindricalPlanetGear)

        @property
        def face_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.FaceGear)

        @property
        def gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2528

            return self._parent._cast(_2528.Gear)

        @property
        def hypoid_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "Component._Cast_Component",
        ):
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.StraightBevelSunGear)

        @property
        def worm_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.WormGear)

        @property
        def zerol_bevel_gear(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.ZerolBevelGear)

        @property
        def cycloidal_disc(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.cycloidal import _2567

            return self._parent._cast(_2567.CycloidalDisc)

        @property
        def ring_pins(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.cycloidal import _2568

            return self._parent._cast(_2568.RingPins)

        @property
        def clutch_half(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2577

            return self._parent._cast(_2577.ClutchHalf)

        @property
        def concept_coupling_half(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2580

            return self._parent._cast(_2580.ConceptCouplingHalf)

        @property
        def coupling_half(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2582

            return self._parent._cast(_2582.CouplingHalf)

        @property
        def cvt_pulley(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2585

            return self._parent._cast(_2585.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2587

            return self._parent._cast(_2587.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2588

            return self._parent._cast(_2588.Pulley)

        @property
        def rolling_ring(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2594

            return self._parent._cast(_2594.RollingRing)

        @property
        def shaft_hub_connection(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.ShaftHubConnection)

        @property
        def spring_damper_half(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2599

            return self._parent._cast(_2599.SpringDamperHalf)

        @property
        def synchroniser_half(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.SynchroniserHalf)

        @property
        def synchroniser_part(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2603

            return self._parent._cast(_2603.SynchroniserPart)

        @property
        def synchroniser_sleeve(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.SynchroniserSleeve)

        @property
        def torque_converter_pump(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.TorqueConverterPump)

        @property
        def torque_converter_turbine(self: "Component._Cast_Component"):
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.TorqueConverterTurbine)

        @property
        def component(self: "Component._Cast_Component") -> "Component":
            return self._parent

        def __getattr__(self: "Component._Cast_Component", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Component.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return temp

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(self: Self, value: "float"):
        self.wrapped.AdditionalModalDampingRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def polar_inertia(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PolarInertia

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @polar_inertia.setter
    @enforce_parameter_types
    def polar_inertia(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PolarInertia = value

    @property
    def polar_inertia_for_synchroniser_sizing_only(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PolarInertiaForSynchroniserSizingOnly

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @polar_inertia_for_synchroniser_sizing_only.setter
    @enforce_parameter_types
    def polar_inertia_for_synchroniser_sizing_only(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PolarInertiaForSynchroniserSizingOnly = value

    @property
    def reason_mass_properties_are_unknown(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonMassPropertiesAreUnknown

        if temp is None:
            return ""

        return temp

    @property
    def reason_mass_properties_are_zero(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonMassPropertiesAreZero

        if temp is None:
            return ""

        return temp

    @property
    def translation(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Translation

        if temp is None:
            return ""

        return temp

    @property
    def transverse_inertia(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TransverseInertia

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @transverse_inertia.setter
    @enforce_parameter_types
    def transverse_inertia(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TransverseInertia = value

    @property
    def x_axis(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XAxis

        if temp is None:
            return ""

        return temp

    @property
    def y_axis(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YAxis

        if temp is None:
            return ""

        return temp

    @property
    def z_axis(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZAxis

        if temp is None:
            return ""

        return temp

    @property
    def coordinate_system_euler_angles(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.CoordinateSystemEulerAngles

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @coordinate_system_euler_angles.setter
    @enforce_parameter_types
    def coordinate_system_euler_angles(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.CoordinateSystemEulerAngles = value

    @property
    def local_coordinate_system(self: Self) -> "_1496.CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def position(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.Position

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @position.setter
    @enforce_parameter_types
    def position(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.Position = value

    @property
    def component_connections(self: Self) -> "List[_2268.ComponentConnection]":
        """List[mastapy.system_model.connections_and_sockets.ComponentConnection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def available_socket_offsets(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AvailableSocketOffsets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @property
    def centre_offset(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreOffset

        if temp is None:
            return 0.0

        return temp

    @property
    def translation_vector(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TranslationVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def x_axis_vector(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def y_axis_vector(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def z_axis_vector(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZAxisVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def can_connect_to(self: Self, component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.CanConnectTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def can_delete_connection(self: Self, connection: "_2270.Connection") -> "bool":
        """bool

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.CanDeleteConnection(
            connection.wrapped if connection else None
        )
        return method_result

    @enforce_parameter_types
    def connect_to(
        self: Self, component: "Component"
    ) -> "_2443.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_COMPONENT](
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connect_to_socket(
        self: Self, socket: "_2294.Socket"
    ) -> "_2443.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_SOCKET](
            socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_coordinate_system_editor(self: Self) -> "_1497.CoordinateSystemEditor":
        """mastapy.math_utility.CoordinateSystemEditor"""
        method_result = self.wrapped.CreateCoordinateSystemEditor()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def diameter_at_middle_of_connection(
        self: Self, connection: "_2270.Connection"
    ) -> "float":
        """float

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.DiameterAtMiddleOfConnection(
            connection.wrapped if connection else None
        )
        return method_result

    @enforce_parameter_types
    def diameter_of_socket_for(self: Self, connection: "_2270.Connection") -> "float":
        """float

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.DiameterOfSocketFor(
            connection.wrapped if connection else None
        )
        return method_result

    @enforce_parameter_types
    def is_coaxially_connected_to(self: Self, component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.IsCoaxiallyConnectedTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def is_directly_connected_to(self: Self, component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.IsDirectlyConnectedTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def is_directly_or_indirectly_connected_to(
        self: Self, component: "Component"
    ) -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.IsDirectlyOrIndirectlyConnectedTo(
            component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def move_all_concentric_parts_radially(
        self: Self, delta_x: "float", delta_y: "float"
    ) -> "bool":
        """bool

        Args:
            delta_x (float)
            delta_y (float)
        """
        delta_x = float(delta_x)
        delta_y = float(delta_y)
        method_result = self.wrapped.MoveAllConcentricPartsRadially(
            delta_x if delta_x else 0.0, delta_y if delta_y else 0.0
        )
        return method_result

    @enforce_parameter_types
    def move_along_axis(self: Self, delta: "float"):
        """Method does not return.

        Args:
            delta (float)
        """
        delta = float(delta)
        self.wrapped.MoveAlongAxis(delta if delta else 0.0)

    @enforce_parameter_types
    def move_with_concentric_parts_to_new_origin(
        self: Self, target_origin: "Vector3D"
    ) -> "bool":
        """bool

        Args:
            target_origin (Vector3D)
        """
        target_origin = conversion.mp_to_pn_vector3d(target_origin)
        method_result = self.wrapped.MoveWithConcentricPartsToNewOrigin(target_origin)
        return method_result

    @enforce_parameter_types
    def possible_sockets_to_connect_with_component(
        self: Self, component: "Component"
    ) -> "List[_2294.Socket]":
        """List[mastapy.system_model.connections_and_sockets.Socket]

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.PossibleSocketsToConnectWith.Overloads[_COMPONENT](
                component.wrapped if component else None
            )
        )

    @enforce_parameter_types
    def possible_sockets_to_connect_with(
        self: Self, socket: "_2294.Socket"
    ) -> "List[_2294.Socket]":
        """List[mastapy.system_model.connections_and_sockets.Socket]

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.PossibleSocketsToConnectWith.Overloads[_SOCKET](
                socket.wrapped if socket else None
            )
        )

    @enforce_parameter_types
    def set_position_and_axis_of_component_and_connected_components(
        self: Self, origin: "Vector3D", z_axis: "Vector3D"
    ) -> "_2289.RealignmentResult":
        """mastapy.system_model.connections_and_sockets.RealignmentResult

        Args:
            origin (Vector3D)
            z_axis (Vector3D)
        """
        origin = conversion.mp_to_pn_vector3d(origin)
        z_axis = conversion.mp_to_pn_vector3d(z_axis)
        method_result = (
            self.wrapped.SetPositionAndAxisOfComponentAndConnectedComponents(
                origin, z_axis
            )
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def set_position_and_rotation_of_component_and_connected_components(
        self: Self, new_coordinate_system: "_1496.CoordinateSystem3D"
    ) -> "_2289.RealignmentResult":
        """mastapy.system_model.connections_and_sockets.RealignmentResult

        Args:
            new_coordinate_system (mastapy.math_utility.CoordinateSystem3D)
        """
        method_result = (
            self.wrapped.SetPositionAndRotationOfComponentAndConnectedComponents(
                new_coordinate_system.wrapped if new_coordinate_system else None
            )
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def set_position_of_component_and_connected_components(
        self: Self, position: "Vector3D"
    ) -> "_2289.RealignmentResult":
        """mastapy.system_model.connections_and_sockets.RealignmentResult

        Args:
            position (Vector3D)
        """
        position = conversion.mp_to_pn_vector3d(position)
        method_result = self.wrapped.SetPositionOfComponentAndConnectedComponents(
            position
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def socket_named(self: Self, socket_name: "str") -> "_2294.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            socket_name (str)
        """
        socket_name = str(socket_name)
        method_result = self.wrapped.SocketNamed(socket_name if socket_name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_connect_to(
        self: Self, component: "Component", hint_offset: "float" = float("nan")
    ) -> "_2443.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy.system_model.part_model.Component)
            hint_offset (float, optional)
        """
        hint_offset = float(hint_offset)
        method_result = self.wrapped.TryConnectTo(
            component.wrapped if component else None,
            hint_offset if hint_offset else 0.0,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "Component._Cast_Component":
        return self._Cast_Component(self)
