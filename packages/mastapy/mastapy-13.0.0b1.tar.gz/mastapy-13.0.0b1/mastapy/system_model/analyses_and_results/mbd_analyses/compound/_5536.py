"""BeltDriveCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5624
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "BeltDriveCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2574
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5385


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BeltDriveCompoundMultibodyDynamicsAnalysis")


class BeltDriveCompoundMultibodyDynamicsAnalysis(
    _5624.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
):
    """BeltDriveCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_BeltDriveCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BeltDriveCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BeltDriveCompoundMultibodyDynamicsAnalysis._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis",
            parent: "BeltDriveCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "BeltDriveCompoundMultibodyDynamicsAnalysis._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5624.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "BeltDriveCompoundMultibodyDynamicsAnalysis._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5526,
            )

            return self._parent._cast(
                _5526.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "BeltDriveCompoundMultibodyDynamicsAnalysis._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(_5605.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "BeltDriveCompoundMultibodyDynamicsAnalysis._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltDriveCompoundMultibodyDynamicsAnalysis._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveCompoundMultibodyDynamicsAnalysis._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "BeltDriveCompoundMultibodyDynamicsAnalysis._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(_5567.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "BeltDriveCompoundMultibodyDynamicsAnalysis._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis",
        ) -> "BeltDriveCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltDriveCompoundMultibodyDynamicsAnalysis._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BeltDriveCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2574.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2574.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

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
    ) -> "List[_5385.BeltDriveMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BeltDriveMultibodyDynamicsAnalysis]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5385.BeltDriveMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BeltDriveMultibodyDynamicsAnalysis]

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
    ) -> "BeltDriveCompoundMultibodyDynamicsAnalysis._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis":
        return self._Cast_BeltDriveCompoundMultibodyDynamicsAnalysis(self)
