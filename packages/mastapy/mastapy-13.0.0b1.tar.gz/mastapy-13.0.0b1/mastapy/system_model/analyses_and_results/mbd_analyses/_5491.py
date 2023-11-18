"""SpringDamperHalfMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5414
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SpringDamperHalfMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.static_loads import _6955


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpringDamperHalfMultibodyDynamicsAnalysis")


class SpringDamperHalfMultibodyDynamicsAnalysis(
    _5414.CouplingHalfMultibodyDynamicsAnalysis
):
    """SpringDamperHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfMultibodyDynamicsAnalysis"
    )

    class _Cast_SpringDamperHalfMultibodyDynamicsAnalysis:
        """Special nested class for casting SpringDamperHalfMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
            parent: "SpringDamperHalfMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5414.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(_5401.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
        ) -> "SpringDamperHalfMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperHalfMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def spring_relative_displacement(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpringRelativeDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def spring_relative_rotation(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpringRelativeRotation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2599.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6955.SpringDamperHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperHalfMultibodyDynamicsAnalysis._Cast_SpringDamperHalfMultibodyDynamicsAnalysis":
        return self._Cast_SpringDamperHalfMultibodyDynamicsAnalysis(self)
