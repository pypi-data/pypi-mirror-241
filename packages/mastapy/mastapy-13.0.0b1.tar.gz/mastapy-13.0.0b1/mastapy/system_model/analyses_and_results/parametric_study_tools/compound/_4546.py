"""StraightBevelDiffGearMeshCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4457,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "StraightBevelDiffGearMeshCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4416


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshCompoundParametricStudyTool")


class StraightBevelDiffGearMeshCompoundParametricStudyTool(
    _4457.BevelGearMeshCompoundParametricStudyTool
):
    """StraightBevelDiffGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool"
    )

    class _Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool:
        """Special nested class for casting StraightBevelDiffGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
            parent: "StraightBevelDiffGearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4457.BevelGearMeshCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4445,
            )

            return self._parent._cast(
                _4445.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(_4473.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.GearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(
                _4505.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
        ) -> "StraightBevelDiffGearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool",
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
        instance_to_wrap: "StraightBevelDiffGearMeshCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2323.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2323.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4416.StraightBevelDiffGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelDiffGearMeshParametricStudyTool]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4416.StraightBevelDiffGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelDiffGearMeshParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshCompoundParametricStudyTool._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool":
        return self._Cast_StraightBevelDiffGearMeshCompoundParametricStudyTool(self)
