"""KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4232
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.power_flows import _4106
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4236,
        _4237,
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow(
    _4232.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
        ):
            return self._parent._cast(
                _4232.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def conical_gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4164,
            )

            return self._parent._cast(_4164.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(
        self: Self,
    ) -> "_2539.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(
        self: Self,
    ) -> "_2539.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4106.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_power_flow(
        self: Self,
    ) -> "List[_4236.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_power_flow(
        self: Self,
    ) -> "List[_4237.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4106.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow(
            self
        )
