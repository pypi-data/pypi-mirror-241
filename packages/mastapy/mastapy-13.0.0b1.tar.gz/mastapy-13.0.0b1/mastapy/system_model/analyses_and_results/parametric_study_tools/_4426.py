"""SynchroniserPartParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4331
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SynchroniserPartParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartParametricStudyTool",)


Self = TypeVar("Self", bound="SynchroniserPartParametricStudyTool")


class SynchroniserPartParametricStudyTool(_4331.CouplingHalfParametricStudyTool):
    """SynchroniserPartParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartParametricStudyTool")

    class _Cast_SynchroniserPartParametricStudyTool:
        """Special nested class for casting SynchroniserPartParametricStudyTool to subclasses."""

        def __init__(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
            parent: "SynchroniserPartParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ):
            return self._parent._cast(_4331.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4427,
            )

            return self._parent._cast(_4427.SynchroniserSleeveParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
        ) -> "SynchroniserPartParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool",
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
        self: Self, instance_to_wrap: "SynchroniserPartParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
        "SynchroniserPartParametricStudyTool._Cast_SynchroniserPartParametricStudyTool"
    ):
        return self._Cast_SynchroniserPartParametricStudyTool(self)
