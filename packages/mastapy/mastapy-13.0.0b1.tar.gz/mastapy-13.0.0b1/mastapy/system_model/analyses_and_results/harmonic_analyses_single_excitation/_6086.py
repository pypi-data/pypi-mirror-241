"""PartHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "PartHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5763
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6067,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses import _4659


__docformat__ = "restructuredtext en"
__all__ = ("PartHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="PartHarmonicAnalysisOfSingleExcitation")


class PartHarmonicAnalysisOfSingleExcitation(_7545.PartStaticLoadAnalysisCase):
    """PartHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_PartHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PartHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
            parent: "PartHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6005,
            )

            return self._parent._cast(
                _6005.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6006,
            )

            return self._parent._cast(
                _6006.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6007,
            )

            return self._parent._cast(
                _6007.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6009,
            )

            return self._parent._cast(
                _6009.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6011,
            )

            return self._parent._cast(
                _6011.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(_6012.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6013,
            )

            return self._parent._cast(_6013.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6015,
            )

            return self._parent._cast(_6015.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(
                _6016.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6018,
            )

            return self._parent._cast(
                _6018.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6019,
            )

            return self._parent._cast(
                _6019.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6020,
            )

            return self._parent._cast(
                _6020.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6021,
            )

            return self._parent._cast(_6021.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6023,
            )

            return self._parent._cast(
                _6023.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6024,
            )

            return self._parent._cast(
                _6024.BoltedJointHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6025,
            )

            return self._parent._cast(_6025.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6027,
            )

            return self._parent._cast(
                _6027.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6028,
            )

            return self._parent._cast(_6028.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(_6030.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6032,
            )

            return self._parent._cast(
                _6032.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(
                _6033.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6037,
            )

            return self._parent._cast(
                _6037.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(_6041.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(_6044.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(_6046.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(_6047.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6048,
            )

            return self._parent._cast(
                _6048.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(
                _6050.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6052,
            )

            return self._parent._cast(
                _6052.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(
                _6054.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6055,
            )

            return self._parent._cast(
                _6055.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6056,
            )

            return self._parent._cast(_6056.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6057,
            )

            return self._parent._cast(
                _6057.ExternalCADModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(_6058.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6060,
            )

            return self._parent._cast(
                _6060.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(_6061.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6062,
            )

            return self._parent._cast(
                _6062.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6063,
            )

            return self._parent._cast(_6063.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(_6065.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(
                _6066.GuideDxfModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(
                _6068.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(
                _6070.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6072,
            )

            return self._parent._cast(
                _6072.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6075,
            )

            return self._parent._cast(
                _6075.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6078,
            )

            return self._parent._cast(
                _6078.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(
                _6080.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(_6081.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(
                _6082.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(
                _6088.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(
                _6089.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(
                _6091.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(
                _6092.PlanetCarrierHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6093,
            )

            return self._parent._cast(_6093.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(_6094.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(_6095.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6096,
            )

            return self._parent._cast(_6096.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6098,
            )

            return self._parent._cast(
                _6098.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6100,
            )

            return self._parent._cast(
                _6100.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(
                _6101.RootAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(_6102.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6103,
            )

            return self._parent._cast(
                _6103.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(
                _6105.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6106,
            )

            return self._parent._cast(
                _6106.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(
                _6110.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6112,
            )

            return self._parent._cast(
                _6112.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(
                _6115.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(
                _6118.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(
                _6119.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.SynchroniserHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(
                _6122.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6123,
            )

            return self._parent._cast(
                _6123.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(
                _6125.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(
                _6126.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6129,
            )

            return self._parent._cast(
                _6129.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6130,
            )

            return self._parent._cast(_6130.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6133,
            )

            return self._parent._cast(
                _6133.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(
                _6135.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
        ) -> "PartHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "PartHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_options(self: Self) -> "_5763.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "_6067.HarmonicAnalysisOfSingleExcitation":
        """mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def uncoupled_modal_analysis(self: Self) -> "_4659.PartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UncoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartHarmonicAnalysisOfSingleExcitation._Cast_PartHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PartHarmonicAnalysisOfSingleExcitation(self)
