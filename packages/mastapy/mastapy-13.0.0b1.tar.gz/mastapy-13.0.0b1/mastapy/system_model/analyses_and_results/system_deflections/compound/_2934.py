"""PlanetaryGearSetCompoundSystemDeflection"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.system_deflections.compound import _2898
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "PlanetaryGearSetCompoundSystemDeflection",
)


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundSystemDeflection",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundSystemDeflection")


class PlanetaryGearSetCompoundSystemDeflection(
    _2898.CylindricalGearSetCompoundSystemDeflection
):
    """PlanetaryGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundSystemDeflection"
    )

    class _Cast_PlanetaryGearSetCompoundSystemDeflection:
        """Special nested class for casting PlanetaryGearSetCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
            parent: "PlanetaryGearSetCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ):
            return self._parent._cast(_2898.CylindricalGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2849,
            )

            return self._parent._cast(_2849.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
        ) -> "PlanetaryGearSetCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundSystemDeflection._Cast_PlanetaryGearSetCompoundSystemDeflection":
        return self._Cast_PlanetaryGearSetCompoundSystemDeflection(self)
