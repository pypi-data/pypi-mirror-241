"""NamedDatabaseItem"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_DATABASE_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Databases", "NamedDatabaseItem"
)

if TYPE_CHECKING:
    from mastapy.utility import _1580
    from mastapy.utility.databases import _1828


__docformat__ = "restructuredtext en"
__all__ = ("NamedDatabaseItem",)


Self = TypeVar("Self", bound="NamedDatabaseItem")


class NamedDatabaseItem(_0.APIBase):
    """NamedDatabaseItem

    This is a mastapy class.
    """

    TYPE = _NAMED_DATABASE_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedDatabaseItem")

    class _Cast_NamedDatabaseItem:
        """Special nested class for casting NamedDatabaseItem to subclasses."""

        def __init__(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
            parent: "NamedDatabaseItem",
        ):
            self._parent = parent

        @property
        def shaft_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.shafts import _24

            return self._parent._cast(_24.ShaftMaterial)

        @property
        def shaft_settings_item(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.shafts import _40

            return self._parent._cast(_40.ShaftSettingsItem)

        @property
        def simple_shaft_definition(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.shafts import _43

            return self._parent._cast(_43.SimpleShaftDefinition)

        @property
        def analysis_settings_item(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.nodal_analysis import _50

            return self._parent._cast(_50.AnalysisSettingsItem)

        @property
        def bearing_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.materials import _243

            return self._parent._cast(_243.BearingMaterial)

        @property
        def lubrication_detail(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.materials import _265

            return self._parent._cast(_265.LubricationDetail)

        @property
        def material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.materials import _267

            return self._parent._cast(_267.Material)

        @property
        def materials_settings_item(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.materials import _271

            return self._parent._cast(_271.MaterialsSettingsItem)

        @property
        def pocketing_power_loss_coefficients(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears import _340

            return self._parent._cast(_340.PocketingPowerLossCoefficients)

        @property
        def cylindrical_gear_design_and_rating_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.rating.cylindrical import _452

            return self._parent._cast(_452.CylindricalGearDesignAndRatingSettingsItem)

        @property
        def cylindrical_plastic_gear_rating_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.rating.cylindrical import _468

            return self._parent._cast(_468.CylindricalPlasticGearRatingSettingsItem)

        @property
        def agma_cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.materials import _581

            return self._parent._cast(_581.AGMACylindricalGearMaterial)

        @property
        def bevel_gear_iso_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.gears.materials import _583

            return self._parent._cast(_583.BevelGearISOMaterial)

        @property
        def bevel_gear_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.gears.materials import _585

            return self._parent._cast(_585.BevelGearMaterial)

        @property
        def cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.materials import _589

            return self._parent._cast(_589.CylindricalGearMaterial)

        @property
        def gear_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.GearMaterial)

        @property
        def iso_cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.materials import _595

            return self._parent._cast(_595.ISOCylindricalGearMaterial)

        @property
        def isotr1417912001_coefficient_of_friction_constants(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.materials import _596

            return self._parent._cast(
                _596.ISOTR1417912001CoefficientOfFrictionConstants
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.materials import _599

            return self._parent._cast(_599.KlingelnbergCycloPalloidConicalGearMaterial)

        @property
        def plastic_cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.materials import _601

            return self._parent._cast(_601.PlasticCylindricalGearMaterial)

        @property
        def raw_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.gears.materials import _604

            return self._parent._cast(_604.RawMaterial)

        @property
        def cylindrical_gear_abstract_cutter_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _704

            return self._parent._cast(_704.CylindricalGearAbstractCutterDesign)

        @property
        def cylindrical_gear_form_grinding_wheel(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _705

            return self._parent._cast(_705.CylindricalGearFormGrindingWheel)

        @property
        def cylindrical_gear_grinding_worm(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _706

            return self._parent._cast(_706.CylindricalGearGrindingWorm)

        @property
        def cylindrical_gear_hob_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _707

            return self._parent._cast(_707.CylindricalGearHobDesign)

        @property
        def cylindrical_gear_plunge_shaver(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _708

            return self._parent._cast(_708.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_rack_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _710

            return self._parent._cast(_710.CylindricalGearRackDesign)

        @property
        def cylindrical_gear_real_cutter_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _711

            return self._parent._cast(_711.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_shaper(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.gears.manufacturing.cylindrical.cutters import _712

            return self._parent._cast(_712.CylindricalGearShaper)

        @property
        def cylindrical_gear_shaver(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.gears.manufacturing.cylindrical.cutters import _713

            return self._parent._cast(_713.CylindricalGearShaver)

        @property
        def involute_cutter_design(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.gears.manufacturing.cylindrical.cutters import _716

            return self._parent._cast(_716.InvoluteCutterDesign)

        @property
        def manufacturing_machine(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.gears.manufacturing.bevel import _797

            return self._parent._cast(_797.ManufacturingMachine)

        @property
        def bevel_hypoid_gear_design_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.gear_designs import _939

            return self._parent._cast(_939.BevelHypoidGearDesignSettingsItem)

        @property
        def bevel_hypoid_gear_rating_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.gear_designs import _941

            return self._parent._cast(_941.BevelHypoidGearRatingSettingsItem)

        @property
        def design_constraints_collection(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.gear_designs import _944

            return self._parent._cast(_944.DesignConstraintsCollection)

        @property
        def cylindrical_gear_design_constraints(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1012

            return self._parent._cast(_1012.CylindricalGearDesignConstraints)

        @property
        def cylindrical_gear_micro_geometry_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1020

            return self._parent._cast(_1020.CylindricalGearMicroGeometrySettingsItem)

        @property
        def magnet_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.electric_machines import _1280

            return self._parent._cast(_1280.MagnetMaterial)

        @property
        def stator_rotor_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.electric_machines import _1298

            return self._parent._cast(_1298.StatorRotorMaterial)

        @property
        def winding_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.electric_machines import _1311

            return self._parent._cast(_1311.WindingMaterial)

        @property
        def spline_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.detailed_rigid_connectors.splines import _1413

            return self._parent._cast(_1413.SplineMaterial)

        @property
        def cycloidal_disc_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.cycloidal import _1453

            return self._parent._cast(_1453.CycloidalDiscMaterial)

        @property
        def ring_pins_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.cycloidal import _1460

            return self._parent._cast(_1460.RingPinsMaterial)

        @property
        def bolted_joint_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.bolts import _1463

            return self._parent._cast(_1463.BoltedJointMaterial)

        @property
        def bolt_geometry(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.bolts import _1465

            return self._parent._cast(_1465.BoltGeometry)

        @property
        def bolt_material(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.bolts import _1467

            return self._parent._cast(_1467.BoltMaterial)

        @property
        def pareto_optimisation_strategy(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.math_utility.optimisation import _1547

            return self._parent._cast(_1547.ParetoOptimisationStrategy)

        @property
        def bearing_settings_item(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.bearings import _1879

            return self._parent._cast(_1879.BearingSettingsItem)

        @property
        def iso14179_settings(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.bearings.bearing_results.rolling import _1972

            return self._parent._cast(_1972.ISO14179Settings)

        @property
        def conical_gear_optimisation_strategy(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.system_model.optimization import _2224

            return self._parent._cast(_2224.ConicalGearOptimisationStrategy)

        @property
        def cylindrical_gear_optimisation_strategy(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.system_model.optimization import _2227

            return self._parent._cast(_2227.CylindricalGearOptimisationStrategy)

        @property
        def optimization_strategy(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.system_model.optimization import _2232

            return self._parent._cast(_2232.OptimizationStrategy)

        @property
        def optimization_strategy_base(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ):
            from mastapy.system_model.optimization import _2233

            return self._parent._cast(_2233.OptimizationStrategyBase)

        @property
        def supercharger_rotor_set(self: "NamedDatabaseItem._Cast_NamedDatabaseItem"):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2561,
            )

            return self._parent._cast(_2561.SuperchargerRotorSet)

        @property
        def named_database_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "NamedDatabaseItem":
            return self._parent

        def __getattr__(self: "NamedDatabaseItem._Cast_NamedDatabaseItem", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedDatabaseItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def no_history(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NoHistory

        if temp is None:
            return ""

        return temp

    @property
    def history(self: Self) -> "_1580.FileHistory":
        """mastapy.utility.FileHistory

        Note:
            This property is readonly.
        """
        temp = self.wrapped.History

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def database_key(self: Self) -> "_1828.NamedKey":
        """mastapy.utility.databases.NamedKey"""
        temp = self.wrapped.DatabaseKey

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @database_key.setter
    @enforce_parameter_types
    def database_key(self: Self, value: "_1828.NamedKey"):
        self.wrapped.DatabaseKey = value.wrapped

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "NamedDatabaseItem._Cast_NamedDatabaseItem":
        return self._Cast_NamedDatabaseItem(self)
