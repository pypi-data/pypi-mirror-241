"""AGMAGleasonConicalGearDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AGMAGleasonConicalGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearDynamicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearDynamicAnalysis")


class AGMAGleasonConicalGearDynamicAnalysis(_6306.ConicalGearDynamicAnalysis):
    """AGMAGleasonConicalGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearDynamicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearDynamicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
            parent: "AGMAGleasonConicalGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            return self._parent._cast(_6306.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(_6288.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.BevelGearDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.HypoidGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(_6375.SpiralBevelGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.StraightBevelSunGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402

            return self._parent._cast(_6402.ZerolBevelGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "AGMAGleasonConicalGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2511.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis":
        return self._Cast_AGMAGleasonConicalGearDynamicAnalysis(self)
