"""SpecialisedAssemblyModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4569
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SpecialisedAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474
    from mastapy.system_model.analyses_and_results.system_deflections import _2804


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyModalAnalysis")


class SpecialisedAssemblyModalAnalysis(_4569.AbstractAssemblyModalAnalysis):
    """SpecialisedAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyModalAnalysis")

    class _Cast_SpecialisedAssemblyModalAnalysis:
        """Special nested class for casting SpecialisedAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
            parent: "SpecialisedAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            return self._parent._cast(_4569.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575

            return self._parent._cast(_4575.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579

            return self._parent._cast(_4579.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582

            return self._parent._cast(_4582.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587

            return self._parent._cast(_4587.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BoltedJointModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4592

            return self._parent._cast(_4592.ClutchModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ConicalGearSetModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.CVTModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.CycloidalAssemblyModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(_4619.CylindricalGearSetModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.FaceGearSetModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630

            return self._parent._cast(_4630.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634

            return self._parent._cast(_4634.GearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(
                _4642.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(
                _4645.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(
                _4648.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.PlanetaryGearSetModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(_4671.RollingRingAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.StraightBevelGearSetModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.SynchroniserModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.TorqueConverterModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4709

            return self._parent._cast(_4709.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.ZerolBevelGearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
        ) -> "SpecialisedAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecialisedAssemblyModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2474.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2804.SpecialisedAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyModalAnalysis._Cast_SpecialisedAssemblyModalAnalysis":
        return self._Cast_SpecialisedAssemblyModalAnalysis(self)
