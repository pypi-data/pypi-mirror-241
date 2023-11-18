"""AGMAGleasonConicalGearSetParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4327
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AGMAGleasonConicalGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2512


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetParametricStudyTool")


class AGMAGleasonConicalGearSetParametricStudyTool(
    _4327.ConicalGearSetParametricStudyTool
):
    """AGMAGleasonConicalGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearSetParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
            parent: "AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            return self._parent._cast(_4327.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4360,
            )

            return self._parent._cast(_4360.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4293,
            )

            return self._parent._cast(_4293.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4306,
            )

            return self._parent._cast(_4306.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4311,
            )

            return self._parent._cast(_4311.BevelGearSetParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4364,
            )

            return self._parent._cast(_4364.HypoidGearSetParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4412,
            )

            return self._parent._cast(_4412.SpiralBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4418,
            )

            return self._parent._cast(_4418.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.StraightBevelGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4439,
            )

            return self._parent._cast(_4439.ZerolBevelGearSetParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ) -> "AGMAGleasonConicalGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
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
        self: Self,
        instance_to_wrap: "AGMAGleasonConicalGearSetParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2512.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

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
    ) -> "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearSetParametricStudyTool(self)
