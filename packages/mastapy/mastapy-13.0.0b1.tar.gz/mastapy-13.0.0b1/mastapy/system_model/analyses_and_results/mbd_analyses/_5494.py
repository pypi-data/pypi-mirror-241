"""StraightBevelDiffGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5392
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "StraightBevelDiffGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6957


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMultibodyDynamicsAnalysis")


class StraightBevelDiffGearMultibodyDynamicsAnalysis(
    _5392.BevelGearMultibodyDynamicsAnalysis
):
    """StraightBevelDiffGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis"
    )

    class _Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelDiffGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
            parent: "StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5392.BevelGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378

            return self._parent._cast(
                _5378.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(_5401.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(
                _5499.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(
                _5500.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
        ) -> "StraightBevelDiffGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6957.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

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
    ) -> "StraightBevelDiffGearMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelDiffGearMultibodyDynamicsAnalysis(self)
