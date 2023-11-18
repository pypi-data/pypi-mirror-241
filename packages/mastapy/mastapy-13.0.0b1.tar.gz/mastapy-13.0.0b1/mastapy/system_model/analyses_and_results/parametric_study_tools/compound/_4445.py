"""AGMAGleasonConicalGearMeshCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4473,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4297


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundParametricStudyTool")


class AGMAGleasonConicalGearMeshCompoundParametricStudyTool(
    _4473.ConicalGearMeshCompoundParametricStudyTool
):
    """AGMAGleasonConicalGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
            parent: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4473.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.GearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(
                _4505.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4452,
            )

            return self._parent._cast(
                _4452.BevelDifferentialGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(_4457.BevelGearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4540,
            )

            return self._parent._cast(
                _4540.SpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(
                _4546.StraightBevelDiffGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.StraightBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(
                _4567.ZerolBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
        ) -> "AGMAGleasonConicalGearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4297.AGMAGleasonConicalGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4297.AGMAGleasonConicalGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool(self)
