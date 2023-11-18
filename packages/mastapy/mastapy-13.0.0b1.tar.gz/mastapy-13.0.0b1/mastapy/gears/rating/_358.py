"""GearMeshRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _351
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_RATING = python_net_import("SMT.MastaAPI.Gears.Rating", "GearMeshRating")

if TYPE_CHECKING:
    from mastapy.gears.load_case import _873


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshRating",)


Self = TypeVar("Self", bound="GearMeshRating")


class GearMeshRating(_351.AbstractGearMeshRating):
    """GearMeshRating

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshRating")

    class _Cast_GearMeshRating:
        """Special nested class for casting GearMeshRating to subclasses."""

        def __init__(
            self: "GearMeshRating._Cast_GearMeshRating", parent: "GearMeshRating"
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            return self._parent._cast(_351.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.analysis import _1214

            return self._parent._cast(_1214.AbstractGearMeshAnalysis)

        @property
        def zerol_bevel_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.zerol_bevel import _367

            return self._parent._cast(_367.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.worm import _371

            return self._parent._cast(_371.WormGearMeshRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.straight_bevel import _393

            return self._parent._cast(_393.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _396

            return self._parent._cast(_396.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.spiral_bevel import _400

            return self._parent._cast(_400.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _403

            return self._parent._cast(
                _403.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _406

            return self._parent._cast(_406.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _409

            return self._parent._cast(
                _409.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def hypoid_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.hypoid import _436

            return self._parent._cast(_436.HypoidGearMeshRating)

        @property
        def face_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.face import _445

            return self._parent._cast(_445.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.cylindrical import _456

            return self._parent._cast(_456.CylindricalGearMeshRating)

        @property
        def conical_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.conical import _537

            return self._parent._cast(_537.ConicalGearMeshRating)

        @property
        def concept_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.concept import _548

            return self._parent._cast(_548.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(self: "GearMeshRating._Cast_GearMeshRating"):
            from mastapy.gears.rating.bevel import _552

            return self._parent._cast(_552.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _563

            return self._parent._cast(_563.AGMAGleasonConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "GearMeshRating._Cast_GearMeshRating",
        ) -> "GearMeshRating":
            return self._parent

        def __getattr__(self: "GearMeshRating._Cast_GearMeshRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def driving_gear(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DrivingGear

        if temp is None:
            return ""

        return temp

    @property
    def energy_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def is_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def mesh_efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionName

        if temp is None:
            return ""

        return temp

    @property
    def pinion_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_pinion_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedPinionTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_wheel_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedWheelTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def total_energy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelName

        if temp is None:
            return ""

        return temp

    @property
    def wheel_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_load_case(self: Self) -> "_873.MeshLoadCase":
        """mastapy.gears.load_case.MeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMeshRating._Cast_GearMeshRating":
        return self._Cast_GearMeshRating(self)
