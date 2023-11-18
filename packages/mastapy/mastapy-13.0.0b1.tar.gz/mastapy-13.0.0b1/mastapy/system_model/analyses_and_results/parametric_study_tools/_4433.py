"""VirtualComponentParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4378
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "VirtualComponentParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentParametricStudyTool",)


Self = TypeVar("Self", bound="VirtualComponentParametricStudyTool")


class VirtualComponentParametricStudyTool(_4378.MountableComponentParametricStudyTool):
    """VirtualComponentParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentParametricStudyTool")

    class _Cast_VirtualComponentParametricStudyTool:
        """Special nested class for casting VirtualComponentParametricStudyTool to subclasses."""

        def __init__(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
            parent: "VirtualComponentParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            return self._parent._cast(_4378.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def mass_disc_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(_4375.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(_4376.MeasurementComponentParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(_4397.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(_4398.PowerLoadParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
        ) -> "VirtualComponentParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool",
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
        self: Self, instance_to_wrap: "VirtualComponentParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> (
        "VirtualComponentParametricStudyTool._Cast_VirtualComponentParametricStudyTool"
    ):
        return self._Cast_VirtualComponentParametricStudyTool(self)
