"""GearMeshAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7074,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "GearMeshAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2311
    from mastapy.system_model.analyses_and_results.system_deflections import _2757


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="GearMeshAdvancedTimeSteppingAnalysisForModulation")


class GearMeshAdvancedTimeSteppingAnalysisForModulation(
    _7074.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """GearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting GearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
            parent: "GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7074.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7012,
            )

            return self._parent._cast(
                _7012.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7020,
            )

            return self._parent._cast(
                _7020.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7025,
            )

            return self._parent._cast(
                _7025.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7038,
            )

            return self._parent._cast(
                _7038.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7056,
            )

            return self._parent._cast(
                _7056.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7109,
            )

            return self._parent._cast(
                _7109.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7133,
            )

            return self._parent._cast(
                _7133.WormGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "GearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "GearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_teeth_passed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfTeethPassed

        if temp is None:
            return 0.0

        return temp

    @number_of_teeth_passed.setter
    @enforce_parameter_types
    def number_of_teeth_passed(self: Self, value: "float"):
        self.wrapped.NumberOfTeethPassed = float(value) if value is not None else 0.0

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
    def system_deflection_results(self: Self) -> "_2757.GearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_GearMeshAdvancedTimeSteppingAnalysisForModulation(self)
