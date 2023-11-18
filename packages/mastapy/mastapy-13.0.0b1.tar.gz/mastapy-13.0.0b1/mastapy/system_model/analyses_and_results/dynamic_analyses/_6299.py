"""ComponentDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ComponentDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442


__docformat__ = "restructuredtext en"
__all__ = ("ComponentDynamicAnalysis",)


Self = TypeVar("Self", bound="ComponentDynamicAnalysis")


class ComponentDynamicAnalysis(_6355.PartDynamicAnalysis):
    """ComponentDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentDynamicAnalysis")

    class _Cast_ComponentDynamicAnalysis:
        """Special nested class for casting ComponentDynamicAnalysis to subclasses."""

        def __init__(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
            parent: "ComponentDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6275

            return self._parent._cast(_6275.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276

            return self._parent._cast(_6276.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278

            return self._parent._cast(_6278.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(_6282.BearingDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(_6288.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.BevelGearDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BoltDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297

            return self._parent._cast(_6297.ClutchHalfDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.ConceptGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306

            return self._parent._cast(_6306.ConicalGearDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ConnectorDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.CouplingHalfDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329

            return self._parent._cast(_6329.FaceGearDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.FEPartDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.GearDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.HypoidGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(
                _6342.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(
                _6345.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(
                _6348.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(_6351.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.OilSealDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(_6361.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.RollingRingDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372

            return self._parent._cast(_6372.ShaftHubConnectionDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(_6375.SpiralBevelGearDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.WormGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402

            return self._parent._cast(_6402.ZerolBevelGearDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "ComponentDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    ) -> "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis":
        return self._Cast_ComponentDynamicAnalysis(self)
