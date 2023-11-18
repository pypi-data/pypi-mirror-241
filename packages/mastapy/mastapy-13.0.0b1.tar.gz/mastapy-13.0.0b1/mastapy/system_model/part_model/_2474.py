"""SpecialisedAssembly"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model import _2432
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "SpecialisedAssembly"
)


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssembly",)


Self = TypeVar("Self", bound="SpecialisedAssembly")


class SpecialisedAssembly(_2432.AbstractAssembly):
    """SpecialisedAssembly

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssembly")

    class _Cast_SpecialisedAssembly:
        """Special nested class for casting SpecialisedAssembly to subclasses."""

        def __init__(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
            parent: "SpecialisedAssembly",
        ):
            self._parent = parent

        @property
        def abstract_assembly(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            return self._parent._cast(_2432.AbstractAssembly)

        @property
        def part(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.Part)

        @property
        def design_entity(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def bolted_joint(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.BoltedJoint)

        @property
        def flexible_pin_assembly(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ):
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.FlexiblePinAssembly)

        @property
        def agma_gleason_conical_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2512

            return self._parent._cast(_2512.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2514

            return self._parent._cast(_2514.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.BevelGearSet)

        @property
        def concept_gear_set(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.ConceptGearSet)

        @property
        def conical_gear_set(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.ConicalGearSet)

        @property
        def cylindrical_gear_set(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.CylindricalGearSet)

        @property
        def face_gear_set(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.FaceGearSet)

        @property
        def gear_set(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.GearSet)

        @property
        def hypoid_gear_set(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.PlanetaryGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ):
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.StraightBevelGearSet)

        @property
        def worm_gear_set(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.WormGearSet)

        @property
        def zerol_bevel_gear_set(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.cycloidal import _2566

            return self._parent._cast(_2566.CycloidalAssembly)

        @property
        def belt_drive(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.couplings import _2574

            return self._parent._cast(_2574.BeltDrive)

        @property
        def clutch(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.couplings import _2576

            return self._parent._cast(_2576.Clutch)

        @property
        def concept_coupling(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.couplings import _2579

            return self._parent._cast(_2579.ConceptCoupling)

        @property
        def coupling(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.couplings import _2581

            return self._parent._cast(_2581.Coupling)

        @property
        def cvt(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.couplings import _2584

            return self._parent._cast(_2584.CVT)

        @property
        def part_to_part_shear_coupling(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ):
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.PartToPartShearCoupling)

        @property
        def rolling_ring_assembly(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ):
            from mastapy.system_model.part_model.couplings import _2595

            return self._parent._cast(_2595.RollingRingAssembly)

        @property
        def spring_damper(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.SpringDamper)

        @property
        def synchroniser(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.couplings import _2600

            return self._parent._cast(_2600.Synchroniser)

        @property
        def torque_converter(self: "SpecialisedAssembly._Cast_SpecialisedAssembly"):
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.TorqueConverter)

        @property
        def specialised_assembly(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly",
        ) -> "SpecialisedAssembly":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssembly._Cast_SpecialisedAssembly", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecialisedAssembly.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SpecialisedAssembly._Cast_SpecialisedAssembly":
        return self._Cast_SpecialisedAssembly(self)
