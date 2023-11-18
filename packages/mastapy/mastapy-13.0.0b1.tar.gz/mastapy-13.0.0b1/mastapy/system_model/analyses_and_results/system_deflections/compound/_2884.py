"""ConnectionCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7536
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2725


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ConnectionCompoundSystemDeflection")


class ConnectionCompoundSystemDeflection(_7536.ConnectionCompoundAnalysis):
    """ConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCompoundSystemDeflection")

    class _Cast_ConnectionCompoundSystemDeflection:
        """Special nested class for casting ConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
            parent: "ConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2852,
            )

            return self._parent._cast(
                _2852.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2854,
            )

            return self._parent._cast(
                _2854.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def belt_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2858,
            )

            return self._parent._cast(_2858.BeltConnectionCompoundSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2861,
            )

            return self._parent._cast(
                _2861.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2866,
            )

            return self._parent._cast(_2866.BevelGearMeshCompoundSystemDeflection)

        @property
        def clutch_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2871,
            )

            return self._parent._cast(_2871.ClutchConnectionCompoundSystemDeflection)

        @property
        def coaxial_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.CoaxialConnectionCompoundSystemDeflection)

        @property
        def concept_coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(
                _2876.ConceptCouplingConnectionCompoundSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(_2879.ConceptGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ConicalGearMeshCompoundSystemDeflection)

        @property
        def coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(_2887.CouplingConnectionCompoundSystemDeflection)

        @property
        def cvt_belt_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.CVTBeltConnectionCompoundSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(
                _2893.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(
                _2895.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.CylindricalGearMeshCompoundSystemDeflection)

        @property
        def face_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.FaceGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.GearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.HypoidGearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(
                _2915.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(
                _2917.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(
                _2920.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(
                _2923.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(
                _2931.PartToPartShearCouplingConnectionCompoundSystemDeflection
            )

        @property
        def planetary_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.PlanetaryConnectionCompoundSystemDeflection)

        @property
        def ring_pins_to_disc_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(
                _2940.RingPinsToDiscConnectionCompoundSystemDeflection
            )

        @property
        def rolling_ring_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(
                _2943.RollingRingConnectionCompoundSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(
                _2948.ShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def spring_damper_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(
                _2954.SpringDamperConnectionCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(
                _2957.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(
                _2960.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def torque_converter_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(
                _2969.TorqueConverterConnectionCompoundSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.WormGearMeshCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ) -> "ConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ConnectionCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2725.ConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection]

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
    ) -> "List[_2725.ConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection]

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
    ) -> "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection":
        return self._Cast_ConnectionCompoundSystemDeflection(self)
