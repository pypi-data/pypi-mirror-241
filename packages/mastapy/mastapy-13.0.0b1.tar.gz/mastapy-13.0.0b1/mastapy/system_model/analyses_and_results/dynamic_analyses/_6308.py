"""ConicalGearSetDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ConicalGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetDynamicAnalysis")


class ConicalGearSetDynamicAnalysis(_6336.GearSetDynamicAnalysis):
    """ConicalGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetDynamicAnalysis")

    class _Cast_ConicalGearSetDynamicAnalysis:
        """Special nested class for casting ConicalGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
            parent: "ConicalGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            return self._parent._cast(_6336.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6274

            return self._parent._cast(_6274.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280

            return self._parent._cast(_6280.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.BevelGearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(_6340.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(
                _6344.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(
                _6347.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(
                _6350.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.SpiralBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.ZerolBevelGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
        ) -> "ConicalGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2522.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetDynamicAnalysis._Cast_ConicalGearSetDynamicAnalysis":
        return self._Cast_ConicalGearSetDynamicAnalysis(self)
