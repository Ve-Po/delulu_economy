
import pytest

from economy.agents.household import Household
from economy.agents.population import HouseholdPopulation


@pytest.fixture
def equal_population():
    households = [
        Household(f"H-{i:03}", 100, 10)
        for i in range(1, 11)
    ]

    return HouseholdPopulation(households)


@pytest.fixture
def unequal_population():
    households = [
        Household(f"H-{i:03}", 10, 10)
        for i in range(1, 10)
    ]

    households.append(
        Household("H-010", 910, 10)
    )

    return HouseholdPopulation(households)


def test_population_size(equal_population):
    assert equal_population.size == 10


def test_total_balance(equal_population):
    assert equal_population.total_balance() == 1000


def test_average_balance(equal_population):
    assert equal_population.average_balance() == 100


def test_equal_population_demand(equal_population):
    assert equal_population.total_demand(5) == 100


def test_unequal_population_demand(unequal_population):
    assert unequal_population.total_demand(5) == 28


def test_equal_and_unequal_populations_have_same_total_balance(
    equal_population,
    unequal_population,
):
    assert equal_population.total_balance() == (
        unequal_population.total_balance()
    )


def test_empty_population_is_rejected():
    with pytest.raises(ValueError):
        HouseholdPopulation([])


def test_duplicate_household_ids_are_rejected():
    first = Household("H-001", 100, 5)
    second = Household("H-001", 200, 5)

    with pytest.raises(ValueError):
        HouseholdPopulation([first, second])


def test_calculating_demand_does_not_change_balances(
    unequal_population,
):
    initial_balance = unequal_population.total_balance()

    unequal_population.total_demand(5)

    assert unequal_population.total_balance() == initial_balance
