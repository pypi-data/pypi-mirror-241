"""ComponentMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5464
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ComponentMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442


__docformat__ = "restructuredtext en"
__all__ = ("ComponentMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ComponentMultibodyDynamicsAnalysis")


class ComponentMultibodyDynamicsAnalysis(_5464.PartMultibodyDynamicsAnalysis):
    """ComponentMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentMultibodyDynamicsAnalysis")

    class _Cast_ComponentMultibodyDynamicsAnalysis:
        """Special nested class for casting ComponentMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
            parent: "ComponentMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5374

            return self._parent._cast(_5374.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5375

            return self._parent._cast(
                _5375.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378

            return self._parent._cast(
                _5378.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def bearing_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382

            return self._parent._cast(_5382.BearingMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(
                _5387.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(
                _5389.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(
                _5390.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392

            return self._parent._cast(_5392.BevelGearMultibodyDynamicsAnalysis)

        @property
        def bolt_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5395

            return self._parent._cast(_5395.BoltMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(
                _5403.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(_5424.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5426

            return self._parent._cast(
                _5426.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def datum_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427

            return self._parent._cast(_5427.DatumMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ExternalCADModelMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430

            return self._parent._cast(_5430.FaceGearMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432

            return self._parent._cast(_5432.FEPartMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.GuideDxfModelMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440

            return self._parent._cast(_5440.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(
                _5448.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5454

            return self._parent._cast(
                _5454.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5456

            return self._parent._cast(_5456.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(
                _5460.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(
                _5466.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(_5470.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(_5471.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(_5473.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5474

            return self._parent._cast(_5474.RingPinsMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(_5478.RollingRingMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(_5482.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483

            return self._parent._cast(_5483.ShaftMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(
                _5494.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(_5497.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(
                _5499.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(
                _5500.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(_5501.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(_5503.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5504

            return self._parent._cast(_5504.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(
                _5508.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(_5511.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5512

            return self._parent._cast(_5512.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(_5515.WormGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5518

            return self._parent._cast(_5518.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
        ) -> "ComponentMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ComponentMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_acceleration_theta_z(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularAccelerationThetaZ

        if temp is None:
            return 0.0

        return temp

    @property
    def angular_displacement_theta_z(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularDisplacementThetaZ

        if temp is None:
            return 0.0

        return temp

    @property
    def angular_velocity_theta_z(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularVelocityThetaZ

        if temp is None:
            return 0.0

        return temp

    @property
    def planetary_angular_displacement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetaryAngularDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def planetary_radial_displacement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetaryRadialDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def planetary_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetaryVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def total_degrees_of_freedom(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def component_design(self: Self) -> "_2442.Component":
        """mastapy.system_model.part_model.Component

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
    ) -> "ComponentMultibodyDynamicsAnalysis._Cast_ComponentMultibodyDynamicsAnalysis":
        return self._Cast_ComponentMultibodyDynamicsAnalysis(self)
