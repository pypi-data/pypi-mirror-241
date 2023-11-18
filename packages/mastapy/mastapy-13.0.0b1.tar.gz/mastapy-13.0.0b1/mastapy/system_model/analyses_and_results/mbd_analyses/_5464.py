"""PartMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7546
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PartMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5462
    from mastapy.math_utility.convergence import _1573
    from mastapy.system_model.drawing import _2248


__docformat__ = "restructuredtext en"
__all__ = ("PartMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PartMultibodyDynamicsAnalysis")


class PartMultibodyDynamicsAnalysis(_7546.PartTimeSeriesLoadAnalysisCase):
    """PartMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartMultibodyDynamicsAnalysis")

    class _Cast_PartMultibodyDynamicsAnalysis:
        """Special nested class for casting PartMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
            parent: "PartMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_time_series_load_analysis_case(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5373

            return self._parent._cast(_5373.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5374

            return self._parent._cast(_5374.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5375

            return self._parent._cast(
                _5375.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378

            return self._parent._cast(
                _5378.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379

            return self._parent._cast(
                _5379.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5381

            return self._parent._cast(_5381.AssemblyMultibodyDynamicsAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382

            return self._parent._cast(_5382.BearingMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385

            return self._parent._cast(_5385.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(
                _5387.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388

            return self._parent._cast(
                _5388.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(
                _5389.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(
                _5390.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392

            return self._parent._cast(_5392.BevelGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393

            return self._parent._cast(_5393.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394

            return self._parent._cast(_5394.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def bolt_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5395

            return self._parent._cast(_5395.BoltMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398

            return self._parent._cast(_5398.ClutchMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(_5401.ComponentMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(
                _5403.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(_5415.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(_5417.CVTMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(_5424.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5426

            return self._parent._cast(
                _5426.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def datum_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427

            return self._parent._cast(_5427.DatumMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ExternalCADModelMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430

            return self._parent._cast(_5430.FaceGearMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431

            return self._parent._cast(_5431.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432

            return self._parent._cast(_5432.FEPartMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(
                _5433.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GearSetMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.GuideDxfModelMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440

            return self._parent._cast(_5440.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441

            return self._parent._cast(_5441.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(
                _5448.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(
                _5452.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5454

            return self._parent._cast(
                _5454.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455

            return self._parent._cast(
                _5455.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5456

            return self._parent._cast(_5456.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(
                _5460.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(
                _5466.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(
                _5467.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(_5469.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def planet_carrier_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(_5470.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(_5471.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(_5473.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5474

            return self._parent._cast(_5474.RingPinsMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476

            return self._parent._cast(
                _5476.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(_5478.RollingRingMultibodyDynamicsAnalysis)

        @property
        def root_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479

            return self._parent._cast(_5479.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(_5482.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483

            return self._parent._cast(_5483.ShaftMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(
                _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(_5489.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(_5492.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(
                _5494.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(
                _5495.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(_5497.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(
                _5499.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(
                _5500.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(_5501.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5502

            return self._parent._cast(_5502.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(_5503.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5504

            return self._parent._cast(_5504.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5507

            return self._parent._cast(_5507.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(
                _5508.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(_5511.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5512

            return self._parent._cast(_5512.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(_5515.WormGearMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5518

            return self._parent._cast(_5518.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "PartMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartMultibodyDynamicsAnalysis.TYPE"):
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
    def multibody_dynamics_analysis(self: Self) -> "_5462.MultibodyDynamicsAnalysis":
        """mastapy.system_model.analyses_and_results.mbd_analyses.MultibodyDynamicsAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MultibodyDynamicsAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def data_logger(self: Self) -> "_1573.DataLogger":
        """mastapy.math_utility.convergence.DataLogger

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2248.MBDAnalysisViewable":
        """mastapy.system_model.drawing.MBDAnalysisViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis":
        return self._Cast_PartMultibodyDynamicsAnalysis(self)
