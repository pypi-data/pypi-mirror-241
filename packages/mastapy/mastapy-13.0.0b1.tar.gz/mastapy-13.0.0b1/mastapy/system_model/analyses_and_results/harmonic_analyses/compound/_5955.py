"""PartCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "PartCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5785


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="PartCompoundHarmonicAnalysis")


class PartCompoundHarmonicAnalysis(_7543.PartCompoundAnalysis):
    """PartCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundHarmonicAnalysis")

    class _Cast_PartCompoundHarmonicAnalysis:
        """Special nested class for casting PartCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
            parent: "PartCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5876,
            )

            return self._parent._cast(_5876.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5877,
            )

            return self._parent._cast(_5877.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5878,
            )

            return self._parent._cast(
                _5878.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5880,
            )

            return self._parent._cast(
                _5880.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5882,
            )

            return self._parent._cast(
                _5882.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5883,
            )

            return self._parent._cast(_5883.AssemblyCompoundHarmonicAnalysis)

        @property
        def bearing_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5884,
            )

            return self._parent._cast(_5884.BearingCompoundHarmonicAnalysis)

        @property
        def belt_drive_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5886,
            )

            return self._parent._cast(_5886.BeltDriveCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(
                _5887.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5889,
            )

            return self._parent._cast(
                _5889.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5890,
            )

            return self._parent._cast(
                _5890.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5891,
            )

            return self._parent._cast(
                _5891.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5892,
            )

            return self._parent._cast(_5892.BevelGearCompoundHarmonicAnalysis)

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5894,
            )

            return self._parent._cast(_5894.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def bolt_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5895,
            )

            return self._parent._cast(_5895.BoltCompoundHarmonicAnalysis)

        @property
        def bolted_joint_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5896,
            )

            return self._parent._cast(_5896.BoltedJointCompoundHarmonicAnalysis)

        @property
        def clutch_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5897,
            )

            return self._parent._cast(_5897.ClutchCompoundHarmonicAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5899,
            )

            return self._parent._cast(_5899.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(_5901.ComponentCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5902,
            )

            return self._parent._cast(_5902.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(_5905.ConceptGearCompoundHarmonicAnalysis)

        @property
        def concept_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5907,
            )

            return self._parent._cast(_5907.ConceptGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5908,
            )

            return self._parent._cast(_5908.ConicalGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5910,
            )

            return self._parent._cast(_5910.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ConnectorCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5913,
            )

            return self._parent._cast(_5913.CouplingCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5915,
            )

            return self._parent._cast(_5915.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5917,
            )

            return self._parent._cast(_5917.CVTCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5918,
            )

            return self._parent._cast(_5918.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def cycloidal_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5919,
            )

            return self._parent._cast(_5919.CycloidalAssemblyCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5921,
            )

            return self._parent._cast(_5921.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5923,
            )

            return self._parent._cast(_5923.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(_5925.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5926,
            )

            return self._parent._cast(
                _5926.CylindricalPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def datum_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5927,
            )

            return self._parent._cast(_5927.DatumCompoundHarmonicAnalysis)

        @property
        def external_cad_model_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5928,
            )

            return self._parent._cast(_5928.ExternalCADModelCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5929,
            )

            return self._parent._cast(_5929.FaceGearCompoundHarmonicAnalysis)

        @property
        def face_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5931,
            )

            return self._parent._cast(_5931.FaceGearSetCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5932,
            )

            return self._parent._cast(_5932.FEPartCompoundHarmonicAnalysis)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.FlexiblePinAssemblyCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5934,
            )

            return self._parent._cast(_5934.GearCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5936,
            )

            return self._parent._cast(_5936.GearSetCompoundHarmonicAnalysis)

        @property
        def guide_dxf_model_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5937,
            )

            return self._parent._cast(_5937.GuideDxfModelCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.HypoidGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5942,
            )

            return self._parent._cast(
                _5942.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5945,
            )

            return self._parent._cast(
                _5945.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(
                _5947.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5948,
            )

            return self._parent._cast(
                _5948.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5950,
            )

            return self._parent._cast(
                _5950.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def mass_disc_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5951,
            )

            return self._parent._cast(_5951.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(
                _5952.MeasurementComponentCompoundHarmonicAnalysis
            )

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5953,
            )

            return self._parent._cast(_5953.MountableComponentCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(_5954.OilSealCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(
                _5956.PartToPartShearCouplingCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(
                _5958.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.PlanetaryGearSetCompoundHarmonicAnalysis)

        @property
        def planet_carrier_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5961,
            )

            return self._parent._cast(_5961.PlanetCarrierCompoundHarmonicAnalysis)

        @property
        def point_load_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5962,
            )

            return self._parent._cast(_5962.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5963,
            )

            return self._parent._cast(_5963.PowerLoadCompoundHarmonicAnalysis)

        @property
        def pulley_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.PulleyCompoundHarmonicAnalysis)

        @property
        def ring_pins_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(_5965.RingPinsCompoundHarmonicAnalysis)

        @property
        def rolling_ring_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(_5967.RollingRingAssemblyCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5968,
            )

            return self._parent._cast(_5968.RollingRingCompoundHarmonicAnalysis)

        @property
        def root_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5970,
            )

            return self._parent._cast(_5970.RootAssemblyCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5971,
            )

            return self._parent._cast(_5971.ShaftCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5972,
            )

            return self._parent._cast(_5972.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5974,
            )

            return self._parent._cast(_5974.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5975,
            )

            return self._parent._cast(_5975.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def spring_damper_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5978,
            )

            return self._parent._cast(_5978.SpringDamperCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5980,
            )

            return self._parent._cast(_5980.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5981,
            )

            return self._parent._cast(
                _5981.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(
                _5983.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5986,
            )

            return self._parent._cast(
                _5986.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5987,
            )

            return self._parent._cast(
                _5987.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(
                _5988.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def synchroniser_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5989,
            )

            return self._parent._cast(_5989.SynchroniserCompoundHarmonicAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5990,
            )

            return self._parent._cast(_5990.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(_5991.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5992,
            )

            return self._parent._cast(_5992.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5993,
            )

            return self._parent._cast(_5993.TorqueConverterCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5995,
            )

            return self._parent._cast(_5995.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5996,
            )

            return self._parent._cast(
                _5996.TorqueConverterTurbineCompoundHarmonicAnalysis
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5997,
            )

            return self._parent._cast(_5997.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5998,
            )

            return self._parent._cast(_5998.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5999,
            )

            return self._parent._cast(_5999.WormGearCompoundHarmonicAnalysis)

        @property
        def worm_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6001,
            )

            return self._parent._cast(_6001.WormGearSetCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(_6002.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6004,
            )

            return self._parent._cast(_6004.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
        ) -> "PartCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_5785.PartHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PartHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5785.PartHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PartHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartCompoundHarmonicAnalysis._Cast_PartCompoundHarmonicAnalysis":
        return self._Cast_PartCompoundHarmonicAnalysis(self)
