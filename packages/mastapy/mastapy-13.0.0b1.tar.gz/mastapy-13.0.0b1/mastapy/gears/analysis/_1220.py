"""GearMeshDesignAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1214
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshDesignAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1216, _1224


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshDesignAnalysis",)


Self = TypeVar("Self", bound="GearMeshDesignAnalysis")


class GearMeshDesignAnalysis(_1214.AbstractGearMeshAnalysis):
    """GearMeshDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshDesignAnalysis")

    class _Cast_GearMeshDesignAnalysis:
        """Special nested class for casting GearMeshDesignAnalysis to subclasses."""

        def __init__(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
            parent: "GearMeshDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            return self._parent._cast(_1214.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _616

            return self._parent._cast(_616.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _617

            return self._parent._cast(_617.CylindricalManufacturedGearMeshLoadCase)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.cylindrical import _620

            return self._parent._cast(_620.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _782

            return self._parent._cast(_782.ConicalMeshManufacturingAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _783

            return self._parent._cast(_783.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _784

            return self._parent._cast(_784.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.ltca import _839

            return self._parent._cast(_839.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.ltca.cylindrical import _855

            return self._parent._cast(_855.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.ltca.conical import _868

            return self._parent._cast(_868.ConicalMeshLoadDistributionAnalysis)

        @property
        def mesh_load_case(self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis"):
            from mastapy.gears.load_case import _873

            return self._parent._cast(_873.MeshLoadCase)

        @property
        def worm_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.worm import _876

            return self._parent._cast(_876.WormMeshLoadCase)

        @property
        def face_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.face import _879

            return self._parent._cast(_879.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.cylindrical import _882

            return self._parent._cast(_882.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.conical import _885

            return self._parent._cast(_885.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.concept import _888

            return self._parent._cast(_888.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.load_case.bevel import _890

            return self._parent._cast(_890.BevelMeshLoadCase)

        @property
        def cylindrical_gear_mesh_tiff_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _892

            return self._parent._cast(_892.CylindricalGearMeshTIFFAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.gear_two_d_fe_analysis import _893

            return self._parent._cast(_893.CylindricalGearMeshTIFFAnalysisDutyCycle)

        @property
        def face_gear_mesh_micro_geometry(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.face import _990

            return self._parent._cast(_990.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1096

            return self._parent._cast(_1096.CylindricalGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1097

            return self._parent._cast(_1097.CylindricalGearMeshMicroGeometryDutyCycle)

        @property
        def gear_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.fe_model import _1196

            return self._parent._cast(_1196.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.fe_model.cylindrical import _1200

            return self._parent._cast(_1200.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.fe_model.conical import _1203

            return self._parent._cast(_1203.ConicalMeshFEModel)

        @property
        def gear_mesh_implementation_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_implementation_detail(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ):
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "GearMeshDesignAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a(self: Self) -> "_1216.GearDesignAnalysis":
        """mastapy.gears.analysis.GearDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_1216.GearDesignAnalysis":
        """mastapy.gears.analysis.GearDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set(self: Self) -> "_1224.GearSetDesignAnalysis":
        """mastapy.gears.analysis.GearSetDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis":
        return self._Cast_GearMeshDesignAnalysis(self)
