"""KlingelnbergCycloPalloidHypoidGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _977
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.connections_and_sockets.gears import _2317


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSet",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSet")


class KlingelnbergCycloPalloidHypoidGearSet(
    _2535.KlingelnbergCycloPalloidConicalGearSet
):
    """KlingelnbergCycloPalloidHypoidGearSet

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSet"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSet:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSet to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
            parent: "KlingelnbergCycloPalloidHypoidGearSet",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ):
            return self._parent._cast(_2535.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def conical_gear_set(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.ConicalGearSet)

        @property
        def gear_set(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.GearSet)

        @property
        def specialised_assembly(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ):
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ):
            from mastapy.system_model.part_model import _2432

            return self._parent._cast(_2432.AbstractAssembly)

        @property
        def part(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Part)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
        ) -> "KlingelnbergCycloPalloidHypoidGearSet":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSet.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_conical_gear_set_design(
        self: Self,
    ) -> "_977.KlingelnbergCycloPalloidHypoidGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_design(
        self: Self,
    ) -> "_977.KlingelnbergCycloPalloidHypoidGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears(
        self: Self,
    ) -> "List[_2536.KlingelnbergCycloPalloidHypoidGear]":
        """List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes(
        self: Self,
    ) -> "List[_2317.KlingelnbergCycloPalloidHypoidGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSet._Cast_KlingelnbergCycloPalloidHypoidGearSet":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSet(self)
