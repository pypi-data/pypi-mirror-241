"""KlingelnbergCycloPalloidHypoidGearMeshRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.klingelnberg_conical import _409
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergHypoid",
    "KlingelnbergCycloPalloidHypoidGearMeshRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.klingelnberg_conical.kn3030 import _416
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _976
    from mastapy.gears.rating.klingelnberg_hypoid import _407


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearMeshRating")


class KlingelnbergCycloPalloidHypoidGearMeshRating(
    _409.KlingelnbergCycloPalloidConicalGearMeshRating
):
    """KlingelnbergCycloPalloidHypoidGearMeshRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshRating"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshRating:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshRating._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidHypoidGearMeshRating._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating",
        ):
            return self._parent._cast(
                _409.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def conical_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidHypoidGearMeshRating._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating",
        ):
            from mastapy.gears.rating.conical import _537

            return self._parent._cast(_537.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "KlingelnbergCycloPalloidHypoidGearMeshRating._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating",
        ):
            from mastapy.gears.rating import _358

            return self._parent._cast(_358.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidHypoidGearMeshRating._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating",
        ):
            from mastapy.gears.rating import _351

            return self._parent._cast(_351.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshRating._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating",
        ):
            from mastapy.gears.analysis import _1214

            return self._parent._cast(_1214.AbstractGearMeshAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "KlingelnbergCycloPalloidHypoidGearMeshRating._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshRating._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def kn3030_pitting_and_bending_klingelnberg_mesh_single_flank_rating(
        self: Self,
    ) -> "_416.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating":
        """mastapy.gears.rating.klingelnberg_conical.kn3030.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KN3030PittingAndBendingKlingelnbergMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def kn3030_scuffing_klingelnberg_mesh_single_flank_rating(
        self: Self,
    ) -> "_416.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating":
        """mastapy.gears.rating.klingelnberg_conical.kn3030.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KN3030ScuffingKlingelnbergMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: Self,
    ) -> "_976.KlingelnbergCycloPalloidHypoidGearMeshDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_ratings(
        self: Self,
    ) -> "List[_407.KlingelnbergCycloPalloidHypoidGearRating]":
        """List[mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshRating._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshRating(self)
