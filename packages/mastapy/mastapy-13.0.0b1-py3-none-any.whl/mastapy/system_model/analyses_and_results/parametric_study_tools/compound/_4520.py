"""PartToPartShearCouplingCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4477,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "PartToPartShearCouplingCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4393


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="PartToPartShearCouplingCompoundParametricStudyTool")


class PartToPartShearCouplingCompoundParametricStudyTool(
    _4477.CouplingCompoundParametricStudyTool
):
    """PartToPartShearCouplingCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingCompoundParametricStudyTool"
    )

    class _Cast_PartToPartShearCouplingCompoundParametricStudyTool:
        """Special nested class for casting PartToPartShearCouplingCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool",
            parent: "PartToPartShearCouplingCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_compound_parametric_study_tool(
            self: "PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4477.CouplingCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(
                _4538.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4440,
            )

            return self._parent._cast(_4440.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool",
        ) -> "PartToPartShearCouplingCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool",
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
        instance_to_wrap: "PartToPartShearCouplingCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2586.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2586.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4393.PartToPartShearCouplingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4393.PartToPartShearCouplingParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PartToPartShearCouplingParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingCompoundParametricStudyTool._Cast_PartToPartShearCouplingCompoundParametricStudyTool":
        return self._Cast_PartToPartShearCouplingCompoundParametricStudyTool(self)
