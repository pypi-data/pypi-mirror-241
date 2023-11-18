"""AbstractGearMeshAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearMeshAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1213


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearMeshAnalysis",)


Self = TypeVar("Self", bound="AbstractGearMeshAnalysis")


class AbstractGearMeshAnalysis(_0.APIBase):
    """AbstractGearMeshAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_MESH_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearMeshAnalysis")

    class _Cast_AbstractGearMeshAnalysis:
        """Special nested class for casting AbstractGearMeshAnalysis to subclasses."""

        def __init__(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
            parent: "AbstractGearMeshAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating import _351

            return self._parent._cast(_351.AbstractGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating import _358

            return self._parent._cast(_358.GearMeshRating)

        @property
        def mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.MeshDutyCycleRating)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.zerol_bevel import _367

            return self._parent._cast(_367.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.worm import _371

            return self._parent._cast(_371.WormGearMeshRating)

        @property
        def worm_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.worm import _375

            return self._parent._cast(_375.WormMeshDutyCycleRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.straight_bevel import _393

            return self._parent._cast(_393.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _396

            return self._parent._cast(_396.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.spiral_bevel import _400

            return self._parent._cast(_400.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _403

            return self._parent._cast(
                _403.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _406

            return self._parent._cast(_406.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _409

            return self._parent._cast(
                _409.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def hypoid_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.hypoid import _436

            return self._parent._cast(_436.HypoidGearMeshRating)

        @property
        def face_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.face import _444

            return self._parent._cast(_444.FaceGearMeshDutyCycleRating)

        @property
        def face_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.face import _445

            return self._parent._cast(_445.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.cylindrical import _456

            return self._parent._cast(_456.CylindricalGearMeshRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.cylindrical import _464

            return self._parent._cast(_464.CylindricalMeshDutyCycleRating)

        @property
        def conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.conical import _537

            return self._parent._cast(_537.ConicalGearMeshRating)

        @property
        def conical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.concept import _547

            return self._parent._cast(_547.ConceptGearMeshDutyCycleRating)

        @property
        def concept_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.concept import _548

            return self._parent._cast(_548.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.bevel import _552

            return self._parent._cast(_552.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _563

            return self._parent._cast(_563.AGMAGleasonConicalGearMeshRating)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _616

            return self._parent._cast(_616.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _617

            return self._parent._cast(_617.CylindricalManufacturedGearMeshLoadCase)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _620

            return self._parent._cast(_620.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _782

            return self._parent._cast(_782.ConicalMeshManufacturingAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _783

            return self._parent._cast(_783.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _784

            return self._parent._cast(_784.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.ltca import _839

            return self._parent._cast(_839.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _855

            return self._parent._cast(_855.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.ltca.conical import _868

            return self._parent._cast(_868.ConicalMeshLoadDistributionAnalysis)

        @property
        def mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case import _873

            return self._parent._cast(_873.MeshLoadCase)

        @property
        def worm_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.worm import _876

            return self._parent._cast(_876.WormMeshLoadCase)

        @property
        def face_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.face import _879

            return self._parent._cast(_879.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.cylindrical import _882

            return self._parent._cast(_882.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.conical import _885

            return self._parent._cast(_885.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.concept import _888

            return self._parent._cast(_888.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.load_case.bevel import _890

            return self._parent._cast(_890.BevelMeshLoadCase)

        @property
        def cylindrical_gear_mesh_tiff_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _892

            return self._parent._cast(_892.CylindricalGearMeshTIFFAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _893

            return self._parent._cast(_893.CylindricalGearMeshTIFFAnalysisDutyCycle)

        @property
        def face_gear_mesh_micro_geometry(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.gear_designs.face import _990

            return self._parent._cast(_990.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1096

            return self._parent._cast(_1096.CylindricalGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1097

            return self._parent._cast(_1097.CylindricalGearMeshMicroGeometryDutyCycle)

        @property
        def gear_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.fe_model import _1196

            return self._parent._cast(_1196.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.fe_model.cylindrical import _1200

            return self._parent._cast(_1200.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.fe_model.conical import _1203

            return self._parent._cast(_1203.ConicalMeshFEModel)

        @property
        def gear_mesh_design_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.analysis import _1220

            return self._parent._cast(_1220.GearMeshDesignAnalysis)

        @property
        def gear_mesh_implementation_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_implementation_detail(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ):
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.GearMeshImplementationDetail)

        @property
        def abstract_gear_mesh_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "AbstractGearMeshAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearMeshAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshName

        if temp is None:
            return ""

        return temp

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
    def gear_a(self: Self) -> "_1213.AbstractGearAnalysis":
        """mastapy.gears.analysis.AbstractGearAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_1213.AbstractGearAnalysis":
        """mastapy.gears.analysis.AbstractGearAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

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
    def cast_to(
        self: Self,
    ) -> "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis":
        return self._Cast_AbstractGearMeshAnalysis(self)
