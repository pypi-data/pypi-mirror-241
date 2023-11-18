"""PlanetaryGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4619
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "PlanetaryGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetModalAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetModalAnalysis")


class PlanetaryGearSetModalAnalysis(_4619.CylindricalGearSetModalAnalysis):
    """PlanetaryGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetModalAnalysis")

    class _Cast_PlanetaryGearSetModalAnalysis:
        """Special nested class for casting PlanetaryGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
            parent: "PlanetaryGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
        ):
            return self._parent._cast(_4619.CylindricalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634

            return self._parent._cast(_4634.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4569

            return self._parent._cast(_4569.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
        ) -> "PlanetaryGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2540.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
    ) -> "PlanetaryGearSetModalAnalysis._Cast_PlanetaryGearSetModalAnalysis":
        return self._Cast_PlanetaryGearSetModalAnalysis(self)
