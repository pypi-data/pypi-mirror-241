"""DesignEntity"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY = python_net_import("SMT.MastaAPI.SystemModel", "DesignEntity")

if TYPE_CHECKING:
    from mastapy.system_model import _2198
    from mastapy.utility.model_validation import _1792, _1791
    from mastapy.utility.scripting import _1739


__docformat__ = "restructuredtext en"
__all__ = ("DesignEntity",)


Self = TypeVar("Self", bound="DesignEntity")


class DesignEntity(_0.APIBase):
    """DesignEntity

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignEntity")

    class _Cast_DesignEntity:
        """Special nested class for casting DesignEntity to subclasses."""

        def __init__(self: "DesignEntity._Cast_DesignEntity", parent: "DesignEntity"):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets import _2263

            return self._parent._cast(_2263.AbstractShaftToMountableComponentConnection)

        @property
        def belt_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2266

            return self._parent._cast(_2266.BeltConnection)

        @property
        def coaxial_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2267

            return self._parent._cast(_2267.CoaxialConnection)

        @property
        def connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2270

            return self._parent._cast(_2270.Connection)

        @property
        def cvt_belt_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2271

            return self._parent._cast(_2271.CVTBeltConnection)

        @property
        def inter_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.InterMountableComponentConnection)

        @property
        def planetary_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2285

            return self._parent._cast(_2285.PlanetaryConnection)

        @property
        def rolling_ring_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.RollingRingConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets import _2293

            return self._parent._cast(_2293.ShaftToMountableComponentConnection)

        @property
        def agma_gleason_conical_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2297

            return self._parent._cast(_2297.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2299

            return self._parent._cast(_2299.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2301

            return self._parent._cast(_2301.BevelGearMesh)

        @property
        def concept_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2303

            return self._parent._cast(_2303.ConceptGearMesh)

        @property
        def conical_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2305

            return self._parent._cast(_2305.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2307

            return self._parent._cast(_2307.CylindricalGearMesh)

        @property
        def face_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2309

            return self._parent._cast(_2309.FaceGearMesh)

        @property
        def gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2311

            return self._parent._cast(_2311.GearMesh)

        @property
        def hypoid_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2313

            return self._parent._cast(_2313.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2316

            return self._parent._cast(_2316.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.ZerolBevelGearMesh)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2333

            return self._parent._cast(_2333.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2336

            return self._parent._cast(_2336.CycloidalDiscPlanetaryBearingConnection)

        @property
        def ring_pins_to_disc_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2339

            return self._parent._cast(_2339.RingPinsToDiscConnection)

        @property
        def clutch_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.couplings import _2340

            return self._parent._cast(_2340.ClutchConnection)

        @property
        def concept_coupling_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.couplings import _2342

            return self._parent._cast(_2342.ConceptCouplingConnection)

        @property
        def coupling_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.couplings import _2344

            return self._parent._cast(_2344.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2346

            return self._parent._cast(_2346.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.couplings import _2348

            return self._parent._cast(_2348.SpringDamperConnection)

        @property
        def torque_converter_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.couplings import _2350

            return self._parent._cast(_2350.TorqueConverterConnection)

        @property
        def assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2431

            return self._parent._cast(_2431.Assembly)

        @property
        def abstract_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2432

            return self._parent._cast(_2432.AbstractAssembly)

        @property
        def abstract_shaft(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2433

            return self._parent._cast(_2433.AbstractShaft)

        @property
        def abstract_shaft_or_housing(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2434

            return self._parent._cast(_2434.AbstractShaftOrHousing)

        @property
        def bearing(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2437

            return self._parent._cast(_2437.Bearing)

        @property
        def bolt(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2440

            return self._parent._cast(_2440.Bolt)

        @property
        def bolted_joint(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.BoltedJoint)

        @property
        def component(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2442

            return self._parent._cast(_2442.Component)

        @property
        def connector(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2445

            return self._parent._cast(_2445.Connector)

        @property
        def datum(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Datum)

        @property
        def external_cad_model(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2450

            return self._parent._cast(_2450.ExternalCADModel)

        @property
        def fe_part(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.FEPart)

        @property
        def flexible_pin_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.FlexiblePinAssembly)

        @property
        def guide_dxf_model(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2453

            return self._parent._cast(_2453.GuideDxfModel)

        @property
        def mass_disc(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2460

            return self._parent._cast(_2460.MassDisc)

        @property
        def measurement_component(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2461

            return self._parent._cast(_2461.MeasurementComponent)

        @property
        def mountable_component(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.MountableComponent)

        @property
        def oil_seal(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.OilSeal)

        @property
        def part(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Part)

        @property
        def planet_carrier(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2467

            return self._parent._cast(_2467.PlanetCarrier)

        @property
        def point_load(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.PointLoad)

        @property
        def power_load(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.PowerLoad)

        @property
        def root_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2472

            return self._parent._cast(_2472.RootAssembly)

        @property
        def specialised_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.SpecialisedAssembly)

        @property
        def unbalanced_mass(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.UnbalancedMass)

        @property
        def virtual_component(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2477

            return self._parent._cast(_2477.VirtualComponent)

        @property
        def shaft(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.shaft_model import _2480

            return self._parent._cast(_2480.Shaft)

        @property
        def agma_gleason_conical_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2511

            return self._parent._cast(_2511.AGMAGleasonConicalGear)

        @property
        def agma_gleason_conical_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2512

            return self._parent._cast(_2512.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2513

            return self._parent._cast(_2513.BevelDifferentialGear)

        @property
        def bevel_differential_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2514

            return self._parent._cast(_2514.BevelDifferentialGearSet)

        @property
        def bevel_differential_planet_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2516

            return self._parent._cast(_2516.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelGear)

        @property
        def bevel_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.BevelGearSet)

        @property
        def concept_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.ConceptGear)

        @property
        def concept_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.ConceptGearSet)

        @property
        def conical_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.ConicalGear)

        @property
        def conical_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.ConicalGearSet)

        @property
        def cylindrical_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.CylindricalGear)

        @property
        def cylindrical_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.CylindricalGearSet)

        @property
        def cylindrical_planet_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.CylindricalPlanetGear)

        @property
        def face_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.FaceGear)

        @property
        def face_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.FaceGearSet)

        @property
        def gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2528

            return self._parent._cast(_2528.Gear)

        @property
        def gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.GearSet)

        @property
        def hypoid_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.HypoidGear)

        @property
        def hypoid_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.PlanetaryGearSet)

        @property
        def spiral_bevel_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.SpiralBevelGear)

        @property
        def spiral_bevel_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.StraightBevelDiffGear)

        @property
        def straight_bevel_diff_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.StraightBevelGear)

        @property
        def straight_bevel_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.StraightBevelGearSet)

        @property
        def straight_bevel_planet_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.StraightBevelSunGear)

        @property
        def worm_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.WormGear)

        @property
        def worm_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.WormGearSet)

        @property
        def zerol_bevel_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.ZerolBevelGear)

        @property
        def zerol_bevel_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.cycloidal import _2566

            return self._parent._cast(_2566.CycloidalAssembly)

        @property
        def cycloidal_disc(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.cycloidal import _2567

            return self._parent._cast(_2567.CycloidalDisc)

        @property
        def ring_pins(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.cycloidal import _2568

            return self._parent._cast(_2568.RingPins)

        @property
        def belt_drive(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2574

            return self._parent._cast(_2574.BeltDrive)

        @property
        def clutch(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2576

            return self._parent._cast(_2576.Clutch)

        @property
        def clutch_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2577

            return self._parent._cast(_2577.ClutchHalf)

        @property
        def concept_coupling(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2579

            return self._parent._cast(_2579.ConceptCoupling)

        @property
        def concept_coupling_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2580

            return self._parent._cast(_2580.ConceptCouplingHalf)

        @property
        def coupling(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2581

            return self._parent._cast(_2581.Coupling)

        @property
        def coupling_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2582

            return self._parent._cast(_2582.CouplingHalf)

        @property
        def cvt(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2584

            return self._parent._cast(_2584.CVT)

        @property
        def cvt_pulley(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2585

            return self._parent._cast(_2585.CVTPulley)

        @property
        def part_to_part_shear_coupling(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.PartToPartShearCoupling)

        @property
        def part_to_part_shear_coupling_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2587

            return self._parent._cast(_2587.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2588

            return self._parent._cast(_2588.Pulley)

        @property
        def rolling_ring(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2594

            return self._parent._cast(_2594.RollingRing)

        @property
        def rolling_ring_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2595

            return self._parent._cast(_2595.RollingRingAssembly)

        @property
        def shaft_hub_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.ShaftHubConnection)

        @property
        def spring_damper(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.SpringDamper)

        @property
        def spring_damper_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2599

            return self._parent._cast(_2599.SpringDamperHalf)

        @property
        def synchroniser(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2600

            return self._parent._cast(_2600.Synchroniser)

        @property
        def synchroniser_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.SynchroniserHalf)

        @property
        def synchroniser_part(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2603

            return self._parent._cast(_2603.SynchroniserPart)

        @property
        def synchroniser_sleeve(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.SynchroniserSleeve)

        @property
        def torque_converter(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.TorqueConverter)

        @property
        def torque_converter_pump(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.TorqueConverterPump)

        @property
        def torque_converter_turbine(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.TorqueConverterTurbine)

        @property
        def design_entity(self: "DesignEntity._Cast_DesignEntity") -> "DesignEntity":
            return self._parent

        def __getattr__(self: "DesignEntity._Cast_DesignEntity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return ""

        return temp

    @property
    def icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Icon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def small_icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallIcon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def unique_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UniqueName

        if temp is None:
            return ""

        return temp

    @property
    def design_properties(self: Self) -> "_2198.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_design_entities(self: Self) -> "List[DesignEntity]":
        """List[mastapy.system_model.DesignEntity]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllDesignEntities

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_status_errors(self: Self) -> "List[_1792.StatusItem]":
        """List[mastapy.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def status(self: Self) -> "_1791.Status":
        """mastapy.utility.model_validation.Status

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def user_specified_data(self: Self) -> "_1739.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "DesignEntity._Cast_DesignEntity":
        return self._Cast_DesignEntity(self)
