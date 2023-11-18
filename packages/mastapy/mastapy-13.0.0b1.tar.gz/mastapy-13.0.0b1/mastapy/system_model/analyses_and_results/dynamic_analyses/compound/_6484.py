"""PartCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "PartCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="PartCompoundDynamicAnalysis")


class PartCompoundDynamicAnalysis(_7543.PartCompoundAnalysis):
    """PartCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundDynamicAnalysis")

    class _Cast_PartCompoundDynamicAnalysis:
        """Special nested class for casting PartCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
            parent: "PartCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6405,
            )

            return self._parent._cast(_6405.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6406,
            )

            return self._parent._cast(_6406.AbstractShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6407,
            )

            return self._parent._cast(
                _6407.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6409,
            )

            return self._parent._cast(
                _6409.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6411,
            )

            return self._parent._cast(
                _6411.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(_6412.AssemblyCompoundDynamicAnalysis)

        @property
        def bearing_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6413,
            )

            return self._parent._cast(_6413.BearingCompoundDynamicAnalysis)

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6415,
            )

            return self._parent._cast(_6415.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(
                _6416.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6418,
            )

            return self._parent._cast(
                _6418.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6419,
            )

            return self._parent._cast(
                _6419.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(
                _6420.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(_6421.BevelGearCompoundDynamicAnalysis)

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6423,
            )

            return self._parent._cast(_6423.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolt_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(_6424.BoltCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6425,
            )

            return self._parent._cast(_6425.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6426,
            )

            return self._parent._cast(_6426.ClutchCompoundDynamicAnalysis)

        @property
        def clutch_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6428,
            )

            return self._parent._cast(_6428.ClutchHalfCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.ComponentCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6431,
            )

            return self._parent._cast(_6431.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(_6434.ConceptGearCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6437,
            )

            return self._parent._cast(_6437.ConicalGearCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6439,
            )

            return self._parent._cast(_6439.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ConnectorCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.CouplingCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6444,
            )

            return self._parent._cast(_6444.CouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(_6446.CVTCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.CVTPulleyCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6448,
            )

            return self._parent._cast(_6448.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6450,
            )

            return self._parent._cast(_6450.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6452,
            )

            return self._parent._cast(_6452.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(_6454.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6455,
            )

            return self._parent._cast(
                _6455.CylindricalPlanetGearCompoundDynamicAnalysis
            )

        @property
        def datum_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6456,
            )

            return self._parent._cast(_6456.DatumCompoundDynamicAnalysis)

        @property
        def external_cad_model_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6457,
            )

            return self._parent._cast(_6457.ExternalCADModelCompoundDynamicAnalysis)

        @property
        def face_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6458,
            )

            return self._parent._cast(_6458.FaceGearCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6460,
            )

            return self._parent._cast(_6460.FaceGearSetCompoundDynamicAnalysis)

        @property
        def fe_part_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(_6461.FEPartCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6463,
            )

            return self._parent._cast(_6463.GearCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6465,
            )

            return self._parent._cast(_6465.GearSetCompoundDynamicAnalysis)

        @property
        def guide_dxf_model_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.GuideDxfModelCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.HypoidGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(_6469.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6471,
            )

            return self._parent._cast(
                _6471.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(
                _6473.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(
                _6474.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(
                _6476.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6477,
            )

            return self._parent._cast(
                _6477.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(
                _6479.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6480,
            )

            return self._parent._cast(_6480.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(_6481.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.MountableComponentCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6483,
            )

            return self._parent._cast(_6483.OilSealCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(
                _6485.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(
                _6487.PartToPartShearCouplingHalfCompoundDynamicAnalysis
            )

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(_6489.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def planet_carrier_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(_6490.PlanetCarrierCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6491,
            )

            return self._parent._cast(_6491.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(_6492.PowerLoadCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.PulleyCompoundDynamicAnalysis)

        @property
        def ring_pins_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(_6494.RingPinsCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6496,
            )

            return self._parent._cast(_6496.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6497,
            )

            return self._parent._cast(_6497.RollingRingCompoundDynamicAnalysis)

        @property
        def root_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(_6499.RootAssemblyCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6500,
            )

            return self._parent._cast(_6500.ShaftCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(_6501.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6503,
            )

            return self._parent._cast(_6503.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(_6504.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6507,
            )

            return self._parent._cast(_6507.SpringDamperCompoundDynamicAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6510,
            )

            return self._parent._cast(
                _6510.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(
                _6512.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(_6515.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6516,
            )

            return self._parent._cast(
                _6516.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(_6517.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.SynchroniserCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6519,
            )

            return self._parent._cast(_6519.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(_6521.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6522,
            )

            return self._parent._cast(_6522.TorqueConverterCompoundDynamicAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(_6524.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(
                _6525.TorqueConverterTurbineCompoundDynamicAnalysis
            )

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(_6526.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.VirtualComponentCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6528,
            )

            return self._parent._cast(_6528.WormGearCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6530,
            )

            return self._parent._cast(_6530.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6531,
            )

            return self._parent._cast(_6531.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6533,
            )

            return self._parent._cast(_6533.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
        ) -> "PartCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_6355.PartDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PartDynamicAnalysis]

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
    def component_analysis_cases_ready(self: Self) -> "List[_6355.PartDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PartDynamicAnalysis]

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
    ) -> "PartCompoundDynamicAnalysis._Cast_PartCompoundDynamicAnalysis":
        return self._Cast_PartCompoundDynamicAnalysis(self)
