
import pytest

from economy.agents.household import Household


@pytest.fixture
def household():
    return Household(
        household_id="H-001",
        balance=100,
        desired_quantity=3,
    )


def test_household_creation(household):
    assert household.household_id == "H-001"
    assert household.balance == 100
    assert household.desired_quantity == 3


def test_affordable_quantity(household):
    assert household.affordable_quantity(5) == 20


def test_demand_is_limited_by_desired_quantity(household):
    assert household.calculate_demand(5) == 3


def test_demand_is_limited_by_budget():
    household = Household(
        household_id="H-002",
        balance=10,
        desired_quantity=10,
    )

    assert household.calculate_demand(5) == 2


def test_zero_price_does_not_limit_demand(household):
    assert household.calculate_demand(0) == 3


def test_zero_balance_means_zero_affordable_demand():
    household = Household(
        household_id="H-003",
        balance=0,
        desired_quantity=5,
    )

    assert household.calculate_demand(5) == 0


def test_negative_price_is_rejected(household):
    with pytest.raises(ValueError):
        household.calculate_demand(-1)


def test_negative_balance_is_rejected():
    with pytest.raises(ValueError):
        Household(
            household_id="H-004",
            balance=-10,
            desired_quantity=2,
        )


def test_negative_desired_quantity_is_rejected():
    with pytest.raises(ValueError):
        Household(
            household_id="H-005",
            balance=100,
            desired_quantity=-2,
        )


def test_empty_household_id_is_rejected():
    with pytest.raises(ValueError):
        Household(
            household_id="",
            balance=100,
            desired_quantity=2,
        )


def test_nan_balance_is_rejected():
    with pytest.raises(ValueError):
        Household(
            household_id="H-006",
            balance=float("nan"),
            desired_quantity=2,
        )
