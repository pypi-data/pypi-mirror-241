"""CylindricalGearCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6463
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CylindricalGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearCompoundDynamicAnalysis")


class CylindricalGearCompoundDynamicAnalysis(_6463.GearCompoundDynamicAnalysis):
    """CylindricalGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearCompoundDynamicAnalysis"
    )

    class _Cast_CylindricalGearCompoundDynamicAnalysis:
        """Special nested class for casting CylindricalGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis",
            parent: "CylindricalGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_dynamic_analysis(
            self: "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6463.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6455,
            )

            return self._parent._cast(
                _6455.CylindricalPlanetGearCompoundDynamicAnalysis
            )

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis",
        ) -> "CylindricalGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2523.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6321.CylindricalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[CylindricalGearCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.CylindricalGearCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6321.CylindricalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearCompoundDynamicAnalysis._Cast_CylindricalGearCompoundDynamicAnalysis":
        return self._Cast_CylindricalGearCompoundDynamicAnalysis(self)
