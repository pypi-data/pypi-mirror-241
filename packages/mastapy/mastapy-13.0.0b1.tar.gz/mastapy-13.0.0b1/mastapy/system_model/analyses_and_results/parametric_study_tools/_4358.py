"""GearMeshParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4365
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "GearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2311


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="GearMeshParametricStudyTool")


class GearMeshParametricStudyTool(
    _4365.InterMountableComponentConnectionParametricStudyTool
):
    """GearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshParametricStudyTool")

    class _Cast_GearMeshParametricStudyTool:
        """Special nested class for casting GearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
            parent: "GearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            return self._parent._cast(
                _4365.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4297,
            )

            return self._parent._cast(
                _4297.AGMAGleasonConicalGearMeshParametricStudyTool
            )

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(
                _4304.BevelDifferentialGearMeshParametricStudyTool
            )

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.BevelGearMeshParametricStudyTool)

        @property
        def concept_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.ConceptGearMeshParametricStudyTool)

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConicalGearMeshParametricStudyTool)

        @property
        def cylindrical_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.CylindricalGearMeshParametricStudyTool)

        @property
        def face_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4353,
            )

            return self._parent._cast(_4353.FaceGearMeshParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.HypoidGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(
                _4366.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4369,
            )

            return self._parent._cast(
                _4369.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4372,
            )

            return self._parent._cast(
                _4372.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.SpiralBevelGearMeshParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(
                _4416.StraightBevelDiffGearMeshParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.StraightBevelGearMeshParametricStudyTool)

        @property
        def worm_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.WormGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.ZerolBevelGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
        ) -> "GearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2311.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshParametricStudyTool._Cast_GearMeshParametricStudyTool":
        return self._Cast_GearMeshParametricStudyTool(self)
