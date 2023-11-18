"""FaceGearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4092
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "FaceGearSetPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.static_loads import _6884
    from mastapy.gears.rating.face import _448
    from mastapy.system_model.analyses_and_results.power_flows import _4085, _4084


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetPowerFlow",)


Self = TypeVar("Self", bound="FaceGearSetPowerFlow")


class FaceGearSetPowerFlow(_4092.GearSetPowerFlow):
    """FaceGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetPowerFlow")

    class _Cast_FaceGearSetPowerFlow:
        """Special nested class for casting FaceGearSetPowerFlow to subclasses."""

        def __init__(
            self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow",
            parent: "FaceGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_set_power_flow(
            self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow",
        ):
            return self._parent._cast(_4092.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def face_gear_set_power_flow(
            self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow",
        ) -> "FaceGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2527.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6884.FaceGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_448.FaceGearSetRating":
        """mastapy.gears.rating.face.FaceGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_448.FaceGearSetRating":
        """mastapy.gears.rating.face.FaceGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4085.FaceGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.FaceGearPowerFlow]

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
    def face_gears_power_flow(self: Self) -> "List[_4085.FaceGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.FaceGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(self: Self) -> "List[_4084.FaceGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.FaceGearMeshPowerFlow]

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

    @property
    def face_meshes_power_flow(self: Self) -> "List[_4084.FaceGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.FaceGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FaceGearSetPowerFlow._Cast_FaceGearSetPowerFlow":
        return self._Cast_FaceGearSetPowerFlow(self)
