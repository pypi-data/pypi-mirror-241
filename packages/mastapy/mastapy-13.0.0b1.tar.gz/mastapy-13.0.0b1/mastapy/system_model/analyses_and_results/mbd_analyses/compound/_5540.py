"""BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
        "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5389


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis"
)


class BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis(
    _5537.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
):
    """BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
            parent: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5537.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(_5542.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5530,
            )

            return self._parent._cast(
                _5530.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5558,
            )

            return self._parent._cast(
                _5558.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(_5584.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(
                _5603.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(_5551.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(_5605.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
        ) -> "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5389.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5389.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis]

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
    ) -> "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis(
            self
        )
