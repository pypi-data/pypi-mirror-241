"""ConceptGearSetCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4500,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ConceptGearSetCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4324
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4469,
        _4470,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ConceptGearSetCompoundParametricStudyTool")


class ConceptGearSetCompoundParametricStudyTool(
    _4500.GearSetCompoundParametricStudyTool
):
    """ConceptGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearSetCompoundParametricStudyTool"
    )

    class _Cast_ConceptGearSetCompoundParametricStudyTool:
        """Special nested class for casting ConceptGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ConceptGearSetCompoundParametricStudyTool._Cast_ConceptGearSetCompoundParametricStudyTool",
            parent: "ConceptGearSetCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_set_compound_parametric_study_tool(
            self: "ConceptGearSetCompoundParametricStudyTool._Cast_ConceptGearSetCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4500.GearSetCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "ConceptGearSetCompoundParametricStudyTool._Cast_ConceptGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(
                _4538.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "ConceptGearSetCompoundParametricStudyTool._Cast_ConceptGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4440,
            )

            return self._parent._cast(_4440.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "ConceptGearSetCompoundParametricStudyTool._Cast_ConceptGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ConceptGearSetCompoundParametricStudyTool._Cast_ConceptGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearSetCompoundParametricStudyTool._Cast_ConceptGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetCompoundParametricStudyTool._Cast_ConceptGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "ConceptGearSetCompoundParametricStudyTool._Cast_ConceptGearSetCompoundParametricStudyTool",
        ) -> "ConceptGearSetCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetCompoundParametricStudyTool._Cast_ConceptGearSetCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConceptGearSetCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2520.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2520.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

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
    ) -> "List[_4324.ConceptGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearSetParametricStudyTool]

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
    def concept_gears_compound_parametric_study_tool(
        self: Self,
    ) -> "List[_4469.ConceptGearCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptGearCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsCompoundParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_compound_parametric_study_tool(
        self: Self,
    ) -> "List[_4470.ConceptGearMeshCompoundParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.compound.ConceptGearMeshCompoundParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesCompoundParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4324.ConceptGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearSetParametricStudyTool]

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
    ) -> "ConceptGearSetCompoundParametricStudyTool._Cast_ConceptGearSetCompoundParametricStudyTool":
        return self._Cast_ConceptGearSetCompoundParametricStudyTool(self)
