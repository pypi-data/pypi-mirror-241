"""PartModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "PartModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5191,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PartModalAnalysisAtASpeed")


class PartModalAnalysisAtASpeed(_7545.PartStaticLoadAnalysisCase):
    """PartModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartModalAnalysisAtASpeed")

    class _Cast_PartModalAnalysisAtASpeed:
        """Special nested class for casting PartModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
            parent: "PartModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5114,
            )

            return self._parent._cast(_5114.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_shaft_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5115,
            )

            return self._parent._cast(_5115.AbstractShaftModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5116,
            )

            return self._parent._cast(_5116.AbstractShaftOrHousingModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5119,
            )

            return self._parent._cast(_5119.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5120,
            )

            return self._parent._cast(
                _5120.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def assembly_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5121,
            )

            return self._parent._cast(_5121.AssemblyModalAnalysisAtASpeed)

        @property
        def bearing_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5122,
            )

            return self._parent._cast(_5122.BearingModalAnalysisAtASpeed)

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5124,
            )

            return self._parent._cast(_5124.BeltDriveModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5126,
            )

            return self._parent._cast(_5126.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5127,
            )

            return self._parent._cast(
                _5127.BevelDifferentialGearSetModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5128,
            )

            return self._parent._cast(
                _5128.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5129,
            )

            return self._parent._cast(
                _5129.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5131,
            )

            return self._parent._cast(_5131.BevelGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5132,
            )

            return self._parent._cast(_5132.BevelGearSetModalAnalysisAtASpeed)

        @property
        def bolted_joint_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5133,
            )

            return self._parent._cast(_5133.BoltedJointModalAnalysisAtASpeed)

        @property
        def bolt_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5134,
            )

            return self._parent._cast(_5134.BoltModalAnalysisAtASpeed)

        @property
        def clutch_half_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5136,
            )

            return self._parent._cast(_5136.ClutchHalfModalAnalysisAtASpeed)

        @property
        def clutch_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5137,
            )

            return self._parent._cast(_5137.ClutchModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5139,
            )

            return self._parent._cast(_5139.ComponentModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(_5141.ConceptCouplingHalfModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(_5144.ConceptGearModalAnalysisAtASpeed)

        @property
        def concept_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(_5145.ConceptGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5147,
            )

            return self._parent._cast(_5147.ConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ConnectorModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.CouplingHalfModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5153,
            )

            return self._parent._cast(_5153.CouplingModalAnalysisAtASpeed)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(_5155.CVTModalAnalysisAtASpeed)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5156,
            )

            return self._parent._cast(_5156.CVTPulleyModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5157,
            )

            return self._parent._cast(_5157.CycloidalAssemblyModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5159,
            )

            return self._parent._cast(_5159.CycloidalDiscModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5162,
            )

            return self._parent._cast(_5162.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5164,
            )

            return self._parent._cast(_5164.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def datum_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(_5165.DatumModalAnalysisAtASpeed)

        @property
        def external_cad_model_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5166,
            )

            return self._parent._cast(_5166.ExternalCADModelModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5168,
            )

            return self._parent._cast(_5168.FaceGearModalAnalysisAtASpeed)

        @property
        def face_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5169,
            )

            return self._parent._cast(_5169.FaceGearSetModalAnalysisAtASpeed)

        @property
        def fe_part_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5170,
            )

            return self._parent._cast(_5170.FEPartModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5171,
            )

            return self._parent._cast(_5171.FlexiblePinAssemblyModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.GearModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5174,
            )

            return self._parent._cast(_5174.GearSetModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.GuideDxfModelModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.HypoidGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5178,
            )

            return self._parent._cast(_5178.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5181,
            )

            return self._parent._cast(
                _5181.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(
                _5182.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5184,
            )

            return self._parent._cast(
                _5184.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5185,
            )

            return self._parent._cast(
                _5185.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5187,
            )

            return self._parent._cast(
                _5187.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(
                _5188.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
            )

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5189,
            )

            return self._parent._cast(_5189.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(_5190.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5192,
            )

            return self._parent._cast(_5192.MountableComponentModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.OilSealModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(
                _5196.PartToPartShearCouplingHalfModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(
                _5197.PartToPartShearCouplingModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def planet_carrier_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5200,
            )

            return self._parent._cast(_5200.PlanetCarrierModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5201,
            )

            return self._parent._cast(_5201.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.PowerLoadModalAnalysisAtASpeed)

        @property
        def pulley_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.PulleyModalAnalysisAtASpeed)

        @property
        def ring_pins_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5204,
            )

            return self._parent._cast(_5204.RingPinsModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5206,
            )

            return self._parent._cast(_5206.RollingRingAssemblyModalAnalysisAtASpeed)

        @property
        def rolling_ring_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5208,
            )

            return self._parent._cast(_5208.RollingRingModalAnalysisAtASpeed)

        @property
        def root_assembly_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5209,
            )

            return self._parent._cast(_5209.RootAssemblyModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5210,
            )

            return self._parent._cast(_5210.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def shaft_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5211,
            )

            return self._parent._cast(_5211.ShaftModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5215,
            )

            return self._parent._cast(_5215.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def spring_damper_half_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.SpringDamperHalfModalAnalysisAtASpeed)

        @property
        def spring_damper_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5219,
            )

            return self._parent._cast(_5219.SpringDamperModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5221,
            )

            return self._parent._cast(_5221.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5222,
            )

            return self._parent._cast(
                _5222.StraightBevelDiffGearSetModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5224,
            )

            return self._parent._cast(_5224.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5225,
            )

            return self._parent._cast(_5225.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5226,
            )

            return self._parent._cast(
                _5226.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5227,
            )

            return self._parent._cast(_5227.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5228,
            )

            return self._parent._cast(_5228.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5229,
            )

            return self._parent._cast(_5229.SynchroniserModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5230,
            )

            return self._parent._cast(_5230.SynchroniserPartModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5231,
            )

            return self._parent._cast(_5231.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def torque_converter_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5233,
            )

            return self._parent._cast(_5233.TorqueConverterModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5234,
            )

            return self._parent._cast(_5234.TorqueConverterPumpModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5235,
            )

            return self._parent._cast(_5235.TorqueConverterTurbineModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5236,
            )

            return self._parent._cast(_5236.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5237,
            )

            return self._parent._cast(_5237.VirtualComponentModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5239,
            )

            return self._parent._cast(_5239.WormGearModalAnalysisAtASpeed)

        @property
        def worm_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5240,
            )

            return self._parent._cast(_5240.WormGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5242,
            )

            return self._parent._cast(_5242.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5243,
            )

            return self._parent._cast(_5243.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed",
        ) -> "PartModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartModalAnalysisAtASpeed.TYPE"):
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
    def modal_analysis_at_a_speed(self: Self) -> "_5191.ModalAnalysisAtASpeed":
        """mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ModalAnalysisAtASpeed

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysisAtASpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartModalAnalysisAtASpeed._Cast_PartModalAnalysisAtASpeed":
        return self._Cast_PartModalAnalysisAtASpeed(self)
