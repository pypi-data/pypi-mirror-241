"""MountableComponentParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4318
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "MountableComponentParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentParametricStudyTool",)


Self = TypeVar("Self", bound="MountableComponentParametricStudyTool")


class MountableComponentParametricStudyTool(_4318.ComponentParametricStudyTool):
    """MountableComponentParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentParametricStudyTool"
    )

    class _Cast_MountableComponentParametricStudyTool:
        """Special nested class for casting MountableComponentParametricStudyTool to subclasses."""

        def __init__(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
            parent: "MountableComponentParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            return self._parent._cast(_4318.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(_4298.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4301,
            )

            return self._parent._cast(_4301.BearingParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4305,
            )

            return self._parent._cast(_4305.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(
                _4307.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4308,
            )

            return self._parent._cast(_4308.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(_4310.BevelGearParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4315,
            )

            return self._parent._cast(_4315.ClutchHalfParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ConceptGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.ConicalGearParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.CouplingHalfParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.CVTPulleyParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4341,
            )

            return self._parent._cast(_4341.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4343,
            )

            return self._parent._cast(_4343.CylindricalPlanetGearParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.FaceGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.GearParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.HypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4367,
            )

            return self._parent._cast(
                _4367.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(
                _4370.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4373,
            )

            return self._parent._cast(
                _4373.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(_4375.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(_4376.MeasurementComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4379,
            )

            return self._parent._cast(_4379.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(
                _4392.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def planet_carrier_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4396,
            )

            return self._parent._cast(_4396.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(_4397.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(_4398.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(_4400.RingPinsParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.RollingRingParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4406,
            )

            return self._parent._cast(_4406.ShaftHubConnectionParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.SpiralBevelGearParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpringDamperHalfParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4427,
            )

            return self._parent._cast(_4427.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4430,
            )

            return self._parent._cast(_4430.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.WormGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.ZerolBevelGearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "MountableComponentParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
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
        self: Self, instance_to_wrap: "MountableComponentParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

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
    ) -> "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool":
        return self._Cast_MountableComponentParametricStudyTool(self)
