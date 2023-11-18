"""ComponentLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6926
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ComponentLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442


__docformat__ = "restructuredtext en"
__all__ = ("ComponentLoadCase",)


Self = TypeVar("Self", bound="ComponentLoadCase")


class ComponentLoadCase(_6926.PartLoadCase):
    """ComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _COMPONENT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentLoadCase")

    class _Cast_ComponentLoadCase:
        """Special nested class for casting ComponentLoadCase to subclasses."""

        def __init__(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
            parent: "ComponentLoadCase",
        ):
            self._parent = parent

        @property
        def part_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_analysis(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6805

            return self._parent._cast(_6805.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(_6806.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6811

            return self._parent._cast(_6811.AGMAGleasonConicalGearLoadCase)

        @property
        def bearing_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.BearingLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6820

            return self._parent._cast(_6820.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelGearLoadCase)

        @property
        def bolt_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.BoltLoadCase)

        @property
        def clutch_half_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ConceptCouplingHalfLoadCase)

        @property
        def concept_gear_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6839

            return self._parent._cast(_6839.ConceptGearLoadCase)

        @property
        def conical_gear_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.ConicalGearLoadCase)

        @property
        def connector_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.ConnectorLoadCase)

        @property
        def coupling_half_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.CouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.CVTPulleyLoadCase)

        @property
        def cycloidal_disc_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.CylindricalGearLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6867

            return self._parent._cast(_6867.DatumLoadCase)

        @property
        def external_cad_model_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6881

            return self._parent._cast(_6881.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6882

            return self._parent._cast(_6882.FaceGearLoadCase)

        @property
        def fe_part_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.FEPartLoadCase)

        @property
        def gear_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.GearLoadCase)

        @property
        def guide_dxf_model_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6894

            return self._parent._cast(_6894.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6903

            return self._parent._cast(_6903.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6910

            return self._parent._cast(_6910.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6913

            return self._parent._cast(_6913.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(
                _6916.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def mass_disc_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6919

            return self._parent._cast(_6919.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(_6920.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartToPartShearCouplingHalfLoadCase)

        @property
        def planet_carrier_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6936

            return self._parent._cast(_6936.PointLoadLoadCase)

        @property
        def power_load_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PowerLoadLoadCase)

        @property
        def pulley_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(_6938.PulleyLoadCase)

        @property
        def ring_pins_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(_6941.RingPinsLoadCase)

        @property
        def rolling_ring_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6945

            return self._parent._cast(_6945.RollingRingLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(_6947.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.ShaftLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.SpiralBevelGearLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.SpringDamperHalfLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6972

            return self._parent._cast(_6972.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6978

            return self._parent._cast(_6978.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(self: "ComponentLoadCase._Cast_ComponentLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.WormGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.ZerolBevelGearLoadCase)

        @property
        def component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "ComponentLoadCase":
            return self._parent

        def __getattr__(self: "ComponentLoadCase._Cast_ComponentLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AdditionalModalDampingRatio = value

    @property
    def is_connected_to_ground(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsConnectedToGround

        if temp is None:
            return False

        return temp

    @property
    def is_torsionally_free(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsTorsionallyFree

        if temp is None:
            return False

        return temp

    @property
    def magnitude_of_rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MagnitudeOfRotation

        if temp is None:
            return 0.0

        return temp

    @magnitude_of_rotation.setter
    @enforce_parameter_types
    def magnitude_of_rotation(self: Self, value: "float"):
        self.wrapped.MagnitudeOfRotation = float(value) if value is not None else 0.0

    @property
    def rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rayleigh_damping_beta.setter
    @enforce_parameter_types
    def rayleigh_damping_beta(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RayleighDampingBeta = value

    @property
    def rotation_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAngle

        if temp is None:
            return 0.0

        return temp

    @rotation_angle.setter
    @enforce_parameter_types
    def rotation_angle(self: Self, value: "float"):
        self.wrapped.RotationAngle = float(value) if value is not None else 0.0

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
    def cast_to(self: Self) -> "ComponentLoadCase._Cast_ComponentLoadCase":
        return self._Cast_ComponentLoadCase(self)
