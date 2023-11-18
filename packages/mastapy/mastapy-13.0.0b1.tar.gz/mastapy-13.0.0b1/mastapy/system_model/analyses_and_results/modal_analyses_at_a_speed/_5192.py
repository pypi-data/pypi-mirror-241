"""MountableComponentModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5139
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "MountableComponentModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="MountableComponentModalAnalysisAtASpeed")


class MountableComponentModalAnalysisAtASpeed(_5139.ComponentModalAnalysisAtASpeed):
    """MountableComponentModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentModalAnalysisAtASpeed"
    )

    class _Cast_MountableComponentModalAnalysisAtASpeed:
        """Special nested class for casting MountableComponentModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
            parent: "MountableComponentModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def component_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5139.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5119,
            )

            return self._parent._cast(_5119.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def bearing_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5122,
            )

            return self._parent._cast(_5122.BearingModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5126,
            )

            return self._parent._cast(_5126.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5128,
            )

            return self._parent._cast(
                _5128.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5129,
            )

            return self._parent._cast(
                _5129.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5131,
            )

            return self._parent._cast(_5131.BevelGearModalAnalysisAtASpeed)

        @property
        def clutch_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5136,
            )

            return self._parent._cast(_5136.ClutchHalfModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(_5141.ConceptCouplingHalfModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(_5144.ConceptGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5147,
            )

            return self._parent._cast(_5147.ConicalGearModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ConnectorModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.CouplingHalfModalAnalysisAtASpeed)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5156,
            )

            return self._parent._cast(_5156.CVTPulleyModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5162,
            )

            return self._parent._cast(_5162.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5164,
            )

            return self._parent._cast(_5164.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5168,
            )

            return self._parent._cast(_5168.FaceGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.GearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.HypoidGearModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5181,
            )

            return self._parent._cast(
                _5181.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5184,
            )

            return self._parent._cast(
                _5184.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5187,
            )

            return self._parent._cast(
                _5187.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
            )

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5189,
            )

            return self._parent._cast(_5189.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(_5190.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.OilSealModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(
                _5196.PartToPartShearCouplingHalfModalAnalysisAtASpeed
            )

        @property
        def planet_carrier_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5200,
            )

            return self._parent._cast(_5200.PlanetCarrierModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5201,
            )

            return self._parent._cast(_5201.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.PowerLoadModalAnalysisAtASpeed)

        @property
        def pulley_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.PulleyModalAnalysisAtASpeed)

        @property
        def ring_pins_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5204,
            )

            return self._parent._cast(_5204.RingPinsModalAnalysisAtASpeed)

        @property
        def rolling_ring_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5208,
            )

            return self._parent._cast(_5208.RollingRingModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5210,
            )

            return self._parent._cast(_5210.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5215,
            )

            return self._parent._cast(_5215.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def spring_damper_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.SpringDamperHalfModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5221,
            )

            return self._parent._cast(_5221.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5224,
            )

            return self._parent._cast(_5224.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5226,
            )

            return self._parent._cast(
                _5226.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5227,
            )

            return self._parent._cast(_5227.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5228,
            )

            return self._parent._cast(_5228.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5230,
            )

            return self._parent._cast(_5230.SynchroniserPartModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5231,
            )

            return self._parent._cast(_5231.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5234,
            )

            return self._parent._cast(_5234.TorqueConverterPumpModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5235,
            )

            return self._parent._cast(_5235.TorqueConverterTurbineModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5236,
            )

            return self._parent._cast(_5236.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5237,
            )

            return self._parent._cast(_5237.VirtualComponentModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5239,
            )

            return self._parent._cast(_5239.WormGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5242,
            )

            return self._parent._cast(_5242.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
        ) -> "MountableComponentModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "MountableComponentModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(
        self: Self,
    ) -> "MountableComponentModalAnalysisAtASpeed._Cast_MountableComponentModalAnalysisAtASpeed":
        return self._Cast_MountableComponentModalAnalysisAtASpeed(self)
