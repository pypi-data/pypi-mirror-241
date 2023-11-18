"""AbstractAssemblySystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2783
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AbstractAssemblySystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2432
    from mastapy.system_model.analyses_and_results.system_deflections import _2713
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2846,
    )
    from mastapy.system_model.analyses_and_results.power_flows import _4030


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblySystemDeflection",)


Self = TypeVar("Self", bound="AbstractAssemblySystemDeflection")


class AbstractAssemblySystemDeflection(_2783.PartSystemDeflection):
    """AbstractAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblySystemDeflection")

    class _Cast_AbstractAssemblySystemDeflection:
        """Special nested class for casting AbstractAssemblySystemDeflection to subclasses."""

        def __init__(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
            parent: "AbstractAssemblySystemDeflection",
        ):
            self._parent = parent

        @property
        def part_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2690,
            )

            return self._parent._cast(_2690.AssemblySystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2698,
            )

            return self._parent._cast(_2698.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelGearSetSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BoltedJointSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.ClutchSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ConceptGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConicalGearSetSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.CouplingSystemDeflection)

        @property
        def cvt_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.CycloidalAssemblySystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(
                _2742.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.FaceGearSetSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.GearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.PartToPartShearCouplingSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.RollingRingAssemblySystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(_2798.RootAssemblySystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpiralBevelGearSetSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelGearSetSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.SynchroniserSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.TorqueConverterSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.WormGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.ZerolBevelGearSetSystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "AbstractAssemblySystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblySystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2432.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2432.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def components_with_unknown_mass_properties(
        self: Self,
    ) -> "List[_2713.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithUnknownMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def components_with_zero_mass_properties(
        self: Self,
    ) -> "List[_2713.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithZeroMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rigidly_connected_groups(
        self: Self,
    ) -> "List[_2846.RigidlyConnectedComponentGroupSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.reporting.RigidlyConnectedComponentGroupSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidlyConnectedGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4030.AbstractAssemblyPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AbstractAssemblyPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection":
        return self._Cast_AbstractAssemblySystemDeflection(self)
