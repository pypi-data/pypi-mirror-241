"""TorqueConverterPumpCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4479,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "TorqueConverterPumpCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4430


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="TorqueConverterPumpCompoundParametricStudyTool")


class TorqueConverterPumpCompoundParametricStudyTool(
    _4479.CouplingHalfCompoundParametricStudyTool
):
    """TorqueConverterPumpCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpCompoundParametricStudyTool"
    )

    class _Cast_TorqueConverterPumpCompoundParametricStudyTool:
        """Special nested class for casting TorqueConverterPumpCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
            parent: "TorqueConverterPumpCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4479.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
        ) -> "TorqueConverterPumpCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool",
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
        instance_to_wrap: "TorqueConverterPumpCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

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
    ) -> "List[_4430.TorqueConverterPumpParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterPumpParametricStudyTool]

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
    ) -> "List[_4430.TorqueConverterPumpParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.TorqueConverterPumpParametricStudyTool]

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
    ) -> "TorqueConverterPumpCompoundParametricStudyTool._Cast_TorqueConverterPumpCompoundParametricStudyTool":
        return self._Cast_TorqueConverterPumpCompoundParametricStudyTool(self)
