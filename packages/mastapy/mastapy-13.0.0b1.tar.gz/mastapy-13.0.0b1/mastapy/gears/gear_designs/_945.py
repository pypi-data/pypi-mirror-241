"""GearDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.gear_designs import _946
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN = python_net_import("SMT.MastaAPI.Gears.GearDesigns", "GearDesign")

if TYPE_CHECKING:
    from mastapy.gears.fe_model import _1195


__docformat__ = "restructuredtext en"
__all__ = ("GearDesign",)


Self = TypeVar("Self", bound="GearDesign")


class GearDesign(_946.GearDesignComponent):
    """GearDesign

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearDesign")

    class _Cast_GearDesign:
        """Special nested class for casting GearDesign to subclasses."""

        def __init__(self: "GearDesign._Cast_GearDesign", parent: "GearDesign"):
            self._parent = parent

        @property
        def gear_design_component(self: "GearDesign._Cast_GearDesign"):
            return self._parent._cast(_946.GearDesignComponent)

        @property
        def zerol_bevel_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.zerol_bevel import _950

            return self._parent._cast(_950.ZerolBevelGearDesign)

        @property
        def worm_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.worm import _954

            return self._parent._cast(_954.WormDesign)

        @property
        def worm_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.worm import _955

            return self._parent._cast(_955.WormGearDesign)

        @property
        def worm_wheel_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.worm import _958

            return self._parent._cast(_958.WormWheelDesign)

        @property
        def straight_bevel_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.straight_bevel import _959

            return self._parent._cast(_959.StraightBevelGearDesign)

        @property
        def straight_bevel_diff_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.straight_bevel_diff import _963

            return self._parent._cast(_963.StraightBevelDiffGearDesign)

        @property
        def spiral_bevel_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.spiral_bevel import _967

            return self._parent._cast(_967.SpiralBevelGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _971

            return self._parent._cast(
                _971.KlingelnbergCycloPalloidSpiralBevelGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _975

            return self._parent._cast(_975.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_conical_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.klingelnberg_conical import _979

            return self._parent._cast(_979.KlingelnbergConicalGearDesign)

        @property
        def hypoid_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.hypoid import _983

            return self._parent._cast(_983.HypoidGearDesign)

        @property
        def face_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.face import _987

            return self._parent._cast(_987.FaceGearDesign)

        @property
        def face_gear_pinion_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.face import _992

            return self._parent._cast(_992.FaceGearPinionDesign)

        @property
        def face_gear_wheel_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.face import _995

            return self._parent._cast(_995.FaceGearWheelDesign)

        @property
        def cylindrical_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.cylindrical import _1010

            return self._parent._cast(_1010.CylindricalGearDesign)

        @property
        def cylindrical_planet_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.cylindrical import _1040

            return self._parent._cast(_1040.CylindricalPlanetGearDesign)

        @property
        def conical_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.conical import _1152

            return self._parent._cast(_1152.ConicalGearDesign)

        @property
        def concept_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.concept import _1174

            return self._parent._cast(_1174.ConceptGearDesign)

        @property
        def bevel_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.bevel import _1178

            return self._parent._cast(_1178.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(self: "GearDesign._Cast_GearDesign"):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1191

            return self._parent._cast(_1191.AGMAGleasonConicalGearDesign)

        @property
        def gear_design(self: "GearDesign._Cast_GearDesign") -> "GearDesign":
            return self._parent

        def __getattr__(self: "GearDesign._Cast_GearDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_shaft_inner_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AbsoluteShaftInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def mass(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

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
    def names_of_meshing_gears(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NamesOfMeshingGears

        if temp is None:
            return ""

        return temp

    @property
    def number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: Self, value: "int"):
        self.wrapped.NumberOfTeeth = int(value) if value is not None else 0

    @property
    def number_of_teeth_maintaining_ratio(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeethMaintainingRatio

        if temp is None:
            return 0

        return temp

    @number_of_teeth_maintaining_ratio.setter
    @enforce_parameter_types
    def number_of_teeth_maintaining_ratio(self: Self, value: "int"):
        self.wrapped.NumberOfTeethMaintainingRatio = (
            int(value) if value is not None else 0
        )

    @property
    def shaft_inner_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_outer_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tifffe_model(self: Self) -> "_1195.GearFEModel":
        """mastapy.gears.fe_model.GearFEModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TIFFFEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearDesign._Cast_GearDesign":
        return self._Cast_GearDesign(self)
