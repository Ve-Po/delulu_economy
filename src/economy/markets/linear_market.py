
from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Equilibrium:
    """Stores the equilibrium price and quantity of a market."""

    price: float
    quantity: float


@dataclass
class LinearMarket:
    """
    A simplified competitive market with linear demand and supply.

    Demand:  Qd = max(0, a - b * P)
    Supply:  Qs = max(0, c + d * P)
    """

    a: float
    b: float
    c: float
    d: float

    def __post_init__(self) -> None:
        """Validate market parameters after initialization."""

        parameters = {
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "d": self.d,
        }

        for name, value in parameters.items():
            if not isfinite(value):
                raise ValueError(f"{name} must be a finite number")

        if self.a < 0:
            raise ValueError("a must be non-negative")

        if self.b <= 0:
            raise ValueError("b must be greater than zero")

        if self.d <= 0:
            raise ValueError("d must be greater than zero")

    def calculate_demand(self, price: float) -> float:
        """Calculate quantity demanded at a given non-negative price."""

        self._validate_price(price)
        return max(0.0, self.a - self.b * price)

    def calculate_supply(self, price: float) -> float:
        """Calculate quantity supplied at a given non-negative price."""

        self._validate_price(price)
        return max(0.0, self.c + self.d * price)

    def calculate_equilibrium(self) -> Equilibrium:
        """
        Calculate an interior market equilibrium.

        Raises ValueError if the intersection is outside the
        non-negative price and quantity region.
        """

        price = (self.a - self.c) / (self.b + self.d)
        quantity = self.a - self.b * price

        if price < 0 or quantity < 0:
            raise ValueError(
                "No feasible interior equilibrium for these parameters"
            )

        return Equilibrium(
            price=price,
            quantity=quantity,
        )

    @staticmethod
    def _validate_price(price: float) -> None:
        """Ensure that a price is finite and non-negative."""

        if not isfinite(price):
            raise ValueError("price must be a finite number")

        if price < 0:
            raise ValueError("price must be non-negative")
