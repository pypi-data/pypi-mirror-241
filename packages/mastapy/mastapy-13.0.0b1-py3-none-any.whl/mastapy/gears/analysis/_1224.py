"""GearSetDesignAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1215
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetDesignAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearSetDesignAnalysis",)


Self = TypeVar("Self", bound="GearSetDesignAnalysis")


class GearSetDesignAnalysis(_1215.AbstractGearSetAnalysis):
    """GearSetDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetDesignAnalysis")

    class _Cast_GearSetDesignAnalysis:
        """Special nested class for casting GearSetDesignAnalysis to subclasses."""

        def __init__(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
            parent: "GearSetDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _618

            return self._parent._cast(_618.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _619

            return self._parent._cast(_619.CylindricalManufacturedGearSetLoadCase)

        @property
        def cylindrical_set_manufacturing_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _623

            return self._parent._cast(_623.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _788

            return self._parent._cast(_788.ConicalSetManufacturingAnalysis)

        @property
        def conical_set_manufacturing_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _789

            return self._parent._cast(_789.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _790

            return self._parent._cast(_790.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _791

            return self._parent._cast(_791.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.ltca import _844

            return self._parent._cast(_844.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _858

            return self._parent._cast(_858.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _860

            return self._parent._cast(_860.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.ltca.conical import _866

            return self._parent._cast(_866.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_case_base(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case import _872

            return self._parent._cast(_872.GearSetLoadCaseBase)

        @property
        def worm_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.worm import _875

            return self._parent._cast(_875.WormGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.face import _878

            return self._parent._cast(_878.FaceGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.cylindrical import _881

            return self._parent._cast(_881.CylindricalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.conical import _884

            return self._parent._cast(_884.ConicalGearSetLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.concept import _887

            return self._parent._cast(_887.ConceptGearSetLoadCase)

        @property
        def bevel_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.load_case.bevel import _891

            return self._parent._cast(_891.BevelSetLoadCase)

        @property
        def cylindrical_gear_set_tiff_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _894

            return self._parent._cast(_894.CylindricalGearSetTIFFAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _895

            return self._parent._cast(_895.CylindricalGearSetTIFFAnalysisDutyCycle)

        @property
        def face_gear_set_micro_geometry(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.face import _994

            return self._parent._cast(_994.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1105

            return self._parent._cast(_1105.CylindricalGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1106

            return self._parent._cast(_1106.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.fe_model import _1198

            return self._parent._cast(_1198.GearSetFEModel)

        @property
        def cylindrical_gear_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.fe_model.cylindrical import _1201

            return self._parent._cast(_1201.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.fe_model.conical import _1204

            return self._parent._cast(_1204.ConicalSetFEModel)

        @property
        def gear_set_implementation_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_detail(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1229

            return self._parent._cast(_1229.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "GearSetDesignAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis":
        return self._Cast_GearSetDesignAnalysis(self)
