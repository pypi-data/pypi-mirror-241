"""AbstractGearSetAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearSetAnalysis"
)

if TYPE_CHECKING:
    from mastapy.utility.model_validation import _1792, _1791


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearSetAnalysis",)


Self = TypeVar("Self", bound="AbstractGearSetAnalysis")


class AbstractGearSetAnalysis(_0.APIBase):
    """AbstractGearSetAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_SET_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearSetAnalysis")

    class _Cast_AbstractGearSetAnalysis:
        """Special nested class for casting AbstractGearSetAnalysis to subclasses."""

        def __init__(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
            parent: "AbstractGearSetAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating import _353

            return self._parent._cast(_353.AbstractGearSetRating)

        @property
        def gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating import _360

            return self._parent._cast(_360.GearSetDutyCycleRating)

        @property
        def gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.GearSetRating)

        @property
        def zerol_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.zerol_bevel import _369

            return self._parent._cast(_369.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.worm import _373

            return self._parent._cast(_373.WormGearSetDutyCycleRating)

        @property
        def worm_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.worm import _374

            return self._parent._cast(_374.WormGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.straight_bevel import _395

            return self._parent._cast(_395.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _398

            return self._parent._cast(_398.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.spiral_bevel import _402

            return self._parent._cast(_402.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _405

            return self._parent._cast(
                _405.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _408

            return self._parent._cast(_408.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _411

            return self._parent._cast(_411.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.hypoid import _438

            return self._parent._cast(_438.HypoidGearSetRating)

        @property
        def face_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.face import _447

            return self._parent._cast(_447.FaceGearSetDutyCycleRating)

        @property
        def face_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.face import _448

            return self._parent._cast(_448.FaceGearSetRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.cylindrical import _461

            return self._parent._cast(_461.CylindricalGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.cylindrical import _462

            return self._parent._cast(_462.CylindricalGearSetRating)

        @property
        def reduced_cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.cylindrical import _478

            return self._parent._cast(_478.ReducedCylindricalGearSetDutyCycleRating)

        @property
        def conical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.conical import _539

            return self._parent._cast(_539.ConicalGearSetDutyCycleRating)

        @property
        def conical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.conical import _540

            return self._parent._cast(_540.ConicalGearSetRating)

        @property
        def concept_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.concept import _550

            return self._parent._cast(_550.ConceptGearSetDutyCycleRating)

        @property
        def concept_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.concept import _551

            return self._parent._cast(_551.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.bevel import _554

            return self._parent._cast(_554.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _565

            return self._parent._cast(_565.AGMAGleasonConicalGearSetRating)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _618

            return self._parent._cast(_618.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _619

            return self._parent._cast(_619.CylindricalManufacturedGearSetLoadCase)

        @property
        def cylindrical_set_manufacturing_config(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _623

            return self._parent._cast(_623.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _788

            return self._parent._cast(_788.ConicalSetManufacturingAnalysis)

        @property
        def conical_set_manufacturing_config(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _789

            return self._parent._cast(_789.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _790

            return self._parent._cast(_790.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _791

            return self._parent._cast(_791.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.ltca import _844

            return self._parent._cast(_844.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _858

            return self._parent._cast(_858.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _860

            return self._parent._cast(_860.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.ltca.conical import _866

            return self._parent._cast(_866.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_case_base(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.load_case import _872

            return self._parent._cast(_872.GearSetLoadCaseBase)

        @property
        def worm_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.load_case.worm import _875

            return self._parent._cast(_875.WormGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.load_case.face import _878

            return self._parent._cast(_878.FaceGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.load_case.cylindrical import _881

            return self._parent._cast(_881.CylindricalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.load_case.conical import _884

            return self._parent._cast(_884.ConicalGearSetLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.load_case.concept import _887

            return self._parent._cast(_887.ConceptGearSetLoadCase)

        @property
        def bevel_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.load_case.bevel import _891

            return self._parent._cast(_891.BevelSetLoadCase)

        @property
        def cylindrical_gear_set_tiff_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _894

            return self._parent._cast(_894.CylindricalGearSetTIFFAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _895

            return self._parent._cast(_895.CylindricalGearSetTIFFAnalysisDutyCycle)

        @property
        def face_gear_set_micro_geometry(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.gear_designs.face import _994

            return self._parent._cast(_994.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1105

            return self._parent._cast(_1105.CylindricalGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1106

            return self._parent._cast(_1106.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_fe_model(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.fe_model import _1198

            return self._parent._cast(_1198.GearSetFEModel)

        @property
        def cylindrical_gear_set_fe_model(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.fe_model.cylindrical import _1201

            return self._parent._cast(_1201.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.fe_model.conical import _1204

            return self._parent._cast(_1204.ConicalSetFEModel)

        @property
        def gear_set_design_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearSetDesignAnalysis)

        @property
        def gear_set_implementation_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_detail(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ):
            from mastapy.gears.analysis import _1229

            return self._parent._cast(_1229.GearSetImplementationDetail)

        @property
        def abstract_gear_set_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "AbstractGearSetAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearSetAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def all_status_errors(self: Self) -> "List[_1792.StatusItem]":
        """List[mastapy.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def status(self: Self) -> "_1791.Status":
        """mastapy.utility.model_validation.Status

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: Self) -> "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis":
        return self._Cast_AbstractGearSetAnalysis(self)
