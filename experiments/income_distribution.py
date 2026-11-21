
from economy.agents.household import Household
from economy.agents.population import HouseholdPopulation


def create_equal_population() -> HouseholdPopulation:
    """Create 10 households with equal balances."""

    households = [
        Household(
            household_id=f"A-{i:03}",
            balance=100,
            desired_quantity=10,
        )
        for i in range(1, 11)
    ]

    return HouseholdPopulation(households)


def create_unequal_population() -> HouseholdPopulation:
    """Create 10 households with unequal balances."""

    households = [
        Household(
            household_id=f"B-{i:03}",
            balance=10,
            desired_quantity=10,
        )
        for i in range(1, 10)
    ]

    households.append(
        Household(
            household_id="B-010",
            balance=910,
            desired_quantity=10,
        )
    )

    return HouseholdPopulation(households)


def main() -> None:
    price = 5

    populations = {
        "Equal distribution": create_equal_population(),
        "Unequal distribution": create_unequal_population(),
    }

    print(f"Bread price: {price}")
    print("-" * 45)

    for name, population in populations.items():
        print(f"\n{name}")
        print(f"Households: {population.size}")
        print(f"Total balance: {population.total_balance()}")
        print(f"Average balance: {population.average_balance()}")
        print(f"Aggregate demand: {population.total_demand(price)}")


if __name__ == "__main__":
    main()
