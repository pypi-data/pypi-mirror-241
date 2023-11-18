"""InterMountableComponentConnectionCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7438,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7337,
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundAdvancedSystemDeflection"
)


class InterMountableComponentConnectionCompoundAdvancedSystemDeflection(
    _7438.ConnectionCompoundAdvancedSystemDeflection
):
    """InterMountableComponentConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting InterMountableComponentConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
            parent: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7438.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7408,
            )

            return self._parent._cast(
                _7408.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def belt_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7412,
            )

            return self._parent._cast(
                _7412.BeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7415,
            )

            return self._parent._cast(
                _7415.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7420,
            )

            return self._parent._cast(
                _7420.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def clutch_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7425,
            )

            return self._parent._cast(
                _7425.ClutchConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7430,
            )

            return self._parent._cast(
                _7430.ConceptCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(
                _7433.ConceptGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(
                _7441.CouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_belt_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(
                _7443.CVTBeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(
                _7451.CylindricalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(
                _7457.FaceGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7462,
            )

            return self._parent._cast(_7462.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(
                _7466.HypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(
                _7470.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(
                _7473.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(
                _7476.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(
                _7484.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(
                _7493.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(
                _7496.RollingRingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(
                _7503.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpringDamperConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.TorqueConverterConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(
                _7527.WormGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7337.InterMountableComponentConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.InterMountableComponentConnectionAdvancedSystemDeflection]

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
    ) -> "List[_7337.InterMountableComponentConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.InterMountableComponentConnectionAdvancedSystemDeflection]

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
    ) -> "InterMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_InterMountableComponentConnectionCompoundAdvancedSystemDeflection(
            self
        )
