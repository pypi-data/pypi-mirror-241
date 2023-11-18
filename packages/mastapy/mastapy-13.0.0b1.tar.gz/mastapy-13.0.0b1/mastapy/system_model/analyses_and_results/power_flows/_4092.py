"""GearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4132
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "GearSetPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.gears.rating import _361
    from mastapy.system_model.analyses_and_results.power_flows import _4091, _4090


__docformat__ = "restructuredtext en"
__all__ = ("GearSetPowerFlow",)


Self = TypeVar("Self", bound="GearSetPowerFlow")


class GearSetPowerFlow(_4132.SpecialisedAssemblyPowerFlow):
    """GearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetPowerFlow")

    class _Cast_GearSetPowerFlow:
        """Special nested class for casting GearSetPowerFlow to subclasses."""

        def __init__(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow", parent: "GearSetPowerFlow"
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            return self._parent._cast(_4132.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(self: "GearSetPowerFlow._Cast_GearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "GearSetPowerFlow._Cast_GearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "GearSetPowerFlow._Cast_GearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "GearSetPowerFlow._Cast_GearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4036

            return self._parent._cast(_4036.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4043

            return self._parent._cast(_4043.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(self: "GearSetPowerFlow._Cast_GearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4048

            return self._parent._cast(_4048.BevelGearSetPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.ConceptGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConicalGearSetPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.CylindricalGearSetPowerFlow)

        @property
        def face_gear_set_power_flow(self: "GearSetPowerFlow._Cast_GearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.FaceGearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(self: "GearSetPowerFlow._Cast_GearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4100

            return self._parent._cast(
                _4100.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(
                _4103.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(
                _4106.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def planetary_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PlanetaryGearSetPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.SpiralBevelGearSetPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelGearSetPowerFlow)

        @property
        def worm_gear_set_power_flow(self: "GearSetPowerFlow._Cast_GearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4163

            return self._parent._cast(_4163.ZerolBevelGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "GearSetPowerFlow":
            return self._parent

        def __getattr__(self: "GearSetPowerFlow._Cast_GearSetPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2530.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_361.GearSetRating":
        """mastapy.gears.rating.GearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4091.GearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(self: Self) -> "List[_4090.GearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def set_face_widths_for_specified_safety_factors(self: Self):
        """Method does not return."""
        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors()

    @property
    def cast_to(self: Self) -> "GearSetPowerFlow._Cast_GearSetPowerFlow":
        return self._Cast_GearSetPowerFlow(self)
