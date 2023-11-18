"""FaceGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4359
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "FaceGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.static_loads import _6882
    from mastapy.system_model.analyses_and_results.system_deflections import _2754


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearParametricStudyTool",)


Self = TypeVar("Self", bound="FaceGearParametricStudyTool")


class FaceGearParametricStudyTool(_4359.GearParametricStudyTool):
    """FaceGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearParametricStudyTool")

    class _Cast_FaceGearParametricStudyTool:
        """Special nested class for casting FaceGearParametricStudyTool to subclasses."""

        def __init__(
            self: "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool",
            parent: "FaceGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_parametric_study_tool(
            self: "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool",
        ):
            return self._parent._cast(_4359.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def face_gear_parametric_study_tool(
            self: "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool",
        ) -> "FaceGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2526.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6882.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2754.FaceGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearParametricStudyTool._Cast_FaceGearParametricStudyTool":
        return self._Cast_FaceGearParametricStudyTool(self)
