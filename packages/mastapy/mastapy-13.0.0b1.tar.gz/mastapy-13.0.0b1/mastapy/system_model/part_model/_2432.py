"""AbstractAssembly"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.part_model import _2466
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractAssembly"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssembly",)


Self = TypeVar("Self", bound="AbstractAssembly")


class AbstractAssembly(_2466.Part):
    """AbstractAssembly

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssembly")

    class _Cast_AbstractAssembly:
        """Special nested class for casting AbstractAssembly to subclasses."""

        def __init__(
            self: "AbstractAssembly._Cast_AbstractAssembly", parent: "AbstractAssembly"
        ):
            self._parent = parent

        @property
        def part(self: "AbstractAssembly._Cast_AbstractAssembly"):
            return self._parent._cast(_2466.Part)

        @property
        def design_entity(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def assembly(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model import _2431

            return self._parent._cast(_2431.Assembly)

        @property
        def bolted_joint(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.BoltedJoint)

        @property
        def flexible_pin_assembly(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.FlexiblePinAssembly)

        @property
        def root_assembly(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model import _2472

            return self._parent._cast(_2472.RootAssembly)

        @property
        def specialised_assembly(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.SpecialisedAssembly)

        @property
        def agma_gleason_conical_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2512

            return self._parent._cast(_2512.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2514

            return self._parent._cast(_2514.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.BevelGearSet)

        @property
        def concept_gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.ConceptGearSet)

        @property
        def conical_gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.ConicalGearSet)

        @property
        def cylindrical_gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.CylindricalGearSet)

        @property
        def face_gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.FaceGearSet)

        @property
        def gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.GearSet)

        @property
        def hypoid_gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.PlanetaryGearSet)

        @property
        def spiral_bevel_gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.StraightBevelGearSet)

        @property
        def worm_gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.WormGearSet)

        @property
        def zerol_bevel_gear_set(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.cycloidal import _2566

            return self._parent._cast(_2566.CycloidalAssembly)

        @property
        def belt_drive(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.couplings import _2574

            return self._parent._cast(_2574.BeltDrive)

        @property
        def clutch(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.couplings import _2576

            return self._parent._cast(_2576.Clutch)

        @property
        def concept_coupling(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.couplings import _2579

            return self._parent._cast(_2579.ConceptCoupling)

        @property
        def coupling(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.couplings import _2581

            return self._parent._cast(_2581.Coupling)

        @property
        def cvt(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.couplings import _2584

            return self._parent._cast(_2584.CVT)

        @property
        def part_to_part_shear_coupling(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ):
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.PartToPartShearCoupling)

        @property
        def rolling_ring_assembly(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.couplings import _2595

            return self._parent._cast(_2595.RollingRingAssembly)

        @property
        def spring_damper(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.SpringDamper)

        @property
        def synchroniser(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.couplings import _2600

            return self._parent._cast(_2600.Synchroniser)

        @property
        def torque_converter(self: "AbstractAssembly._Cast_AbstractAssembly"):
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.TorqueConverter)

        @property
        def abstract_assembly(
            self: "AbstractAssembly._Cast_AbstractAssembly",
        ) -> "AbstractAssembly":
            return self._parent

        def __getattr__(self: "AbstractAssembly._Cast_AbstractAssembly", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssembly.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass_of_assembly(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassOfAssembly

        if temp is None:
            return 0.0

        return temp

    @property
    def components_with_unknown_mass_properties(self: Self) -> "List[_2442.Component]":
        """List[mastapy.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithUnknownMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def components_with_zero_mass_properties(self: Self) -> "List[_2442.Component]":
        """List[mastapy.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithZeroMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "AbstractAssembly._Cast_AbstractAssembly":
        return self._Cast_AbstractAssembly(self)
