"""KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3963
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.stability_analyses import _3836
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3967,
        _3968,
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis(
    _3963.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
        ):
            return self._parent._cast(
                _3963.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(_3929.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(_3955.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(
                _3993.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3895,
            )

            return self._parent._cast(_3895.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis.TYPE",
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
    ) -> "List[_3836.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis]

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
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_stability_analysis(
        self: Self,
    ) -> "List[_3967.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundStabilityAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_stability_analysis(
        self: Self,
    ) -> "List[_3968.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundStabilityAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3836.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis]

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis(
            self
        )
