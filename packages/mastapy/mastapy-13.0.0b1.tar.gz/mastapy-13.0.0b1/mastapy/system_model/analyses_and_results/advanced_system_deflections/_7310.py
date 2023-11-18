"""CouplingHalfAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7350
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CouplingHalfAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingHalfAdvancedSystemDeflection")


class CouplingHalfAdvancedSystemDeflection(
    _7350.MountableComponentAdvancedSystemDeflection
):
    """CouplingHalfAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfAdvancedSystemDeflection")

    class _Cast_CouplingHalfAdvancedSystemDeflection:
        """Special nested class for casting CouplingHalfAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
            parent: "CouplingHalfAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7350.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7293,
            )

            return self._parent._cast(_7293.ClutchHalfAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.CVTPulleyAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(
                _7355.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def pulley_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.PulleyAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(_7364.RollingRingAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(_7377.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(_7387.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(_7388.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(_7389.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(_7392.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7393,
            )

            return self._parent._cast(
                _7393.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def coupling_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ) -> "CouplingHalfAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingHalfAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2582.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection":
        return self._Cast_CouplingHalfAdvancedSystemDeflection(self)
