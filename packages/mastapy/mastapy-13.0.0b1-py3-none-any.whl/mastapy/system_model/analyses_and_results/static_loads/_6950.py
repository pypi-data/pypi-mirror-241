"""SpecialisedAssemblyLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6804
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpecialisedAssemblyLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyLoadCase",)


Self = TypeVar("Self", bound="SpecialisedAssemblyLoadCase")


class SpecialisedAssemblyLoadCase(_6804.AbstractAssemblyLoadCase):
    """SpecialisedAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyLoadCase")

    class _Cast_SpecialisedAssemblyLoadCase:
        """Special nested class for casting SpecialisedAssemblyLoadCase to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
            parent: "SpecialisedAssemblyLoadCase",
        ):
            self._parent = parent

        @property
        def abstract_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            return self._parent._cast(_6804.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6813

            return self._parent._cast(_6813.AGMAGleasonConicalGearSetLoadCase)

        @property
        def belt_drive_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6819

            return self._parent._cast(_6819.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.BoltedJointLoadCase)

        @property
        def clutch_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6832

            return self._parent._cast(_6832.ClutchLoadCase)

        @property
        def concept_coupling_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.ConceptCouplingLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.ConceptGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ConicalGearSetLoadCase)

        @property
        def coupling_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.CouplingLoadCase)

        @property
        def cvt_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.CVTLoadCase)

        @property
        def cycloidal_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.CycloidalAssemblyLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6863

            return self._parent._cast(_6863.CylindricalGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6884

            return self._parent._cast(_6884.FaceGearSetLoadCase)

        @property
        def flexible_pin_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6886

            return self._parent._cast(_6886.FlexiblePinAssemblyLoadCase)

        @property
        def gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.GearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6905

            return self._parent._cast(_6905.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(
                _6912.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(
                _6915.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6918

            return self._parent._cast(
                _6918.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def part_to_part_shear_coupling_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PlanetaryGearSetLoadCase)

        @property
        def rolling_ring_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6943

            return self._parent._cast(_6943.RollingRingAssemblyLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.StraightBevelGearSetLoadCase)

        @property
        def synchroniser_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.SynchroniserLoadCase)

        @property
        def torque_converter_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.TorqueConverterLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.ZerolBevelGearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
        ) -> "SpecialisedAssemblyLoadCase":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecialisedAssemblyLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2474.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase":
        return self._Cast_SpecialisedAssemblyLoadCase(self)
