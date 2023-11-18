"""BevelGearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4444,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "BevelGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4310


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="BevelGearCompoundParametricStudyTool")


class BevelGearCompoundParametricStudyTool(
    _4444.AGMAGleasonConicalGearCompoundParametricStudyTool
):
    """BevelGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearCompoundParametricStudyTool")

    class _Cast_BevelGearCompoundParametricStudyTool:
        """Special nested class for casting BevelGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
            parent: "BevelGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4444.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(_4472.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(
                _4451.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4454,
            )

            return self._parent._cast(
                _4454.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(
                _4455.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4539,
            )

            return self._parent._cast(_4539.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(
                _4545.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4548,
            )

            return self._parent._cast(
                _4548.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(
                _4551.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(
                _4552.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4566,
            )

            return self._parent._cast(_4566.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
        ) -> "BevelGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "BevelGearCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4310.BevelGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearParametricStudyTool]

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
    ) -> "List[_4310.BevelGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelGearParametricStudyTool]

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
    ) -> "BevelGearCompoundParametricStudyTool._Cast_BevelGearCompoundParametricStudyTool":
        return self._Cast_BevelGearCompoundParametricStudyTool(self)
