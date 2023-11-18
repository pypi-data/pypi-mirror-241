"""ZerolBevelGearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4456,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ZerolBevelGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4438


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ZerolBevelGearCompoundParametricStudyTool")


class ZerolBevelGearCompoundParametricStudyTool(
    _4456.BevelGearCompoundParametricStudyTool
):
    """ZerolBevelGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearCompoundParametricStudyTool"
    )

    class _Cast_ZerolBevelGearCompoundParametricStudyTool:
        """Special nested class for casting ZerolBevelGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
            parent: "ZerolBevelGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4456.BevelGearCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4444,
            )

            return self._parent._cast(
                _4444.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(_4472.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
        ) -> "ZerolBevelGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ZerolBevelGearCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4438.ZerolBevelGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearParametricStudyTool]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4438.ZerolBevelGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ZerolBevelGearParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearCompoundParametricStudyTool._Cast_ZerolBevelGearCompoundParametricStudyTool":
        return self._Cast_ZerolBevelGearCompoundParametricStudyTool(self)
