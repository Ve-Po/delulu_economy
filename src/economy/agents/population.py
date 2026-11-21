
from dataclasses import dataclass

from economy.agents.household import Household


@dataclass
class HouseholdPopulation:
    """
    Represents a collection of households.

    The population aggregates individual household
    balances and demand without changing their state.
    """

    households: list[Household]

    def __post_init__(self) -> None:
        """Validate the population."""

        if not self.households:
            raise ValueError("Population cannot be empty")

        household_ids = [
            household.household_id
            for household in self.households
        ]

        if len(household_ids) != len(set(household_ids)):
            raise ValueError("Household IDs must be unique")

    @property
    def size(self) -> int:
        """Return the number of households."""
        return len(self.households)

    def total_balance(self) -> float:
        """Return the total monetary balance."""
        return sum(
            household.balance
            for household in self.households
        )

    def total_demand(self, price: float) -> float:
        """Aggregate individual effective demand."""
        return sum(
            household.calculate_demand(price)
            for household in self.households
        )

    def average_balance(self) -> float:
        """Return the average household balance."""
        return self.total_balance() / self.size

