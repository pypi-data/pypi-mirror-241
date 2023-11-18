"""BoltedJointCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7501,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BoltedJointCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7290,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BoltedJointCompoundAdvancedSystemDeflection")


class BoltedJointCompoundAdvancedSystemDeflection(
    _7501.SpecialisedAssemblyCompoundAdvancedSystemDeflection
):
    """BoltedJointCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BoltedJointCompoundAdvancedSystemDeflection"
    )

    class _Cast_BoltedJointCompoundAdvancedSystemDeflection:
        """Special nested class for casting BoltedJointCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BoltedJointCompoundAdvancedSystemDeflection._Cast_BoltedJointCompoundAdvancedSystemDeflection",
            parent: "BoltedJointCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "BoltedJointCompoundAdvancedSystemDeflection._Cast_BoltedJointCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7501.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "BoltedJointCompoundAdvancedSystemDeflection._Cast_BoltedJointCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7403,
            )

            return self._parent._cast(
                _7403.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "BoltedJointCompoundAdvancedSystemDeflection._Cast_BoltedJointCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(_7482.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BoltedJointCompoundAdvancedSystemDeflection._Cast_BoltedJointCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltedJointCompoundAdvancedSystemDeflection._Cast_BoltedJointCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointCompoundAdvancedSystemDeflection._Cast_BoltedJointCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bolted_joint_compound_advanced_system_deflection(
            self: "BoltedJointCompoundAdvancedSystemDeflection._Cast_BoltedJointCompoundAdvancedSystemDeflection",
        ) -> "BoltedJointCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BoltedJointCompoundAdvancedSystemDeflection._Cast_BoltedJointCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BoltedJointCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2441.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2441.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

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
    ) -> "List[_7290.BoltedJointAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BoltedJointAdvancedSystemDeflection]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7290.BoltedJointAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BoltedJointAdvancedSystemDeflection]

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
    ) -> "BoltedJointCompoundAdvancedSystemDeflection._Cast_BoltedJointCompoundAdvancedSystemDeflection":
        return self._Cast_BoltedJointCompoundAdvancedSystemDeflection(self)
