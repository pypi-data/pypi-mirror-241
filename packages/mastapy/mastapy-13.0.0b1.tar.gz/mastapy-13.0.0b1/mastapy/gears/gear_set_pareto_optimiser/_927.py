"""ParetoFaceRatingOptimisationStrategyDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility.optimisation import _1550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_FACE_RATING_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoFaceRatingOptimisationStrategyDatabase",
)


__docformat__ = "restructuredtext en"
__all__ = ("ParetoFaceRatingOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoFaceRatingOptimisationStrategyDatabase")


class ParetoFaceRatingOptimisationStrategyDatabase(
    _1550.ParetoOptimisationStrategyDatabase
):
    """ParetoFaceRatingOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_FACE_RATING_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParetoFaceRatingOptimisationStrategyDatabase"
    )

    class _Cast_ParetoFaceRatingOptimisationStrategyDatabase:
        """Special nested class for casting ParetoFaceRatingOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase",
            parent: "ParetoFaceRatingOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase",
        ):
            return self._parent._cast(_1550.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase",
        ):
            from mastapy.math_utility.optimisation import _1537

            return self._parent._cast(_1537.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.SQLDatabase)

        @property
        def database(
            self: "ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase",
        ):
            pass

            from mastapy.utility.databases import _1822

            return self._parent._cast(_1822.Database)

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _925

            return self._parent._cast(
                _925.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _926

            return self._parent._cast(
                _926.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase",
        ) -> "ParetoFaceRatingOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoFaceRatingOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase":
        return self._Cast_ParetoFaceRatingOptimisationStrategyDatabase(self)
