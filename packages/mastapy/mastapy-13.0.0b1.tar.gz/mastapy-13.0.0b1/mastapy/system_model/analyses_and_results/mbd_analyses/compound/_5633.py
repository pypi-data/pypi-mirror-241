"""StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5495
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5631,
        _5632,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis"
)


class StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis(
    _5544.BevelGearSetCompoundMultibodyDynamicsAnalysis
):
    """StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
            parent: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5544.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5532,
            )

            return self._parent._cast(
                _5532.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(_5586.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(
                _5624.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5526,
            )

            return self._parent._cast(
                _5526.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(_5605.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2544.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2544.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

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
    ) -> "List[_5495.StraightBevelDiffGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearSetMultibodyDynamicsAnalysis]

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
    def straight_bevel_diff_gears_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5631.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5632.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesCompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5495.StraightBevelDiffGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearSetMultibodyDynamicsAnalysis]

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
    ) -> "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis(
            self
        )
