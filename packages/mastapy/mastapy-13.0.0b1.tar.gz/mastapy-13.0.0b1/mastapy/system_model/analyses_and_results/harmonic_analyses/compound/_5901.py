"""ComponentCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5955
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ComponentCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5702


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundHarmonicAnalysis")


class ComponentCompoundHarmonicAnalysis(_5955.PartCompoundHarmonicAnalysis):
    """ComponentCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundHarmonicAnalysis")

    class _Cast_ComponentCompoundHarmonicAnalysis:
        """Special nested class for casting ComponentCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
            parent: "ComponentCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5955.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5877,
            )

            return self._parent._cast(_5877.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5878,
            )

            return self._parent._cast(
                _5878.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5880,
            )

            return self._parent._cast(
                _5880.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def bearing_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5884,
            )

            return self._parent._cast(_5884.BearingCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(
                _5887.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5890,
            )

            return self._parent._cast(
                _5890.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5891,
            )

            return self._parent._cast(
                _5891.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5892,
            )

            return self._parent._cast(_5892.BevelGearCompoundHarmonicAnalysis)

        @property
        def bolt_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5895,
            )

            return self._parent._cast(_5895.BoltCompoundHarmonicAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5899,
            )

            return self._parent._cast(_5899.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(_5905.ConceptGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5908,
            )

            return self._parent._cast(_5908.ConicalGearCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ConnectorCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5915,
            )

            return self._parent._cast(_5915.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5918,
            )

            return self._parent._cast(_5918.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5921,
            )

            return self._parent._cast(_5921.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5923,
            )

            return self._parent._cast(_5923.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5926,
            )

            return self._parent._cast(
                _5926.CylindricalPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def datum_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5927,
            )

            return self._parent._cast(_5927.DatumCompoundHarmonicAnalysis)

        @property
        def external_cad_model_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5928,
            )

            return self._parent._cast(_5928.ExternalCADModelCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5929,
            )

            return self._parent._cast(_5929.FaceGearCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5932,
            )

            return self._parent._cast(_5932.FEPartCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5934,
            )

            return self._parent._cast(_5934.GearCompoundHarmonicAnalysis)

        @property
        def guide_dxf_model_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5937,
            )

            return self._parent._cast(_5937.GuideDxfModelCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.HypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5942,
            )

            return self._parent._cast(
                _5942.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5945,
            )

            return self._parent._cast(
                _5945.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5948,
            )

            return self._parent._cast(
                _5948.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def mass_disc_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5951,
            )

            return self._parent._cast(_5951.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(
                _5952.MeasurementComponentCompoundHarmonicAnalysis
            )

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5953,
            )

            return self._parent._cast(_5953.MountableComponentCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(_5954.OilSealCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(
                _5958.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
            )

        @property
        def planet_carrier_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5961,
            )

            return self._parent._cast(_5961.PlanetCarrierCompoundHarmonicAnalysis)

        @property
        def point_load_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5962,
            )

            return self._parent._cast(_5962.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5963,
            )

            return self._parent._cast(_5963.PowerLoadCompoundHarmonicAnalysis)

        @property
        def pulley_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.PulleyCompoundHarmonicAnalysis)

        @property
        def ring_pins_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(_5965.RingPinsCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5968,
            )

            return self._parent._cast(_5968.RollingRingCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5971,
            )

            return self._parent._cast(_5971.ShaftCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5972,
            )

            return self._parent._cast(_5972.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5975,
            )

            return self._parent._cast(_5975.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5980,
            )

            return self._parent._cast(_5980.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5981,
            )

            return self._parent._cast(
                _5981.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5987,
            )

            return self._parent._cast(
                _5987.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(
                _5988.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5990,
            )

            return self._parent._cast(_5990.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(_5991.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5992,
            )

            return self._parent._cast(_5992.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5995,
            )

            return self._parent._cast(_5995.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5996,
            )

            return self._parent._cast(
                _5996.TorqueConverterTurbineCompoundHarmonicAnalysis
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5997,
            )

            return self._parent._cast(_5997.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5998,
            )

            return self._parent._cast(_5998.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5999,
            )

            return self._parent._cast(_5999.WormGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(_6002.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
        ) -> "ComponentCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ComponentCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_5702.ComponentHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ComponentHarmonicAnalysis]

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
    ) -> "List[_5702.ComponentHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ComponentHarmonicAnalysis]

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
    ) -> "ComponentCompoundHarmonicAnalysis._Cast_ComponentCompoundHarmonicAnalysis":
        return self._Cast_ComponentCompoundHarmonicAnalysis(self)
