"""GearDesignAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearDesignAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearDesignAnalysis",)


Self = TypeVar("Self", bound="GearDesignAnalysis")


class GearDesignAnalysis(_1213.AbstractGearAnalysis):
    """GearDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearDesignAnalysis")

    class _Cast_GearDesignAnalysis:
        """Special nested class for casting GearDesignAnalysis to subclasses."""

        def __init__(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
            parent: "GearDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_analysis(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            return self._parent._cast(_1213.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _610

            return self._parent._cast(_610.CylindricalGearManufacturingConfig)

        @property
        def cylindrical_manufactured_gear_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _614

            return self._parent._cast(_614.CylindricalManufacturedGearDutyCycle)

        @property
        def cylindrical_manufactured_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _615

            return self._parent._cast(_615.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _773

            return self._parent._cast(_773.ConicalGearManufacturingAnalysis)

        @property
        def conical_gear_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _774

            return self._parent._cast(_774.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _775

            return self._parent._cast(_775.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _776

            return self._parent._cast(_776.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _786

            return self._parent._cast(_786.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _787

            return self._parent._cast(_787.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _792

            return self._parent._cast(_792.ConicalWheelManufacturingConfig)

        @property
        def gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.ltca import _838

            return self._parent._cast(_838.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _854

            return self._parent._cast(_854.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.ltca.conical import _865

            return self._parent._cast(_865.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_case_base(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case import _871

            return self._parent._cast(_871.GearLoadCaseBase)

        @property
        def worm_gear_load_case(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case.worm import _874

            return self._parent._cast(_874.WormGearLoadCase)

        @property
        def face_gear_load_case(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case.face import _877

            return self._parent._cast(_877.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.load_case.cylindrical import _880

            return self._parent._cast(_880.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case.conical import _883

            return self._parent._cast(_883.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case.concept import _886

            return self._parent._cast(_886.ConceptGearLoadCase)

        @property
        def bevel_load_case(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.load_case.bevel import _889

            return self._parent._cast(_889.BevelLoadCase)

        @property
        def cylindrical_gear_tiff_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _896

            return self._parent._cast(_896.CylindricalGearTIFFAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _897

            return self._parent._cast(_897.CylindricalGearTIFFAnalysisDutyCycle)

        @property
        def face_gear_micro_geometry(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.face import _991

            return self._parent._cast(_991.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1098

            return self._parent._cast(_1098.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1099

            return self._parent._cast(_1099.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1100

            return self._parent._cast(_1100.CylindricalGearMicroGeometryDutyCycle)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102

            return self._parent._cast(_1102.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.fe_model import _1195

            return self._parent._cast(_1195.GearFEModel)

        @property
        def cylindrical_gear_fe_model(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.fe_model.cylindrical import _1199

            return self._parent._cast(_1199.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(self: "GearDesignAnalysis._Cast_GearDesignAnalysis"):
            from mastapy.gears.fe_model.conical import _1202

            return self._parent._cast(_1202.ConicalGearFEModel)

        @property
        def gear_implementation_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.GearImplementationAnalysis)

        @property
        def gear_implementation_analysis_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1218

            return self._parent._cast(_1218.GearImplementationAnalysisDutyCycle)

        @property
        def gear_implementation_detail(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1219

            return self._parent._cast(_1219.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "GearDesignAnalysis":
            return self._parent

        def __getattr__(self: "GearDesignAnalysis._Cast_GearDesignAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearDesignAnalysis._Cast_GearDesignAnalysis":
        return self._Cast_GearDesignAnalysis(self)
