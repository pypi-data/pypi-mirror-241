"""MountableComponentSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2713
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "MountableComponentSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.system_deflections import _2755
    from mastapy.system_model.fe import _2383
    from mastapy.system_model.analyses_and_results.power_flows import _4109


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentSystemDeflection",)


Self = TypeVar("Self", bound="MountableComponentSystemDeflection")


class MountableComponentSystemDeflection(_2713.ComponentSystemDeflection):
    """MountableComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentSystemDeflection")

    class _Cast_MountableComponentSystemDeflection:
        """Special nested class for casting MountableComponentSystemDeflection to subclasses."""

        def __init__(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
            parent: "MountableComponentSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AGMAGleasonConicalGearSystemDeflection)

        @property
        def bearing_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2696,
            )

            return self._parent._cast(_2696.BearingSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2703,
            )

            return self._parent._cast(_2703.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelGearSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.ClutchHalfSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ConceptGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.CouplingHalfSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.CVTPulleySystemDeflection)

        @property
        def cylindrical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(
                _2745.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.CylindricalPlanetGearSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.FaceGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(
                _2768.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(
                _2771.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(
                _2774.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(_2777.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(_2778.MeasurementComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.OilSealSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(_2789.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(_2791.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.RingPinsSystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(_2797.RollingRingSystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.ShaftHubConnectionSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.SpringDamperHalfSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.SynchroniserSleeveSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.VirtualComponentSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.ZerolBevelGearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "MountableComponentSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
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
        self: Self, instance_to_wrap: "MountableComponentSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dip_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DipFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2462.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_fe_part(self: Self) -> "_2755.FEPartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerFEPart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_fe_substructure_nodes(self: Self) -> "List[_2383.FESubstructureNode]":
        """List[mastapy.system_model.fe.FESubstructureNode]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerFESubstructureNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4109.MountableComponentPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow

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
    ) -> "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection":
        return self._Cast_MountableComponentSystemDeflection(self)
