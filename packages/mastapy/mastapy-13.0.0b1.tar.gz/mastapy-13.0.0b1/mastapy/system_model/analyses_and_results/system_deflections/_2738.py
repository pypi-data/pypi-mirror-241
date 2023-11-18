"""CylindricalGearMeshSystemDeflectionTimestep"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2737
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION_TIMESTEP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalGearMeshSystemDeflectionTimestep",
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _856


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshSystemDeflectionTimestep",)


Self = TypeVar("Self", bound="CylindricalGearMeshSystemDeflectionTimestep")


class CylindricalGearMeshSystemDeflectionTimestep(
    _2737.CylindricalGearMeshSystemDeflection
):
    """CylindricalGearMeshSystemDeflectionTimestep

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION_TIMESTEP
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshSystemDeflectionTimestep"
    )

    class _Cast_CylindricalGearMeshSystemDeflectionTimestep:
        """Special nested class for casting CylindricalGearMeshSystemDeflectionTimestep to subclasses."""

        def __init__(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
            parent: "CylindricalGearMeshSystemDeflectionTimestep",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ):
            return self._parent._cast(_2737.CylindricalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(
                _2765.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
        ) -> "CylindricalGearMeshSystemDeflectionTimestep":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshSystemDeflectionTimestep.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_contact_lines(
        self: Self,
    ) -> "List[_856.CylindricalGearMeshLoadedContactLine]":
        """List[mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactLine]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedContactLines

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshSystemDeflectionTimestep._Cast_CylindricalGearMeshSystemDeflectionTimestep":
        return self._Cast_CylindricalGearMeshSystemDeflectionTimestep(self)
