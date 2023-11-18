"""BevelDifferentialSunGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "BevelDifferentialSunGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2516


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearParametricStudyTool",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearParametricStudyTool")


class BevelDifferentialSunGearParametricStudyTool(
    _4305.BevelDifferentialGearParametricStudyTool
):
    """BevelDifferentialSunGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearParametricStudyTool"
    )

    class _Cast_BevelDifferentialSunGearParametricStudyTool:
        """Special nested class for casting BevelDifferentialSunGearParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
            parent: "BevelDifferentialSunGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            return self._parent._cast(_4305.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(_4310.BevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(_4298.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
        ) -> "BevelDifferentialSunGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "BevelDifferentialSunGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2516.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

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
    ) -> "BevelDifferentialSunGearParametricStudyTool._Cast_BevelDifferentialSunGearParametricStudyTool":
        return self._Cast_BevelDifferentialSunGearParametricStudyTool(self)
