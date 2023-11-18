"""IndependentReportablePropertiesBase"""
from __future__ import annotations

from typing import TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_REPORTABLE_PROPERTIES_BASE = python_net_import(
    "SMT.MastaAPI.Utility", "IndependentReportablePropertiesBase"
)


__docformat__ = "restructuredtext en"
__all__ = ("IndependentReportablePropertiesBase",)


Self = TypeVar("Self", bound="IndependentReportablePropertiesBase")
T = TypeVar("T", bound="IndependentReportablePropertiesBase")


class IndependentReportablePropertiesBase(_0.APIBase, Generic[T]):
    """IndependentReportablePropertiesBase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _INDEPENDENT_REPORTABLE_PROPERTIES_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_IndependentReportablePropertiesBase")

    class _Cast_IndependentReportablePropertiesBase:
        """Special nested class for casting IndependentReportablePropertiesBase to subclasses."""

        def __init__(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
            parent: "IndependentReportablePropertiesBase",
        ):
            self._parent = parent

        @property
        def oil_pump_detail(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.materials.efficiency import _296

            return self._parent._cast(_296.OilPumpDetail)

        @property
        def packaging_limits(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.geometry import _307

            return self._parent._cast(_307.PackagingLimits)

        @property
        def specification_for_the_effect_of_oil_kinematic_viscosity(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.gears import _344

            return self._parent._cast(
                _344.SpecificationForTheEffectOfOilKinematicViscosity
            )

        @property
        def cylindrical_gear_micro_geometry_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1018

            return self._parent._cast(_1018.CylindricalGearMicroGeometrySettings)

        @property
        def hardened_material_properties(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1049

            return self._parent._cast(_1049.HardenedMaterialProperties)

        @property
        def ltca_load_case_modifiable_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1057

            return self._parent._cast(_1057.LTCALoadCaseModifiableSettings)

        @property
        def ltca_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1058

            return self._parent._cast(_1058.LTCASettings)

        @property
        def micropitting(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1061

            return self._parent._cast(_1061.Micropitting)

        @property
        def scuffing(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1068

            return self._parent._cast(_1068.Scuffing)

        @property
        def surface_roughness(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1076

            return self._parent._cast(_1076.SurfaceRoughness)

        @property
        def tiff_analysis_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1078

            return self._parent._cast(_1078.TiffAnalysisSettings)

        @property
        def tooth_flank_fracture_analysis_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1082

            return self._parent._cast(_1082.ToothFlankFractureAnalysisSettings)

        @property
        def usage(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1086

            return self._parent._cast(_1086.Usage)

        @property
        def eccentricity(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.electric_machines import _1258

            return self._parent._cast(_1258.Eccentricity)

        @property
        def temperatures(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.electric_machines.load_cases_and_analyses import _1374

            return self._parent._cast(_1374.Temperatures)

        @property
        def lookup_table_base(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.math_utility.measured_data import _1564

            return self._parent._cast(_1564.LookupTableBase)

        @property
        def onedimensional_function_lookup_table(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.math_utility.measured_data import _1565

            return self._parent._cast(_1565.OnedimensionalFunctionLookupTable)

        @property
        def twodimensional_function_lookup_table(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.math_utility.measured_data import _1566

            return self._parent._cast(_1566.TwodimensionalFunctionLookupTable)

        @property
        def roundness_specification(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.bearings.tolerances import _1916

            return self._parent._cast(_1916.RoundnessSpecification)

        @property
        def equivalent_load_factors(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.bearings.bearing_results import _1943

            return self._parent._cast(_1943.EquivalentLoadFactors)

        @property
        def iso14179_settings_per_bearing_type(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.bearings.bearing_results.rolling import _1974

            return self._parent._cast(_1974.ISO14179SettingsPerBearingType)

        @property
        def rolling_bearing_friction_coefficients(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.bearings.bearing_results.rolling import _2068

            return self._parent._cast(_2068.RollingBearingFrictionCoefficients)

        @property
        def additional_acceleration_options(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6808

            return self._parent._cast(_6808.AdditionalAccelerationOptions)

        @property
        def independent_reportable_properties_base(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "IndependentReportablePropertiesBase":
            return self._parent

        def __getattr__(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
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
        self: Self, instance_to_wrap: "IndependentReportablePropertiesBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase"
    ):
        return self._Cast_IndependentReportablePropertiesBase(self)
