"""CylindricalGearMeshFEModel"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.fe_model import _1196
from mastapy._internal.cast_exception import CastException

_GEAR_FE_MODEL = python_net_import("SMT.MastaAPI.Gears.FEModel", "GearFEModel")
_GEAR_FLANKS = python_net_import("SMT.MastaAPI.Gears", "GearFlanks")
_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_CYLINDRICAL_GEAR_MESH_FE_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.FEModel.Cylindrical", "CylindricalGearMeshFEModel"
)

if TYPE_CHECKING:
    from mastapy.gears.fe_model import _1195
    from mastapy.gears import _324
    from mastapy.gears.ltca import _833
    from mastapy import _7556


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshFEModel",)


Self = TypeVar("Self", bound="CylindricalGearMeshFEModel")


class CylindricalGearMeshFEModel(_1196.GearMeshFEModel):
    """CylindricalGearMeshFEModel

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_FE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMeshFEModel")

    class _Cast_CylindricalGearMeshFEModel:
        """Special nested class for casting CylindricalGearMeshFEModel to subclasses."""

        def __init__(
            self: "CylindricalGearMeshFEModel._Cast_CylindricalGearMeshFEModel",
            parent: "CylindricalGearMeshFEModel",
        ):
            self._parent = parent

        @property
        def gear_mesh_fe_model(
            self: "CylindricalGearMeshFEModel._Cast_CylindricalGearMeshFEModel",
        ):
            return self._parent._cast(_1196.GearMeshFEModel)

        @property
        def gear_mesh_implementation_detail(
            self: "CylindricalGearMeshFEModel._Cast_CylindricalGearMeshFEModel",
        ):
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "CylindricalGearMeshFEModel._Cast_CylindricalGearMeshFEModel",
        ):
            from mastapy.gears.analysis import _1220

            return self._parent._cast(_1220.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "CylindricalGearMeshFEModel._Cast_CylindricalGearMeshFEModel",
        ):
            from mastapy.gears.analysis import _1214

            return self._parent._cast(_1214.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "CylindricalGearMeshFEModel._Cast_CylindricalGearMeshFEModel",
        ) -> "CylindricalGearMeshFEModel":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshFEModel._Cast_CylindricalGearMeshFEModel",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMeshFEModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def stiffness_wrt_contacts_for(
        self: Self, gear: "_1195.GearFEModel", flank: "_324.GearFlanks"
    ) -> "List[_833.GearContactStiffness]":
        """List[mastapy.gears.ltca.GearContactStiffness]

        Args:
            gear (mastapy.gears.fe_model.GearFEModel)
            flank (mastapy.gears.GearFlanks)
        """
        flank = conversion.mp_to_pn_enum(flank, "SMT.MastaAPI.Gears.GearFlanks")
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.StiffnessWrtContactsFor.Overloads[
                _GEAR_FE_MODEL, _GEAR_FLANKS
            ](gear.wrapped if gear else None, flank)
        )

    @enforce_parameter_types
    def stiffness_wrt_contacts_for_with_progress(
        self: Self,
        gear: "_1195.GearFEModel",
        flank: "_324.GearFlanks",
        progress: "_7556.TaskProgress",
    ) -> "List[_833.GearContactStiffness]":
        """List[mastapy.gears.ltca.GearContactStiffness]

        Args:
            gear (mastapy.gears.fe_model.GearFEModel)
            flank (mastapy.gears.GearFlanks)
            progress (mastapy.TaskProgress)
        """
        flank = conversion.mp_to_pn_enum(flank, "SMT.MastaAPI.Gears.GearFlanks")
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.StiffnessWrtContactsFor.Overloads[
                _GEAR_FE_MODEL, _GEAR_FLANKS, _TASK_PROGRESS
            ](
                gear.wrapped if gear else None,
                flank,
                progress.wrapped if progress else None,
            )
        )

    @enforce_parameter_types
    def generate_stiffness_wrt_contacts_for(self: Self, progress: "_7556.TaskProgress"):
        """Method does not return.

        Args:
            progress (mastapy.TaskProgress)
        """
        self.wrapped.GenerateStiffnessWrtContactsFor.Overloads[_TASK_PROGRESS](
            progress.wrapped if progress else None
        )

    @enforce_parameter_types
    def generate_stiffness_wrt_contacts_for_flank(
        self: Self, flank: "_324.GearFlanks", progress: "_7556.TaskProgress"
    ):
        """Method does not return.

        Args:
            flank (mastapy.gears.GearFlanks)
            progress (mastapy.TaskProgress)
        """
        flank = conversion.mp_to_pn_enum(flank, "SMT.MastaAPI.Gears.GearFlanks")
        self.wrapped.GenerateStiffnessWrtContactsFor.Overloads[
            _GEAR_FLANKS, _TASK_PROGRESS
        ](flank, progress.wrapped if progress else None)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshFEModel._Cast_CylindricalGearMeshFEModel":
        return self._Cast_CylindricalGearMeshFEModel(self)
