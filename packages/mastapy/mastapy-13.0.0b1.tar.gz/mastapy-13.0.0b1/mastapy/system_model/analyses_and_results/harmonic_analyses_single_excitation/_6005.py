"""AbstractAssemblyHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6086,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2432


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="AbstractAssemblyHarmonicAnalysisOfSingleExcitation")


class AbstractAssemblyHarmonicAnalysisOfSingleExcitation(
    _6086.PartHarmonicAnalysisOfSingleExcitation
):
    """AbstractAssemblyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractAssemblyHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6011,
            )

            return self._parent._cast(
                _6011.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(_6012.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6015,
            )

            return self._parent._cast(_6015.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6018,
            )

            return self._parent._cast(
                _6018.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6023,
            )

            return self._parent._cast(
                _6023.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6024,
            )

            return self._parent._cast(
                _6024.BoltedJointHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6028,
            )

            return self._parent._cast(_6028.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(
                _6033.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(_6044.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(_6046.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6048,
            )

            return self._parent._cast(
                _6048.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(
                _6054.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6060,
            )

            return self._parent._cast(
                _6060.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6062,
            )

            return self._parent._cast(
                _6062.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(_6065.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(
                _6070.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(
                _6080.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(
                _6089.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(
                _6091.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6098,
            )

            return self._parent._cast(
                _6098.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(
                _6101.RootAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(
                _6105.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.SynchroniserHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(
                _6125.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(
                _6135.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AbstractAssemblyHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2432.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2432.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

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
    ) -> "AbstractAssemblyHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractAssemblyHarmonicAnalysisOfSingleExcitation(self)
