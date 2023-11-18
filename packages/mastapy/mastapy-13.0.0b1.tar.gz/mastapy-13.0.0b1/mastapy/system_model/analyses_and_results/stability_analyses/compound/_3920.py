"""ComponentCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3974
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ComponentCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3786


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundStabilityAnalysis")


class ComponentCompoundStabilityAnalysis(_3974.PartCompoundStabilityAnalysis):
    """ComponentCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundStabilityAnalysis")

    class _Cast_ComponentCompoundStabilityAnalysis:
        """Special nested class for casting ComponentCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
            parent: "ComponentCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3896,
            )

            return self._parent._cast(_3896.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3897,
            )

            return self._parent._cast(
                _3897.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3899,
            )

            return self._parent._cast(
                _3899.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def bearing_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3903,
            )

            return self._parent._cast(_3903.BearingCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3906,
            )

            return self._parent._cast(
                _3906.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(
                _3910.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3911,
            )

            return self._parent._cast(_3911.BevelGearCompoundStabilityAnalysis)

        @property
        def bolt_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3914,
            )

            return self._parent._cast(_3914.BoltCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(_3918.ClutchHalfCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(
                _3923.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def concept_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(_3924.ConceptGearCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.ConicalGearCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(_3931.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3934,
            )

            return self._parent._cast(_3934.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3942,
            )

            return self._parent._cast(_3942.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(
                _3945.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def datum_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3946,
            )

            return self._parent._cast(_3946.DatumCompoundStabilityAnalysis)

        @property
        def external_cad_model_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3947,
            )

            return self._parent._cast(_3947.ExternalCADModelCompoundStabilityAnalysis)

        @property
        def face_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(_3948.FaceGearCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.FEPartCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.GearCompoundStabilityAnalysis)

        @property
        def guide_dxf_model_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.GuideDxfModelCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.HypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3961,
            )

            return self._parent._cast(
                _3961.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(
                _3964.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(
                _3967.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def mass_disc_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(_3970.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(
                _3971.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def mountable_component_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.OilSealCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3977,
            )

            return self._parent._cast(
                _3977.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def planet_carrier_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(_3981.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(_3983.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.RingPinsCompoundStabilityAnalysis)

        @property
        def rolling_ring_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3987,
            )

            return self._parent._cast(_3987.RollingRingCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(_3990.ShaftCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3991,
            )

            return self._parent._cast(_3991.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(_3994.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(
                _4000.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(_4003.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(
                _4007.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4009,
            )

            return self._parent._cast(_4009.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4010,
            )

            return self._parent._cast(_4010.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(_4011.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4014,
            )

            return self._parent._cast(
                _4014.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(
                _4015.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(_4016.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(_4017.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(_4018.WormGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
        ) -> "ComponentCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ComponentCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3786.ComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ComponentStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3786.ComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ComponentStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentCompoundStabilityAnalysis._Cast_ComponentCompoundStabilityAnalysis":
        return self._Cast_ComponentCompoundStabilityAnalysis(self)
