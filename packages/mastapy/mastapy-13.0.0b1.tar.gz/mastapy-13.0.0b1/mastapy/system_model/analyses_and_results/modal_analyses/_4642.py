"""KlingelnbergCycloPalloidConicalGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4603
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.system_deflections import _2767


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetModalAnalysis")


class KlingelnbergCycloPalloidConicalGearSetModalAnalysis(
    _4603.ConicalGearSetModalAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            return self._parent._cast(_4603.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634

            return self._parent._cast(_4634.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4569

            return self._parent._cast(_4569.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(
                _4645.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(
                _4648.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2535.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2767.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSetSystemDeflection

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetModalAnalysis(self)
