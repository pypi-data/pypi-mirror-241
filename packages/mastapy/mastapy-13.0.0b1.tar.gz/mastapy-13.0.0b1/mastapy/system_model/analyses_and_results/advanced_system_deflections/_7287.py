"""BevelGearMeshAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7275
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "BevelGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2301


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearMeshAdvancedSystemDeflection")


class BevelGearMeshAdvancedSystemDeflection(
    _7275.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
):
    """BevelGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshAdvancedSystemDeflection"
    )

    class _Cast_BevelGearMeshAdvancedSystemDeflection:
        """Special nested class for casting BevelGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
            parent: "BevelGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7275.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(
                _7337.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7282,
            )

            return self._parent._cast(
                _7282.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(_7373.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(
                _7379.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
        ) -> "BevelGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelGearMeshAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2301.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

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
    ) -> "BevelGearMeshAdvancedSystemDeflection._Cast_BevelGearMeshAdvancedSystemDeflection":
        return self._Cast_BevelGearMeshAdvancedSystemDeflection(self)
