"""ComponentCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6484
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ComponentCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundDynamicAnalysis")


class ComponentCompoundDynamicAnalysis(_6484.PartCompoundDynamicAnalysis):
    """ComponentCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundDynamicAnalysis")

    class _Cast_ComponentCompoundDynamicAnalysis:
        """Special nested class for casting ComponentCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
            parent: "ComponentCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6484.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6406,
            )

            return self._parent._cast(_6406.AbstractShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6407,
            )

            return self._parent._cast(
                _6407.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6409,
            )

            return self._parent._cast(
                _6409.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def bearing_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6413,
            )

            return self._parent._cast(_6413.BearingCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(
                _6416.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6419,
            )

            return self._parent._cast(
                _6419.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(
                _6420.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(_6421.BevelGearCompoundDynamicAnalysis)

        @property
        def bolt_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(_6424.BoltCompoundDynamicAnalysis)

        @property
        def clutch_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6428,
            )

            return self._parent._cast(_6428.ClutchHalfCompoundDynamicAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(_6434.ConceptGearCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6437,
            )

            return self._parent._cast(_6437.ConicalGearCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ConnectorCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6444,
            )

            return self._parent._cast(_6444.CouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.CVTPulleyCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6450,
            )

            return self._parent._cast(_6450.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6452,
            )

            return self._parent._cast(_6452.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6455,
            )

            return self._parent._cast(
                _6455.CylindricalPlanetGearCompoundDynamicAnalysis
            )

        @property
        def datum_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6456,
            )

            return self._parent._cast(_6456.DatumCompoundDynamicAnalysis)

        @property
        def external_cad_model_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6457,
            )

            return self._parent._cast(_6457.ExternalCADModelCompoundDynamicAnalysis)

        @property
        def face_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6458,
            )

            return self._parent._cast(_6458.FaceGearCompoundDynamicAnalysis)

        @property
        def fe_part_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(_6461.FEPartCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6463,
            )

            return self._parent._cast(_6463.GearCompoundDynamicAnalysis)

        @property
        def guide_dxf_model_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.GuideDxfModelCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.HypoidGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6471,
            )

            return self._parent._cast(
                _6471.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(
                _6474.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6477,
            )

            return self._parent._cast(
                _6477.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6480,
            )

            return self._parent._cast(_6480.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(_6481.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.MountableComponentCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6483,
            )

            return self._parent._cast(_6483.OilSealCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(
                _6487.PartToPartShearCouplingHalfCompoundDynamicAnalysis
            )

        @property
        def planet_carrier_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(_6490.PlanetCarrierCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6491,
            )

            return self._parent._cast(_6491.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(_6492.PowerLoadCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.PulleyCompoundDynamicAnalysis)

        @property
        def ring_pins_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(_6494.RingPinsCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6497,
            )

            return self._parent._cast(_6497.RollingRingCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6500,
            )

            return self._parent._cast(_6500.ShaftCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(_6501.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(_6504.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6510,
            )

            return self._parent._cast(
                _6510.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6516,
            )

            return self._parent._cast(
                _6516.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(_6517.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6519,
            )

            return self._parent._cast(_6519.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(_6521.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(_6524.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(
                _6525.TorqueConverterTurbineCompoundDynamicAnalysis
            )

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(_6526.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.VirtualComponentCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6528,
            )

            return self._parent._cast(_6528.WormGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6531,
            )

            return self._parent._cast(_6531.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ) -> "ComponentCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_6299.ComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ComponentDynamicAnalysis]

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
    ) -> "List[_6299.ComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ComponentDynamicAnalysis]

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
    ) -> "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis":
        return self._Cast_ComponentCompoundDynamicAnalysis(self)
