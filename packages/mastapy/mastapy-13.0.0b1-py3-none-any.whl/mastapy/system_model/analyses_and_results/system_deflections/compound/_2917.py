"""KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2882
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2766


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection"
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection(
    _2882.ConicalGearMeshCompoundSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
        ):
            return self._parent._cast(_2882.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(
                _2915.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(
                _2920.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(
                _2923.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2766.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection]

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
    ) -> "List[_2766.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection]

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection(
                self
            )
        )
