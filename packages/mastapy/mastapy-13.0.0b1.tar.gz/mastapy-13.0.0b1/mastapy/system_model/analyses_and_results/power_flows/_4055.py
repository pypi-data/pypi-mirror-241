"""ComponentPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4111
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ComponentPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442


__docformat__ = "restructuredtext en"
__all__ = ("ComponentPowerFlow",)


Self = TypeVar("Self", bound="ComponentPowerFlow")


class ComponentPowerFlow(_4111.PartPowerFlow):
    """ComponentPowerFlow

    This is a mastapy class.
    """

    TYPE = _COMPONENT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentPowerFlow")

    class _Cast_ComponentPowerFlow:
        """Special nested class for casting ComponentPowerFlow to subclasses."""

        def __init__(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
            parent: "ComponentPowerFlow",
        ):
            self._parent = parent

        @property
        def part_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4031

            return self._parent._cast(_4031.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4035

            return self._parent._cast(_4035.AGMAGleasonConicalGearPowerFlow)

        @property
        def bearing_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4038

            return self._parent._cast(_4038.BearingPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4042

            return self._parent._cast(_4042.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelGearPowerFlow)

        @property
        def bolt_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4050

            return self._parent._cast(_4050.BoltPowerFlow)

        @property
        def clutch_half_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.ClutchHalfPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ConceptCouplingHalfPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.ConceptGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ConicalGearPowerFlow)

        @property
        def connector_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.CouplingHalfPowerFlow)

        @property
        def cvt_pulley_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.CVTPulleyPowerFlow)

        @property
        def cycloidal_disc_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(_4076.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4079

            return self._parent._cast(_4079.CylindricalGearPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.FaceGearPowerFlow)

        @property
        def fe_part_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.FEPartPowerFlow)

        @property
        def gear_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.GearPowerFlow)

        @property
        def guide_dxf_model_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(
                _4099.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(
                _4105.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def mass_disc_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(_4107.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartToPartShearCouplingHalfPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.PointLoadPowerFlow)

        @property
        def power_load_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(_4123.RingPinsPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.RollingRingPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(_4129.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(_4130.ShaftPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.SpiralBevelGearPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpringDamperHalfPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.SynchroniserPartPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4150

            return self._parent._cast(_4150.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.WormGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.ZerolBevelGearPowerFlow)

        @property
        def component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "ComponentPowerFlow":
            return self._parent

        def __getattr__(self: "ComponentPowerFlow._Cast_ComponentPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

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
    def cast_to(self: Self) -> "ComponentPowerFlow._Cast_ComponentPowerFlow":
        return self._Cast_ComponentPowerFlow(self)
