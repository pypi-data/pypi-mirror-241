"""ConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7536
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ConnectionCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5149,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConnectionCompoundModalAnalysisAtASpeed")


class ConnectionCompoundModalAnalysisAtASpeed(_7536.ConnectionCompoundAnalysis):
    """ConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionCompoundModalAnalysisAtASpeed"
    )

    class _Cast_ConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
            parent: "ConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5247,
            )

            return self._parent._cast(
                _5247.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5253,
            )

            return self._parent._cast(_5253.BeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(
                _5256.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5261,
            )

            return self._parent._cast(_5261.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def clutch_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5266,
            )

            return self._parent._cast(
                _5266.ClutchConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(
                _5268.CoaxialConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(
                _5271.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(
                _5274.ConceptGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(
                _5277.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(
                _5282.CouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(
                _5284.CVTBeltConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(
                _5288.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(
                _5290.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(
                _5292.CylindricalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(_5298.FaceGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(
                _5309.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(
                _5311.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(
                _5325.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.PlanetaryConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(
                _5334.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5337,
            )

            return self._parent._cast(
                _5337.RollingRingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(
                _5341.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(
                _5344.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpringDamperConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(
                _5362.TorqueConverterConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(_5368.WormGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
        ) -> "ConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "ConnectionCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5149.ConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5149.ConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConnectionModalAnalysisAtASpeed]

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
    ) -> "ConnectionCompoundModalAnalysisAtASpeed._Cast_ConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_ConnectionCompoundModalAnalysisAtASpeed(self)
