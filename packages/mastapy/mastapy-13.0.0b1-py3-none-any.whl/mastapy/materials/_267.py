"""Material"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1827
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIAL = python_net_import("SMT.MastaAPI.Materials", "Material")

if TYPE_CHECKING:
    from mastapy.materials import _256, _272


__docformat__ = "restructuredtext en"
__all__ = ("Material",)


Self = TypeVar("Self", bound="Material")


class Material(_1827.NamedDatabaseItem):
    """Material

    This is a mastapy class.
    """

    TYPE = _MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Material")

    class _Cast_Material:
        """Special nested class for casting Material to subclasses."""

        def __init__(self: "Material._Cast_Material", parent: "Material"):
            self._parent = parent

        @property
        def named_database_item(self: "Material._Cast_Material"):
            return self._parent._cast(_1827.NamedDatabaseItem)

        @property
        def shaft_material(self: "Material._Cast_Material"):
            from mastapy.shafts import _24

            return self._parent._cast(_24.ShaftMaterial)

        @property
        def bearing_material(self: "Material._Cast_Material"):
            from mastapy.materials import _243

            return self._parent._cast(_243.BearingMaterial)

        @property
        def agma_cylindrical_gear_material(self: "Material._Cast_Material"):
            from mastapy.gears.materials import _581

            return self._parent._cast(_581.AGMACylindricalGearMaterial)

        @property
        def bevel_gear_iso_material(self: "Material._Cast_Material"):
            from mastapy.gears.materials import _583

            return self._parent._cast(_583.BevelGearISOMaterial)

        @property
        def bevel_gear_material(self: "Material._Cast_Material"):
            from mastapy.gears.materials import _585

            return self._parent._cast(_585.BevelGearMaterial)

        @property
        def cylindrical_gear_material(self: "Material._Cast_Material"):
            from mastapy.gears.materials import _589

            return self._parent._cast(_589.CylindricalGearMaterial)

        @property
        def gear_material(self: "Material._Cast_Material"):
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.GearMaterial)

        @property
        def iso_cylindrical_gear_material(self: "Material._Cast_Material"):
            from mastapy.gears.materials import _595

            return self._parent._cast(_595.ISOCylindricalGearMaterial)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_material(
            self: "Material._Cast_Material",
        ):
            from mastapy.gears.materials import _599

            return self._parent._cast(_599.KlingelnbergCycloPalloidConicalGearMaterial)

        @property
        def plastic_cylindrical_gear_material(self: "Material._Cast_Material"):
            from mastapy.gears.materials import _601

            return self._parent._cast(_601.PlasticCylindricalGearMaterial)

        @property
        def magnet_material(self: "Material._Cast_Material"):
            from mastapy.electric_machines import _1280

            return self._parent._cast(_1280.MagnetMaterial)

        @property
        def stator_rotor_material(self: "Material._Cast_Material"):
            from mastapy.electric_machines import _1298

            return self._parent._cast(_1298.StatorRotorMaterial)

        @property
        def winding_material(self: "Material._Cast_Material"):
            from mastapy.electric_machines import _1311

            return self._parent._cast(_1311.WindingMaterial)

        @property
        def spline_material(self: "Material._Cast_Material"):
            from mastapy.detailed_rigid_connectors.splines import _1413

            return self._parent._cast(_1413.SplineMaterial)

        @property
        def cycloidal_disc_material(self: "Material._Cast_Material"):
            from mastapy.cycloidal import _1453

            return self._parent._cast(_1453.CycloidalDiscMaterial)

        @property
        def ring_pins_material(self: "Material._Cast_Material"):
            from mastapy.cycloidal import _1460

            return self._parent._cast(_1460.RingPinsMaterial)

        @property
        def bolted_joint_material(self: "Material._Cast_Material"):
            from mastapy.bolts import _1463

            return self._parent._cast(_1463.BoltedJointMaterial)

        @property
        def bolt_material(self: "Material._Cast_Material"):
            from mastapy.bolts import _1467

            return self._parent._cast(_1467.BoltMaterial)

        @property
        def material(self: "Material._Cast_Material") -> "Material":
            return self._parent

        def __getattr__(self: "Material._Cast_Material", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Material.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_thermal_expansion(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoefficientOfThermalExpansion

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_thermal_expansion.setter
    @enforce_parameter_types
    def coefficient_of_thermal_expansion(self: Self, value: "float"):
        self.wrapped.CoefficientOfThermalExpansion = (
            float(value) if value is not None else 0.0
        )

    @property
    def cost_per_unit_mass(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CostPerUnitMass

        if temp is None:
            return 0.0

        return temp

    @cost_per_unit_mass.setter
    @enforce_parameter_types
    def cost_per_unit_mass(self: Self, value: "float"):
        self.wrapped.CostPerUnitMass = float(value) if value is not None else 0.0

    @property
    def density(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Density

        if temp is None:
            return 0.0

        return temp

    @density.setter
    @enforce_parameter_types
    def density(self: Self, value: "float"):
        self.wrapped.Density = float(value) if value is not None else 0.0

    @property
    def hardness_type(self: Self) -> "_256.HardnessType":
        """mastapy.materials.HardnessType"""
        temp = self.wrapped.HardnessType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Materials.HardnessType")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.materials._256", "HardnessType")(
            value
        )

    @hardness_type.setter
    @enforce_parameter_types
    def hardness_type(self: Self, value: "_256.HardnessType"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Materials.HardnessType")
        self.wrapped.HardnessType = value

    @property
    def heat_conductivity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HeatConductivity

        if temp is None:
            return 0.0

        return temp

    @heat_conductivity.setter
    @enforce_parameter_types
    def heat_conductivity(self: Self, value: "float"):
        self.wrapped.HeatConductivity = float(value) if value is not None else 0.0

    @property
    def material_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialName

        if temp is None:
            return ""

        return temp

    @property
    def maximum_allowable_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumAllowableTemperature

        if temp is None:
            return 0.0

        return temp

    @maximum_allowable_temperature.setter
    @enforce_parameter_types
    def maximum_allowable_temperature(self: Self, value: "float"):
        self.wrapped.MaximumAllowableTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def modulus_of_elasticity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModulusOfElasticity

        if temp is None:
            return 0.0

        return temp

    @modulus_of_elasticity.setter
    @enforce_parameter_types
    def modulus_of_elasticity(self: Self, value: "float"):
        self.wrapped.ModulusOfElasticity = float(value) if value is not None else 0.0

    @property
    def plane_strain_modulus(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlaneStrainModulus

        if temp is None:
            return 0.0

        return temp

    @property
    def poissons_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PoissonsRatio

        if temp is None:
            return 0.0

        return temp

    @poissons_ratio.setter
    @enforce_parameter_types
    def poissons_ratio(self: Self, value: "float"):
        self.wrapped.PoissonsRatio = float(value) if value is not None else 0.0

    @property
    def shear_fatigue_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShearFatigueStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def shear_modulus(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShearModulus

        if temp is None:
            return 0.0

        return temp

    @property
    def shear_yield_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShearYieldStress

        if temp is None:
            return 0.0

        return temp

    @property
    def specific_heat(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecificHeat

        if temp is None:
            return 0.0

        return temp

    @specific_heat.setter
    @enforce_parameter_types
    def specific_heat(self: Self, value: "float"):
        self.wrapped.SpecificHeat = float(value) if value is not None else 0.0

    @property
    def standard(self: Self) -> "_272.MaterialStandards":
        """mastapy.materials.MaterialStandards

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Standard

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.MaterialStandards"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials._272", "MaterialStandards"
        )(value)

    @property
    def surface_hardness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SurfaceHardness

        if temp is None:
            return 0.0

        return temp

    @surface_hardness.setter
    @enforce_parameter_types
    def surface_hardness(self: Self, value: "float"):
        self.wrapped.SurfaceHardness = float(value) if value is not None else 0.0

    @property
    def surface_hardness_range_max_in_hb(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMaxInHB

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_max_in_hrc(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMaxInHRC

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_max_in_hv(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMaxInHV

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_min_in_hb(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMinInHB

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_min_in_hrc(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMinInHRC

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_min_in_hv(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMinInHV

        if temp is None:
            return 0.0

        return temp

    @property
    def tensile_yield_strength(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TensileYieldStrength

        if temp is None:
            return 0.0

        return temp

    @tensile_yield_strength.setter
    @enforce_parameter_types
    def tensile_yield_strength(self: Self, value: "float"):
        self.wrapped.TensileYieldStrength = float(value) if value is not None else 0.0

    @property
    def ultimate_tensile_strength(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UltimateTensileStrength

        if temp is None:
            return 0.0

        return temp

    @ultimate_tensile_strength.setter
    @enforce_parameter_types
    def ultimate_tensile_strength(self: Self, value: "float"):
        self.wrapped.UltimateTensileStrength = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "Material._Cast_Material":
        return self._Cast_Material(self)
