"""GearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4517,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "GearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _356
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4359


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="GearCompoundParametricStudyTool")


class GearCompoundParametricStudyTool(
    _4517.MountableComponentCompoundParametricStudyTool
):
    """GearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundParametricStudyTool")

    class _Cast_GearCompoundParametricStudyTool:
        """Special nested class for casting GearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
            parent: "GearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4517.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4444,
            )

            return self._parent._cast(
                _4444.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(
                _4451.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4454,
            )

            return self._parent._cast(
                _4454.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(
                _4455.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4456,
            )

            return self._parent._cast(_4456.BevelGearCompoundParametricStudyTool)

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4469,
            )

            return self._parent._cast(_4469.ConceptGearCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(_4472.ConicalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4487,
            )

            return self._parent._cast(_4487.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(
                _4490.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def face_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4493,
            )

            return self._parent._cast(_4493.FaceGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(_4502.HypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4506,
            )

            return self._parent._cast(
                _4506.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(
                _4509.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4512,
            )

            return self._parent._cast(
                _4512.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4539,
            )

            return self._parent._cast(_4539.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(
                _4545.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4548,
            )

            return self._parent._cast(
                _4548.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(
                _4551.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(
                _4552.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4563,
            )

            return self._parent._cast(_4563.WormGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4566,
            )

            return self._parent._cast(_4566.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "GearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_results(self: Self) -> "_356.GearDutyCycleRating":
        """mastapy.gears.rating.GearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: Self) -> "List[_4359.GearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4359.GearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool":
        return self._Cast_GearCompoundParametricStudyTool(self)
