"""CouplingHalfCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5603
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CouplingHalfCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5414


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundMultibodyDynamicsAnalysis")


class CouplingHalfCompoundMultibodyDynamicsAnalysis(
    _5603.MountableComponentCompoundMultibodyDynamicsAnalysis
):
    """CouplingHalfCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingHalfCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
            parent: "CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5603.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(_5551.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(_5605.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5549,
            )

            return self._parent._cast(_5549.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(
                _5554.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(_5568.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(
                _5608.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5614,
            )

            return self._parent._cast(_5614.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5618,
            )

            return self._parent._cast(
                _5618.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5640,
            )

            return self._parent._cast(
                _5640.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5646,
            )

            return self._parent._cast(
                _5646.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "CouplingHalfCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CouplingHalfCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5414.CouplingHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CouplingHalfMultibodyDynamicsAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5414.CouplingHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CouplingHalfMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundMultibodyDynamicsAnalysis._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CouplingHalfCompoundMultibodyDynamicsAnalysis(self)
