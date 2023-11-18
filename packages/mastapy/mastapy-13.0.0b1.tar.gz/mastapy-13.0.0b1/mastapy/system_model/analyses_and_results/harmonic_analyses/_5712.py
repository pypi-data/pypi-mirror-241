"""ConnectionHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5758
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6067,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2725


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConnectionHarmonicAnalysis")


class ConnectionHarmonicAnalysis(_7538.ConnectionStaticLoadAnalysisCase):
    """ConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionHarmonicAnalysis")

    class _Cast_ConnectionHarmonicAnalysis:
        """Special nested class for casting ConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
            parent: "ConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5679,
            )

            return self._parent._cast(
                _5679.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5681,
            )

            return self._parent._cast(_5681.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def belt_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5685,
            )

            return self._parent._cast(_5685.BeltConnectionHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5688,
            )

            return self._parent._cast(_5688.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.BevelGearMeshHarmonicAnalysis)

        @property
        def clutch_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5697,
            )

            return self._parent._cast(_5697.ClutchConnectionHarmonicAnalysis)

        @property
        def coaxial_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.CoaxialConnectionHarmonicAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.ConceptCouplingConnectionHarmonicAnalysis)

        @property
        def concept_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.ConceptGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ConicalGearMeshHarmonicAnalysis)

        @property
        def coupling_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.CouplingConnectionHarmonicAnalysis)

        @property
        def cvt_belt_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.CVTBeltConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(
                _5721.CycloidalDiscCentralBearingConnectionHarmonicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(
                _5723.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5725,
            )

            return self._parent._cast(_5725.CylindricalGearMeshHarmonicAnalysis)

        @property
        def face_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5745,
            )

            return self._parent._cast(_5745.FaceGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5752,
            )

            return self._parent._cast(_5752.GearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5769,
            )

            return self._parent._cast(_5769.HypoidGearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(
                _5771.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(
                _5773.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(
                _5776.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(
                _5779.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(
                _5786.PartToPartShearCouplingConnectionHarmonicAnalysis
            )

        @property
        def planetary_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(_5790.PlanetaryConnectionHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(_5798.RingPinsToDiscConnectionHarmonicAnalysis)

        @property
        def rolling_ring_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.RollingRingConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(
                _5805.ShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def spring_damper_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.SpringDamperConnectionHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.TorqueConverterConnectionHarmonicAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.WormGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def connection_harmonic_analysis(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
        ) -> "ConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2270.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2270.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis(self: Self) -> "_5758.HarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analyses_of_single_excitations(
        self: Self,
    ) -> "List[_6067.HarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysesOfSingleExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2725.ConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection

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
    ) -> "ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis":
        return self._Cast_ConnectionHarmonicAnalysis(self)
