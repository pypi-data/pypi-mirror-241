"""CouplingConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4920,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CouplingConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2344


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CouplingConnectionModalAnalysisAtAStiffness")


class CouplingConnectionModalAnalysisAtAStiffness(
    _4920.InterMountableComponentConnectionModalAnalysisAtAStiffness
):
    """CouplingConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_CouplingConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
            parent: "CouplingConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4920.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(_4889.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_connection_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4875,
            )

            return self._parent._cast(_4875.ClutchConnectionModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(
                _4880.ConceptCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(
                _4936.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4958,
            )

            return self._parent._cast(
                _4958.SpringDamperConnectionModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4973,
            )

            return self._parent._cast(
                _4973.TorqueConverterConnectionModalAnalysisAtAStiffness
            )

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
        ) -> "CouplingConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CouplingConnectionModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2344.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness":
        return self._Cast_CouplingConnectionModalAnalysisAtAStiffness(self)
