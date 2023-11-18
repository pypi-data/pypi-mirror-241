"""AbstractPeriodicExcitationDetail"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractPeriodicExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.electric_machines.harmonic_load_data import _1377


__docformat__ = "restructuredtext en"
__all__ = ("AbstractPeriodicExcitationDetail",)


Self = TypeVar("Self", bound="AbstractPeriodicExcitationDetail")


class AbstractPeriodicExcitationDetail(_0.APIBase):
    """AbstractPeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractPeriodicExcitationDetail")

    class _Cast_AbstractPeriodicExcitationDetail:
        """Special nested class for casting AbstractPeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
            parent: "AbstractPeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5730,
            )

            return self._parent._cast(_5730.ElectricMachinePeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(
                _5731.ElectricMachineRotorXForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_x_moment_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5732,
            )

            return self._parent._cast(
                _5732.ElectricMachineRotorXMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5733,
            )

            return self._parent._cast(
                _5733.ElectricMachineRotorYForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_moment_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5734,
            )

            return self._parent._cast(
                _5734.ElectricMachineRotorYMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_z_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5735,
            )

            return self._parent._cast(
                _5735.ElectricMachineRotorZForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(
                _5736.ElectricMachineStatorToothAxialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5737,
            )

            return self._parent._cast(
                _5737.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5738,
            )

            return self._parent._cast(
                _5738.ElectricMachineStatorToothMomentsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5739,
            )

            return self._parent._cast(
                _5739.ElectricMachineStatorToothRadialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(
                _5740.ElectricMachineStatorToothTangentialLoadsExcitationDetail
            )

        @property
        def electric_machine_torque_ripple_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5741,
            )

            return self._parent._cast(
                _5741.ElectricMachineTorqueRipplePeriodicExcitationDetail
            )

        @property
        def gear_mesh_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(_5751.GearMeshExcitationDetail)

        @property
        def gear_mesh_misalignment_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5753,
            )

            return self._parent._cast(_5753.GearMeshMisalignmentExcitationDetail)

        @property
        def gear_mesh_te_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5754,
            )

            return self._parent._cast(_5754.GearMeshTEExcitationDetail)

        @property
        def general_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5756,
            )

            return self._parent._cast(_5756.GeneralPeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5789,
            )

            return self._parent._cast(_5789.PeriodicExcitationWithReferenceShaft)

        @property
        def single_node_periodic_excitation_with_reference_shaft(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(
                _5806.SingleNodePeriodicExcitationWithReferenceShaft
            )

        @property
        def unbalanced_mass_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.UnbalancedMassExcitationDetail)

        @property
        def abstract_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "AbstractPeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractPeriodicExcitationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_load_data(self: Self) -> "_1377.HarmonicLoadDataBase":
        """mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicLoadData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail":
        return self._Cast_AbstractPeriodicExcitationDetail(self)
