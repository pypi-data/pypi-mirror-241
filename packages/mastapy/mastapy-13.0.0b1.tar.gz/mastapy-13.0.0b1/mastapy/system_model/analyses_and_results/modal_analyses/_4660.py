"""PartToPartShearCouplingConnectionModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4607
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "PartToPartShearCouplingConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346
    from mastapy.system_model.analyses_and_results.static_loads import _6927
    from mastapy.system_model.analyses_and_results.system_deflections import _2784


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionModalAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionModalAnalysis")


class PartToPartShearCouplingConnectionModalAnalysis(
    _4607.CouplingConnectionModalAnalysis
):
    """PartToPartShearCouplingConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingConnectionModalAnalysis"
    )

    class _Cast_PartToPartShearCouplingConnectionModalAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
            parent: "PartToPartShearCouplingConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ):
            return self._parent._cast(_4607.CouplingConnectionModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(
                _4639.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ) -> "PartToPartShearCouplingConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionModalAnalysis.TYPE",
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
    def system_deflection_results(
        self: Self,
    ) -> "_2784.PartToPartShearCouplingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis":
        return self._Cast_PartToPartShearCouplingConnectionModalAnalysis(self)
