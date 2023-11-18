"""CouplingHalfCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4517,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CouplingHalfCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4331


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CouplingHalfCompoundParametricStudyTool")


class CouplingHalfCompoundParametricStudyTool(
    _4517.MountableComponentCompoundParametricStudyTool
):
    """CouplingHalfCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundParametricStudyTool"
    )

    class _Cast_CouplingHalfCompoundParametricStudyTool:
        """Special nested class for casting CouplingHalfCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
            parent: "CouplingHalfCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4517.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4463,
            )

            return self._parent._cast(_4463.ClutchHalfCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(
                _4468.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.CVTPulleyCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(
                _4522.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def pulley_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(_4528.PulleyCompoundParametricStudyTool)

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4532,
            )

            return self._parent._cast(_4532.RollingRingCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(_4544.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(_4554.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(_4555.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(
                _4556.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(
                _4559.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(
                _4560.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
        ) -> "CouplingHalfCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4331.CouplingHalfParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingHalfParametricStudyTool]

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
    ) -> "List[_4331.CouplingHalfParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CouplingHalfParametricStudyTool]

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
    ) -> "CouplingHalfCompoundParametricStudyTool._Cast_CouplingHalfCompoundParametricStudyTool":
        return self._Cast_CouplingHalfCompoundParametricStudyTool(self)
