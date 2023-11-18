"""MountableComponentModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "MountableComponentModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.system_deflections import _2780


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentModalAnalysis",)


Self = TypeVar("Self", bound="MountableComponentModalAnalysis")


class MountableComponentModalAnalysis(_4594.ComponentModalAnalysis):
    """MountableComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentModalAnalysis")

    class _Cast_MountableComponentModalAnalysis:
        """Special nested class for casting MountableComponentModalAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
            parent: "MountableComponentModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            return self._parent._cast(_4594.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574

            return self._parent._cast(_4574.AGMAGleasonConicalGearModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577

            return self._parent._cast(_4577.BearingModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581

            return self._parent._cast(_4581.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4583

            return self._parent._cast(_4583.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4584

            return self._parent._cast(_4584.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.BevelGearModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4591

            return self._parent._cast(_4591.ClutchHalfModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ConceptGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConicalGearModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.CouplingHalfModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.CVTPulleyModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.CylindricalGearModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.CylindricalPlanetGearModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4627

            return self._parent._cast(_4627.FaceGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.GearModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.HypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(
                _4641.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(
                _4644.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(
                _4647.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649

            return self._parent._cast(_4649.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650

            return self._parent._cast(_4650.MeasurementComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.OilSealModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(_4665.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(_4667.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(_4668.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669

            return self._parent._cast(_4669.RingPinsModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.RollingRingModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.ShaftHubConnectionModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.SpiralBevelGearModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.SpringDamperHalfModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4703

            return self._parent._cast(_4703.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.WormGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.ZerolBevelGearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
        ) -> "MountableComponentModalAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentModalAnalysis.TYPE"):
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
    def system_deflection_results(
        self: Self,
    ) -> "_2780.MountableComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentModalAnalysis._Cast_MountableComponentModalAnalysis":
        return self._Cast_MountableComponentModalAnalysis(self)
