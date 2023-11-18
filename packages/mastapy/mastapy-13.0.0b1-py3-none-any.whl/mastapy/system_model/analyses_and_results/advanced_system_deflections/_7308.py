"""CouplingAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7371
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CouplingAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581


__docformat__ = "restructuredtext en"
__all__ = ("CouplingAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingAdvancedSystemDeflection")


class CouplingAdvancedSystemDeflection(
    _7371.SpecialisedAssemblyAdvancedSystemDeflection
):
    """CouplingAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingAdvancedSystemDeflection")

    class _Cast_CouplingAdvancedSystemDeflection:
        """Special nested class for casting CouplingAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
            parent: "CouplingAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7371.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7267,
            )

            return self._parent._cast(_7267.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7291,
            )

            return self._parent._cast(_7291.ClutchAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(_7296.ConceptCouplingAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(
                _7353.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def spring_damper_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(_7375.SpringDamperAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7390,
            )

            return self._parent._cast(_7390.TorqueConverterAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
        ) -> "CouplingAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2581.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingAdvancedSystemDeflection._Cast_CouplingAdvancedSystemDeflection":
        return self._Cast_CouplingAdvancedSystemDeflection(self)
