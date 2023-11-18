"""ConicalGearMeshCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5303,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ConicalGearMeshCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5146,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundModalAnalysisAtASpeed")


class ConicalGearMeshCompoundModalAnalysisAtASpeed(
    _5303.GearMeshCompoundModalAnalysisAtASpeed
):
    """ConicalGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed"
    )

    class _Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ConicalGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
            parent: "ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5303.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(
                _5309.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5279,
            )

            return self._parent._cast(_5279.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(
                _5256.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5261,
            )

            return self._parent._cast(_5261.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(
                _5311.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(
                _5344.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "ConicalGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "ConicalGearMeshCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.ConicalGearMeshCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5146.ConicalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConicalGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5146.ConicalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConicalGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshCompoundModalAnalysisAtASpeed._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_ConicalGearMeshCompoundModalAnalysisAtASpeed(self)
