"""KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5455
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5598,
        _5599,
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis(
    _5594.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5594.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(_5586.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(
                _5624.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5526,
            )

            return self._parent._cast(
                _5526.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(_5605.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis.TYPE",
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
    ) -> "List[_5455.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis]

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
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5598.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundMultibodyDynamicsAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5599.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundMultibodyDynamicsAnalysis
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
    ) -> "List[_5455.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis]

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis(
            self
        )
