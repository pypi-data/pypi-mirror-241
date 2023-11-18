"""BevelDifferentialGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4587
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BevelDifferentialGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.system_model.analyses_and_results.static_loads import _6822
    from mastapy.system_model.analyses_and_results.system_deflections import _2700
    from mastapy.system_model.analyses_and_results.modal_analyses import _4581, _4580


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetModalAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetModalAnalysis")


class BevelDifferentialGearSetModalAnalysis(_4587.BevelGearSetModalAnalysis):
    """BevelDifferentialGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetModalAnalysis"
    )

    class _Cast_BevelDifferentialGearSetModalAnalysis:
        """Special nested class for casting BevelDifferentialGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
            parent: "BevelDifferentialGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            return self._parent._cast(_4587.BevelGearSetModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575

            return self._parent._cast(_4575.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634

            return self._parent._cast(_4634.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4569

            return self._parent._cast(_4569.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
        ) -> "BevelDifferentialGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearSetModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2514.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6822.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2700.BevelDifferentialGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_differential_gears_modal_analysis(
        self: Self,
    ) -> "List[_4581.BevelDifferentialGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4580.BevelDifferentialGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetModalAnalysis._Cast_BevelDifferentialGearSetModalAnalysis":
        return self._Cast_BevelDifferentialGearSetModalAnalysis(self)
