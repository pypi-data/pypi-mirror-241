"""ComponentStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ComponentStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442


__docformat__ = "restructuredtext en"
__all__ = ("ComponentStabilityAnalysis",)


Self = TypeVar("Self", bound="ComponentStabilityAnalysis")


class ComponentStabilityAnalysis(_3842.PartStabilityAnalysis):
    """ComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentStabilityAnalysis")

    class _Cast_ComponentStabilityAnalysis:
        """Special nested class for casting ComponentStabilityAnalysis to subclasses."""

        def __init__(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
            parent: "ComponentStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3762,
            )

            return self._parent._cast(_3762.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3763,
            )

            return self._parent._cast(_3763.AbstractShaftStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3767,
            )

            return self._parent._cast(_3767.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3769,
            )

            return self._parent._cast(_3769.BearingStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3774,
            )

            return self._parent._cast(_3774.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3775,
            )

            return self._parent._cast(
                _3775.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3776,
            )

            return self._parent._cast(_3776.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3779,
            )

            return self._parent._cast(_3779.BevelGearStabilityAnalysis)

        @property
        def bolt_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3781,
            )

            return self._parent._cast(_3781.BoltStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.ClutchHalfStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.ConicalGearStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.ConnectorStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.CouplingHalfStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.CVTPulleyStabilityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3808,
            )

            return self._parent._cast(_3808.CycloidalDiscStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3812,
            )

            return self._parent._cast(_3812.CylindricalPlanetGearStabilityAnalysis)

        @property
        def datum_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3813,
            )

            return self._parent._cast(_3813.DatumStabilityAnalysis)

        @property
        def external_cad_model_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3815,
            )

            return self._parent._cast(_3815.ExternalCADModelStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.FaceGearStabilityAnalysis)

        @property
        def fe_part_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.FEPartStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GearStabilityAnalysis)

        @property
        def guide_dxf_model_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3824,
            )

            return self._parent._cast(_3824.GuideDxfModelStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(_3827.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3831,
            )

            return self._parent._cast(
                _3831.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3834,
            )

            return self._parent._cast(
                _3834.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(
                _3837.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def mass_disc_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(_3838.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MeasurementComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.OilSealStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(
                _3844.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def planet_carrier_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3849,
            )

            return self._parent._cast(_3849.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.RingPinsStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(_3856.RollingRingStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(_3858.ShaftHubConnectionStabilityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(_3859.ShaftStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3864,
            )

            return self._parent._cast(_3864.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpringDamperHalfStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3873,
            )

            return self._parent._cast(_3873.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.SynchroniserSleeveStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3888,
            )

            return self._parent._cast(_3888.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3891,
            )

            return self._parent._cast(_3891.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3894,
            )

            return self._parent._cast(_3894.ZerolBevelGearStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "ComponentStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentStabilityAnalysis.TYPE"):
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
    ) -> "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis":
        return self._Cast_ComponentStabilityAnalysis(self)
