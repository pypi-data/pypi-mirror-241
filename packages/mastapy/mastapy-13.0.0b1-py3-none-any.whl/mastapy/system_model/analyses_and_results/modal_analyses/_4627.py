"""FaceGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4633
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "FaceGearModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.static_loads import _6882
    from mastapy.system_model.analyses_and_results.system_deflections import _2754


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearModalAnalysis",)


Self = TypeVar("Self", bound="FaceGearModalAnalysis")


class FaceGearModalAnalysis(_4633.GearModalAnalysis):
    """FaceGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearModalAnalysis")

    class _Cast_FaceGearModalAnalysis:
        """Special nested class for casting FaceGearModalAnalysis to subclasses."""

        def __init__(
            self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis",
            parent: "FaceGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_modal_analysis(
            self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis",
        ):
            return self._parent._cast(_4633.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis",
        ) -> "FaceGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2526.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6882.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2754.FaceGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FaceGearModalAnalysis._Cast_FaceGearModalAnalysis":
        return self._Cast_FaceGearModalAnalysis(self)
