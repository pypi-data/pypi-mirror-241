"""ExternalCADModelMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5401
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ExternalCADModelMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450
    from mastapy.system_model.analyses_and_results.static_loads import _6881


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ExternalCADModelMultibodyDynamicsAnalysis")


class ExternalCADModelMultibodyDynamicsAnalysis(
    _5401.ComponentMultibodyDynamicsAnalysis
):
    """ExternalCADModelMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelMultibodyDynamicsAnalysis"
    )

    class _Cast_ExternalCADModelMultibodyDynamicsAnalysis:
        """Special nested class for casting ExternalCADModelMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
            parent: "ExternalCADModelMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_multibody_dynamics_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5401.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ) -> "ExternalCADModelMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ExternalCADModelMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2450.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6881.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis":
        return self._Cast_ExternalCADModelMultibodyDynamicsAnalysis(self)
