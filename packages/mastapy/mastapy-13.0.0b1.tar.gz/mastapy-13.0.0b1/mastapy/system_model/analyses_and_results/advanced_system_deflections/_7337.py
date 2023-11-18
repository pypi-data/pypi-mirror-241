"""InterMountableComponentConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "InterMountableComponentConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionAdvancedSystemDeflection"
)


class InterMountableComponentConnectionAdvancedSystemDeflection(
    _7305.ConnectionAdvancedSystemDeflection
):
    """InterMountableComponentConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
    )

    class _Cast_InterMountableComponentConnectionAdvancedSystemDeflection:
        """Special nested class for casting InterMountableComponentConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
            parent: "InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7305.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7275,
            )

            return self._parent._cast(
                _7275.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def belt_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7279,
            )

            return self._parent._cast(_7279.BeltConnectionAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7282,
            )

            return self._parent._cast(
                _7282.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(_7287.BevelGearMeshAdvancedSystemDeflection)

        @property
        def clutch_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(_7292.ClutchConnectionAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(
                _7297.ConceptCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.ConceptGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(_7309.CouplingConnectionAdvancedSystemDeflection)

        @property
        def cvt_belt_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.CVTBeltConnectionAdvancedSystemDeflection)

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.CylindricalGearMeshAdvancedSystemDeflection)

        @property
        def face_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7326,
            )

            return self._parent._cast(_7326.FaceGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.GearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(
                _7339.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(
                _7342.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7345,
            )

            return self._parent._cast(
                _7345.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(
                _7354.PartToPartShearCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(
                _7363.RingPinsToDiscConnectionAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(
                _7366.RollingRingConnectionAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(_7373.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def spring_damper_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(
                _7376.SpringDamperConnectionAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(
                _7379.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(
                _7391.TorqueConverterConnectionAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.WormGearMeshAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "InterMountableComponentConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "InterMountableComponentConnectionAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2279.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

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
    ) -> "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection":
        return self._Cast_InterMountableComponentConnectionAdvancedSystemDeflection(
            self
        )
