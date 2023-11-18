"""ElectricMachineStatorToothLoadsExcitationDetail"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5730
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_TOOTH_LOADS_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineStatorToothLoadsExcitationDetail",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineStatorToothLoadsExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachineStatorToothLoadsExcitationDetail")


class ElectricMachineStatorToothLoadsExcitationDetail(
    _5730.ElectricMachinePeriodicExcitationDetail
):
    """ElectricMachineStatorToothLoadsExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_TOOTH_LOADS_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineStatorToothLoadsExcitationDetail"
    )

    class _Cast_ElectricMachineStatorToothLoadsExcitationDetail:
        """Special nested class for casting ElectricMachineStatorToothLoadsExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
            parent: "ElectricMachineStatorToothLoadsExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ):
            return self._parent._cast(_5730.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5789,
            )

            return self._parent._cast(_5789.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5676,
            )

            return self._parent._cast(_5676.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(
                _5736.ElectricMachineStatorToothAxialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5738,
            )

            return self._parent._cast(
                _5738.ElectricMachineStatorToothMomentsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5739,
            )

            return self._parent._cast(
                _5739.ElectricMachineStatorToothRadialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(
                _5740.ElectricMachineStatorToothTangentialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ) -> "ElectricMachineStatorToothLoadsExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
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
        instance_to_wrap: "ElectricMachineStatorToothLoadsExcitationDetail.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail":
        return self._Cast_ElectricMachineStatorToothLoadsExcitationDetail(self)
