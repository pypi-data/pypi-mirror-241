"""AbstractAssemblyCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4804
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AbstractAssemblyCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4569


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundModalAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundModalAnalysis")


class AbstractAssemblyCompoundModalAnalysis(_4804.PartCompoundModalAnalysis):
    """AbstractAssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundModalAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundModalAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
            parent: "AbstractAssemblyCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4731,
            )

            return self._parent._cast(
                _4731.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4732,
            )

            return self._parent._cast(_4732.AssemblyCompoundModalAnalysis)

        @property
        def belt_drive_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4735,
            )

            return self._parent._cast(_4735.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(
                _4738.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(_4743.BevelGearSetCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4745,
            )

            return self._parent._cast(_4745.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.ClutchCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConicalGearSetCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.CouplingCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(_4766.CVTCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4768,
            )

            return self._parent._cast(_4768.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.CylindricalGearSetCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(_4780.FaceGearSetCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4782,
            )

            return self._parent._cast(_4782.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.GearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4789,
            )

            return self._parent._cast(_4789.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4793,
            )

            return self._parent._cast(
                _4793.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(
                _4799.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(
                _4805.PartToPartShearCouplingCompoundModalAnalysis
            )

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(_4816.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def root_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(_4819.RootAssemblyCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4827,
            )

            return self._parent._cast(_4827.SpringDamperCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(
                _4832.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(_4835.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.SynchroniserCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.TorqueConverterCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
        ) -> "AbstractAssemblyCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4569.AbstractAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractAssemblyModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4569.AbstractAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractAssemblyModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis":
        return self._Cast_AbstractAssemblyCompoundModalAnalysis(self)
