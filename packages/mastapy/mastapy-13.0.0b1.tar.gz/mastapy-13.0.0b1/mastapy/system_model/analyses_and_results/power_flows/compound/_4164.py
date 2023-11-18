"""AbstractAssemblyCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4243
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AbstractAssemblyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4030


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundPowerFlow",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundPowerFlow")


class AbstractAssemblyCompoundPowerFlow(_4243.PartCompoundPowerFlow):
    """AbstractAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyCompoundPowerFlow")

    class _Cast_AbstractAssemblyCompoundPowerFlow:
        """Special nested class for casting AbstractAssemblyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
            parent: "AbstractAssemblyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def part_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4170,
            )

            return self._parent._cast(_4170.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4171,
            )

            return self._parent._cast(_4171.AssemblyCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4174,
            )

            return self._parent._cast(_4174.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(_4177.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4182,
            )

            return self._parent._cast(_4182.BevelGearSetCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4184,
            )

            return self._parent._cast(_4184.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4185,
            )

            return self._parent._cast(_4185.ClutchCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConicalGearSetCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.CouplingCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.CVTCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4207,
            )

            return self._parent._cast(_4207.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.CylindricalGearSetCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.FaceGearSetCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4221,
            )

            return self._parent._cast(_4221.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.GearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4228,
            )

            return self._parent._cast(_4228.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(
                _4235.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(
                _4238.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def part_to_part_shear_coupling_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def planetary_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.PlanetaryGearSetCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(_4255.RollingRingAssemblyCompoundPowerFlow)

        @property
        def root_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4258,
            )

            return self._parent._cast(_4258.RootAssemblyCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4266,
            )

            return self._parent._cast(_4266.SpringDamperCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelGearSetCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.SynchroniserCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4281,
            )

            return self._parent._cast(_4281.TorqueConverterCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
        ) -> "AbstractAssemblyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4030.AbstractAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractAssemblyPowerFlow]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4030.AbstractAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractAssemblyPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyCompoundPowerFlow._Cast_AbstractAssemblyCompoundPowerFlow":
        return self._Cast_AbstractAssemblyCompoundPowerFlow(self)
