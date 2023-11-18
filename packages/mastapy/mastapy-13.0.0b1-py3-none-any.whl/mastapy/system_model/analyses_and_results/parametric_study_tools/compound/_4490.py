"""CylindricalPlanetGearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4487,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "CylindricalPlanetGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4343


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundParametricStudyTool")


class CylindricalPlanetGearCompoundParametricStudyTool(
    _4487.CylindricalGearCompoundParametricStudyTool
):
    """CylindricalPlanetGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCompoundParametricStudyTool"
    )

    class _Cast_CylindricalPlanetGearCompoundParametricStudyTool:
        """Special nested class for casting CylindricalPlanetGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
            parent: "CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4487.CylindricalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
        ) -> "CylindricalPlanetGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4343.CylindricalPlanetGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalPlanetGearParametricStudyTool]

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
    ) -> "List[_4343.CylindricalPlanetGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.CylindricalPlanetGearParametricStudyTool]

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
    ) -> "CylindricalPlanetGearCompoundParametricStudyTool._Cast_CylindricalPlanetGearCompoundParametricStudyTool":
        return self._Cast_CylindricalPlanetGearCompoundParametricStudyTool(self)
