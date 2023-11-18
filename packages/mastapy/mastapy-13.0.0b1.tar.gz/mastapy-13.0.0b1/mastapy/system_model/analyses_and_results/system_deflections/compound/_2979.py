"""ZerolBevelGearSetCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2867
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ZerolBevelGearSetCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.system_deflections import _2838
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2977,
        _2978,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearSetCompoundSystemDeflection")


class ZerolBevelGearSetCompoundSystemDeflection(
    _2867.BevelGearSetCompoundSystemDeflection
):
    """ZerolBevelGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetCompoundSystemDeflection"
    )

    class _Cast_ZerolBevelGearSetCompoundSystemDeflection:
        """Special nested class for casting ZerolBevelGearSetCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
            parent: "ZerolBevelGearSetCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
        ):
            return self._parent._cast(_2867.BevelGearSetCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2855,
            )

            return self._parent._cast(
                _2855.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def conical_gear_set_compound_system_deflection(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(_2883.ConicalGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2849,
            )

            return self._parent._cast(_2849.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
        ) -> "ZerolBevelGearSetCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ZerolBevelGearSetCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2552.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2552.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2838.ZerolBevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gears_compound_system_deflection(
        self: Self,
    ) -> "List[_2977.ZerolBevelGearCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ZerolBevelGearCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_compound_system_deflection(
        self: Self,
    ) -> "List[_2978.ZerolBevelGearMeshCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ZerolBevelGearMeshCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2838.ZerolBevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetCompoundSystemDeflection._Cast_ZerolBevelGearSetCompoundSystemDeflection":
        return self._Cast_ZerolBevelGearSetCompoundSystemDeflection(self)
