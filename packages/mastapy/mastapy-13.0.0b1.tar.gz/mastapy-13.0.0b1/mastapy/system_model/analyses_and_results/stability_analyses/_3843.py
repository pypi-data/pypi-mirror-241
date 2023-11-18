"""PartToPartShearCouplingConnectionStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3798
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PartToPartShearCouplingConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346
    from mastapy.system_model.analyses_and_results.static_loads import _6927


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionStabilityAnalysis")


class PartToPartShearCouplingConnectionStabilityAnalysis(
    _3798.CouplingConnectionStabilityAnalysis
):
    """PartToPartShearCouplingConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingConnectionStabilityAnalysis"
    )

    class _Cast_PartToPartShearCouplingConnectionStabilityAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
            parent: "PartToPartShearCouplingConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_stability_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ):
            return self._parent._cast(_3798.CouplingConnectionStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(
                _3828.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ) -> "PartToPartShearCouplingConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2346.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6927.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis":
        return self._Cast_PartToPartShearCouplingConnectionStabilityAnalysis(self)
