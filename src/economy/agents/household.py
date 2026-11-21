
from dataclasses import dataclass
from math import isfinite


@dataclass
class Household:
    """
    Represents an individual household in the economy.

    The household has a limited monetary balance and
    a desired quantity of bread.
    """

    household_id: str
    balance: float
    desired_quantity: float

    def __post_init__(self) -> None:
        """Validate the household's initial state."""

        if not self.household_id.strip():
            raise ValueError("household_id cannot be empty")

        if not isfinite(self.balance):
            raise ValueError("balance must be a finite number")

        if not isfinite(self.desired_quantity):
            raise ValueError(
                "desired_quantity must be a finite number"
            )

        if self.balance < 0:
            raise ValueError("balance cannot be negative")

        if self.desired_quantity < 0:
            raise ValueError(
                "desired_quantity cannot be negative"
            )

    def affordable_quantity(self, price: float) -> float:
        """
        Calculate the maximum quantity the household
        can afford at the given price.
        """

        self._validate_price(price)

        if price == 0:
            return float("inf")

        return self.balance / price

    def calculate_demand(self, price: float) -> float:
        """
        Calculate effective demand.

        Effective demand cannot exceed either:
        - desired quantity;
        - quantity affordable with the current balance.
        """

        affordable = self.affordable_quantity(price)

        return min(self.desired_quantity, affordable)

    @staticmethod
    def _validate_price(price: float) -> None:
        """Ensure that price is finite and non-negative."""

        if not isfinite(price):
            raise ValueError("price must be a finite number")

        if price < 0:
            raise ValueError("price cannot be negative")
