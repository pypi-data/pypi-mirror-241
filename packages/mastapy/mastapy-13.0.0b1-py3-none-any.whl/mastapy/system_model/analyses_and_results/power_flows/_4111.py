"""PartPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PartPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.power_flows import _4119
    from mastapy.system_model.drawing import _2252


__docformat__ = "restructuredtext en"
__all__ = ("PartPowerFlow",)


Self = TypeVar("Self", bound="PartPowerFlow")


class PartPowerFlow(_7545.PartStaticLoadAnalysisCase):
    """PartPowerFlow

    This is a mastapy class.
    """

    TYPE = _PART_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartPowerFlow")

    class _Cast_PartPowerFlow:
        """Special nested class for casting PartPowerFlow to subclasses."""

        def __init__(
            self: "PartPowerFlow._Cast_PartPowerFlow", parent: "PartPowerFlow"
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(self: "PartPowerFlow._Cast_PartPowerFlow"):
            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_assembly_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4031

            return self._parent._cast(_4031.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4035

            return self._parent._cast(_4035.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4036

            return self._parent._cast(_4036.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4037

            return self._parent._cast(_4037.AssemblyPowerFlow)

        @property
        def bearing_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4038

            return self._parent._cast(_4038.BearingPowerFlow)

        @property
        def belt_drive_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4042

            return self._parent._cast(_4042.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4043

            return self._parent._cast(_4043.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4048

            return self._parent._cast(_4048.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4049

            return self._parent._cast(_4049.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4050

            return self._parent._cast(_4050.BoltPowerFlow)

        @property
        def clutch_half_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.ClutchPowerFlow)

        @property
        def component_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.ComponentPowerFlow)

        @property
        def concept_coupling_half_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.ConceptCouplingPowerFlow)

        @property
        def concept_gear_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.ConceptGearSetPowerFlow)

        @property
        def conical_gear_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConicalGearSetPowerFlow)

        @property
        def connector_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.CouplingPowerFlow)

        @property
        def cvt_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(_4076.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4079

            return self._parent._cast(_4079.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.GearPowerFlow)

        @property
        def gear_set_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(
                _4099.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4100

            return self._parent._cast(
                _4100.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(
                _4103.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(
                _4105.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(
                _4106.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def mass_disc_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(_4107.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.PointLoadPowerFlow)

        @property
        def power_load_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(_4123.RingPinsPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(_4125.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(_4129.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(_4130.ShaftPowerFlow)

        @property
        def specialised_assembly_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_half_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4150

            return self._parent._cast(_4150.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(self: "PartPowerFlow._Cast_PartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4163

            return self._parent._cast(_4163.ZerolBevelGearSetPowerFlow)

        @property
        def part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "PartPowerFlow":
            return self._parent

        def __getattr__(self: "PartPowerFlow._Cast_PartPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_power_flow(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2466.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow(self: Self) -> "_4119.PowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2252.PowerFlowViewable":
        """mastapy.system_model.drawing.PowerFlowViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartPowerFlow._Cast_PartPowerFlow":
        return self._Cast_PartPowerFlow(self)
