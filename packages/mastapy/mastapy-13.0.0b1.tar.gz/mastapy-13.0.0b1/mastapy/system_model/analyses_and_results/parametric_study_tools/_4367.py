"""KlingelnbergCycloPalloidConicalGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4326
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearParametricStudyTool",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearParametricStudyTool")


class KlingelnbergCycloPalloidConicalGearParametricStudyTool(
    _4326.ConicalGearParametricStudyTool
):
    """KlingelnbergCycloPalloidConicalGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
            parent: "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            return self._parent._cast(_4326.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(
                _4370.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4373,
            )

            return self._parent._cast(
                _4373.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidConicalGearParametricStudyTool(self)
