"""AbstractGearAnalysis"""
from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearAnalysis",)


Self = TypeVar("Self", bound="AbstractGearAnalysis")


class AbstractGearAnalysis(_0.APIBase):
    """AbstractGearAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearAnalysis")

    class _Cast_AbstractGearAnalysis:
        """Special nested class for casting AbstractGearAnalysis to subclasses."""

        def __init__(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
            parent: "AbstractGearAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating import _352

            return self._parent._cast(_352.AbstractGearRating)

        @property
        def gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.GearDutyCycleRating)

        @property
        def gear_rating(self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis"):
            from mastapy.gears.rating import _359

            return self._parent._cast(_359.GearRating)

        @property
        def zerol_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.zerol_bevel import _368

            return self._parent._cast(_368.ZerolBevelGearRating)

        @property
        def worm_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.worm import _370

            return self._parent._cast(_370.WormGearDutyCycleRating)

        @property
        def worm_gear_rating(self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis"):
            from mastapy.gears.rating.worm import _372

            return self._parent._cast(_372.WormGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.straight_bevel import _394

            return self._parent._cast(_394.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _397

            return self._parent._cast(_397.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.spiral_bevel import _401

            return self._parent._cast(_401.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _404

            return self._parent._cast(
                _404.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _407

            return self._parent._cast(_407.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _410

            return self._parent._cast(_410.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis"):
            from mastapy.gears.rating.hypoid import _437

            return self._parent._cast(_437.HypoidGearRating)

        @property
        def face_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.face import _443

            return self._parent._cast(_443.FaceGearDutyCycleRating)

        @property
        def face_gear_rating(self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis"):
            from mastapy.gears.rating.face import _446

            return self._parent._cast(_446.FaceGearRating)

        @property
        def cylindrical_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.cylindrical import _453

            return self._parent._cast(_453.CylindricalGearDutyCycleRating)

        @property
        def cylindrical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.cylindrical import _458

            return self._parent._cast(_458.CylindricalGearRating)

        @property
        def conical_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.conical import _536

            return self._parent._cast(_536.ConicalGearDutyCycleRating)

        @property
        def conical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.conical import _538

            return self._parent._cast(_538.ConicalGearRating)

        @property
        def concept_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.concept import _546

            return self._parent._cast(_546.ConceptGearDutyCycleRating)

        @property
        def concept_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.concept import _549

            return self._parent._cast(_549.ConceptGearRating)

        @property
        def bevel_gear_rating(self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis"):
            from mastapy.gears.rating.bevel import _553

            return self._parent._cast(_553.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _564

            return self._parent._cast(_564.AGMAGleasonConicalGearRating)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _610

            return self._parent._cast(_610.CylindricalGearManufacturingConfig)

        @property
        def cylindrical_manufactured_gear_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _614

            return self._parent._cast(_614.CylindricalManufacturedGearDutyCycle)

        @property
        def cylindrical_manufactured_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _615

            return self._parent._cast(_615.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _773

            return self._parent._cast(_773.ConicalGearManufacturingAnalysis)

        @property
        def conical_gear_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _774

            return self._parent._cast(_774.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _775

            return self._parent._cast(_775.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _776

            return self._parent._cast(_776.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _786

            return self._parent._cast(_786.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _787

            return self._parent._cast(_787.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _792

            return self._parent._cast(_792.ConicalWheelManufacturingConfig)

        @property
        def gear_load_distribution_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.ltca import _838

            return self._parent._cast(_838.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _854

            return self._parent._cast(_854.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.ltca.conical import _865

            return self._parent._cast(_865.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_case_base(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.load_case import _871

            return self._parent._cast(_871.GearLoadCaseBase)

        @property
        def worm_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.load_case.worm import _874

            return self._parent._cast(_874.WormGearLoadCase)

        @property
        def face_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.load_case.face import _877

            return self._parent._cast(_877.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.load_case.cylindrical import _880

            return self._parent._cast(_880.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.load_case.conical import _883

            return self._parent._cast(_883.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.load_case.concept import _886

            return self._parent._cast(_886.ConceptGearLoadCase)

        @property
        def bevel_load_case(self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis"):
            from mastapy.gears.load_case.bevel import _889

            return self._parent._cast(_889.BevelLoadCase)

        @property
        def cylindrical_gear_tiff_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _896

            return self._parent._cast(_896.CylindricalGearTIFFAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _897

            return self._parent._cast(_897.CylindricalGearTIFFAnalysisDutyCycle)

        @property
        def face_gear_micro_geometry(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.gear_designs.face import _991

            return self._parent._cast(_991.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1098

            return self._parent._cast(_1098.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1099

            return self._parent._cast(_1099.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1100

            return self._parent._cast(_1100.CylindricalGearMicroGeometryDutyCycle)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102

            return self._parent._cast(_1102.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis"):
            from mastapy.gears.fe_model import _1195

            return self._parent._cast(_1195.GearFEModel)

        @property
        def cylindrical_gear_fe_model(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.fe_model.cylindrical import _1199

            return self._parent._cast(_1199.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.fe_model.conical import _1202

            return self._parent._cast(_1202.ConicalGearFEModel)

        @property
        def gear_design_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.GearDesignAnalysis)

        @property
        def gear_implementation_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.GearImplementationAnalysis)

        @property
        def gear_implementation_analysis_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.analysis import _1218

            return self._parent._cast(_1218.GearImplementationAnalysisDutyCycle)

        @property
        def gear_implementation_detail(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ):
            from mastapy.gears.analysis import _1219

            return self._parent._cast(_1219.GearImplementationDetail)

        @property
        def abstract_gear_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "AbstractGearAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def name_with_gear_set_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NameWithGearSetName

        if temp is None:
            return ""

        return temp

    @property
    def planet_index(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PlanetIndex

        if temp is None:
            return 0

        return temp

    @planet_index.setter
    @enforce_parameter_types
    def planet_index(self: Self, value: "int"):
        self.wrapped.PlanetIndex = int(value) if value is not None else 0

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
    def cast_to(self: Self) -> "AbstractGearAnalysis._Cast_AbstractGearAnalysis":
        return self._Cast_AbstractGearAnalysis(self)
