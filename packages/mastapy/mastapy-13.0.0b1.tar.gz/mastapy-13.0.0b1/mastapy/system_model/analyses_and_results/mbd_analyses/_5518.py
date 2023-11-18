"""ZerolBevelGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5392
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ZerolBevelGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.static_loads import _6983


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearMultibodyDynamicsAnalysis")


class ZerolBevelGearMultibodyDynamicsAnalysis(_5392.BevelGearMultibodyDynamicsAnalysis):
    """ZerolBevelGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearMultibodyDynamicsAnalysis"
    )

    class _Cast_ZerolBevelGearMultibodyDynamicsAnalysis:
        """Special nested class for casting ZerolBevelGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
            parent: "ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5392.BevelGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378

            return self._parent._cast(
                _5378.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(_5401.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "ZerolBevelGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6983.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

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
    ) -> "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis":
        return self._Cast_ZerolBevelGearMultibodyDynamicsAnalysis(self)
