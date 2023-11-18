"""CylindricalGearSystemDeflectionTimestep"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.system_deflections import _2743
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SYSTEM_DEFLECTION_TIMESTEP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalGearSystemDeflectionTimestep",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSystemDeflectionTimestep",)


Self = TypeVar("Self", bound="CylindricalGearSystemDeflectionTimestep")


class CylindricalGearSystemDeflectionTimestep(_2743.CylindricalGearSystemDeflection):
    """CylindricalGearSystemDeflectionTimestep

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SYSTEM_DEFLECTION_TIMESTEP
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSystemDeflectionTimestep"
    )

    class _Cast_CylindricalGearSystemDeflectionTimestep:
        """Special nested class for casting CylindricalGearSystemDeflectionTimestep to subclasses."""

        def __init__(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
            parent: "CylindricalGearSystemDeflectionTimestep",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_system_deflection(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ):
            return self._parent._cast(_2743.CylindricalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "CylindricalGearSystemDeflectionTimestep":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
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
        self: Self, instance_to_wrap: "CylindricalGearSystemDeflectionTimestep.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep":
        return self._Cast_CylindricalGearSystemDeflectionTimestep(self)
