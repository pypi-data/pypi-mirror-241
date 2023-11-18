"""BevelDifferentialGearSetParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4311
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "BevelDifferentialGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.system_model.analyses_and_results.static_loads import _6822
    from mastapy.system_model.analyses_and_results.system_deflections import _2700
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4305,
        _4304,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetParametricStudyTool")


class BevelDifferentialGearSetParametricStudyTool(
    _4311.BevelGearSetParametricStudyTool
):
    """BevelDifferentialGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetParametricStudyTool"
    )

    class _Cast_BevelDifferentialGearSetParametricStudyTool:
        """Special nested class for casting BevelDifferentialGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
            parent: "BevelDifferentialGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ):
            return self._parent._cast(_4311.BevelGearSetParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4299,
            )

            return self._parent._cast(
                _4299.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def conical_gear_set_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4327,
            )

            return self._parent._cast(_4327.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4360,
            )

            return self._parent._cast(_4360.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4293,
            )

            return self._parent._cast(_4293.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
        ) -> "BevelDifferentialGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearSetParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2514.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6822.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2700.BevelDifferentialGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gears_parametric_study_tool(
        self: Self,
    ) -> "List[_4305.BevelDifferentialGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_parametric_study_tool(
        self: Self,
    ) -> "List[_4304.BevelDifferentialGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.BevelDifferentialGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetParametricStudyTool._Cast_BevelDifferentialGearSetParametricStudyTool":
        return self._Cast_BevelDifferentialGearSetParametricStudyTool(self)
