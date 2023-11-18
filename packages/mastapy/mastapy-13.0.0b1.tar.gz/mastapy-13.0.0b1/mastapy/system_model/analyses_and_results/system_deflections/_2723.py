"""ConicalGearSetSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2758
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConicalGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.power_flows import _4064


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearSetSystemDeflection")


class ConicalGearSetSystemDeflection(_2758.GearSetSystemDeflection):
    """ConicalGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetSystemDeflection")

    class _Cast_ConicalGearSetSystemDeflection:
        """Special nested class for casting ConicalGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
            parent: "ConicalGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            return self._parent._cast(_2758.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2683,
            )

            return self._parent._cast(_2683.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelGearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpiralBevelGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.ZerolBevelGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
        ) -> "ConicalGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2522.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4064.ConicalGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConicalGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetSystemDeflection._Cast_ConicalGearSetSystemDeflection":
        return self._Cast_ConicalGearSetSystemDeflection(self)
