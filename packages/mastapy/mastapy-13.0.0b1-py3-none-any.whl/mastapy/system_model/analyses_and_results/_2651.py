"""DesignEntitySingleContextAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2649
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY_SINGLE_CONTEXT_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "DesignEntitySingleContextAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("DesignEntitySingleContextAnalysis",)


Self = TypeVar("Self", bound="DesignEntitySingleContextAnalysis")


class DesignEntitySingleContextAnalysis(_2649.DesignEntityAnalysis):
    """DesignEntitySingleContextAnalysis

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY_SINGLE_CONTEXT_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignEntitySingleContextAnalysis")

    class _Cast_DesignEntitySingleContextAnalysis:
        """Special nested class for casting DesignEntitySingleContextAnalysis to subclasses."""

        def __init__(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
            parent: "DesignEntitySingleContextAnalysis",
        ):
            self._parent = parent

        @property
        def design_entity_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def connection_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def part_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2683,
            )

            return self._parent._cast(_2683.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2684,
            )

            return self._parent._cast(_2684.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2685,
            )

            return self._parent._cast(_2685.AbstractShaftSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2686,
            )

            return self._parent._cast(
                _2686.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2690,
            )

            return self._parent._cast(_2690.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2696,
            )

            return self._parent._cast(_2696.BearingSystemDeflection)

        @property
        def belt_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2697,
            )

            return self._parent._cast(_2697.BeltConnectionSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2698,
            )

            return self._parent._cast(_2698.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2703,
            )

            return self._parent._cast(_2703.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelGearMeshSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.BoltSystemDeflection)

        @property
        def clutch_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.ClutchConnectionSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.ClutchSystemDeflection)

        @property
        def coaxial_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.CoaxialConnectionSystemDeflection)

        @property
        def component_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ConceptCouplingConnectionSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2718,
            )

            return self._parent._cast(_2718.ConceptGearMeshSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ConceptGearSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConicalGearMeshSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConicalGearSystemDeflection)

        @property
        def connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConnectionSystemDeflection)

        @property
        def connector_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConnectorSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.CouplingConnectionSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.CouplingSystemDeflection)

        @property
        def cvt_belt_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.CVTBeltConnectionSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(
                _2734.CycloidalDiscCentralBearingConnectionSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(
                _2735.CycloidalDiscPlanetaryBearingConnectionSystemDeflection
            )

        @property
        def cycloidal_disc_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2737,
            )

            return self._parent._cast(_2737.CylindricalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2739,
            )

            return self._parent._cast(
                _2739.CylindricalGearMeshSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(_2741.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(
                _2742.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(
                _2745.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ExternalCADModelSystemDeflection)

        @property
        def face_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.FaceGearMeshSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(_2755.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.GearMeshSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.GearSetSystemDeflection)

        @property
        def gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2760,
            )

            return self._parent._cast(_2760.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.HypoidGearMeshSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.HypoidGearSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(
                _2765.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(
                _2766.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(
                _2768.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(
                _2769.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(
                _2771.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(
                _2774.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(_2777.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(_2778.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.OilSealSystemDeflection)

        @property
        def part_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(
                _2784.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.PartToPartShearCouplingSystemDeflection)

        @property
        def planetary_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PlanetaryConnectionSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(_2789.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(_2791.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.RingPinsSystemDeflection)

        @property
        def ring_pins_to_disc_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.RingPinsToDiscConnectionSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(_2796.RollingRingConnectionSystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(_2797.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(_2798.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.ShaftSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(
                _2803.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def specialised_assembly_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.SpiralBevelGearMeshSystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpringDamperConnectionSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.StraightBevelGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.SynchroniserSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.TorqueConverterConnectionSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.VirtualComponentSystemDeflection)

        @property
        def worm_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.WormGearMeshSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.ZerolBevelGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.ZerolBevelGearSystemDeflection)

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2981,
            )

            return self._parent._cast(
                _2981.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2982,
            )

            return self._parent._cast(
                _2982.AbstractShaftOrHousingSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2983,
            )

            return self._parent._cast(_2983.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2984,
            )

            return self._parent._cast(
                _2984.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2985,
            )

            return self._parent._cast(
                _2985.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2986,
            )

            return self._parent._cast(
                _2986.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2987,
            )

            return self._parent._cast(
                _2987.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def assembly_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2988,
            )

            return self._parent._cast(_2988.AssemblySteadyStateSynchronousResponse)

        @property
        def bearing_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2989,
            )

            return self._parent._cast(_2989.BearingSteadyStateSynchronousResponse)

        @property
        def belt_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2990,
            )

            return self._parent._cast(
                _2990.BeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def belt_drive_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(_2991.BeltDriveSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2992,
            )

            return self._parent._cast(
                _2992.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2993,
            )

            return self._parent._cast(
                _2993.BevelDifferentialGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2994,
            )

            return self._parent._cast(
                _2994.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2995,
            )

            return self._parent._cast(
                _2995.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2996,
            )

            return self._parent._cast(
                _2996.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2997,
            )

            return self._parent._cast(_2997.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2998,
            )

            return self._parent._cast(_2998.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2999,
            )

            return self._parent._cast(_2999.BevelGearSteadyStateSynchronousResponse)

        @property
        def bolted_joint_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3000,
            )

            return self._parent._cast(_3000.BoltedJointSteadyStateSynchronousResponse)

        @property
        def bolt_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3001,
            )

            return self._parent._cast(_3001.BoltSteadyStateSynchronousResponse)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3002,
            )

            return self._parent._cast(
                _3002.ClutchConnectionSteadyStateSynchronousResponse
            )

        @property
        def clutch_half_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3003,
            )

            return self._parent._cast(_3003.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def clutch_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(_3004.ClutchSteadyStateSynchronousResponse)

        @property
        def coaxial_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(
                _3005.CoaxialConnectionSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(_3006.ComponentSteadyStateSynchronousResponse)

        @property
        def concept_coupling_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3007,
            )

            return self._parent._cast(
                _3007.ConceptCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3008,
            )

            return self._parent._cast(
                _3008.ConceptCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3009,
            )

            return self._parent._cast(
                _3009.ConceptCouplingSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(
                _3010.ConceptGearMeshSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3011,
            )

            return self._parent._cast(
                _3011.ConceptGearSetSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(_3012.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(
                _3013.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(
                _3014.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(_3015.ConicalGearSteadyStateSynchronousResponse)

        @property
        def connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ConnectionSteadyStateSynchronousResponse)

        @property
        def connector_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3017,
            )

            return self._parent._cast(_3017.ConnectorSteadyStateSynchronousResponse)

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(
                _3018.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3019,
            )

            return self._parent._cast(_3019.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def coupling_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(_3020.CouplingSteadyStateSynchronousResponse)

        @property
        def cvt_belt_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3021,
            )

            return self._parent._cast(
                _3021.CVTBeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3022,
            )

            return self._parent._cast(_3022.CVTPulleySteadyStateSynchronousResponse)

        @property
        def cvt_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(_3023.CVTSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3024,
            )

            return self._parent._cast(
                _3024.CycloidalAssemblySteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(
                _3025.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(
                _3026.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3027,
            )

            return self._parent._cast(_3027.CycloidalDiscSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3028,
            )

            return self._parent._cast(
                _3028.CylindricalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(
                _3029.CylindricalGearSetSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3030,
            )

            return self._parent._cast(
                _3030.CylindricalGearSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(
                _3031.CylindricalPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def datum_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3032,
            )

            return self._parent._cast(_3032.DatumSteadyStateSynchronousResponse)

        @property
        def external_cad_model_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3034,
            )

            return self._parent._cast(
                _3034.ExternalCADModelSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3035,
            )

            return self._parent._cast(_3035.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def face_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3036,
            )

            return self._parent._cast(_3036.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def face_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3037,
            )

            return self._parent._cast(_3037.FaceGearSteadyStateSynchronousResponse)

        @property
        def fe_part_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3038,
            )

            return self._parent._cast(_3038.FEPartSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(
                _3039.FlexiblePinAssemblySteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.GearMeshSteadyStateSynchronousResponse)

        @property
        def gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.GearSetSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3042,
            )

            return self._parent._cast(_3042.GearSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3043,
            )

            return self._parent._cast(_3043.GuideDxfModelSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3044,
            )

            return self._parent._cast(
                _3044.HypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(_3046.HypoidGearSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(
                _3047.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3048,
            )

            return self._parent._cast(
                _3048.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3049,
            )

            return self._parent._cast(
                _3049.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3050,
            )

            return self._parent._cast(
                _3050.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3051,
            )

            return self._parent._cast(
                _3051.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(
                _3052.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3053,
            )

            return self._parent._cast(
                _3053.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3055,
            )

            return self._parent._cast(
                _3055.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(
                _3056.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(_3057.MassDiscSteadyStateSynchronousResponse)

        @property
        def measurement_component_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.MeasurementComponentSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(
                _3059.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.OilSealSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.PartSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3062,
            )

            return self._parent._cast(
                _3062.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(
                _3063.PartToPartShearCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(
                _3064.PartToPartShearCouplingSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(
                _3065.PlanetaryConnectionSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(
                _3066.PlanetaryGearSetSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3067,
            )

            return self._parent._cast(_3067.PlanetCarrierSteadyStateSynchronousResponse)

        @property
        def point_load_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3068,
            )

            return self._parent._cast(_3068.PointLoadSteadyStateSynchronousResponse)

        @property
        def power_load_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3069,
            )

            return self._parent._cast(_3069.PowerLoadSteadyStateSynchronousResponse)

        @property
        def pulley_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3070,
            )

            return self._parent._cast(_3070.PulleySteadyStateSynchronousResponse)

        @property
        def ring_pins_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.RingPinsSteadyStateSynchronousResponse)

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(
                _3072.RingPinsToDiscConnectionSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3073,
            )

            return self._parent._cast(
                _3073.RollingRingAssemblySteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3074,
            )

            return self._parent._cast(
                _3074.RollingRingConnectionSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3075,
            )

            return self._parent._cast(_3075.RollingRingSteadyStateSynchronousResponse)

        @property
        def root_assembly_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3076,
            )

            return self._parent._cast(_3076.RootAssemblySteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3077,
            )

            return self._parent._cast(
                _3077.ShaftHubConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3078,
            )

            return self._parent._cast(_3078.ShaftSteadyStateSynchronousResponse)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(
                _3079.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3080,
            )

            return self._parent._cast(
                _3080.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3081,
            )

            return self._parent._cast(
                _3081.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.SpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3083,
            )

            return self._parent._cast(
                _3083.SpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.SpringDamperConnectionSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3085,
            )

            return self._parent._cast(
                _3085.SpringDamperHalfSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.SpringDamperSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(
                _3090.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3091,
            )

            return self._parent._cast(
                _3091.StraightBevelDiffGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3092,
            )

            return self._parent._cast(
                _3092.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(
                _3093.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3094,
            )

            return self._parent._cast(
                _3094.StraightBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3095,
            )

            return self._parent._cast(
                _3095.StraightBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3096,
            )

            return self._parent._cast(
                _3096.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3097,
            )

            return self._parent._cast(
                _3097.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3098,
            )

            return self._parent._cast(
                _3098.SynchroniserHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3099,
            )

            return self._parent._cast(
                _3099.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3100,
            )

            return self._parent._cast(
                _3100.SynchroniserSleeveSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3101,
            )

            return self._parent._cast(_3101.SynchroniserSteadyStateSynchronousResponse)

        @property
        def torque_converter_connection_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3102,
            )

            return self._parent._cast(
                _3102.TorqueConverterConnectionSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(
                _3103.TorqueConverterPumpSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3104,
            )

            return self._parent._cast(
                _3104.TorqueConverterSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.TorqueConverterTurbineSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.UnbalancedMassSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3107,
            )

            return self._parent._cast(
                _3107.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3108,
            )

            return self._parent._cast(_3108.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def worm_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3109,
            )

            return self._parent._cast(_3109.WormGearSetSteadyStateSynchronousResponse)

        @property
        def worm_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3110,
            )

            return self._parent._cast(_3110.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(
                _3111.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3112,
            )

            return self._parent._cast(
                _3112.ZerolBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3113,
            )

            return self._parent._cast(
                _3113.ZerolBevelGearSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3243,
            )

            return self._parent._cast(
                _3243.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3244,
            )

            return self._parent._cast(
                _3244.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3245,
            )

            return self._parent._cast(
                _3245.AbstractShaftSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3246,
            )

            return self._parent._cast(
                _3246.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3247,
            )

            return self._parent._cast(
                _3247.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3248,
            )

            return self._parent._cast(
                _3248.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3249,
            )

            return self._parent._cast(
                _3249.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3250,
            )

            return self._parent._cast(
                _3250.AssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3251,
            )

            return self._parent._cast(
                _3251.BearingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3252,
            )

            return self._parent._cast(
                _3252.BeltConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3253,
            )

            return self._parent._cast(
                _3253.BeltDriveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3254,
            )

            return self._parent._cast(
                _3254.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3255,
            )

            return self._parent._cast(
                _3255.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3256,
            )

            return self._parent._cast(
                _3256.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3257,
            )

            return self._parent._cast(
                _3257.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3258,
            )

            return self._parent._cast(
                _3258.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3259,
            )

            return self._parent._cast(
                _3259.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3260,
            )

            return self._parent._cast(
                _3260.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3261,
            )

            return self._parent._cast(
                _3261.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3262,
            )

            return self._parent._cast(
                _3262.BoltedJointSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolt_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3263,
            )

            return self._parent._cast(_3263.BoltSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3264,
            )

            return self._parent._cast(
                _3264.ClutchConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3265,
            )

            return self._parent._cast(
                _3265.ClutchHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3266,
            )

            return self._parent._cast(
                _3266.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coaxial_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3267,
            )

            return self._parent._cast(
                _3267.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3269,
            )

            return self._parent._cast(
                _3269.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3271,
            )

            return self._parent._cast(
                _3271.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3272,
            )

            return self._parent._cast(
                _3272.ConceptGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.ConceptGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3274,
            )

            return self._parent._cast(
                _3274.ConceptGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3275,
            )

            return self._parent._cast(
                _3275.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3276,
            )

            return self._parent._cast(
                _3276.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3277,
            )

            return self._parent._cast(
                _3277.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3279,
            )

            return self._parent._cast(
                _3279.ConnectorSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.CouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3281,
            )

            return self._parent._cast(
                _3281.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3282,
            )

            return self._parent._cast(
                _3282.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3283,
            )

            return self._parent._cast(
                _3283.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3284,
            )

            return self._parent._cast(
                _3284.CVTPulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3285,
            )

            return self._parent._cast(_3285.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3286,
            )

            return self._parent._cast(
                _3286.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(
                _3287.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3289,
            )

            return self._parent._cast(
                _3289.CycloidalDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3290,
            )

            return self._parent._cast(
                _3290.CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3292,
            )

            return self._parent._cast(
                _3292.CylindricalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3293,
            )

            return self._parent._cast(
                _3293.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def datum_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3294,
            )

            return self._parent._cast(_3294.DatumSteadyStateSynchronousResponseOnAShaft)

        @property
        def external_cad_model_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3295,
            )

            return self._parent._cast(
                _3295.ExternalCADModelSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3296,
            )

            return self._parent._cast(
                _3296.FaceGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3297,
            )

            return self._parent._cast(
                _3297.FaceGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3298,
            )

            return self._parent._cast(
                _3298.FaceGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3299,
            )

            return self._parent._cast(
                _3299.FEPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3300,
            )

            return self._parent._cast(
                _3300.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(
                _3302.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3303,
            )

            return self._parent._cast(_3303.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def guide_dxf_model_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3304,
            )

            return self._parent._cast(
                _3304.GuideDxfModelSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3305,
            )

            return self._parent._cast(
                _3305.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3306,
            )

            return self._parent._cast(
                _3306.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(
                _3307.HypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3308,
            )

            return self._parent._cast(
                _3308.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3309,
            )

            return self._parent._cast(
                _3309.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3310,
            )

            return self._parent._cast(
                _3310.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3311,
            )

            return self._parent._cast(
                _3311.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3313,
            )

            return self._parent._cast(
                _3313.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3314,
            )

            return self._parent._cast(
                _3314.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3315,
            )

            return self._parent._cast(
                _3315.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3316,
            )

            return self._parent._cast(
                _3316.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3317,
            )

            return self._parent._cast(
                _3317.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.MassDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3319,
            )

            return self._parent._cast(
                _3319.MeasurementComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3320,
            )

            return self._parent._cast(
                _3320.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(
                _3321.OilSealSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(_3322.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3323,
            )

            return self._parent._cast(
                _3323.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3325,
            )

            return self._parent._cast(
                _3325.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(
                _3326.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3328,
            )

            return self._parent._cast(
                _3328.PlanetCarrierSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3329,
            )

            return self._parent._cast(
                _3329.PointLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3330,
            )

            return self._parent._cast(
                _3330.PowerLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3331,
            )

            return self._parent._cast(
                _3331.PulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(
                _3332.RingPinsSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3333,
            )

            return self._parent._cast(
                _3333.RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3334,
            )

            return self._parent._cast(
                _3334.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3335,
            )

            return self._parent._cast(
                _3335.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3336,
            )

            return self._parent._cast(
                _3336.RollingRingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3337,
            )

            return self._parent._cast(
                _3337.RootAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3338,
            )

            return self._parent._cast(
                _3338.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3339,
            )

            return self._parent._cast(_3339.ShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3340,
            )

            return self._parent._cast(
                _3340.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3342,
            )

            return self._parent._cast(
                _3342.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3344,
            )

            return self._parent._cast(
                _3344.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(
                _3345.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3346,
            )

            return self._parent._cast(
                _3346.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(
                _3347.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3350,
            )

            return self._parent._cast(
                _3350.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3351,
            )

            return self._parent._cast(
                _3351.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3353,
            )

            return self._parent._cast(
                _3353.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3354,
            )

            return self._parent._cast(
                _3354.StraightBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3355,
            )

            return self._parent._cast(
                _3355.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3356,
            )

            return self._parent._cast(
                _3356.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3357,
            )

            return self._parent._cast(
                _3357.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3358,
            )

            return self._parent._cast(
                _3358.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3359,
            )

            return self._parent._cast(
                _3359.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3360,
            )

            return self._parent._cast(
                _3360.SynchroniserSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3361,
            )

            return self._parent._cast(
                _3361.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3362,
            )

            return self._parent._cast(
                _3362.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3363,
            )

            return self._parent._cast(
                _3363.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3364,
            )

            return self._parent._cast(
                _3364.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3365,
            )

            return self._parent._cast(
                _3365.UnbalancedMassSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3366,
            )

            return self._parent._cast(
                _3366.VirtualComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3367,
            )

            return self._parent._cast(
                _3367.WormGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3368,
            )

            return self._parent._cast(
                _3368.WormGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3369,
            )

            return self._parent._cast(
                _3369.WormGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3370,
            )

            return self._parent._cast(
                _3370.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3371,
            )

            return self._parent._cast(
                _3371.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3372,
            )

            return self._parent._cast(
                _3372.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3502,
            )

            return self._parent._cast(
                _3502.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3503,
            )

            return self._parent._cast(
                _3503.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3504,
            )

            return self._parent._cast(
                _3504.AbstractShaftSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3505,
            )

            return self._parent._cast(
                _3505.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3506,
            )

            return self._parent._cast(
                _3506.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3507,
            )

            return self._parent._cast(
                _3507.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3508,
            )

            return self._parent._cast(
                _3508.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3509,
            )

            return self._parent._cast(
                _3509.AssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3510,
            )

            return self._parent._cast(
                _3510.BearingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3511,
            )

            return self._parent._cast(
                _3511.BeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3512,
            )

            return self._parent._cast(
                _3512.BeltDriveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3513,
            )

            return self._parent._cast(
                _3513.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3514,
            )

            return self._parent._cast(
                _3514.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3515,
            )

            return self._parent._cast(
                _3515.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3516,
            )

            return self._parent._cast(
                _3516.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3517,
            )

            return self._parent._cast(
                _3517.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3518,
            )

            return self._parent._cast(
                _3518.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3519,
            )

            return self._parent._cast(
                _3519.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3520,
            )

            return self._parent._cast(
                _3520.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3521,
            )

            return self._parent._cast(
                _3521.BoltedJointSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3522,
            )

            return self._parent._cast(_3522.BoltSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3523,
            )

            return self._parent._cast(
                _3523.ClutchConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3524,
            )

            return self._parent._cast(
                _3524.ClutchHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3525,
            )

            return self._parent._cast(
                _3525.ClutchSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coaxial_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3527,
            )

            return self._parent._cast(
                _3527.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3528,
            )

            return self._parent._cast(
                _3528.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3530,
            )

            return self._parent._cast(
                _3530.ConceptCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3532,
            )

            return self._parent._cast(
                _3532.ConceptGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3533,
            )

            return self._parent._cast(
                _3533.ConceptGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3534,
            )

            return self._parent._cast(
                _3534.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3536,
            )

            return self._parent._cast(
                _3536.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3538,
            )

            return self._parent._cast(
                _3538.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3541,
            )

            return self._parent._cast(
                _3541.CouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3543,
            )

            return self._parent._cast(
                _3543.CVTPulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3544,
            )

            return self._parent._cast(_3544.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3545,
            )

            return self._parent._cast(
                _3545.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3546,
            )

            return self._parent._cast(
                _3546.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3548,
            )

            return self._parent._cast(
                _3548.CycloidalDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3549,
            )

            return self._parent._cast(
                _3549.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3551,
            )

            return self._parent._cast(
                _3551.CylindricalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3553,
            )

            return self._parent._cast(_3553.DatumSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3554,
            )

            return self._parent._cast(
                _3554.ExternalCADModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3555,
            )

            return self._parent._cast(
                _3555.FaceGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3556,
            )

            return self._parent._cast(
                _3556.FaceGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3557,
            )

            return self._parent._cast(
                _3557.FaceGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3558,
            )

            return self._parent._cast(
                _3558.FEPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3559,
            )

            return self._parent._cast(
                _3559.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(
                _3561.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(_3562.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3563,
            )

            return self._parent._cast(
                _3563.GuideDxfModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(
                _3564.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3565,
            )

            return self._parent._cast(
                _3565.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(
                _3566.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3567,
            )

            return self._parent._cast(
                _3567.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3568,
            )

            return self._parent._cast(
                _3568.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3569,
            )

            return self._parent._cast(
                _3569.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3570,
            )

            return self._parent._cast(
                _3570.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3572,
            )

            return self._parent._cast(
                _3572.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3573,
            )

            return self._parent._cast(
                _3573.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3574,
            )

            return self._parent._cast(
                _3574.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3576,
            )

            return self._parent._cast(
                _3576.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3577,
            )

            return self._parent._cast(
                _3577.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(
                _3580.OilSealSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(_3581.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3584,
            )

            return self._parent._cast(
                _3584.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3586,
            )

            return self._parent._cast(
                _3586.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(
                _3587.PlanetCarrierSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3588,
            )

            return self._parent._cast(
                _3588.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3590,
            )

            return self._parent._cast(
                _3590.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(
                _3591.RingPinsSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3592,
            )

            return self._parent._cast(
                _3592.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3593,
            )

            return self._parent._cast(
                _3593.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3594,
            )

            return self._parent._cast(
                _3594.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3595,
            )

            return self._parent._cast(
                _3595.RollingRingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3596,
            )

            return self._parent._cast(
                _3596.RootAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3597,
            )

            return self._parent._cast(
                _3597.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3598,
            )

            return self._parent._cast(_3598.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3600,
            )

            return self._parent._cast(
                _3600.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3603,
            )

            return self._parent._cast(
                _3603.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3605,
            )

            return self._parent._cast(
                _3605.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(
                _3606.SpringDamperSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3608,
            )

            return self._parent._cast(
                _3608.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3609,
            )

            return self._parent._cast(
                _3609.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3610,
            )

            return self._parent._cast(
                _3610.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3611,
            )

            return self._parent._cast(
                _3611.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3613,
            )

            return self._parent._cast(
                _3613.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3614,
            )

            return self._parent._cast(
                _3614.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3615,
            )

            return self._parent._cast(
                _3615.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3617,
            )

            return self._parent._cast(
                _3617.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3618,
            )

            return self._parent._cast(
                _3618.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3619,
            )

            return self._parent._cast(
                _3619.SynchroniserSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3621,
            )

            return self._parent._cast(
                _3621.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.TorqueConverterSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3623,
            )

            return self._parent._cast(
                _3623.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3624,
            )

            return self._parent._cast(
                _3624.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3625,
            )

            return self._parent._cast(
                _3625.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.WormGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3627,
            )

            return self._parent._cast(
                _3627.WormGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3628,
            )

            return self._parent._cast(
                _3628.WormGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3630,
            )

            return self._parent._cast(
                _3630.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3631,
            )

            return self._parent._cast(
                _3631.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3761,
            )

            return self._parent._cast(_3761.AbstractAssemblyStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3762,
            )

            return self._parent._cast(_3762.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3763,
            )

            return self._parent._cast(_3763.AbstractShaftStabilityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3764,
            )

            return self._parent._cast(
                _3764.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3766,
            )

            return self._parent._cast(_3766.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3767,
            )

            return self._parent._cast(_3767.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def assembly_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3768,
            )

            return self._parent._cast(_3768.AssemblyStabilityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3769,
            )

            return self._parent._cast(_3769.BearingStabilityAnalysis)

        @property
        def belt_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3770,
            )

            return self._parent._cast(_3770.BeltConnectionStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3772,
            )

            return self._parent._cast(_3772.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3773,
            )

            return self._parent._cast(_3773.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3774,
            )

            return self._parent._cast(_3774.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3775,
            )

            return self._parent._cast(
                _3775.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3776,
            )

            return self._parent._cast(_3776.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(_3777.BevelGearMeshStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelGearSetStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3779,
            )

            return self._parent._cast(_3779.BevelGearStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3780,
            )

            return self._parent._cast(_3780.BoltedJointStabilityAnalysis)

        @property
        def bolt_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3781,
            )

            return self._parent._cast(_3781.BoltStabilityAnalysis)

        @property
        def clutch_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3782,
            )

            return self._parent._cast(_3782.ClutchConnectionStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.ClutchHalfStabilityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.ClutchStabilityAnalysis)

        @property
        def coaxial_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.CoaxialConnectionStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3789,
            )

            return self._parent._cast(_3789.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ConceptGearMeshStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.ConceptGearSetStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.ConicalGearMeshStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.ConicalGearStabilityAnalysis)

        @property
        def connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ConnectionStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.ConnectorStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.CouplingConnectionStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.CouplingHalfStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(_3800.CouplingStabilityAnalysis)

        @property
        def cvt_belt_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.CVTBeltConnectionStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.CVTPulleyStabilityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3805,
            )

            return self._parent._cast(_3805.CycloidalAssemblyStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(
                _3806.CycloidalDiscCentralBearingConnectionStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(
                _3807.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
            )

        @property
        def cycloidal_disc_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3808,
            )

            return self._parent._cast(_3808.CycloidalDiscStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.CylindricalGearMeshStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(_3810.CylindricalGearSetStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3812,
            )

            return self._parent._cast(_3812.CylindricalPlanetGearStabilityAnalysis)

        @property
        def datum_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3813,
            )

            return self._parent._cast(_3813.DatumStabilityAnalysis)

        @property
        def external_cad_model_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3815,
            )

            return self._parent._cast(_3815.ExternalCADModelStabilityAnalysis)

        @property
        def face_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.FaceGearMeshStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.FaceGearSetStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.FaceGearStabilityAnalysis)

        @property
        def fe_part_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.FEPartStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.GearMeshStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearSetStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GearStabilityAnalysis)

        @property
        def guide_dxf_model_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3824,
            )

            return self._parent._cast(_3824.GuideDxfModelStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.HypoidGearMeshStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3826,
            )

            return self._parent._cast(_3826.HypoidGearSetStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(_3827.HypoidGearStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(
                _3828.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(
                _3829.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(
                _3830.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3831,
            )

            return self._parent._cast(
                _3831.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(
                _3833.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3834,
            )

            return self._parent._cast(
                _3834.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(
                _3835.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(
                _3836.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(
                _3837.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def mass_disc_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(_3838.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MeasurementComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.OilSealStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(
                _3843.PartToPartShearCouplingConnectionStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(
                _3844.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PlanetaryConnectionStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.PlanetaryGearSetStabilityAnalysis)

        @property
        def planet_carrier_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3849,
            )

            return self._parent._cast(_3849.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.RingPinsStabilityAnalysis)

        @property
        def ring_pins_to_disc_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(_3853.RingPinsToDiscConnectionStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3854,
            )

            return self._parent._cast(_3854.RollingRingAssemblyStabilityAnalysis)

        @property
        def rolling_ring_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(_3855.RollingRingConnectionStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(_3856.RollingRingStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3857,
            )

            return self._parent._cast(_3857.RootAssemblyStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(_3858.ShaftHubConnectionStabilityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(_3859.ShaftStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(
                _3860.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def specialised_assembly_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(_3862.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3864,
            )

            return self._parent._cast(_3864.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.SpringDamperConnectionStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpringDamperHalfStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3873,
            )

            return self._parent._cast(_3873.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.StraightBevelGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.SynchroniserSleeveStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3882,
            )

            return self._parent._cast(_3882.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.TorqueConverterConnectionStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.TorqueConverterStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3888,
            )

            return self._parent._cast(_3888.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.WormGearMeshStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3890,
            )

            return self._parent._cast(_3890.WormGearSetStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3891,
            )

            return self._parent._cast(_3891.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.ZerolBevelGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3894,
            )

            return self._parent._cast(_3894.ZerolBevelGearStabilityAnalysis)

        @property
        def abstract_assembly_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4031

            return self._parent._cast(_4031.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractShaftPowerFlow)

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4033

            return self._parent._cast(
                _4033.AbstractShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4035

            return self._parent._cast(_4035.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4036

            return self._parent._cast(_4036.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4037

            return self._parent._cast(_4037.AssemblyPowerFlow)

        @property
        def bearing_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4038

            return self._parent._cast(_4038.BearingPowerFlow)

        @property
        def belt_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4039

            return self._parent._cast(_4039.BeltConnectionPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4041

            return self._parent._cast(_4041.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4042

            return self._parent._cast(_4042.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4043

            return self._parent._cast(_4043.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelGearMeshPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4048

            return self._parent._cast(_4048.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4049

            return self._parent._cast(_4049.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4050

            return self._parent._cast(_4050.BoltPowerFlow)

        @property
        def clutch_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4051

            return self._parent._cast(_4051.ClutchConnectionPowerFlow)

        @property
        def clutch_half_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.ClutchPowerFlow)

        @property
        def coaxial_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.CoaxialConnectionPowerFlow)

        @property
        def component_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.ComponentPowerFlow)

        @property
        def concept_coupling_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4056

            return self._parent._cast(_4056.ConceptCouplingConnectionPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.ConceptCouplingPowerFlow)

        @property
        def concept_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ConceptGearMeshPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.ConceptGearSetPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConicalGearMeshPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConicalGearSetPowerFlow)

        @property
        def connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConnectionPowerFlow)

        @property
        def connector_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.ConnectorPowerFlow)

        @property
        def coupling_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.CouplingConnectionPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.CouplingPowerFlow)

        @property
        def cvt_belt_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.CVTBeltConnectionPowerFlow)

        @property
        def cvt_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(
                _4074.CycloidalDiscCentralBearingConnectionPowerFlow
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(
                _4075.CycloidalDiscPlanetaryBearingConnectionPowerFlow
            )

        @property
        def cycloidal_disc_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(_4076.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.CylindricalGearMeshPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4079

            return self._parent._cast(_4079.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.ExternalCADModelPowerFlow)

        @property
        def face_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.FaceGearMeshPowerFlow)

        @property
        def face_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.GearMeshPowerFlow)

        @property
        def gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.GearPowerFlow)

        @property
        def gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.HypoidGearMeshPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.HypoidGearSetPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.InterMountableComponentConnectionPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(
                _4098.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(
                _4099.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4100

            return self._parent._cast(
                _4100.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(
                _4101.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(
                _4103.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(
                _4104.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(
                _4105.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(
                _4106.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def mass_disc_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(_4107.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.OilSealPowerFlow)

        @property
        def part_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.PlanetaryConnectionPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(_4123.RingPinsPowerFlow)

        @property
        def ring_pins_to_disc_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(_4124.RingPinsToDiscConnectionPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(_4125.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(_4126.RollingRingConnectionPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(_4129.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(_4130.ShaftPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(
                _4131.ShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def specialised_assembly_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.SpiralBevelGearMeshPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.SpringDamperConnectionPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.StraightBevelGearMeshPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4150

            return self._parent._cast(_4150.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_connection_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.TorqueConverterConnectionPowerFlow)

        @property
        def torque_converter_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.VirtualComponentPowerFlow)

        @property
        def worm_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.WormGearMeshPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.ZerolBevelGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4163

            return self._parent._cast(_4163.ZerolBevelGearSetPowerFlow)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4293,
            )

            return self._parent._cast(_4293.AbstractAssemblyParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4294,
            )

            return self._parent._cast(_4294.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4295,
            )

            return self._parent._cast(_4295.AbstractShaftParametricStudyTool)

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4296,
            )

            return self._parent._cast(
                _4296.AbstractShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4297,
            )

            return self._parent._cast(
                _4297.AGMAGleasonConicalGearMeshParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(_4298.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4299,
            )

            return self._parent._cast(
                _4299.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def assembly_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4300,
            )

            return self._parent._cast(_4300.AssemblyParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4301,
            )

            return self._parent._cast(_4301.BearingParametricStudyTool)

        @property
        def belt_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4302,
            )

            return self._parent._cast(_4302.BeltConnectionParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4303,
            )

            return self._parent._cast(_4303.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(
                _4304.BevelDifferentialGearMeshParametricStudyTool
            )

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4305,
            )

            return self._parent._cast(_4305.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4306,
            )

            return self._parent._cast(_4306.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(
                _4307.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4308,
            )

            return self._parent._cast(_4308.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.BevelGearMeshParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(_4310.BevelGearParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4311,
            )

            return self._parent._cast(_4311.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4312,
            )

            return self._parent._cast(_4312.BoltedJointParametricStudyTool)

        @property
        def bolt_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4313,
            )

            return self._parent._cast(_4313.BoltParametricStudyTool)

        @property
        def clutch_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4314,
            )

            return self._parent._cast(_4314.ClutchConnectionParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4315,
            )

            return self._parent._cast(_4315.ClutchHalfParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4316,
            )

            return self._parent._cast(_4316.ClutchParametricStudyTool)

        @property
        def coaxial_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.CoaxialConnectionParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ComponentParametricStudyTool)

        @property
        def concept_coupling_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(
                _4319.ConceptCouplingConnectionParametricStudyTool
            )

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.ConceptGearMeshParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ConceptGearParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4324,
            )

            return self._parent._cast(_4324.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConicalGearMeshParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.ConicalGearParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4327,
            )

            return self._parent._cast(_4327.ConicalGearSetParametricStudyTool)

        @property
        def connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConnectionParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ConnectorParametricStudyTool)

        @property
        def coupling_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.CouplingConnectionParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.CouplingHalfParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.CouplingParametricStudyTool)

        @property
        def cvt_belt_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.CVTBeltConnectionParametricStudyTool)

        @property
        def cvt_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.CVTParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4336,
            )

            return self._parent._cast(_4336.CycloidalAssemblyParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(
                _4337.CycloidalDiscCentralBearingConnectionParametricStudyTool
            )

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4338,
            )

            return self._parent._cast(_4338.CycloidalDiscParametricStudyTool)

        @property
        def cycloidal_disc_planetary_bearing_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4339,
            )

            return self._parent._cast(
                _4339.CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
            )

        @property
        def cylindrical_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.CylindricalGearMeshParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4341,
            )

            return self._parent._cast(_4341.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.CylindricalGearSetParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4343,
            )

            return self._parent._cast(_4343.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4353,
            )

            return self._parent._cast(_4353.FaceGearMeshParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.FaceGearParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4355,
            )

            return self._parent._cast(_4355.FaceGearSetParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4356,
            )

            return self._parent._cast(_4356.FEPartParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4357,
            )

            return self._parent._cast(_4357.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.GearMeshParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.GearParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4360,
            )

            return self._parent._cast(_4360.GearSetParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(_4361.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.HypoidGearMeshParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.HypoidGearParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4364,
            )

            return self._parent._cast(_4364.HypoidGearSetParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(
                _4365.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(
                _4366.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4367,
            )

            return self._parent._cast(
                _4367.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4368,
            )

            return self._parent._cast(
                _4368.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4369,
            )

            return self._parent._cast(
                _4369.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(
                _4370.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4371,
            )

            return self._parent._cast(
                _4371.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4372,
            )

            return self._parent._cast(
                _4372.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4373,
            )

            return self._parent._cast(
                _4373.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4374,
            )

            return self._parent._cast(
                _4374.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(_4375.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(_4376.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4379,
            )

            return self._parent._cast(_4379.OilSealParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4390,
            )

            return self._parent._cast(_4390.PartParametricStudyTool)

        @property
        def part_to_part_shear_coupling_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4391,
            )

            return self._parent._cast(
                _4391.PartToPartShearCouplingConnectionParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(
                _4392.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(_4394.PlanetaryConnectionParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PlanetaryGearSetParametricStudyTool)

        @property
        def planet_carrier_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4396,
            )

            return self._parent._cast(_4396.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(_4397.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(_4398.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(_4400.RingPinsParametricStudyTool)

        @property
        def ring_pins_to_disc_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.RingPinsToDiscConnectionParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.RollingRingAssemblyParametricStudyTool)

        @property
        def rolling_ring_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4403,
            )

            return self._parent._cast(_4403.RollingRingConnectionParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.RollingRingParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4405,
            )

            return self._parent._cast(_4405.RootAssemblyParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4406,
            )

            return self._parent._cast(_4406.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4407,
            )

            return self._parent._cast(_4407.ShaftParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(
                _4408.ShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def specialised_assembly_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.SpiralBevelGearMeshParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.SpiralBevelGearParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4412,
            )

            return self._parent._cast(_4412.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4413,
            )

            return self._parent._cast(_4413.SpringDamperConnectionParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpringDamperHalfParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4415,
            )

            return self._parent._cast(_4415.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(
                _4416.StraightBevelDiffGearMeshParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4418,
            )

            return self._parent._cast(_4418.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.StraightBevelGearMeshParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.StraightBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.SynchroniserParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4427,
            )

            return self._parent._cast(_4427.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_connection_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(
                _4428.TorqueConverterConnectionParametricStudyTool
            )

        @property
        def torque_converter_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.TorqueConverterParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4430,
            )

            return self._parent._cast(_4430.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.WormGearMeshParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.WormGearParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4436,
            )

            return self._parent._cast(_4436.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.ZerolBevelGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.ZerolBevelGearParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4439,
            )

            return self._parent._cast(_4439.ZerolBevelGearSetParametricStudyTool)

        @property
        def abstract_assembly_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4569

            return self._parent._cast(_4569.AbstractAssemblyModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4570

            return self._parent._cast(_4570.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4571

            return self._parent._cast(_4571.AbstractShaftOrHousingModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572

            return self._parent._cast(
                _4572.AbstractShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573

            return self._parent._cast(_4573.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574

            return self._parent._cast(_4574.AGMAGleasonConicalGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575

            return self._parent._cast(_4575.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576

            return self._parent._cast(_4576.AssemblyModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577

            return self._parent._cast(_4577.BearingModalAnalysis)

        @property
        def belt_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578

            return self._parent._cast(_4578.BeltConnectionModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579

            return self._parent._cast(_4579.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581

            return self._parent._cast(_4581.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582

            return self._parent._cast(_4582.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4583

            return self._parent._cast(_4583.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4584

            return self._parent._cast(_4584.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelGearMeshModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.BevelGearModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587

            return self._parent._cast(_4587.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BoltedJointModalAnalysis)

        @property
        def bolt_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4589

            return self._parent._cast(_4589.BoltModalAnalysis)

        @property
        def clutch_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.ClutchConnectionModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4591

            return self._parent._cast(_4591.ClutchHalfModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4592

            return self._parent._cast(_4592.ClutchModalAnalysis)

        @property
        def coaxial_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.CoaxialConnectionModalAnalysis)

        @property
        def component_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ComponentModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.ConceptCouplingConnectionModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.ConceptGearMeshModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ConceptGearModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.ConicalGearMeshModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConicalGearModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ConicalGearSetModalAnalysis)

        @property
        def connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConnectionModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ConnectorModalAnalysis)

        @property
        def coupling_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.CouplingConnectionModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.CouplingHalfModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.CouplingModalAnalysis)

        @property
        def cvt_belt_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.CVTBeltConnectionModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.CVTModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.CVTPulleyModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.CycloidalAssemblyModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(
                _4614.CycloidalDiscCentralBearingConnectionModalAnalysis
            )

        @property
        def cycloidal_disc_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.CycloidalDiscModalAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(
                _4616.CycloidalDiscPlanetaryBearingConnectionModalAnalysis
            )

        @property
        def cylindrical_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.CylindricalGearMeshModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.CylindricalGearModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(_4619.CylindricalGearSetModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621

            return self._parent._cast(_4621.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.ExternalCADModelModalAnalysis)

        @property
        def face_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.FaceGearMeshModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4627

            return self._parent._cast(_4627.FaceGearModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.FaceGearSetModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.FEPartModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630

            return self._parent._cast(_4630.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.GearMeshModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.GearModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634

            return self._parent._cast(_4634.GearSetModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.HypoidGearMeshModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.HypoidGearModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.HypoidGearSetModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(
                _4639.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(
                _4640.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(
                _4641.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(
                _4642.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(
                _4643.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(
                _4644.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(
                _4645.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(
                _4646.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(
                _4647.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(
                _4648.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649

            return self._parent._cast(_4649.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650

            return self._parent._cast(_4650.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.OilSealModalAnalysis)

        @property
        def part_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(
                _4660.PartToPartShearCouplingConnectionModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(_4663.PlanetaryConnectionModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.PlanetaryGearSetModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(_4665.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(_4667.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(_4668.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669

            return self._parent._cast(_4669.RingPinsModalAnalysis)

        @property
        def ring_pins_to_disc_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.RingPinsToDiscConnectionModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(_4671.RollingRingAssemblyModalAnalysis)

        @property
        def rolling_ring_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(_4672.RollingRingConnectionModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.RollingRingModalAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(_4674.RootAssemblyModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676

            return self._parent._cast(_4676.ShaftModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(
                _4678.ShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def specialised_assembly_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680

            return self._parent._cast(_4680.SpiralBevelGearMeshModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.SpiralBevelGearModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.SpringDamperConnectionModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.SpringDamperHalfModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.StraightBevelGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.StraightBevelGearSetModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.SynchroniserModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.TorqueConverterConnectionModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.TorqueConverterModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4703

            return self._parent._cast(_4703.VirtualComponentModalAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.WormGearMeshModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.WormGearModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4709

            return self._parent._cast(_4709.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.ZerolBevelGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.ZerolBevelGearModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.ZerolBevelGearSetModalAnalysis)

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4854,
            )

            return self._parent._cast(_4854.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4855,
            )

            return self._parent._cast(_4855.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4856,
            )

            return self._parent._cast(
                _4856.AbstractShaftOrHousingModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4857,
            )

            return self._parent._cast(
                _4857.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4858,
            )

            return self._parent._cast(
                _4858.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4859,
            )

            return self._parent._cast(
                _4859.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4860,
            )

            return self._parent._cast(
                _4860.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def assembly_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4861,
            )

            return self._parent._cast(_4861.AssemblyModalAnalysisAtAStiffness)

        @property
        def bearing_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4862,
            )

            return self._parent._cast(_4862.BearingModalAnalysisAtAStiffness)

        @property
        def belt_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4863,
            )

            return self._parent._cast(_4863.BeltConnectionModalAnalysisAtAStiffness)

        @property
        def belt_drive_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4864,
            )

            return self._parent._cast(_4864.BeltDriveModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(
                _4865.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4866,
            )

            return self._parent._cast(
                _4866.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4867,
            )

            return self._parent._cast(
                _4867.BevelDifferentialGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4868,
            )

            return self._parent._cast(
                _4868.BevelDifferentialPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4869,
            )

            return self._parent._cast(
                _4869.BevelDifferentialSunGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4870,
            )

            return self._parent._cast(_4870.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4871,
            )

            return self._parent._cast(_4871.BevelGearModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4872,
            )

            return self._parent._cast(_4872.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def bolted_joint_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4873,
            )

            return self._parent._cast(_4873.BoltedJointModalAnalysisAtAStiffness)

        @property
        def bolt_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4874,
            )

            return self._parent._cast(_4874.BoltModalAnalysisAtAStiffness)

        @property
        def clutch_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4875,
            )

            return self._parent._cast(_4875.ClutchConnectionModalAnalysisAtAStiffness)

        @property
        def clutch_half_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4876,
            )

            return self._parent._cast(_4876.ClutchHalfModalAnalysisAtAStiffness)

        @property
        def clutch_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4877,
            )

            return self._parent._cast(_4877.ClutchModalAnalysisAtAStiffness)

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.CoaxialConnectionModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4879,
            )

            return self._parent._cast(_4879.ComponentModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(
                _4880.ConceptCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_half_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4881,
            )

            return self._parent._cast(
                _4881.ConceptCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4882,
            )

            return self._parent._cast(_4882.ConceptCouplingModalAnalysisAtAStiffness)

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4883,
            )

            return self._parent._cast(_4883.ConceptGearMeshModalAnalysisAtAStiffness)

        @property
        def concept_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4884,
            )

            return self._parent._cast(_4884.ConceptGearModalAnalysisAtAStiffness)

        @property
        def concept_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4885,
            )

            return self._parent._cast(_4885.ConceptGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(_4886.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4887,
            )

            return self._parent._cast(_4887.ConicalGearModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(_4889.ConnectionModalAnalysisAtAStiffness)

        @property
        def connector_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(_4890.ConnectorModalAnalysisAtAStiffness)

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(_4892.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4893,
            )

            return self._parent._cast(_4893.CouplingModalAnalysisAtAStiffness)

        @property
        def cvt_belt_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(_4894.CVTBeltConnectionModalAnalysisAtAStiffness)

        @property
        def cvt_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4895,
            )

            return self._parent._cast(_4895.CVTModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4896,
            )

            return self._parent._cast(_4896.CVTPulleyModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4897,
            )

            return self._parent._cast(_4897.CycloidalAssemblyModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4898,
            )

            return self._parent._cast(
                _4898.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4899,
            )

            return self._parent._cast(_4899.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4900,
            )

            return self._parent._cast(
                _4900.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4901,
            )

            return self._parent._cast(
                _4901.CylindricalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4902,
            )

            return self._parent._cast(_4902.CylindricalGearModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(_4903.CylindricalGearSetModalAnalysisAtAStiffness)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4904,
            )

            return self._parent._cast(
                _4904.CylindricalPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def datum_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4905,
            )

            return self._parent._cast(_4905.DatumModalAnalysisAtAStiffness)

        @property
        def external_cad_model_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4907,
            )

            return self._parent._cast(_4907.ExternalCADModelModalAnalysisAtAStiffness)

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4908,
            )

            return self._parent._cast(_4908.FaceGearMeshModalAnalysisAtAStiffness)

        @property
        def face_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4909,
            )

            return self._parent._cast(_4909.FaceGearModalAnalysisAtAStiffness)

        @property
        def face_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4910,
            )

            return self._parent._cast(_4910.FaceGearSetModalAnalysisAtAStiffness)

        @property
        def fe_part_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4911,
            )

            return self._parent._cast(_4911.FEPartModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4912,
            )

            return self._parent._cast(
                _4912.FlexiblePinAssemblyModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.GearMeshModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.GearModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4915,
            )

            return self._parent._cast(_4915.GearSetModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4916,
            )

            return self._parent._cast(_4916.GuideDxfModelModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.HypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4918,
            )

            return self._parent._cast(_4918.HypoidGearModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4919,
            )

            return self._parent._cast(_4919.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4920,
            )

            return self._parent._cast(
                _4920.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4921,
            )

            return self._parent._cast(
                _4921.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(
                _4922.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4923,
            )

            return self._parent._cast(
                _4923.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4924,
            )

            return self._parent._cast(
                _4924.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4925,
            )

            return self._parent._cast(
                _4925.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4926,
            )

            return self._parent._cast(
                _4926.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4927,
            )

            return self._parent._cast(
                _4927.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4928,
            )

            return self._parent._cast(
                _4928.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4929,
            )

            return self._parent._cast(
                _4929.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4930,
            )

            return self._parent._cast(_4930.MassDiscModalAnalysisAtAStiffness)

        @property
        def measurement_component_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4931,
            )

            return self._parent._cast(
                _4931.MeasurementComponentModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4933,
            )

            return self._parent._cast(_4933.MountableComponentModalAnalysisAtAStiffness)

        @property
        def oil_seal_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(_4934.OilSealModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.PartModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(
                _4936.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(
                _4937.PartToPartShearCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(
                _4938.PartToPartShearCouplingModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4939,
            )

            return self._parent._cast(
                _4939.PlanetaryConnectionModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.PlanetaryGearSetModalAnalysisAtAStiffness)

        @property
        def planet_carrier_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4941,
            )

            return self._parent._cast(_4941.PlanetCarrierModalAnalysisAtAStiffness)

        @property
        def point_load_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4942,
            )

            return self._parent._cast(_4942.PointLoadModalAnalysisAtAStiffness)

        @property
        def power_load_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4943,
            )

            return self._parent._cast(_4943.PowerLoadModalAnalysisAtAStiffness)

        @property
        def pulley_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(_4944.PulleyModalAnalysisAtAStiffness)

        @property
        def ring_pins_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4945,
            )

            return self._parent._cast(_4945.RingPinsModalAnalysisAtAStiffness)

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(
                _4946.RingPinsToDiscConnectionModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_assembly_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4947,
            )

            return self._parent._cast(
                _4947.RollingRingAssemblyModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4948,
            )

            return self._parent._cast(
                _4948.RollingRingConnectionModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4949,
            )

            return self._parent._cast(_4949.RollingRingModalAnalysisAtAStiffness)

        @property
        def root_assembly_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4950,
            )

            return self._parent._cast(_4950.RootAssemblyModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4951,
            )

            return self._parent._cast(_4951.ShaftHubConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4952,
            )

            return self._parent._cast(_4952.ShaftModalAnalysisAtAStiffness)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4953,
            )

            return self._parent._cast(
                _4953.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4954,
            )

            return self._parent._cast(
                _4954.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4955,
            )

            return self._parent._cast(
                _4955.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(_4956.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(_4957.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4958,
            )

            return self._parent._cast(
                _4958.SpringDamperConnectionModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.SpringDamperHalfModalAnalysisAtAStiffness)

        @property
        def spring_damper_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4960,
            )

            return self._parent._cast(_4960.SpringDamperModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(
                _4961.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4962,
            )

            return self._parent._cast(
                _4962.StraightBevelDiffGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4963,
            )

            return self._parent._cast(
                _4963.StraightBevelDiffGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4964,
            )

            return self._parent._cast(
                _4964.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4965,
            )

            return self._parent._cast(_4965.StraightBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4966,
            )

            return self._parent._cast(
                _4966.StraightBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4967,
            )

            return self._parent._cast(
                _4967.StraightBevelPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4968,
            )

            return self._parent._cast(
                _4968.StraightBevelSunGearModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4969,
            )

            return self._parent._cast(_4969.SynchroniserHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4970,
            )

            return self._parent._cast(_4970.SynchroniserModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4971,
            )

            return self._parent._cast(_4971.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4972,
            )

            return self._parent._cast(_4972.SynchroniserSleeveModalAnalysisAtAStiffness)

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4973,
            )

            return self._parent._cast(
                _4973.TorqueConverterConnectionModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4974,
            )

            return self._parent._cast(_4974.TorqueConverterModalAnalysisAtAStiffness)

        @property
        def torque_converter_pump_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4975,
            )

            return self._parent._cast(
                _4975.TorqueConverterPumpModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4976,
            )

            return self._parent._cast(
                _4976.TorqueConverterTurbineModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4977,
            )

            return self._parent._cast(_4977.UnbalancedMassModalAnalysisAtAStiffness)

        @property
        def virtual_component_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(_4978.VirtualComponentModalAnalysisAtAStiffness)

        @property
        def worm_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4979,
            )

            return self._parent._cast(_4979.WormGearMeshModalAnalysisAtAStiffness)

        @property
        def worm_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(_4980.WormGearModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4981,
            )

            return self._parent._cast(_4981.WormGearSetModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4982,
            )

            return self._parent._cast(_4982.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4983,
            )

            return self._parent._cast(_4983.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4984,
            )

            return self._parent._cast(_4984.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5114,
            )

            return self._parent._cast(_5114.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_shaft_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5115,
            )

            return self._parent._cast(_5115.AbstractShaftModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5116,
            )

            return self._parent._cast(_5116.AbstractShaftOrHousingModalAnalysisAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(
                _5117.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5118,
            )

            return self._parent._cast(
                _5118.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5119,
            )

            return self._parent._cast(_5119.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5120,
            )

            return self._parent._cast(
                _5120.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def assembly_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5121,
            )

            return self._parent._cast(_5121.AssemblyModalAnalysisAtASpeed)

        @property
        def bearing_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5122,
            )

            return self._parent._cast(_5122.BearingModalAnalysisAtASpeed)

        @property
        def belt_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5123,
            )

            return self._parent._cast(_5123.BeltConnectionModalAnalysisAtASpeed)

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5124,
            )

            return self._parent._cast(_5124.BeltDriveModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(
                _5125.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5126,
            )

            return self._parent._cast(_5126.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5127,
            )

            return self._parent._cast(
                _5127.BevelDifferentialGearSetModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5128,
            )

            return self._parent._cast(
                _5128.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5129,
            )

            return self._parent._cast(
                _5129.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5130,
            )

            return self._parent._cast(_5130.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5131,
            )

            return self._parent._cast(_5131.BevelGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5132,
            )

            return self._parent._cast(_5132.BevelGearSetModalAnalysisAtASpeed)

        @property
        def bolted_joint_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5133,
            )

            return self._parent._cast(_5133.BoltedJointModalAnalysisAtASpeed)

        @property
        def bolt_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5134,
            )

            return self._parent._cast(_5134.BoltModalAnalysisAtASpeed)

        @property
        def clutch_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5135,
            )

            return self._parent._cast(_5135.ClutchConnectionModalAnalysisAtASpeed)

        @property
        def clutch_half_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5136,
            )

            return self._parent._cast(_5136.ClutchHalfModalAnalysisAtASpeed)

        @property
        def clutch_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5137,
            )

            return self._parent._cast(_5137.ClutchModalAnalysisAtASpeed)

        @property
        def coaxial_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5138,
            )

            return self._parent._cast(_5138.CoaxialConnectionModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5139,
            )

            return self._parent._cast(_5139.ComponentModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(
                _5140.ConceptCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_half_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(_5141.ConceptCouplingHalfModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def concept_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5143,
            )

            return self._parent._cast(_5143.ConceptGearMeshModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(_5144.ConceptGearModalAnalysisAtASpeed)

        @property
        def concept_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(_5145.ConceptGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5146,
            )

            return self._parent._cast(_5146.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5147,
            )

            return self._parent._cast(_5147.ConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5149,
            )

            return self._parent._cast(_5149.ConnectionModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ConnectorModalAnalysisAtASpeed)

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(_5151.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.CouplingHalfModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5153,
            )

            return self._parent._cast(_5153.CouplingModalAnalysisAtASpeed)

        @property
        def cvt_belt_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(_5154.CVTBeltConnectionModalAnalysisAtASpeed)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(_5155.CVTModalAnalysisAtASpeed)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5156,
            )

            return self._parent._cast(_5156.CVTPulleyModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5157,
            )

            return self._parent._cast(_5157.CycloidalAssemblyModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5158,
            )

            return self._parent._cast(
                _5158.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5159,
            )

            return self._parent._cast(_5159.CycloidalDiscModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(
                _5160.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5161,
            )

            return self._parent._cast(_5161.CylindricalGearMeshModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5162,
            )

            return self._parent._cast(_5162.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5164,
            )

            return self._parent._cast(_5164.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def datum_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(_5165.DatumModalAnalysisAtASpeed)

        @property
        def external_cad_model_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5166,
            )

            return self._parent._cast(_5166.ExternalCADModelModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5167,
            )

            return self._parent._cast(_5167.FaceGearMeshModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5168,
            )

            return self._parent._cast(_5168.FaceGearModalAnalysisAtASpeed)

        @property
        def face_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5169,
            )

            return self._parent._cast(_5169.FaceGearSetModalAnalysisAtASpeed)

        @property
        def fe_part_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5170,
            )

            return self._parent._cast(_5170.FEPartModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5171,
            )

            return self._parent._cast(_5171.FlexiblePinAssemblyModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.GearMeshModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.GearModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5174,
            )

            return self._parent._cast(_5174.GearSetModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.GuideDxfModelModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5176,
            )

            return self._parent._cast(_5176.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.HypoidGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5178,
            )

            return self._parent._cast(_5178.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(
                _5179.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5180,
            )

            return self._parent._cast(
                _5180.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5181,
            )

            return self._parent._cast(
                _5181.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(
                _5182.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5183,
            )

            return self._parent._cast(
                _5183.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5184,
            )

            return self._parent._cast(
                _5184.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5185,
            )

            return self._parent._cast(
                _5185.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5186,
            )

            return self._parent._cast(
                _5186.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5187,
            )

            return self._parent._cast(
                _5187.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(
                _5188.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
            )

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5189,
            )

            return self._parent._cast(_5189.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(_5190.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5192,
            )

            return self._parent._cast(_5192.MountableComponentModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.OilSealModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.PartModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(
                _5195.PartToPartShearCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(
                _5196.PartToPartShearCouplingHalfModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(
                _5197.PartToPartShearCouplingModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5198,
            )

            return self._parent._cast(_5198.PlanetaryConnectionModalAnalysisAtASpeed)

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def planet_carrier_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5200,
            )

            return self._parent._cast(_5200.PlanetCarrierModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5201,
            )

            return self._parent._cast(_5201.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.PowerLoadModalAnalysisAtASpeed)

        @property
        def pulley_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.PulleyModalAnalysisAtASpeed)

        @property
        def ring_pins_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5204,
            )

            return self._parent._cast(_5204.RingPinsModalAnalysisAtASpeed)

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(
                _5205.RingPinsToDiscConnectionModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5206,
            )

            return self._parent._cast(_5206.RollingRingAssemblyModalAnalysisAtASpeed)

        @property
        def rolling_ring_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5207,
            )

            return self._parent._cast(_5207.RollingRingConnectionModalAnalysisAtASpeed)

        @property
        def rolling_ring_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5208,
            )

            return self._parent._cast(_5208.RollingRingModalAnalysisAtASpeed)

        @property
        def root_assembly_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5209,
            )

            return self._parent._cast(_5209.RootAssemblyModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5210,
            )

            return self._parent._cast(_5210.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def shaft_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5211,
            )

            return self._parent._cast(_5211.ShaftModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(
                _5212.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5214,
            )

            return self._parent._cast(_5214.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5215,
            )

            return self._parent._cast(_5215.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5217,
            )

            return self._parent._cast(_5217.SpringDamperConnectionModalAnalysisAtASpeed)

        @property
        def spring_damper_half_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.SpringDamperHalfModalAnalysisAtASpeed)

        @property
        def spring_damper_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5219,
            )

            return self._parent._cast(_5219.SpringDamperModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(
                _5220.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5221,
            )

            return self._parent._cast(_5221.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5222,
            )

            return self._parent._cast(
                _5222.StraightBevelDiffGearSetModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5223,
            )

            return self._parent._cast(_5223.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5224,
            )

            return self._parent._cast(_5224.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5225,
            )

            return self._parent._cast(_5225.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5226,
            )

            return self._parent._cast(
                _5226.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5227,
            )

            return self._parent._cast(_5227.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5228,
            )

            return self._parent._cast(_5228.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5229,
            )

            return self._parent._cast(_5229.SynchroniserModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5230,
            )

            return self._parent._cast(_5230.SynchroniserPartModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5231,
            )

            return self._parent._cast(_5231.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5232,
            )

            return self._parent._cast(
                _5232.TorqueConverterConnectionModalAnalysisAtASpeed
            )

        @property
        def torque_converter_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5233,
            )

            return self._parent._cast(_5233.TorqueConverterModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5234,
            )

            return self._parent._cast(_5234.TorqueConverterPumpModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5235,
            )

            return self._parent._cast(_5235.TorqueConverterTurbineModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5236,
            )

            return self._parent._cast(_5236.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5237,
            )

            return self._parent._cast(_5237.VirtualComponentModalAnalysisAtASpeed)

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5238,
            )

            return self._parent._cast(_5238.WormGearMeshModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5239,
            )

            return self._parent._cast(_5239.WormGearModalAnalysisAtASpeed)

        @property
        def worm_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5240,
            )

            return self._parent._cast(_5240.WormGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5241,
            )

            return self._parent._cast(_5241.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5242,
            )

            return self._parent._cast(_5242.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5243,
            )

            return self._parent._cast(_5243.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5373

            return self._parent._cast(_5373.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5374

            return self._parent._cast(_5374.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5375

            return self._parent._cast(
                _5375.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5376

            return self._parent._cast(
                _5376.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5377

            return self._parent._cast(
                _5377.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378

            return self._parent._cast(
                _5378.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379

            return self._parent._cast(
                _5379.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def assembly_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5381

            return self._parent._cast(_5381.AssemblyMultibodyDynamicsAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382

            return self._parent._cast(_5382.BearingMultibodyDynamicsAnalysis)

        @property
        def belt_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385

            return self._parent._cast(_5385.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386

            return self._parent._cast(
                _5386.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(
                _5387.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388

            return self._parent._cast(
                _5388.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(
                _5389.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(
                _5390.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391

            return self._parent._cast(_5391.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392

            return self._parent._cast(_5392.BevelGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393

            return self._parent._cast(_5393.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394

            return self._parent._cast(_5394.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def bolt_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5395

            return self._parent._cast(_5395.BoltMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396

            return self._parent._cast(_5396.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398

            return self._parent._cast(_5398.ClutchMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(_5401.ComponentMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402

            return self._parent._cast(
                _5402.ConceptCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(
                _5403.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405

            return self._parent._cast(_5405.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408

            return self._parent._cast(_5408.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(_5413.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(_5415.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(_5417.CVTMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(
                _5420.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(
                _5422.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5423

            return self._parent._cast(
                _5423.CylindricalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(_5424.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5426

            return self._parent._cast(
                _5426.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def datum_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427

            return self._parent._cast(_5427.DatumMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ExternalCADModelMultibodyDynamicsAnalysis)

        @property
        def face_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429

            return self._parent._cast(_5429.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430

            return self._parent._cast(_5430.FaceGearMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431

            return self._parent._cast(_5431.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432

            return self._parent._cast(_5432.FEPartMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(
                _5433.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5434

            return self._parent._cast(_5434.GearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GearSetMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.GuideDxfModelMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440

            return self._parent._cast(_5440.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441

            return self._parent._cast(_5441.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5446

            return self._parent._cast(
                _5446.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447

            return self._parent._cast(
                _5447.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(
                _5448.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5450

            return self._parent._cast(
                _5450.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(
                _5452.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(
                _5453.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5454

            return self._parent._cast(
                _5454.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455

            return self._parent._cast(
                _5455.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5456

            return self._parent._cast(_5456.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(
                _5460.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.PartMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465

            return self._parent._cast(
                _5465.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(
                _5466.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(
                _5467.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468

            return self._parent._cast(
                _5468.PlanetaryConnectionMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(_5469.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def planet_carrier_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(_5470.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(_5471.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(_5473.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5474

            return self._parent._cast(_5474.RingPinsMultibodyDynamicsAnalysis)

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(
                _5475.RingPinsToDiscConnectionMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476

            return self._parent._cast(
                _5476.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477

            return self._parent._cast(
                _5477.RollingRingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(_5478.RollingRingMultibodyDynamicsAnalysis)

        @property
        def root_assembly_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479

            return self._parent._cast(_5479.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(_5482.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483

            return self._parent._cast(_5483.ShaftMultibodyDynamicsAnalysis)

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5484

            return self._parent._cast(
                _5484.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(
                _5486.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(
                _5487.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(_5489.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490

            return self._parent._cast(
                _5490.SpringDamperConnectionMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(_5492.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(
                _5493.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(
                _5494.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(
                _5495.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(
                _5496.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(_5497.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(
                _5499.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(
                _5500.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(_5501.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5502

            return self._parent._cast(_5502.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(_5503.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5504

            return self._parent._cast(_5504.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(
                _5505.TorqueConverterConnectionMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5507

            return self._parent._cast(_5507.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(
                _5508.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(_5511.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5512

            return self._parent._cast(_5512.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5514

            return self._parent._cast(_5514.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(_5515.WormGearMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5517

            return self._parent._cast(_5517.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5518

            return self._parent._cast(_5518.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5675,
            )

            return self._parent._cast(_5675.AbstractAssemblyHarmonicAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5677,
            )

            return self._parent._cast(_5677.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5678,
            )

            return self._parent._cast(_5678.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5679,
            )

            return self._parent._cast(
                _5679.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5680,
            )

            return self._parent._cast(_5680.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5681,
            )

            return self._parent._cast(_5681.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5682,
            )

            return self._parent._cast(_5682.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def assembly_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5683,
            )

            return self._parent._cast(_5683.AssemblyHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5684,
            )

            return self._parent._cast(_5684.BearingHarmonicAnalysis)

        @property
        def belt_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5685,
            )

            return self._parent._cast(_5685.BeltConnectionHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5688,
            )

            return self._parent._cast(_5688.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5689,
            )

            return self._parent._cast(_5689.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5690,
            )

            return self._parent._cast(_5690.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5692,
            )

            return self._parent._cast(_5692.BevelGearHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.BevelGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5694,
            )

            return self._parent._cast(_5694.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5695,
            )

            return self._parent._cast(_5695.BoltedJointHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5696,
            )

            return self._parent._cast(_5696.BoltHarmonicAnalysis)

        @property
        def clutch_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5697,
            )

            return self._parent._cast(_5697.ClutchConnectionHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5698,
            )

            return self._parent._cast(_5698.ClutchHalfHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5699,
            )

            return self._parent._cast(_5699.ClutchHarmonicAnalysis)

        @property
        def coaxial_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.CoaxialConnectionHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.ComponentHarmonicAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.ConceptCouplingConnectionHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5705,
            )

            return self._parent._cast(_5705.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5706,
            )

            return self._parent._cast(_5706.ConceptGearHarmonicAnalysis)

        @property
        def concept_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.ConceptGearMeshHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.ConicalGearHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ConicalGearMeshHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConicalGearSetHarmonicAnalysis)

        @property
        def connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.ConnectionHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ConnectorHarmonicAnalysis)

        @property
        def coupling_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.CouplingConnectionHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.CouplingHalfHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.CouplingHarmonicAnalysis)

        @property
        def cvt_belt_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.CVTBeltConnectionHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.CVTHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5719,
            )

            return self._parent._cast(_5719.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(
                _5721.CycloidalDiscCentralBearingConnectionHarmonicAnalysis
            )

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.CycloidalDiscHarmonicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(
                _5723.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
            )

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5724,
            )

            return self._parent._cast(_5724.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5725,
            )

            return self._parent._cast(_5725.CylindricalGearMeshHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.CylindricalGearSetHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5727,
            )

            return self._parent._cast(_5727.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5728,
            )

            return self._parent._cast(_5728.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5743,
            )

            return self._parent._cast(_5743.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5744,
            )

            return self._parent._cast(_5744.FaceGearHarmonicAnalysis)

        @property
        def face_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5745,
            )

            return self._parent._cast(_5745.FaceGearMeshHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5746,
            )

            return self._parent._cast(_5746.FaceGearSetHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5747,
            )

            return self._parent._cast(_5747.FEPartHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5748,
            )

            return self._parent._cast(_5748.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5750,
            )

            return self._parent._cast(_5750.GearHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5752,
            )

            return self._parent._cast(_5752.GearMeshHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(_5755.GearSetHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5757,
            )

            return self._parent._cast(_5757.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5768,
            )

            return self._parent._cast(_5768.HypoidGearHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5769,
            )

            return self._parent._cast(_5769.HypoidGearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5770,
            )

            return self._parent._cast(_5770.HypoidGearSetHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(
                _5771.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5772,
            )

            return self._parent._cast(
                _5772.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(
                _5773.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(
                _5774.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5775,
            )

            return self._parent._cast(
                _5775.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(
                _5776.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(
                _5777.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5778,
            )

            return self._parent._cast(
                _5778.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(
                _5779.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5780,
            )

            return self._parent._cast(
                _5780.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5781,
            )

            return self._parent._cast(_5781.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(_5782.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(_5783.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.OilSealHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.PartHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(
                _5786.PartToPartShearCouplingConnectionHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(_5790.PlanetaryConnectionHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(_5791.PlanetaryGearSetHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5792,
            )

            return self._parent._cast(_5792.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5793,
            )

            return self._parent._cast(_5793.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5795,
            )

            return self._parent._cast(_5795.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5797,
            )

            return self._parent._cast(_5797.RingPinsHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(_5798.RingPinsToDiscConnectionHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(_5799.RollingRingAssemblyHarmonicAnalysis)

        @property
        def rolling_ring_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.RollingRingConnectionHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5801,
            )

            return self._parent._cast(_5801.RollingRingHarmonicAnalysis)

        @property
        def root_assembly_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5802,
            )

            return self._parent._cast(_5802.RootAssemblyHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(_5803.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(_5804.ShaftHubConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(
                _5805.ShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def specialised_assembly_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(_5807.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.SpiralBevelGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5811,
            )

            return self._parent._cast(_5811.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.SpringDamperConnectionHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5813,
            )

            return self._parent._cast(_5813.SpringDamperHalfHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(_5816.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5819,
            )

            return self._parent._cast(_5819.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.StraightBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5824,
            )

            return self._parent._cast(_5824.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.SynchroniserHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5827,
            )

            return self._parent._cast(_5827.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.TorqueConverterConnectionHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.TorqueConverterHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(_5830.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5831,
            )

            return self._parent._cast(_5831.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5834,
            )

            return self._parent._cast(_5834.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5835,
            )

            return self._parent._cast(_5835.WormGearHarmonicAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.WormGearMeshHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.ZerolBevelGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6005,
            )

            return self._parent._cast(
                _6005.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6006,
            )

            return self._parent._cast(
                _6006.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6007,
            )

            return self._parent._cast(
                _6007.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6008,
            )

            return self._parent._cast(
                _6008.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6009,
            )

            return self._parent._cast(
                _6009.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6010,
            )

            return self._parent._cast(
                _6010.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6011,
            )

            return self._parent._cast(
                _6011.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(_6012.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6013,
            )

            return self._parent._cast(_6013.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6014,
            )

            return self._parent._cast(
                _6014.BeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6015,
            )

            return self._parent._cast(_6015.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(
                _6016.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6017,
            )

            return self._parent._cast(
                _6017.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6018,
            )

            return self._parent._cast(
                _6018.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6019,
            )

            return self._parent._cast(
                _6019.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6020,
            )

            return self._parent._cast(
                _6020.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6021,
            )

            return self._parent._cast(_6021.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6022,
            )

            return self._parent._cast(
                _6022.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6023,
            )

            return self._parent._cast(
                _6023.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6024,
            )

            return self._parent._cast(
                _6024.BoltedJointHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6025,
            )

            return self._parent._cast(_6025.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6026,
            )

            return self._parent._cast(
                _6026.ClutchConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6027,
            )

            return self._parent._cast(
                _6027.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6028,
            )

            return self._parent._cast(_6028.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(
                _6029.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(_6030.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6031,
            )

            return self._parent._cast(
                _6031.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6032,
            )

            return self._parent._cast(
                _6032.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(
                _6033.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(
                _6035.ConceptGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6037,
            )

            return self._parent._cast(
                _6037.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(_6041.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.CouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(_6044.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_belt_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(
                _6045.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(_6046.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(_6047.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6048,
            )

            return self._parent._cast(
                _6048.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(
                _6049.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(
                _6050.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6052,
            )

            return self._parent._cast(
                _6052.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6053,
            )

            return self._parent._cast(
                _6053.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(
                _6054.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6055,
            )

            return self._parent._cast(
                _6055.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6056,
            )

            return self._parent._cast(_6056.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6057,
            )

            return self._parent._cast(
                _6057.ExternalCADModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(_6058.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(
                _6059.FaceGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6060,
            )

            return self._parent._cast(
                _6060.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(_6061.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6062,
            )

            return self._parent._cast(
                _6062.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6063,
            )

            return self._parent._cast(_6063.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(_6064.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(_6065.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(
                _6066.GuideDxfModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(
                _6068.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.HypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(
                _6070.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(
                _6071.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6072,
            )

            return self._parent._cast(
                _6072.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(
                _6073.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6075,
            )

            return self._parent._cast(
                _6075.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(
                _6076.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6078,
            )

            return self._parent._cast(
                _6078.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(
                _6080.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(_6081.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(
                _6082.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(
                _6088.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(
                _6089.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6090,
            )

            return self._parent._cast(
                _6090.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(
                _6091.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(
                _6092.PlanetCarrierHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6093,
            )

            return self._parent._cast(_6093.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(_6094.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(_6095.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6096,
            )

            return self._parent._cast(_6096.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(
                _6097.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6098,
            )

            return self._parent._cast(
                _6098.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(
                _6099.RollingRingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6100,
            )

            return self._parent._cast(
                _6100.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(
                _6101.RootAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(_6102.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6103,
            )

            return self._parent._cast(
                _6103.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(
                _6104.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(
                _6105.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6106,
            )

            return self._parent._cast(
                _6106.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6107,
            )

            return self._parent._cast(
                _6107.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(
                _6109.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(
                _6110.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6112,
            )

            return self._parent._cast(
                _6112.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(
                _6115.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(
                _6118.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(
                _6119.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.SynchroniserHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(
                _6122.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6123,
            )

            return self._parent._cast(
                _6123.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(
                _6125.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(
                _6126.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6129,
            )

            return self._parent._cast(
                _6129.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6130,
            )

            return self._parent._cast(_6130.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(
                _6131.WormGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6133,
            )

            return self._parent._cast(
                _6133.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(
                _6135.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6274

            return self._parent._cast(_6274.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6275

            return self._parent._cast(_6275.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276

            return self._parent._cast(_6276.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277

            return self._parent._cast(
                _6277.AbstractShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278

            return self._parent._cast(_6278.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280

            return self._parent._cast(_6280.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281

            return self._parent._cast(_6281.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(_6282.BearingDynamicAnalysis)

        @property
        def belt_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.BeltConnectionDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284

            return self._parent._cast(_6284.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(_6288.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelGearMeshDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294

            return self._parent._cast(_6294.BoltedJointDynamicAnalysis)

        @property
        def clutch_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.ClutchConnectionDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297

            return self._parent._cast(_6297.ClutchHalfDynamicAnalysis)

        @property
        def coaxial_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.CoaxialConnectionDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ComponentDynamicAnalysis)

        @property
        def concept_coupling_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300

            return self._parent._cast(_6300.ConceptCouplingConnectionDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ConceptGearMeshDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306

            return self._parent._cast(_6306.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConicalGearMeshDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConicalGearSetDynamicAnalysis)

        @property
        def connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConnectionDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ConnectorDynamicAnalysis)

        @property
        def coupling_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.CouplingConnectionDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.CouplingHalfDynamicAnalysis)

        @property
        def cvt_belt_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.CVTBeltConnectionDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(
                _6318.CycloidalDiscCentralBearingConnectionDynamicAnalysis
            )

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.CycloidalDiscDynamicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(
                _6320.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis
            )

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.CylindricalGearMeshDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329

            return self._parent._cast(_6329.FaceGearDynamicAnalysis)

        @property
        def face_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.FaceGearMeshDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(_6331.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.GearDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.GearMeshDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.HypoidGearMeshDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(_6340.HypoidGearSetDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(
                _6341.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(
                _6342.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(
                _6343.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(
                _6344.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(
                _6345.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(
                _6347.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(
                _6348.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(
                _6350.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(_6351.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.OilSealDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(
                _6356.PartToPartShearCouplingConnectionDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(_6359.PlanetaryConnectionDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(_6361.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.RingPinsDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.RingPinsToDiscConnectionDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(_6367.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.RollingRingConnectionDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(_6370.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372

            return self._parent._cast(_6372.ShaftHubConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(
                _6373.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def specialised_assembly_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(_6375.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.SpringDamperConnectionDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_connection_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.TorqueConverterConnectionDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.WormGearDynamicAnalysis)

        @property
        def worm_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.WormGearMeshDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402

            return self._parent._cast(_6402.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.ZerolBevelGearSetDynamicAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6540,
            )

            return self._parent._cast(_6540.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6541,
            )

            return self._parent._cast(_6541.AbstractShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6542,
            )

            return self._parent._cast(_6542.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(
                _6543.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6544,
            )

            return self._parent._cast(_6544.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6545,
            )

            return self._parent._cast(
                _6545.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6546,
            )

            return self._parent._cast(
                _6546.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def assembly_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6547,
            )

            return self._parent._cast(_6547.AssemblyCriticalSpeedAnalysis)

        @property
        def bearing_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6548,
            )

            return self._parent._cast(_6548.BearingCriticalSpeedAnalysis)

        @property
        def belt_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6549,
            )

            return self._parent._cast(_6549.BeltConnectionCriticalSpeedAnalysis)

        @property
        def belt_drive_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6550,
            )

            return self._parent._cast(_6550.BeltDriveCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(_6551.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6552,
            )

            return self._parent._cast(
                _6552.BevelDifferentialGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6553,
            )

            return self._parent._cast(
                _6553.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6554,
            )

            return self._parent._cast(
                _6554.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(
                _6555.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(_6556.BevelGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6557,
            )

            return self._parent._cast(_6557.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6558,
            )

            return self._parent._cast(_6558.BevelGearSetCriticalSpeedAnalysis)

        @property
        def bolt_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6559,
            )

            return self._parent._cast(_6559.BoltCriticalSpeedAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6560,
            )

            return self._parent._cast(_6560.BoltedJointCriticalSpeedAnalysis)

        @property
        def clutch_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6561,
            )

            return self._parent._cast(_6561.ClutchConnectionCriticalSpeedAnalysis)

        @property
        def clutch_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6562,
            )

            return self._parent._cast(_6562.ClutchCriticalSpeedAnalysis)

        @property
        def clutch_half_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6563,
            )

            return self._parent._cast(_6563.ClutchHalfCriticalSpeedAnalysis)

        @property
        def coaxial_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(_6565.ComponentCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6566,
            )

            return self._parent._cast(
                _6566.ConceptCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.ConceptGearCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ConceptGearMeshCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6571,
            )

            return self._parent._cast(_6571.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6572,
            )

            return self._parent._cast(_6572.ConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.ConnectionCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.ConnectorCriticalSpeedAnalysis)

        @property
        def coupling_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.CouplingCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6579,
            )

            return self._parent._cast(_6579.CouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(_6583.CVTBeltConnectionCriticalSpeedAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(_6584.CVTCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6585,
            )

            return self._parent._cast(_6585.CVTPulleyCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(_6586.CycloidalAssemblyCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6587,
            )

            return self._parent._cast(
                _6587.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6588,
            )

            return self._parent._cast(_6588.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(
                _6589.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6590,
            )

            return self._parent._cast(_6590.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6591,
            )

            return self._parent._cast(_6591.CylindricalGearMeshCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6592,
            )

            return self._parent._cast(_6592.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6593,
            )

            return self._parent._cast(_6593.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def datum_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.DatumCriticalSpeedAnalysis)

        @property
        def external_cad_model_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6595,
            )

            return self._parent._cast(_6595.ExternalCADModelCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6596,
            )

            return self._parent._cast(_6596.FaceGearCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6597,
            )

            return self._parent._cast(_6597.FaceGearMeshCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(_6598.FaceGearSetCriticalSpeedAnalysis)

        @property
        def fe_part_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6599,
            )

            return self._parent._cast(_6599.FEPartCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6600,
            )

            return self._parent._cast(_6600.FlexiblePinAssemblyCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.GearCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.GearMeshCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.GearSetCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.GuideDxfModelCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6605,
            )

            return self._parent._cast(_6605.HypoidGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6606,
            )

            return self._parent._cast(_6606.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6607,
            )

            return self._parent._cast(_6607.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(
                _6608.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6609,
            )

            return self._parent._cast(
                _6609.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(
                _6610.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6612,
            )

            return self._parent._cast(
                _6612.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(
                _6613.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(
                _6614.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6615,
            )

            return self._parent._cast(
                _6615.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6616,
            )

            return self._parent._cast(
                _6616.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(
                _6617.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def mass_disc_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6618,
            )

            return self._parent._cast(_6618.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(_6620.MountableComponentCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.OilSealCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(
                _6623.PartToPartShearCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(
                _6624.PartToPartShearCouplingCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(
                _6625.PartToPartShearCouplingHalfCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6626,
            )

            return self._parent._cast(_6626.PlanetaryConnectionCriticalSpeedAnalysis)

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def planet_carrier_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(_6628.PlanetCarrierCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6629,
            )

            return self._parent._cast(_6629.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.PowerLoadCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.PulleyCriticalSpeedAnalysis)

        @property
        def ring_pins_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6632,
            )

            return self._parent._cast(_6632.RingPinsCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(
                _6633.RingPinsToDiscConnectionCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_assembly_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6634,
            )

            return self._parent._cast(_6634.RollingRingAssemblyCriticalSpeedAnalysis)

        @property
        def rolling_ring_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(_6635.RollingRingConnectionCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6636,
            )

            return self._parent._cast(_6636.RollingRingCriticalSpeedAnalysis)

        @property
        def root_assembly_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6637,
            )

            return self._parent._cast(_6637.RootAssemblyCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(_6638.ShaftCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6639,
            )

            return self._parent._cast(_6639.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(
                _6640.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(_6641.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6642,
            )

            return self._parent._cast(_6642.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6643,
            )

            return self._parent._cast(_6643.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6645,
            )

            return self._parent._cast(_6645.SpringDamperConnectionCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.SpringDamperCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(_6648.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(
                _6649.StraightBevelDiffGearMeshCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6650,
            )

            return self._parent._cast(
                _6650.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(_6652.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(_6653.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(
                _6654.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6655,
            )

            return self._parent._cast(_6655.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def synchroniser_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.SynchroniserCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6657,
            )

            return self._parent._cast(_6657.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6658,
            )

            return self._parent._cast(_6658.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6659,
            )

            return self._parent._cast(_6659.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(
                _6660.TorqueConverterConnectionCriticalSpeedAnalysis
            )

        @property
        def torque_converter_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6661,
            )

            return self._parent._cast(_6661.TorqueConverterCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6662,
            )

            return self._parent._cast(_6662.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6664,
            )

            return self._parent._cast(_6664.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.VirtualComponentCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6666,
            )

            return self._parent._cast(_6666.WormGearCriticalSpeedAnalysis)

        @property
        def worm_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6667,
            )

            return self._parent._cast(_6667.WormGearMeshCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6669,
            )

            return self._parent._cast(_6669.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6670,
            )

            return self._parent._cast(_6670.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6671,
            )

            return self._parent._cast(_6671.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def abstract_assembly_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6804

            return self._parent._cast(_6804.AbstractAssemblyLoadCase)

        @property
        def abstract_shaft_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6805

            return self._parent._cast(_6805.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(_6806.AbstractShaftOrHousingLoadCase)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6807

            return self._parent._cast(
                _6807.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def agma_gleason_conical_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6811

            return self._parent._cast(_6811.AGMAGleasonConicalGearLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6812

            return self._parent._cast(_6812.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6813

            return self._parent._cast(_6813.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6816

            return self._parent._cast(_6816.AssemblyLoadCase)

        @property
        def bearing_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.BearingLoadCase)

        @property
        def belt_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6818

            return self._parent._cast(_6818.BeltConnectionLoadCase)

        @property
        def belt_drive_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6819

            return self._parent._cast(_6819.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6820

            return self._parent._cast(_6820.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6821

            return self._parent._cast(_6821.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelGearLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelGearMeshLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.BoltedJointLoadCase)

        @property
        def bolt_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.BoltLoadCase)

        @property
        def clutch_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6830

            return self._parent._cast(_6830.ClutchConnectionLoadCase)

        @property
        def clutch_half_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.ClutchHalfLoadCase)

        @property
        def clutch_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6832

            return self._parent._cast(_6832.ClutchLoadCase)

        @property
        def coaxial_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.CoaxialConnectionLoadCase)

        @property
        def component_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ComponentLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6836

            return self._parent._cast(_6836.ConceptCouplingConnectionLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ConceptCouplingHalfLoadCase)

        @property
        def concept_coupling_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6838

            return self._parent._cast(_6838.ConceptCouplingLoadCase)

        @property
        def concept_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6839

            return self._parent._cast(_6839.ConceptGearLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ConceptGearMeshLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.ConceptGearSetLoadCase)

        @property
        def conical_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.ConicalGearLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.ConicalGearMeshLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ConicalGearSetLoadCase)

        @property
        def connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.ConnectionLoadCase)

        @property
        def connector_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.ConnectorLoadCase)

        @property
        def coupling_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.CouplingConnectionLoadCase)

        @property
        def coupling_half_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.CouplingHalfLoadCase)

        @property
        def coupling_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.CouplingLoadCase)

        @property
        def cvt_belt_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.CVTBeltConnectionLoadCase)

        @property
        def cvt_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.CVTLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.CVTPulleyLoadCase)

        @property
        def cycloidal_assembly_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.CycloidalAssemblyLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(
                _6856.CycloidalDiscCentralBearingConnectionLoadCase
            )

        @property
        def cycloidal_disc_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.CycloidalDiscLoadCase)

        @property
        def cycloidal_disc_planetary_bearing_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6858

            return self._parent._cast(
                _6858.CycloidalDiscPlanetaryBearingConnectionLoadCase
            )

        @property
        def cylindrical_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.CylindricalGearLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(_6861.CylindricalGearMeshLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6863

            return self._parent._cast(_6863.CylindricalGearSetLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6867

            return self._parent._cast(_6867.DatumLoadCase)

        @property
        def external_cad_model_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6881

            return self._parent._cast(_6881.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6882

            return self._parent._cast(_6882.FaceGearLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.FaceGearMeshLoadCase)

        @property
        def face_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6884

            return self._parent._cast(_6884.FaceGearSetLoadCase)

        @property
        def fe_part_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.FEPartLoadCase)

        @property
        def flexible_pin_assembly_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6886

            return self._parent._cast(_6886.FlexiblePinAssemblyLoadCase)

        @property
        def gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.GearLoadCase)

        @property
        def gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.GearMeshLoadCase)

        @property
        def gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.GearSetLoadCase)

        @property
        def guide_dxf_model_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6894

            return self._parent._cast(_6894.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6903

            return self._parent._cast(_6903.HypoidGearLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6904

            return self._parent._cast(_6904.HypoidGearMeshLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6905

            return self._parent._cast(_6905.HypoidGearSetLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.InterMountableComponentConnectionLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6910

            return self._parent._cast(_6910.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(
                _6911.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(
                _6912.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6913

            return self._parent._cast(_6913.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(
                _6914.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(
                _6915.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(
                _6916.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(
                _6917.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6918

            return self._parent._cast(
                _6918.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def mass_disc_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6919

            return self._parent._cast(_6919.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(_6920.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.OilSealLoadCase)

        @property
        def part_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartLoadCase)

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.PartToPartShearCouplingConnectionLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartToPartShearCouplingHalfLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PartToPartShearCouplingLoadCase)

        @property
        def planetary_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6930

            return self._parent._cast(_6930.PlanetaryConnectionLoadCase)

        @property
        def planetary_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PlanetaryGearSetLoadCase)

        @property
        def planet_carrier_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6936

            return self._parent._cast(_6936.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PowerLoadLoadCase)

        @property
        def pulley_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(_6938.PulleyLoadCase)

        @property
        def ring_pins_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(_6941.RingPinsLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(_6942.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_assembly_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6943

            return self._parent._cast(_6943.RollingRingAssemblyLoadCase)

        @property
        def rolling_ring_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6944

            return self._parent._cast(_6944.RollingRingConnectionLoadCase)

        @property
        def rolling_ring_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6945

            return self._parent._cast(_6945.RollingRingLoadCase)

        @property
        def root_assembly_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.RootAssemblyLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(_6947.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.ShaftLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.ShaftToMountableComponentConnectionLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.SpiralBevelGearLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpiralBevelGearMeshLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6954

            return self._parent._cast(_6954.SpringDamperConnectionLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.SpringDamperHalfLoadCase)

        @property
        def spring_damper_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.StraightBevelGearLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.StraightBevelGearMeshLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.StraightBevelGearSetLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.SynchroniserHalfLoadCase)

        @property
        def synchroniser_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.SynchroniserLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.TorqueConverterConnectionLoadCase)

        @property
        def torque_converter_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.TorqueConverterLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6972

            return self._parent._cast(_6972.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6978

            return self._parent._cast(_6978.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.WormGearLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.WormGearMeshLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.ZerolBevelGearLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.ZerolBevelGearMeshLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.ZerolBevelGearSetLoadCase)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7003,
            )

            return self._parent._cast(
                _7003.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7004,
            )

            return self._parent._cast(
                _7004.AbstractShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7005,
            )

            return self._parent._cast(
                _7005.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7006,
            )

            return self._parent._cast(
                _7006.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7011,
            )

            return self._parent._cast(
                _7011.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7012,
            )

            return self._parent._cast(
                _7012.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7013,
            )

            return self._parent._cast(
                _7013.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7014,
            )

            return self._parent._cast(
                _7014.AssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7016,
            )

            return self._parent._cast(
                _7016.BearingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7017,
            )

            return self._parent._cast(
                _7017.BeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7018,
            )

            return self._parent._cast(
                _7018.BeltDriveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7019,
            )

            return self._parent._cast(
                _7019.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7020,
            )

            return self._parent._cast(
                _7020.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7021,
            )

            return self._parent._cast(
                _7021.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7022,
            )

            return self._parent._cast(
                _7022.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7023,
            )

            return self._parent._cast(
                _7023.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7024,
            )

            return self._parent._cast(
                _7024.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7025,
            )

            return self._parent._cast(
                _7025.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7026,
            )

            return self._parent._cast(
                _7026.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolt_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7027,
            )

            return self._parent._cast(
                _7027.BoltAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7028,
            )

            return self._parent._cast(
                _7028.BoltedJointAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7029,
            )

            return self._parent._cast(
                _7029.ClutchAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7030,
            )

            return self._parent._cast(
                _7030.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7031,
            )

            return self._parent._cast(
                _7031.ClutchHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7033,
            )

            return self._parent._cast(
                _7033.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7034,
            )

            return self._parent._cast(
                _7034.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7037,
            )

            return self._parent._cast(
                _7037.ConceptGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7038,
            )

            return self._parent._cast(
                _7038.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7039,
            )

            return self._parent._cast(
                _7039.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7040,
            )

            return self._parent._cast(
                _7040.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.ConnectorAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7045,
            )

            return self._parent._cast(
                _7045.CouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7047,
            )

            return self._parent._cast(
                _7047.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.CVTAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7049,
            )

            return self._parent._cast(
                _7049.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7050,
            )

            return self._parent._cast(
                _7050.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7051,
            )

            return self._parent._cast(
                _7051.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7055,
            )

            return self._parent._cast(
                _7055.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7056,
            )

            return self._parent._cast(
                _7056.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7057,
            )

            return self._parent._cast(
                _7057.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def datum_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7059,
            )

            return self._parent._cast(
                _7059.DatumAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def external_cad_model_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7060,
            )

            return self._parent._cast(
                _7060.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7061,
            )

            return self._parent._cast(
                _7061.FaceGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7063,
            )

            return self._parent._cast(
                _7063.FaceGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7064,
            )

            return self._parent._cast(
                _7064.FEPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7065,
            )

            return self._parent._cast(
                _7065.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7066,
            )

            return self._parent._cast(
                _7066.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7067,
            )

            return self._parent._cast(
                _7067.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def guide_dxf_model_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7071,
            )

            return self._parent._cast(
                _7071.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7073,
            )

            return self._parent._cast(
                _7073.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7074,
            )

            return self._parent._cast(
                _7074.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7075,
            )

            return self._parent._cast(
                _7075.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7077,
            )

            return self._parent._cast(
                _7077.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7078,
            )

            return self._parent._cast(
                _7078.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7080,
            )

            return self._parent._cast(
                _7080.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7081,
            )

            return self._parent._cast(
                _7081.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7083,
            )

            return self._parent._cast(
                _7083.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7084,
            )

            return self._parent._cast(
                _7084.MassDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.OilSealAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7089,
            )

            return self._parent._cast(
                _7089.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7093,
            )

            return self._parent._cast(
                _7093.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7094,
            )

            return self._parent._cast(
                _7094.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.PointLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7096,
            )

            return self._parent._cast(
                _7096.PowerLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.PulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7098,
            )

            return self._parent._cast(
                _7098.RingPinsAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7100,
            )

            return self._parent._cast(
                _7100.RollingRingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7101,
            )

            return self._parent._cast(
                _7101.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7102,
            )

            return self._parent._cast(
                _7102.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7103,
            )

            return self._parent._cast(
                _7103.RootAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7104,
            )

            return self._parent._cast(
                _7104.ShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7105,
            )

            return self._parent._cast(
                _7105.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7108,
            )

            return self._parent._cast(
                _7108.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7109,
            )

            return self._parent._cast(
                _7109.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7111,
            )

            return self._parent._cast(
                _7111.SpringDamperAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7114,
            )

            return self._parent._cast(
                _7114.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7116,
            )

            return self._parent._cast(
                _7116.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7119,
            )

            return self._parent._cast(
                _7119.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7121,
            )

            return self._parent._cast(
                _7121.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7122,
            )

            return self._parent._cast(
                _7122.SynchroniserAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7123,
            )

            return self._parent._cast(
                _7123.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7124,
            )

            return self._parent._cast(
                _7124.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7126,
            )

            return self._parent._cast(
                _7126.TorqueConverterAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7127,
            )

            return self._parent._cast(
                _7127.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7128,
            )

            return self._parent._cast(
                _7128.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7129,
            )

            return self._parent._cast(
                _7129.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7130,
            )

            return self._parent._cast(
                _7130.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7131,
            )

            return self._parent._cast(
                _7131.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7132,
            )

            return self._parent._cast(
                _7132.WormGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7133,
            )

            return self._parent._cast(
                _7133.WormGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.WormGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7135,
            )

            return self._parent._cast(
                _7135.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7137,
            )

            return self._parent._cast(
                _7137.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7267,
            )

            return self._parent._cast(_7267.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7268,
            )

            return self._parent._cast(_7268.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7269,
            )

            return self._parent._cast(
                _7269.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7270,
            )

            return self._parent._cast(
                _7270.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7274,
            )

            return self._parent._cast(
                _7274.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7275,
            )

            return self._parent._cast(
                _7275.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7276,
            )

            return self._parent._cast(
                _7276.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def assembly_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7277,
            )

            return self._parent._cast(_7277.AssemblyAdvancedSystemDeflection)

        @property
        def bearing_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7278,
            )

            return self._parent._cast(_7278.BearingAdvancedSystemDeflection)

        @property
        def belt_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7279,
            )

            return self._parent._cast(_7279.BeltConnectionAdvancedSystemDeflection)

        @property
        def belt_drive_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7280,
            )

            return self._parent._cast(_7280.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7281,
            )

            return self._parent._cast(
                _7281.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7282,
            )

            return self._parent._cast(
                _7282.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7283,
            )

            return self._parent._cast(
                _7283.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(
                _7284.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(
                _7285.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7286,
            )

            return self._parent._cast(_7286.BevelGearAdvancedSystemDeflection)

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(_7287.BevelGearMeshAdvancedSystemDeflection)

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7288,
            )

            return self._parent._cast(_7288.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolt_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7289,
            )

            return self._parent._cast(_7289.BoltAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7290,
            )

            return self._parent._cast(_7290.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7291,
            )

            return self._parent._cast(_7291.ClutchAdvancedSystemDeflection)

        @property
        def clutch_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(_7292.ClutchConnectionAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7293,
            )

            return self._parent._cast(_7293.ClutchHalfAdvancedSystemDeflection)

        @property
        def coaxial_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(_7294.CoaxialConnectionAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ComponentAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(_7296.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(
                _7297.ConceptCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7299,
            )

            return self._parent._cast(_7299.ConceptGearAdvancedSystemDeflection)

        @property
        def concept_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.ConceptGearMeshAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7301,
            )

            return self._parent._cast(_7301.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7302,
            )

            return self._parent._cast(_7302.ConicalGearAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(_7304.ConicalGearSetAdvancedSystemDeflection)

        @property
        def connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConnectionAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(_7306.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7308,
            )

            return self._parent._cast(_7308.CouplingAdvancedSystemDeflection)

        @property
        def coupling_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(_7309.CouplingConnectionAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7310,
            )

            return self._parent._cast(_7310.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7311,
            )

            return self._parent._cast(_7311.CVTAdvancedSystemDeflection)

        @property
        def cvt_belt_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.CVTBeltConnectionAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.CVTPulleyAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(_7314.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.CycloidalDiscAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(
                _7316.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(
                _7317.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7318,
            )

            return self._parent._cast(_7318.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.CylindricalGearMeshAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7320,
            )

            return self._parent._cast(_7320.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7322,
            )

            return self._parent._cast(
                _7322.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def datum_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7323,
            )

            return self._parent._cast(_7323.DatumAdvancedSystemDeflection)

        @property
        def external_cad_model_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.ExternalCADModelAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7325,
            )

            return self._parent._cast(_7325.FaceGearAdvancedSystemDeflection)

        @property
        def face_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7326,
            )

            return self._parent._cast(_7326.FaceGearMeshAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(_7327.FaceGearSetAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7328,
            )

            return self._parent._cast(_7328.FEPartAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.GearAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.GearMeshAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7332,
            )

            return self._parent._cast(_7332.GearSetAdvancedSystemDeflection)

        @property
        def guide_dxf_model_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.GuideDxfModelAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.HypoidGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7336,
            )

            return self._parent._cast(_7336.HypoidGearSetAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(
                _7337.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7338,
            )

            return self._parent._cast(
                _7338.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(
                _7339.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(
                _7340.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7341,
            )

            return self._parent._cast(
                _7341.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(
                _7342.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(
                _7343.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(
                _7344.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7345,
            )

            return self._parent._cast(
                _7345.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7346,
            )

            return self._parent._cast(
                _7346.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def mass_disc_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(_7348.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(
                _7349.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def mountable_component_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(_7350.MountableComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.OilSealAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(
                _7353.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(
                _7354.PartToPartShearCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(
                _7355.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def planetary_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.PlanetaryConnectionAdvancedSystemDeflection)

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(_7357.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def planet_carrier_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7358,
            )

            return self._parent._cast(_7358.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7360,
            )

            return self._parent._cast(_7360.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(_7362.RingPinsAdvancedSystemDeflection)

        @property
        def ring_pins_to_disc_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(
                _7363.RingPinsToDiscConnectionAdvancedSystemDeflection
            )

        @property
        def rolling_ring_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(_7364.RollingRingAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7365,
            )

            return self._parent._cast(_7365.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def rolling_ring_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(
                _7366.RollingRingConnectionAdvancedSystemDeflection
            )

        @property
        def root_assembly_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7367,
            )

            return self._parent._cast(_7367.RootAssemblyAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7368,
            )

            return self._parent._cast(_7368.ShaftAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(_7369.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(
                _7370.ShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(_7371.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(_7372.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(_7373.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7374,
            )

            return self._parent._cast(_7374.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(_7375.SpringDamperAdvancedSystemDeflection)

        @property
        def spring_damper_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(
                _7376.SpringDamperConnectionAdvancedSystemDeflection
            )

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(_7377.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(
                _7378.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(
                _7379.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7380,
            )

            return self._parent._cast(
                _7380.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(
                _7383.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(
                _7384.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(
                _7385.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def synchroniser_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(_7386.SynchroniserAdvancedSystemDeflection)

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(_7387.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(_7388.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(_7389.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7390,
            )

            return self._parent._cast(_7390.TorqueConverterAdvancedSystemDeflection)

        @property
        def torque_converter_connection_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(
                _7391.TorqueConverterConnectionAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(_7392.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7393,
            )

            return self._parent._cast(
                _7393.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(_7395.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(_7396.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7397,
            )

            return self._parent._cast(_7397.WormGearAdvancedSystemDeflection)

        @property
        def worm_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.WormGearMeshAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7399,
            )

            return self._parent._cast(_7399.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7402,
            )

            return self._parent._cast(_7402.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def connection_analysis_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_fe_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_time_series_load_analysis_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_fe_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_time_series_load_analysis_case(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartTimeSeriesLoadAnalysisCase)

        @property
        def design_entity_single_context_analysis(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
        ) -> "DesignEntitySingleContextAnalysis":
            return self._parent

        def __getattr__(
            self: "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis",
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
        self: Self, instance_to_wrap: "DesignEntitySingleContextAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def parametric_study_index_1(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricStudyIndex1

        if temp is None:
            return 0

        return temp

    @property
    def parametric_study_index_2(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricStudyIndex2

        if temp is None:
            return 0

        return temp

    @property
    def planetary_original(self: Self) -> "_2649.DesignEntityAnalysis":
        """mastapy.system_model.analyses_and_results.DesignEntityAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetaryOriginal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "DesignEntitySingleContextAnalysis._Cast_DesignEntitySingleContextAnalysis":
        return self._Cast_DesignEntitySingleContextAnalysis(self)
