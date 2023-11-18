"""FlexiblePinAssemblyMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5486
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "FlexiblePinAssemblyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.static_loads import _6886


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyMultibodyDynamicsAnalysis")


class FlexiblePinAssemblyMultibodyDynamicsAnalysis(
    _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
):
    """FlexiblePinAssemblyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis"
    )

    class _Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis:
        """Special nested class for casting FlexiblePinAssemblyMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis",
            parent: "FlexiblePinAssemblyMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5373

            return self._parent._cast(_5373.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis",
        ) -> "FlexiblePinAssemblyMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "FlexiblePinAssemblyMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2452.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6886.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyMultibodyDynamicsAnalysis._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis":
        return self._Cast_FlexiblePinAssemblyMultibodyDynamicsAnalysis(self)
